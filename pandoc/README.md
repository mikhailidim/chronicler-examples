## Pandoc use examples

This folder contains examples for the blog post [Pandoc: My Missing Tool](http://chronicler.tech/pandoc-the-missing-daac-link/).
PDF documents were converted with the [pandoc](https://pandoc.org) converter and pdflatex engine. 

Folder content:
 
* [README.md](#) - This document. Instructions on pandoc installation and sample usage.
* [print-my-document.md](./print-my-document) - Markdown document, to illustrate pandoc usage. 
* [gitmd-out-document.pdf](./gitmd-out-document.pdf)  - Conversion result for GitHub Markdown source.
* [pages-out-document.pdf](./pages-out-document.pdf)  - Conversion result for Commin Markdown source - Page breaks. 
* [toc-out-document.pdf](./toc-out-document.pdf)  - Same as previous + table of content. 
* [all-out-document.pdf](./all-out-document.pdf)  - Combines multiple Markdown sources into single document. 



## Convert Markdown to PDF
There are numerous options, filters and engines that allow you to produce pixel-perfect documents. 
Basic Markdwn to PDF conversion commands are

* Convert document using gitHub flawored markdown. Result  parsing and LaTeX instructons support (page preaks in PDF)

  ```bash
   $ pandoc --from=gfm+smart \
   --output gitmd-my-documents.pdf print-my-document.md
  ```
* Convert with the Common Markdown source. recognizes LaTex instructions

  ```bash
   $ pandoc --from=markdown+smart \
   --output pages-my-documents.pdf print-my-document.md
  ```

* Produces a single PDF from multiple sources 

  ```bash
   $ pandoc --from=markdown+smart \
   --output print-my-documents.pdf *.md
  ```
   
## Installation on Ubuntu

1. Switch to priveleged user and update your system

    ```bash
     $ sudo apt-get update && sudo apt-get upgrade
    ```
2.  Install TexLive PDF engine and fonts

    ```bash
     $ sudo apt-get install texlive-latex-extra \
     texlive-fonts-recommended
    ```
3.  Install Pandoc 
   
    ```bash
     $ sudo apt-get install pandoc
    ```
4.  You may want to install large extra fots collection 
   
    ```bash
     $ sudo apt-get install texlive-fonts-extra
    ```
 5. Test installation 
   
    ```bash
     $ pandoc --list-input-formats
    ```
 
