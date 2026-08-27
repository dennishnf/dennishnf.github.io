
## Preparing a bibliography in LaTeX ##

For any academic/research writing, incorporating references into a document is an important task. Fortunately, LaTeX has a variety of features that make dealing with references much simpler, including built-in support for citing references. However, a much more powerful and flexible solution is achieved thanks to an auxiliary tool called BibTeX (which comes bundled as standard with LaTeX). Recently, BibTeX has been succeeded by BibLaTeX, a tool configurable within LaTeX syntax.

BibTeX provides for the storage of all references in an external, flat-file database. (BibLaTeX uses this same syntax.) This database can be referenced in any LaTeX document, and citations made to any record that is contained within the file. This is often more convenient than embedding them at the end of every document written; a centralized bibliography source can be linked to as many documents as desired (write once, read many!). Of course, bibliographies can be split over as many files as one wishes, so there can be a file containing sources concerning topic A (a.bib) and another concerning topic B (b.bib). When writing about topic AB, both of these files can be linked into the document (perhaps in addition to sources ab.bib specific to topic AB).

### Citations ###

To actually cite a given document is very easy. Go to the point where you want the citation to appear, and use the following: ```\cite{cite_key}```, where the 'cite_key' is that of the bibitem you wish to cite. When LaTeX processes the document, the citation will be cross-referenced with the bibitems and replaced with the appropriate number citation. The advantage here, once again, is that LaTeX looks after the numbering for you. If it were totally manual, then adding or removing a reference would be a real chore, as you would have to re-number all the citations by hand.

Example:

```
... Instead of WYSIWYG editors, typesetting systems like A or B \cite{lamport94} can be used. ...
```

### Referring more specifically ###

Sometimes you want to refer to a certain page, figure or theorem in a text book. For that you can use the arguments to the \cite command:

```
\cite[chapter, p.~215]{citation01}
```

The argument, "p. 215", will show up inside the same brackets. Note the tilde in [p.~215], which replaces the end-of-sentence spacing with a non-breakable inter-word space. There are two reasons: end-of-sentence spacing is too wide, and "p." should not be separated from the page number.

### Multiple citations ###

When a sequence of multiple citations are needed, you should use a single ```\cite{}``` command. The citations are then separated by commas. Here's an example:

```
\cite{citation01,citation02,citation03}
```

The result will then be shown as citations inside the same brackets, depending on the citation style.

### No cite ###

If you only want a reference to appear in the bibliography, but not where it is referenced in the main text, then the ```\nocite{}``` command can be used, for example:

```
Lamport showed in 1995 something...  \nocite{lamport95}.
```

A special version of the command, ```\nocite{*}```, includes all entries from the database, whether they are referenced in the document or not.

### BibTex .bib file ###

A BibTeX database is stored as a .bib file. It is a plain text file, and so can be viewed and edited easily. The structure of the file is also quite simple. An example of a BibTeX entry:

```
@article{greenwade93,
    author  = "George D. Greenwade",
    title   = "The {C}omprehensive {T}ex {A}rchive {N}etwork ({CTAN})",
    year    = "1993",
    journal = "TUGBoat",
    volume  = "14",
    number  = "3",
    pages   = "342--351"
}
```

### Standard templates ###

Be careful if you copy the following templates, the % sign is not valid to comment out lines in bibtex files. If you want to comment out a line, you have to put it outside the entry.

#### @article ####

```
@article{Xarticle,
    author    = "",
    title     = "",
    journal   = "",
    %volume   = "",
    %number   = "",
    %pages    = "",
    year      = "XXXX",
    %month    = "",
    %note     = "",
}
```

#### @book ####

```
@book{Xbook,
    author    = "",
    title     = "",
    publisher = "",
    %volume   = "",
    %number   = "",
    %series   = "",
    %address  = "",
    %edition  = "",
    year      = "XXXX",
    %month    = "",
    %note     = "",
}
```

#### @booklet ####

```
@booklet{Xbooklet,
    %author   = "",
    title     = "",
    %howpublished   = "",
    %address  = "",
    %year      = "XXXX",
    %month    = "",
    %note     = "",
}
```

#### @conference ####

