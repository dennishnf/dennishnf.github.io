
## Create presentations in LaTeX with Beamer Package ##

Beamer is a really easy-to-use package to create nice PDF presentations. Changing a parameter at the beginning of the document allows you to output either a standard presentation, or handouts or even the whole presentation as a standard LaTeX article.

Homepage: [https://bitbucket.org/rivanvx/beamer/wiki/Home](https://bitbucket.org/rivanvx/beamer/wiki/Home)!.

To start our presentation we need to set the document class to ‘beamer’. Next we’ll select a theme using the ```\usetheme``` command. For our example we’ll use the ‘Madrid’ theme.

```
\documentclass{beamer}
\usetheme{Madrid}   % Use a theme, beamer class comes with a number of default slide themes
```

Also, you can use a different theme. Now to complete the preamble we’ll enter title, subtitle, author, institute and date information.

```
\title{My Presentation}
\subtitle{Using Beamer}
\author{Dennis Nunez-Fernandez}
\institute{National University of Engineering}
\date{\today}
```

Just like any other LaTeX document we need to enclose the document in the document environment.

```
\begin{document}
<document goes here>
\end{document}
```

Now to add slides in we use the ‘frame’ environment. We’ll make our first frame the title page by entering the ```\titlepage command```.

```
\begin{frame}
\titlepage   % Print the title page as the first slide
\end{frame}
```

Now create a frame with a table of contents using the ```\tableofcontents``` command.

```
\begin{frame}
\frametitle{Overview}
\tableofcontents
\end{frame}
```

Just like with a normal LaTeX document we want to split our presentation up into sections and subsections. Let’s add in some sections and then add some frames to each section. Then we can give our frames titles using the ```\frametitle``` command and add in some text. For example:

```
\section{First Section}
   
\subsection{Subsection Example}
   
\begin{frame}
\frametitle{Title 1}
Text here!.
\end{frame}
```

Finally, Beamer does not support BibTeX so references must be inserted manually as below:

```
\footnotesize{
\begin{thebibliography}{99}   % Beamer does not support BibTeX
\bibitem[Smith, 2012]{p1} John Smith (2012)
\newblock Title of the publication
\newblock \emph{Journal Name} 12(3), 45 -- 678.
\end{thebibliography}
}
```

To sum up, put together all the parts described before: (copy and test in [https://www.overleaf.com/docs?template=blank](https://www.overleaf.com/docs?template=blank)!).

```
\documentclass{beamer}
\usetheme{Madrid}   % Use a theme, beamer class comes with a number of default slide themes
    
\title{My Presentation}
\subtitle{Using Beamer}
\author{Dennis Nunez-Fernandez}
\institute{National University of Engineering}
\date{\today}
    
    
\begin{document}
    
    
\begin{frame}
\titlepage   % Print the title page as the first slide
\end{frame}
    
    
\begin{frame}
\frametitle{Overview}
\tableofcontents
\end{frame}
     
    
\section{First Section}
     
\subsection{Subsection Example}
     
\begin{frame}
\frametitle{Title 1}
Text here!.
\end{frame}
    
\begin{frame}
\frametitle{Title 2}
Text here!.
\end{frame}
   
   
\section{Second Section}
   
\begin{frame}
\frametitle{Title A}
Text here!.
\end{frame}
   
\begin{frame}
\frametitle{Title B}
Text here!.
\end{frame}
    
    
\section{Bibliography}
    
\begin{frame}
\frametitle{References}
\footnotesize{
\begin{thebibliography}{99}   % Beamer does not support BibTeX
\bibitem[Smith, 2012]{p1} John Smith (2012)
\newblock Title of the publication
\newblock \emph{Journal Name} 12(3), 45 -- 678.
\end{thebibliography}
}
\end{frame}
    
    
\end{document} 
```


### Resources ###

- [https://es.sharelatex.com/blog/2013/08/13/beamer-series-pt1.html](https://es.sharelatex.com/blog/2013/08/13/beamer-series-pt1.html)!.

