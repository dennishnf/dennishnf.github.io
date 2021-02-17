
## Train Convolutional Neural Networks in Google Colab using PyTorch ##

You’ll want to be using GPU for this project, which is incredibly simple to set up on Colab. You just go to the “runtime” dropdown menu, select “change runtime type” and then select “GPU” in the hardware accelerator drop-down menu!

Just to make sure it’s working:

```
import torch
train_on_gpu = torch.cuda.is_available()
if not train_on_gpu:
    print('Bummer!  Training on CPU ...')
else:
    print('You are good to go!  Training on GPU ...')
```

Define the device:

```
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
```

After this, import the files. There are a ton of ways to do this, including mounting your Google Drive if you have your dataset stored there, which is actually really simple:

```
from google.colab import drive
drive.mount('/content/gdrive')
```

However, if you’d rather download a shared zip file link (this wound up being easier and faster for this project), you can use:

```
!wget -cq https://s3.amazonaws.com/content.udacity-data.com/courses/nd188/flower_data.zip
!unzip -qq flower_data.zip
```

After loading the data, I imported the libraries I wanted to use:

```
%matplotlib inline
%config InlineBackend.figure_format = 'retina'
import time
import json
import copy
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import PIL
from PIL import Image
from collections import OrderedDict
import torch
from torch import nn, optim
from torch.optim import lr_scheduler
from torch.autograd import Variable
import torchvision
from torchvision import datasets, models, transforms
from torch.utils.data.sampler import SubsetRandomSampler
import torch.nn as nn
import torch.nn.functional as F
  
import os
data_dir='/content/flower_data/'
```

Next comes the data transformations! You want to make sure to use several different types of transformations on your training set in order to help your program learn as much as it can. You can create a more robust model by training it on flipped, rotated, and cropped images.

```
data_transforms = {
    'train': transforms.Compose([
        transforms.RandomRotation(30),
        transforms.RandomResizedCrop(224),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], 
                             [0.229, 0.224, 0.225])
    ]),
    'valid': transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], 
                             [0.229, 0.224, 0.225])
    ])
}
# Load the datasets with ImageFolder
image_datasets = {x: datasets.ImageFolder(os.path.join(data_dir, x),
                                          data_transforms[x])
                  for x in ['train', 'valid']}
# Using the image datasets and the trainforms, define the dataloaders
batch_size = 64
dataloaders = {x: torch.utils.data.DataLoader(image_datasets[x], batch_size=batch_size,
                                             shuffle=True, num_workers=4)
              for x in ['train', 'valid']}
class_names = image_datasets['train'].classes
dataset_sizes = {x: len(image_datasets[x]) for x in ['train', 'valid']}
class_names = image_datasets['train'].classes
```

To take a very quick look at the data and check my device, I ran:

```
print(dataset_sizes)
print(device)
```

Output:

```
{'train': 6552, 'valid': 818}
cuda:0
```