```
@conference{Xconference,
    author    = "",
    title     = "",
    booktitle = "",
    %editor   = "",
    %volume   = "",
    %number   = "",
    %series   = "",
    %pages    = "",
    %address  = "",
    year      = "XXXX",
    %month    = "",
    %publisher= "",
    %note     = "",
}
```

#### @inbook ####

```
@inbook{Xinbook,
	author	= "",
	editor	= "",
	title	= "",
	chapter	= "",
	pages	= "",
	publisher= "",
	%volume	= "",
	%number	= "",
	%series	= "",
	%type	= "",
	%address= "",
	%edition= "",
	year	= "",
	%month	= "",
	%note	= "",
}
```

#### @incollection ####

```
@incollection{Xincollection,
	author	= "",
	title	= "",
	booktitle= "",
	publisher= "",
	%editor	= "",
	%volume	= "",
	%number	= "",
	%series	= "",
	%type	= "",
	%chapter= "",
	%pages	= "",
	%address= "",
	%edition= "",
	year	= "",
	%month	= "",
	%note	= "",
}
```

#### @inproceedings ####

```
@inproceedings{Xinproceedings,
	author		= "",
	title		= "",
	booktitle	= "",
	%editor		= "",
	%volume		= "",
	%number		= "",
	%series		= "",
	%pages		= "",
	%address	= "",
	%organization	= "",
	%publisher	= "",
	year		= "",
	%month		= "",
	%note		= "",
}
```

#### @manual ####

```
@manual{Xmanual,
	title		= "",
	%author		= "",
	%organization	= "",
	%address	= "",
	%edition	= "",
	year		= "",
	%month		= "",
	%note		= "",
}
```

#### @masterthesis ####

```
@mastersthesis{Xthesis,
    author    = "",
    title     = "",
    school    = "",
    %type     = "diploma thesis",
    %address  = "",
    year      = "XXXX",
    %month    = "",
    %note     = "",
}
```

#### @misc ####

```
@misc{Xmisc,
    %author    = "",
    %title     = "",
    %howpublished = "",
    %year     = "XXXX",
    %month    = "",
    %note     = "",
}
```

#### @phdthesis ####

```
@phdthesis{Xphdthesis,
	author		= "",
	title		= "",
	school		= "",
	%address	= "",
	year		= "",
	%month		= "",
	%keywords	= "",
	%note		= "",
}
```

#### @proceedings ####

```
@proceedings{Xproceedings,
	title		= "",
	%editor		= "",
	%volume		= "",
	%number		= "",
	%series		= "",
	%address	= "",
	%organization	= "",
	%publisher	= "",
	year		= "",
	%month		= "",
	%note		= "",
}
```

#### @techreport ####

```
@techreport{Xtreport,
    author    = "",
    title     = "",
    institution = "",
    %type     = "", 
    %number   = "",
    %address  = "",
    year      = "XXXX",
    %month    = "",
    %note     = "",
}
```

#### @unpublished ####

```
@unpublished{Xunpublished,
	author	= "",
	title	= "",
	%year	= "",
	%month	= "",
	note	= "",
}
```

### A few additional examples ###

Below you will find a few additional examples of bibliography entries. The first one covers the case of multiple authors in the Surname, Firstname format, and the second one deals with the incollection case.

```
@article{AbedonHymanThomas2003,
  author = "Abedon, S. T. and Hyman, P. and Thomas, C.",
  year = "2003",
  title = "Experimental examination of bacteriophage latent-period evolution as a response to bacterial availability",
  journal = "Applied and Environmental Microbiology",
  volume = "69",
  pages = "7499--7506"
},
   
@incollection{Abedon1994,
  author = "Abedon, S. T.",
  title = "Lysis and the interaction between free phages and infected cells",
  pages = "397--405",
  booktitle = "Molecular biology of bacteriophage T4",
  editor = "Karam, Jim D. Karam and Drake, John W. and Kreuzer, Kenneth N. and Mosig, Gisela
            and Hall, Dwight and Eiserling, Frederick A. and Black, Lindsay W. and Kutter, Elizabeth
            and Carlson, Karin and Miller, Eric S. and Spicer, Eleanor",
  publisher = "ASM Press, Washington DC",
  year = "1994"
},
```

