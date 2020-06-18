
## README ##

My personal Website, Dennis Núñez Fernández. At the moment, Bitbucked is used as host server.

The creation of this website was created usng the principles:

- Simplicity.

- Perdurability.

- Portability.

- Modularity.

The creation of new pages is easy due the creation of this pages is done using markdown language.

The pages created with Markdown are converted directly to Html using a script in Python called md2html.py (this script is simple and can be done in another languages like C, C++, or using Matlab/Octave), so the full content of the pages is stored in pure Html.

Due the full website is converted directly from Markdown to Html, this website no depend of another language and tools that can be unstables/unsupported after a long time. So, this make this websie perdurable.

As I mentioned before, the full website is saved in Html, therefore this website can be changed easily to a different host server.

In addition to this, the folders are well organized and can be used easily.

Be careful: In order to use this you should use the same format of the markdown files presented in this website.

### Using ###

Navigate to repository with cd, example:

```
$ cd Repositories/dennishnf.bitbucket.io/
```

To CREATE html files and NOT UPDATE:

```
$ python md2html.py
```

To CREATE html files and UPDATE:

```
$ ./update.sh
```

Also, you can run the update script clicking in the update.sh file.

### Copyright ###

Copyright, Dennis Núñez Fernández 2017.

