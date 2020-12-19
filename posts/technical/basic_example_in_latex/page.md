
## Basic example in LaTeX ##

### 1. Structure of a LaTeX file ###

```
\documentclass[options]{article}
% Preamble       (for LaTeX commands only)
\begin{document}
% Document text  (text with embedded LaTeX commands)
\end{document}
```

The "Document class" determines the overall layout of the document. In addition to "article" class, which is a good all-purpose class, other commonly-used classes are:

- report – for longer documents containing chapters.

- thesis – for writing an RPI thesis.

- book – for books.

- letter – for letters.

- slides – for making transparencies.

Among other things, the classes provide heading commands, such as \part, \chapter, \section.

### 2. Document Class Options & Packages ###

A "Document Class" may be modified by using options:

```
\documentclass[options]{article}
```

Commonly-used options include:

- 11pt Prints document in 11pt type (default 10pt).

- 12pt Prints document in 12pt type.

Example:

```
\documentclass[11pt]{article}
```

LaTeX "Packages" contain extra definitions that provide additional formatting features. To load a package, include the command into "preamble" :

```
\usepackage{packagename}
```

Some commonly-used packages are:

- setspace - Provides easy way to change linespacing.

- graphicx - Provides commands to include graphics files.

- fancyhdr - Customizes headers and footers.

- rotating - Provides rotations, especially for figures & tables.

- color - Provides a way to use colors.

### 3. LaTeX Basics ###

The backslash “\” is used to begin all LaTeX commands. 
In the input file (.tex file), words are separated by one or more blank spaces, paragraphs are separated by one (or more) blank lines.


Commands are case-sensitive. Commands are all lowercase unless there’s a good reason to use uppercase. For example:

- \Delta → ∆.

- \delta → δ.

Some commands take arguments, which are enclosed in braces:

```
\textbf{this text will be bold}
```

Certain characters have special meaning to LaTeX. The most common are listed below.

```
|| Char || Input || Special TeX meaning                 ||
||------||-------||-------------------------------------||
|| #    || \#    || Parameter in a macro                ||
|| $    || \$    || Used to begin and end math mode     ||
|| %    || \%    || Used for comments in the input file ||
|| &    || \&    || Tab mark, used in alignments        ||
|| -    || \-    || Used in math mode for subscripts    ||
```

### 4. Some LaTeX Vocabulary ###

#### Commands: ####

Produce text or space: ```\hspace{2in}``` and ```\textit{some italic words}```.

#### Declarations: ####

Affect the following text: ```\large``` prints the following text in a larger font.

Grouping ```{ }``` is often used to limit the scope of a declaration.

Example: ```{\large only this text is big}```.

#### Environments: ####

Receive special processing and are defined by: ```\begin{name} ... \end{name}```.

Example: ```\begin{quote} ... \end{quote}```.

#### Mandatory arguments: ####

Are included in braces ```{ }```: ```\hspace{2in}``` needs the information provided by the argument to generate the space.

#### Optional arguments: ####

Are enclosed in brackets ```[ ]```: ```\documentclass[11pt]{article}``` gives you 11-point type (the default is 10-point type).

#### Some commands that are apply alone: ####

- ```*``` indicates a variation on a command or environment.

- ```\\``` indicates a line break.

- ```\\*``` indicates a line break where a page cannot be broken.

### 5. Example ###

```
\documentclass[12pt]{article}
\usepackage{amsmath}
\title{\LaTeX}
\date{}
    
\begin{document}
  \maketitle
   
  \LaTeX{} is a document preparation system for 
  the \TeX{} typesetting program. It offers 
  programmable desktop publishing features and 
  extensive facilities for automating most 
  aspects of typesetting and desktop publishing, 
  including numbering and  cross-referencing, 
  tables and figures, page layout, 
  bibliographies, and much more. \LaTeX{} was 
  originally written in 1984 by Leslie Lamport 
  and has become the  dominant method for using 
  \TeX; few people write in plain \TeX{} anymore. 
  The current version is \LaTeXe.
   
  % This is a comment, not shown in final output. 
  % The following shows typesetting  power of LaTeX:
  \begin{align}
    E_0 &= mc^2                              \\
    E &= \frac{mc^2}{\sqrt{1-\frac{v^2}{c^2}}}
  \end{align}
   
\end{document}
```

