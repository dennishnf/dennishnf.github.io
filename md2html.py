

#Convertion file from Markdown to Html for my website
#By Dennis Nunez-Fernandez



import os
import re
import sys
import argparse
import platform
from tempfile import mkstemp
from shutil import move
from os import fdopen, remove
from fnmatch import fnmatch
from shutil import copyfile
from time import gmtime, strftime





def replace(file, pattern, subst):
    # Read contents from file as a single string
    file_handle = open(file, 'r', encoding='utf-8')
    file_string = file_handle.read()
    file_handle.close()

    # Use RE package to allow for replacement (also allowing for (multiline) REGEX)
    file_string = (re.sub(pattern, subst, file_string))

    # Write contents to file.
    # Using mode 'w' truncates the file.
    file_handle = open(file, 'w', encoding='utf-8')
    file_handle.write(file_string)
    file_handle.close()


def convert(pathh):
    path_in=pathh+'.md'
    path_out=pathh+'.html'

    copyfile(path_in, path_out)

    print("___")


    ##alternative <p> </p>
    replace(path_out, r'\n\n0', '\n\n<p align="justify">0')
    replace(path_out, r'\n\n1', '\n\n<p align="justify">1')
    replace(path_out, r'\n\n2', '\n\n<p align="justify">2')
    replace(path_out, r'\n\n3', '\n\n<p align="justify">3')
    replace(path_out, r'\n\n4', '\n\n<p align="justify">4')
    replace(path_out, r'\n\n5', '\n\n<p align="justify">5')
    replace(path_out, r'\n\n6', '\n\n<p align="justify">6')
    replace(path_out, r'\n\n7', '\n\n<p align="justify">7')
    replace(path_out, r'\n\n8', '\n\n<p align="justify">8')
    replace(path_out, r'\n\n9', '\n\n<p align="justify">9')
    replace(path_out, r'\n\nA', '\n\n<p align="justify">A')
    replace(path_out, r'\n\nB', '\n\n<p align="justify">B')
    replace(path_out, r'\n\nC', '\n\n<p align="justify">C')
    replace(path_out, r'\n\nD', '\n\n<p align="justify">D')
    replace(path_out, r'\n\nE', '\n\n<p align="justify">E')
    replace(path_out, r'\n\nF', '\n\n<p align="justify">F')
    replace(path_out, r'\n\nG', '\n\n<p align="justify">G')
    replace(path_out, r'\n\nH', '\n\n<p align="justify">H')
    replace(path_out, r'\n\nI', '\n\n<p align="justify">I')
    replace(path_out, r'\n\nJ', '\n\n<p align="justify">J')
    replace(path_out, r'\n\nK', '\n\n<p align="justify">K')
    replace(path_out, r'\n\nL', '\n\n<p align="justify">L')
    replace(path_out, r'\n\nM', '\n\n<p align="justify">M')
    replace(path_out, r'\n\nN', '\n\n<p align="justify">N')
    replace(path_out, r'\n\nO', '\n\n<p align="justify">O')
    replace(path_out, r'\n\nP', '\n\n<p align="justify">P')
    replace(path_out, r'\n\nQ', '\n\n<p align="justify">Q')
    replace(path_out, r'\n\nR', '\n\n<p align="justify">R')
    replace(path_out, r'\n\nS', '\n\n<p align="justify">S')
    replace(path_out, r'\n\nT', '\n\n<p align="justify">T')
    replace(path_out, r'\n\nU', '\n\n<p align="justify">U')
    replace(path_out, r'\n\nV', '\n\n<p align="justify">V')
    replace(path_out, r'\n\nW', '\n\n<p align="justify">W')
    replace(path_out, r'\n\nX', '\n\n<p align="justify">X')
    replace(path_out, r'\n\nY', '\n\n<p align="justify">Y')
    replace(path_out, r'\n\nZ', '\n\n<p align="justify">Z')
    replace(path_out, r'\n\na', '\n\n<p align="justify">a')
    replace(path_out, r'\n\nb', '\n\n<p align="justify">b')
    replace(path_out, r'\n\nc', '\n\n<p align="justify">c')
    replace(path_out, r'\n\nd', '\n\n<p align="justify">d')
    replace(path_out, r'\n\ne', '\n\n<p align="justify">e')
    replace(path_out, r'\n\nf', '\n\n<p align="justify">f')
    replace(path_out, r'\n\ng', '\n\n<p align="justify">g')
    replace(path_out, r'\n\nh', '\n\n<p align="justify">h')
    replace(path_out, r'\n\ni', '\n\n<p align="justify">i')
    replace(path_out, r'\n\nj', '\n\n<p align="justify">j')
    replace(path_out, r'\n\nk', '\n\n<p align="justify">k')
    replace(path_out, r'\n\nl', '\n\n<p align="justify">l')
    replace(path_out, r'\n\nm', '\n\n<p align="justify">m')
    replace(path_out, r'\n\nn', '\n\n<p align="justify">n')
    replace(path_out, r'\n\no', '\n\n<p align="justify">o')
    replace(path_out, r'\n\np', '\n\n<p align="justify">p')
    replace(path_out, r'\n\nq', '\n\n<p align="justify">q')
    replace(path_out, r'\n\nr', '\n\n<p align="justify">r')
    replace(path_out, r'\n\ns', '\n\n<p align="justify">s')
    replace(path_out, r'\n\nt', '\n\n<p align="justify">t')
    replace(path_out, r'\n\nu', '\n\n<p align="justify">u')
    replace(path_out, r'\n\nv', '\n\n<p align="justify">v')
    replace(path_out, r'\n\nw', '\n\n<p align="justify">w')
    replace(path_out, r'\n\nx', '\n\n<p align="justify">x')
    replace(path_out, r'\n\ny', '\n\n<p align="justify">y')
    replace(path_out, r'\n\nz', '\n\n<p align="justify">z')
    replace(path_out, r'\n\n-', '\n\n<p align="justify">-')
    replace(path_out, r'\n\n,', '\n\n<p align="justify">,')
    replace(path_out, r'\.\n\n', '.</p>\n')
    replace(path_out, r'\:\n\n', ':</p>\n')

    replace(path_out, r'\n#### ', '\n<br/> \n<h4>')
    replace(path_out, r' ####\n', '</h4>\n')
    replace(path_out, r'\n### ', '\n<br/> \n<h3>')
    replace(path_out, r' ###\n', '</h3>\n')
    replace(path_out, r'\n## ', '\n<h2>')
    replace(path_out, r' ##\n', '</h2>\n')

    #Translate text from markdown to html
    #replace(path_out, r'\n\n', '\n<br/>\n')
    #replace(path_out, r'\n \n', '\n<br/><br/>\n')

    replace(path_out, r'```\n\n```\n', '```\n\n<p><code class="barcode">')
    replace(path_out, r'</p>\n```\n', '</p>\n<p><code class="barcode">')
    replace(path_out, r'</h2>\n\n```\n', '</h2>\n\n<p><code class="barcode">')
    replace(path_out, r'</h3>\n\n```\n', '</h3>\n\n<p><code class="barcode">')
    replace(path_out, r'</h4>\n\n```\n', '</h4>\n\n<p><code class="barcode">')
    replace(path_out, r'```\n', '</code></p>\n')

    replace(path_out, r'<<x>', '&lt;')
    replace(path_out, r'<x>>', '&gt;')

    #replace(path_out, r'<br/>\n\n', '<br/>\n')
    #replace(path_out, r'\n\n<br/>', '\n<br/>')
    #replace(path_out, r'<br/>\n<br/>\n', '<br/>\n')
    replace(path_out, r' ```', ' <custom_code>')
    replace(path_out, r'```', '</custom_code>')

    #replace(path_out, r' \*\*', ' <strong>')
    #replace(path_out, r'\*\*', '</strong>')

    replace(path_out, r'\!\[image\]\(', '\n<center><img src=\"')
    replace(path_out, r'.png\){', '.png\" style=\"padding-top:8px; padding-bottom: 8px;\"  width=\"')
    replace(path_out, r'}!', '\"/></center>\n')
    replace(path_out, r'.jpg\){', '.png\" style=\"padding-top:8px; padding-bottom: 8px;\"  width=\"')
    replace(path_out, r'}!', '\"/></center>\n')
    replace(path_out, r'.jpng\){', '.png\" style=\"padding-top:8px; padding-bottom: 8px;\"  width=\"')
    replace(path_out, r'}!', '\"/></center>\n')
    replace(path_out, r'.jpeg\){', '.png\" style=\"padding-top:8px; padding-bottom: 8px;\"  width=\"')
    replace(path_out, r'}!', '\"/></center>\n')
    replace(path_out, r'.png\)', '.png\" style=\"padding-top:8px; padding-bottom: 8px;\" /></center>\n')
    replace(path_out, r'.jpg\)', '.jpg\" style=\"padding-top:8px; padding-bottom: 8px;\" /></center>\n')
    replace(path_out, r'.jpng\)', '.jpng\" style=\"padding-top:8px; padding-bottom: 8px;\" /></center>\n')
    replace(path_out, r'.jpeg\)', '.jpeg\" style=\"padding-top:8px; padding-bottom: 8px;\" /></center>\n')
    replace(path_out, r'.gif\)', '.gif\" style=\"padding-top:8px; padding-bottom: 8px;\" /></center>\n')

    replace(path_out, r'\!{', '\n<center style=\"padding-bottom: 8px; padding-top: 8px;\" ><video width=\"')
    replace(path_out, r'}\[video\]\(', '\" controls><source src=\"')
    replace(path_out, r'\!\[video\]\(', '\n<center style=\"padding-bottom: 8px; padding-top: 8px;\" ><video controls><source src=\"')
    replace(path_out, r'.mp4\)', '.mp4\" type=\"video/mp4\"> Your browser does not support the video tag.</video></center>\n')

    replace(path_out, r'\[htt', '<a target=\"_blank\" href=\"htt')
    replace(path_out, r'\]\(', '\">')
    replace(path_out, r'\)!', '</a>')

    #replace(path_out, r'myW3B', 'https://dennishnf.net')

    ##replace(path_out, r'xxxx', 'xxxx')

    with open(path_out, "a", encoding='utf-8') as myfile:
        myfile.write("\n<br/>\n")
          

    ##COPYING PRE

    with open('pre.html', 'r', encoding='utf-8') as myfile:
        data1=myfile.read()

    f = open(path_out,'r+', encoding='utf-8')
    lines = f.readlines() # read old content
    f.seek(0) # go back to the beginning of the file
    f.write(data1) # write new content at the beginning
    for line in lines: # write old content after new
        f.write(line)
    f.close()

    ## COPYING POST

    with open(path_out, r'a', encoding='utf-8') as output, open('post.html', 'r', encoding='utf-8') as input:
          while True:
              data = input.read(100000)
              if data == '':  # end of file reached
                  break
              output.write(data)
    
    with open(path_out, "a", encoding='utf-8') as myfile:
        timeInfo=strftime("&nbsp;%d-%m-%Y&nbsp;%H:%M", gmtime())
        myfile.write("<a href=\"https://dennishnf.net/README.html\" target=\"_blank\">Built using Python. Powered by Linux.</a> <br/>\n")
        myfile.write("Last updated:")
        myfile.write(timeInfo)
        myfile.write(" GMT. <br/> \n</div> \n")
        myfile.write("<div class=\"clearer\">&nbsp;</div> \n")
        myfile.write("</div> \n")
        myfile.write("</div> \n")
        myfile.write("</div> \n")
        myfile.write("</div> \n")
        myfile.write("</div> \n")
        myfile.write("</div> \n")
        myfile.write("</body> \n\n\n")
        myfile.write("</html> \n")


              
    #Copy .css file from main place to same path .html file









deviceName = platform.system()
timeInfoo=strftime("%d-%m-%Y %H:%M", gmtime())


root = sys.argv[1]


#if deviceName == 'Linux':
#    root = r"/home/dennishnf/Desktop/dennishnf.github.io"

#if deviceName == 'Windows':
#    root = r"C:\Users\Dennis\Desktop\dennishnf.github.io"

pattern = "*.md"

for path, subdirs, files in os.walk(root):
    for name in files:
        if fnmatch(name, pattern):
            print(os.path.splitext(os.path.join(path, name))[0])
            print(os.path.join(path))
            convert(os.path.splitext(os.path.join(path, name))[0])
            


print("\nExecuted in "+deviceName+"\n"+timeInfoo+" GMT"+"\n___")







