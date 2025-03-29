# Basic Unix

1. What is a directory?
2. What is a terminal?
3. Basic Unix commands

## How files are stored in your computer? Introduction to directory!

![System Path](workflow.assets/filesystem.png)
*Figure: File system hierarchy. Source: [Introduction to Data Science](https://rafalab.dfci.harvard.edu/dsbook-part-1/productivity/unix.html)*

Questions:
=== "<1>"
    How does the computer distinguish between `f-1.pdf` in `project-1` vs `f-1.pdf` in `project-2`? Don't they have the same name? If we go to the `project-1` folder and open the `f-1.pdf` file, are we asking the computer to open a file named `f-1.pdf` or are we asking more?
=== "<2>"
    Even though they have the same name, the path from home to their "location" are different<br>
    The path to get from home to `f-1.pdf` in the folder `project-1` is <br>
    `home --> projects --> project-1-->figs--> f-1.pdf`<br>
    Or we say, the path to `f-1.pdf` under `project-1` is 
    ```bash
    /home/projects/project-1/figs/f-1.pdf
    ```
    Meanwhile, the path to `f-1.pdf` under `project-2` is
    ```bash
    /home/projects/project-2/figs/f-1.pdf
    ```
=== "<3>"
    So everytime you ask the computer to open/change/delete a file, you are not merely asking the computer to open/change/delete every file with the same name. In fact, you are asking the computer to open/change/delete the file at this specific path.
=== "<4>"
    Therefore, every file path has to be unique! That's why you cannot have files with the same name in the same folder but you can have two files that share a name in different folders.<br>
    In fact, not just files, folders are also located by their paths.
=== "<5>"
    To copy a file/folder path:<br>
    **In Windows**<br>
    Hold Shift and right-click the file or folder, then select "Copy as Path"<br>
    **In MacOS**<br>
    Hold option and right-click the file or folder, then select "Copy as Pathname"<br>
=== "<6>"
    Why do I need to know this?<br>
    Because if you are using R/Python to access to the content of `a.csv`, say in R:
    ```r
    data<-read.csv("a.csv")
    ```
    R would not know how to find your `a.csv`. In order for this to work, you would have to provide the path to `a.csv`:
    ```r
    data<-read.csv("/home/projects/project-2/data/a.csv")
    ```
=== "<7>"
    So if I want to load the code from `code.R` in `project-2`, access `a.csv`, `b.csv` the code would look like:
    ```r
    source("/home/projects/project-2/code.R")
    data_a<-read.csv("/home/projects/project-2/data/a.csv")
    data_b<-read.csv("/home/projects/project-2/data/b.csv")
    ```
    Any problems?
=== "<8>"
    To avoid typing the same path too many times, we have working directory.
    By setting working directory, we let the computer know that it we will always add the working directory path in front of the file name.
=== "<9>"
    The two code chunks below are the same:
    ```r
    setwd("/home/projects/project-2/data")
    data_a<-read.csv("a.csv")
    data_b<-read.csv("b.csv")
    ```
    ```r
    data_a<-read.csv("/home/projects/project-2/data/a.csv")
    data_b<-read.csv("/home/projects/project-2/data/b.csv")
    ```
=== "<10>"
    The syntax to set up working directory is different based on the program language<br>
    For R 
    ```r
    setwd("/home/projects/project-2/data")
    ```
    For Python
    ```r
    import os
    os.chdir("/home/projects/project-2/data")
    ```
=== "<11>"
    Wait! What about `code.R`? Do you still have to do this?
    ```r
    setwd("/home/projects/project-2/data")
    data_a<-read.csv("a.csv")
    data_b<-read.csv("b.csv")
    source("/home/projects/project-2/code.R")
    ```
    Well no! if you set a working directory, it can be accessed via `.`, and its parent (a path before the working directory) can be accessed via `..`.
=== "<12>"    
    Meaning you can access `code.R` via :
    ```r
    setwd("/home/projects/project-2/data")
    data_a<-read.csv("a.csv")
    data_b<-read.csv("b.csv")
    source("../code.R") 
    # working directory is /home/projects/project-2/data 
    # and .. means /home/projects/project-2
    ```
    Or
    ```r
    setwd("/home/projects/project-2")
    data_a<-read.csv("./data/a.csv")
    data_b<-read.csv("./data/b.csv")
    source("./code.R") 
    # working directory is /home/projects/project-2
    ```

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

## What is a terminal
A text-based interface that allows you to interact directly with your computer
### RStudio
Tools >> Terminal >> New Terminal
### Visual Code Studio
Terminal >> New Terminal
### Test if terminal is running okie?
```bash
pwd
```
This return your current working directory<br>
If you are using terminal in RStudio and it return the error `pwd` is not recognized as an internal or external command<br>
Please <br>
1. Open Tools>> Global Options>>Terminal. Then choose Git Bash for New terminals open with>> Apply<br>
2. Tools >> Terminal >> New Terminal<br>
## But why are we learning about terminal? What are Unix Commands?
1. Unix allow for quick and efficient file management <br>
2. Many research projects require you to do your computation on remote servers and high-performance computing clusters. Unix commands help you to communicate with these remote clusters <br>
3. If you are an expert, which I am not, mastering Unix will save you a lot of time since you are communicating directly with your computer

## Basic Unix commands

=== "<1>"
    `pwd`
    ```bash
    pwd
    ```
    Print your working directory
=== "<2>"
    `echo`
    ```bash
    echo "Hello NYU"
    ```
    echo is command that prints the argument you provide
=== "<3>"
    `~`
    ```bash
    echo ~
    ```
    `~` is short for your home directory (NOT WORKING DIRECTORY). This is your default working directory.
=== "<4>"
    `ls`
    ```bash
    ls
    ```
    `ls` is short for list. This will displays the (non-hidden) contents of your current working directory
=== "<5>"
    `cd`: Change your working directory
    ```bash
    cd <working directory>
    ```
    Example:
    ```bash
    cd ~/Desktop
    ```
    This change your working directory to the Desktop folder.<br>
    Depend on the structure of your computer, the Desktop folder may not be in your home directory. Use `ls` to see what folder is in your current working directory
=== "<6>"
    `mkdir`: Make a new directory<br>
    `rmdir`: Remove an empty directory<br>
    `rm -r`: Remove a non-empty directory DANGEROUS!! No do over in the terminal!
    ```bash
    mkdir <new working directory>
    ```
    Example:
    ```bash
    mkdir ./NYU1111 
    mkdir ~/Desktop/NYU1618
    ```
    The first creates a new folder called `NYU1111` in the current working directory.<br>
    The second command creates a new folder called `NYU1618` in the `Desktop` folder.<br>
    We can remove these newly created empty folder
    ```bash
    rmdir ./NYU1111 
    rmdir ~/Desktop/NYU1618
    ```
    
[Interested in more advance Unix?](https://rafalab.dfci.harvard.edu/dsbook-part-1/productivity/unix.html#advanced-unix)