If you have to cite a website you can use @misc, for example:

```
@misc{website:fermentas-lambda,
      author = "Fermentas Inc.",
      title = "Phage Lambda: description \& restriction map",
      month = "November",
      year = "2008",
      url = "http://www.fermentas.com/techinfo/nucleicacids/maplambda.htm"
},
```

The note field comes in handy if you need to add unstructured information, for example that the corresponding issue of the journal has yet to appear:

```
@article{blackholes,
      author="Rabbert Klein",
      title="Black Holes and Their Relation to Hiding Eggs",
      journal="Theoretical Easter Physics",
      publisher="Eggs Ltd.",
      year="2010",
      note="(to appear)"
}
```

### Bibliography styles ###

There are several different ways to format lists of bibliographic references and the citations to them in the text. These are called citation styles, and consist of two parts: the format of the abbreviated citation (i.e. the marker that is inserted into the text to identify the entry in the list of references) and the format of the corresponding entry in the list of references, which includes full bibliographic details.

Abbreviated citations can be of two main types: numbered or textual. Numbered citations (also known as the 'Vancouver referencing system': [https://en.wikipedia.org/wiki/Vancouver_system](https://en.wikipedia.org/wiki/Vancouver_system)!) are numbered consecutively in order of appearance in the text, and consist in Arabic numerals in parentheses (1), square brackets [1], superscript1, or a combination thereof. Textual citations (also known as the 'Harvard referencing system': [https://en.wikipedia.org/wiki/Parenthetical_referencing](https://en.wikipedia.org/wiki/Parenthetical_referencing)!) use the author surname and (usually) the year as the abbreviated form of the citation, which is normally fully (Smith 2006) or partially enclosed in parenthesis, as in Smith (2006). The latter form allows the citation to be integrated in the sentence it supports.

Here are some more often used styles:

```
|| Style  Name || Author  Name  Format || Reference Format || Sorting       ||
||-------------||----------------------||------------------||---------------||
|| plain       || Homer Jay Simpson    || [ID]             || by author     ||
|| unsrt       || Homer Jay Simpson    || [ID]             || as referenced ||
|| abbrv       || H. J. Simpson        || [ID]             || by author     ||
|| alpha       || Homer Jay Simpson    || Sim95            || by author     ||
|| abstract    || Homer Jay Simpson    || Simpson-1995a    ||               ||
|| acm         || Simpson, H. J.       || [ID]             ||               ||
|| authordate1 || Simpson, Homer Jay   || Simpson, 1995    ||               ||
|| apacite     || Simpson, H. J. (1995)|| Simpson1995      ||               ||
|| named       || Homer Jay Simpson    || Simpson 1995     ||               ||
||             ||                      ||                  ||               ||
```

However, keep in mind that you will need to use the natbib package to use most of these.

### Getting current LaTeX document to use your .bib file ###

At the end of your LaTeX file (that is, after the content, but before ```\end{document}```), you need to place the following commands:

```
\bibliographystyle{plain}
\bibliography{sample1,sample2,...,samplen} 
% Note the lack of whitespace between the commas and the next bib file.
```

### Why won't LaTeX generate any output? ###

The addition of BibTeX adds extra complexity for the processing of the source to the desired output. This is largely hidden from the user, but because of all the complexity of the referencing of citations from your source LaTeX file to the database entries in another file, you actually need multiple passes to accomplish the task. This means you have to run LaTeX a number of times.

### Including URLs in bibliography ###

As you can see, there is no field for URLs. One possibility is to include (into .bib file) the Internet addresses in ```howpublished``` field of ```@misc``` or ```note``` field of ```@techreport```, ```@article```, ```@book```:

```
howpublished = "\url{http://www.example.com}"
```

,or:

```
note = "\url{http://www.example.com}"
```

### Bibliography in the table of contents ###

If you want your bibliography to be in the table of contents, just add the following two lines just before the thebibliography environment:

```
\clearpage% or cleardoublepage
\addcontentsline{toc}{chapter}{Bibliography}
```

### Resources ###

- [https://en.wikibooks.org/wiki/LaTeX/Bibliography_Management](https://en.wikibooks.org/wiki/LaTeX/Bibliography_Management)!.


