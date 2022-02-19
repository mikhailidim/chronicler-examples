This folder contains sample markdown document and generated PDF.
the PDF document {- INSERT LINK -} produced with the [pandoc](https://pandoc.org) converter and pdflatex engine

## Convert Markdown to PDF
There are numerous options, filters and engines that allow you to produce pixel-perfect documents. 
Basic Markdwn to PDF conversion commands are

* Convert with the strict Markdown parsing and LaTeX instructons support (page preaks in PDF)

  ```shell
   $ pandoc --from=markdown+smart --output print-my-documents.pdf print-my-documents.md
  ```
* Convert with the Github Markdown parsing  (ignores page preaks commands)

  ```shell
   $ pandoc --from=gfm+smart --output print-my-documents.pdf print-my-documents.md
  ```

* Produces a single PDF from multiple sources 

  ```shell
   $ pandoc --from=markdown+smart --output print-my-documents.pdf *.md
  ```
   
## Installation on Ubuntu

1. Switch to priveleged user and update your system

   ```shell
    ubuntu@host$ sudo apt-get update && sudo apt-get upgrade
   ```
2.  Install TexLive PDF engine and fonts

    ```bash
     ubuntu@host$ sudo apt-get install texlive-latex-extra texlive-fonts-recommended
    ```
3.  Install Pandoc 
   
    ```bash
     ubuntu@host$ sudo apt-get install pandoc
    ```
4.  You may want to install large extra fots collection 
   
    ```bash
     ubuntu@host$ sudo apt-get install texlive-fonts-extra
    ```
 5. Test installation 
   
    ```bash
     ubuntu@host$ pandoc --list-input-formats
    ```
 