Next, we need to do some mapping from the label number and the actual flower name (find cat_to_name at: https://github.com/udacity/aipnd-project/blob/master/cat_to_name.json):

```
with open('cat_to_name.json', 'r') as f:
    cat_to_name = json.load(f)
```

Then:

```
ls
```

In order to test the data loader, run:

```
images, labels = next(iter(dataloaders['train']))
rand_idx = np.random.randint(len(images))
# Print(rand_idx)
print("label: {}, class: {}, name: {}".format(labels[rand_idx].item(),
                                               class_names[labels[rand_idx].item()],
                                               cat_to_name[class_names[labels[rand_idx].item()]]))
```

PyTorch makes it easy to load pre-trained models and build on them, which is exactly what we’re going to do for this project. The choice of model is entirely up to you! (choose model at: https://pytorch.org/docs/stable/torchvision/models.html):

```
model = models.densenet161(pretrained=True)
```

In order to set up a choice in architecture, run:

```
model_name = 'densenet' #vgg
if model_name == 'densenet':
    model = models.densenet161(pretrained=True)
    num_in_features = 2208
    print(model)
elif model_name == 'vgg':
    model = models.vgg19(pretrained=True)
    num_in_features = 25088
    print(model.classifier)
else:
    print("Unknown model, please choose 'densenet' or 'vgg'")
```

After that, you can start to build your classifier, using the parameters that work best for you. I went ahead and built the next code, which allows for an easy way to change the number of hidden layers that I’m using, as well as quickly adjusting the dropout rate. You may decide to add additional ReLU and dropout layers in order to more finely hone your model.

```
for param in model.parameters():
    param.requires_grad = False
def build_classifier(num_in_features, hidden_layers, num_out_features):
   
    classifier = nn.Sequential()
    if hidden_layers == None:
        classifier.add_module('fc0', nn.Linear(num_in_features, 102))
    else:
        layer_sizes = zip(hidden_layers[:-1], hidden_layers[1:])
        classifier.add_module('fc0', nn.Linear(num_in_features, hidden_layers[0]))
        classifier.add_module('relu0', nn.ReLU())
        classifier.add_module('drop0', nn.Dropout(.6))
        classifier.add_module('relu1', nn.ReLU())
        classifier.add_module('drop1', nn.Dropout(.5))
        for i, (h1, h2) in enumerate(layer_sizes):
            classifier.add_module('fc'+str(i+1), nn.Linear(h1, h2))
            classifier.add_module('relu'+str(i+1), nn.ReLU())
            classifier.add_module('drop'+str(i+1), nn.Dropout(.5))
        classifier.add_module('output', nn.Linear(hidden_layers[-1], num_out_features))
        
    return classifier
```

Next, work on training your classifier parameters. I decided to make sure I only trained the classifier parameters here while having feature parameters frozen. You can get as creative as you want with your optimizer, criterion, and scheduler. The criterion is the method used to evaluate the model fit, the optimizer is the optimization method used to update the weights, and the scheduler provides different methods for adjusting the learning rate and step size used during optimization.

Try as many options and combinations as you can to see what gives you the best result. You can see all of the official documentation here (https://pytorch.org/docs/stable/optim.html). I recommend taking a look at it and making your own decisions about what you want to use. You don’t literally have an infinite number of options here, but it sure feels like it once you start playing around!.

```
hidden_layers = None
classifier = build_classifier(num_in_features, hidden_layers, 102)
print(classifier)
# Only train the classifier parameters, feature parameters are frozen
if model_name == 'densenet':
    model.classifier = classifier
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adadelta(model.parameters())
    sched = optim.lr_scheduler.StepLR(optimizer, step_size=4)
elif model_name == 'vgg':
    model.classifier = classifier
    criterion = nn.NLLLoss()
    optimizer = optim.Adam(model.classifier.parameters(), lr=0.0001)
    sched = lr_scheduler.StepLR(optimizer, step_size=4, gamma=0.1)
else:
    pass
```

Now it’s time to train your model!!!:

```
# Adapted from https://pytorch.org/tutorials/beginner/transfer_learning_tutorial.html
def train_model(model, criterion, optimizer, sched, num_epochs=5):
  since = time.time()
  best_model_wts = copy.deepcopy(model.state_dict())
  best_acc = 0.0
  
  for epoch in range(num_epochs):
    print('Epoch {}/{}'.format(epoch+1, num_epochs))
    print('-' * 10)
    
    # Each epoch has a training and validation phase
    for phase in ['train', 'valid']:
      if phase == 'train':
        model.train()  # Set model to training mode
      else:
        model.eval()   # Set model to evaluate mode
      running_loss = 0.0
      running_corrects = 0
      
      # Iterate over data.
      for inputs, labels in dataloaders[phase]:
        inputs = inputs.to(device)
        labels = labels.to(device)
        
        # Zero the parameter gradients
        optimizer.zero_grad()
        
        # Forward
        # track history if only in train
        with torch.set_grad_enabled(phase == 'train'):
          outputs = model(inputs)
          _, preds = torch.max(outputs, 1)
          loss = criterion(outputs, labels)
          
          # Backward + optimize only if in training phase
          if phase == 'train':
            #sched.step()
            loss.backward()
            optimizer.step()
        
        # Statistics
        running_loss += loss.item() * inputs.size(0)
        running_corrects += torch.sum(preds == labels.data)
      epoch_loss = running_loss / dataset_sizes[phase]
      epoch_acc = running_corrects.double() / dataset_sizes[phase]
      
      print('{} Loss: {:.4f} Acc: {:.4f}'.format(
          phase, epoch_loss, epoch_acc))
      
      # Deep copy the model
      if phase == 'valid' and epoch_acc > best_acc:
        best_acc = epoch_acc
        best_model_wts = copy.deepcopy(model.state_dict())
  
    print()
  
  time_elapsed = time.time() - since
  print('Training complete in {:.0f}m {:.0f}s'.format(
      time_elapsed // 60, time_elapsed % 60))
  print('Best val Acc: {:4f}'.format(best_acc))
  
  # Load best model weights
  model.load_state_dict(best_model_wts)
    
  return model
  
  
epochs = 30
model.to(device)
model = train_model(model, criterion, optimizer, sched, epochs)
```

Now it’s time for evaluation:

```
model.eval()
  
accuracy = 0
  
for inputs, labels in dataloaders['valid']:
    inputs, labels = inputs.to(device), labels.to(device)
    outputs = model(inputs)
    
    # Class with the highest probability is our predicted class
    equality = (labels.data == outputs.max(1)[1])
    
# Accuracy = number of correct predictions divided by all predictions
    accuracy += equality.type_as(torch.FloatTensor()).mean()
    
print("Test accuracy: {:.3f}".format(accuracy/len(dataloaders['valid'])))
```

It’s important to save your checkpoint:

```
model.class_to_idx = image_datasets['train'].class_to_idx
    
checkpoint = {'input_size': 2208,
              'output_size': 102,
              'epochs': epochs,
              'batch_size': 64,
              'model': models.densenet161(pretrained=True),
              'classifier': classifier,
              'scheduler': sched,
              'optimizer': optimizer.state_dict(),
              'state_dict': model.state_dict(),
              'class_to_idx': model.class_to_idx
             }
   
torch.save(checkpoint, 'checkpoint.pth')
```

You don’t have to save all of the parameters, but I’m including them here as an example. This checkpoint specifically saves the model with a pre-trained densenet161 architecture, but if you want to save your checkpoint with the two-choice option, you can absolutely do that. Simply adjust the input size and model.

Now you’re able to load your checkpoint, you can check your keys by running:

```
ckpt = torch.load('checkpoint.pth')
ckpt.keys()
```

Then load and rebuild your model!:

```
def load_checkpoint(filepath):
    checkpoint = torch.load(filepath)
    model = checkpoint['model']
    model.classifier = checkpoint['classifier']
    model.load_state_dict(checkpoint['state_dict'])
    model.class_to_idx = checkpoint['class_to_idx']
    optimizer = checkpoint['optimizer']
    epochs = checkpoint['epochs']
    
    for param in model.parameters():
        param.requires_grad = False
        
    return model, checkpoint['class_to_idx']
    
model, class_to_idx = load_checkpoint('checkpoint.pth')
```

Want to keep going? It’s a good idea to do some image preprocessing and inference for classification. Go ahead and define your image path and open an image:

```
image_path = 'flower_data/valid/102/image_08006.jpg'
img = Image.open(image_path)
```

Process your image and take a look at a processed image:

```
def process_image(image):
    ''' Scales, crops, and normalizes a PIL image for a PyTorch model,
        returns an Numpy array
    '''
    # Process a PIL image for use in a PyTorch model
    # tensor.numpy().transpose(1, 2, 0)
    preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], 
                             std=[0.229, 0.224, 0.225])
    ])
    image = preprocess(image)
    return image
    
def imshow(image, ax=None, title=None):
    """Imshow for Tensor."""
    if ax is None:
        fig, ax = plt.subplots()
    
    # PyTorch tensors assume the color channel is the first dimension
    # but matplotlib assumes is the third dimension
    image = image.numpy().transpose((1, 2, 0))
    
    # Undo preprocessing
    mean = np.array([0.485, 0.456, 0.406])
    std = np.array([0.229, 0.224, 0.225])
    image = std * image + mean
    
    # Image needs to be clipped between 0 and 1 or it looks like noise when displayed
    image = np.clip(image, 0, 1)
    
    ax.imshow(image)
    
    return ax
    
with Image.open('flower_data/valid/102/image_08006.jpg') as image:
    plt.imshow(image)
    
model.class_to_idx = image_datasets['train'].class_to_idx
```

Create a function for prediction:

```
def predict2(image_path, model, topk=5):
    ''' Predict the class (or classes) of an image using a trained deep learning model.
    '''
    
    # Implement the code to predict the class from an image file
    img = Image.open(image_path)
    img = process_image(img)
    
    # Convert 2D image to 1D vector
    img = np.expand_dims(img, 0)
    
    
    img = torch.from_numpy(img)
    
    model.eval()
    inputs = Variable(img).to(device)
    logits = model.forward(inputs)
    
    ps = F.softmax(logits,dim=1)
    topk = ps.cpu().topk(topk)
    
    return (e.data.numpy().squeeze().tolist() for e in topk)
```

Once the images are in the correct format, you can write a function to make predictions with your model. One common practice is to predict the top 5 or so (usually called top-KK) most probable classes. You’ll want to calculate the class probabilities then find the KK largest values.

This method should take a path to an image and a model checkpoint, then return the probabilities and classes:

```
img_path = 'flower_data/valid/18/image_04252.jpg'
probs, classes = predict2(img_path, model.to(device))
print(probs)
print(classes)
flower_names = [cat_to_name[class_names[e]] for e in classes]
print(flower_names)
```

Try using matplotlib to plot the probabilities for the top five classes in a bar graph along with the input image:

```
def view_classify(img_path, prob, classes, mapping):
    ''' Function for viewing an image and it's predicted classes.
    '''
    image = Image.open(img_path)
    
    fig, (ax1, ax2) = plt.subplots(figsize=(6,10), ncols=1, nrows=2)
    flower_name = mapping[img_path.split('/')[-2]]
    ax1.set_title(flower_name)
    ax1.imshow(image)
    ax1.axis('off')
    
    y_pos = np.arange(len(prob))
    ax2.barh(y_pos, prob, align='center')
    ax2.set_yticks(y_pos)
    ax2.set_yticklabels(flower_names)
    ax2.invert_yaxis()  # labels read top-to-bottom
    ax2.set_title('Class Probability')
    
view_classify(img_path, probs, classes, cat_to_name)
```

Great! That's all!! You can test a few other images to see how close your predictions are on a variety of images.

### References: ###

- [https://www.freecodecamp.org/news/how-to-build-the-best-image-classifier-3c72010b3d55/](https://www.freecodecamp.org/news/how-to-build-the-best-image-classifier-3c72010b3d55/)!.

