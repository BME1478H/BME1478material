---
title: Introduction to Bash
author: Sara
---
## Lesson Preamble
### Lesson objectives:
- get familiar with terms "command line", "terminal", "console", "shell", "interactive prompt", "git-bash", etc.
- learn basics of interacting with a computer using Bash (the Bourne Again Shell) by typing commands
### Lesson prerequisites
- have `bash` installed: refer to [installation manual]()
### Lesson Outline
- why command line
- basics of Unix Shell
- finding available commands and syntax
- combine commands, pipes, etc.
- making scripts
-----

## Why using a command line?
The command line is a very precise and powerful way to interact with a computer. Because it is a scripting language, you can automate and perform complex tasks without much overhead.

Shells are particularly well suited to interacting with files and running programs -- possibly your own! Not having a graphical interface turns out to be a strength, because it makes remote computing simple and reliable.

At first, typing in commands will feel a bit cumbersome, but like learning any language the only way to get better is with practice. Lucky for us, bash is based on English with a very simplified grammar.

**Example shells**
In this lesson, we're using bash, but most shells support all of the features covered here. Sometimes with different syntax. Some of the more modern shells include:
- Bash
- Zsh
- Fish (the Friendly Interactive Shell)
- rc   ("run commands" - the Plan 9 shell)
- Powershell (the better Windows shell)
Of the above, Powershell is the most different. The others are all based on the *Bourne shell*, but with many additions to make it easier to work with.

## Basics of Bash command syntax
The basic unit for a command line interpreter (CLI) is a *command*. This is a line that starts with a *commmand name* followed (optionally) by *arguments*. Examples of commands are,
```
ls
ls -a
cd Documents
rm unwanted_file
```

Some arguments activate/deactivate options. Usually they are prefixed by a dash `-`. For example, `ls -a` lists **a**ll** files, even hidden ones. Sometimes they are longer than one character, in which case they *usually* have two dashes e.g. `--help`.

The command line options (aka flags or switches) can usually be found in the man pages. Often there will be a `-h` or `--help` flag to display common usage.

# Common commands/tasks
There are many commands available -- any executable or built-in command. The following are some that are used more often:

- ls (-alhS...)
- cd (-)
- cp
- mv
- mkdir
- rm (-r)
- head/tail (-nf)
- grep
- man

Many command names are the first two consonants of what they do: **c**o**p**y, **l**i**s**t, **m**o**v**e, **r**e**m**ove**. Others are acronyms/abbreviations: **c**hange **d**irectory, **man**ual, **s**tream **ed**itor.**

- To list files, use `ls`. Common flags include `-a` for all files, `-l` for the full details (size, date, permissions...), `-h` for "human-readable" file sizes,  `-S` to sort by file size.
- Change directories with `cd`. On many systems, `cd` with no arguments changes to your home directory (`cd ~`), and `cd -` changes to your previous directory, `cd .. ` goes one directory up from your current directory.
- Copy and move files with `cp` and `mv`. The last argument is the new filename/directory. E.g. `cp a.py b.py c/` copies files `a.py` and `b.py` into the `c` directory. **Warning** `cp` and `mv` will overwrite files without warning you.
- Remove files with `rm`. The files cannot be recovered easily, and you won't be asked for confirmation. Directories won't be removed unless you use `-r` (for **r**ecursive**).
- Probe contents of files with `head`, `tail`, `grep`.
  - `head -n 10` shows the first 10 lines, and
  - `tail` shows the last few lines in a file.
  - To search for every line that contains a string, use `grep`. E.g. `grep cat animals.txt` finds the string "cat" in the file `animals.txt`.
- Finally, `man` provides manual pages for most commands that you can use from bash. Syntax: `man <command-name>`.

### challenge
1) copy the provided folder BashTest at your Desktop, move to that directory and try `grep cat animals.txt`, what happens? try `grep pony animals.txt`
2) try these and figure out what they do
```
date
man date
vim hello.txt
sed -e 's/cat/dog/g' pets-file
echo 'hello world'
find . -not -name '*.py' -type f -exec rm {} +
which python
cal
```

## Directories and Files

Many commands end up using files, so it's good to have an idea of how to name them. Files are specified in arguments with a *pathname*.

    [directory-name/]filename

Except for a few cases, the pathname is relative to the *current working directory*. So if you are in your home directory, `Desktop/my_script.py` refers to the `my_script.py` file in your own Desktop folder, not anyone else's. If you're in your `Desktop` folder, then `Desktop/my_script.py` refers to a file inside the Desktop folder inside your Desktop folder (which probably isn't there), but `my_script.py` refers to the previous file.

Try it out: from your home directory, run the following commands (`touch` creates a file):

```
cd desktop
mkdir Project1
cd Project1
mkdir scripts
mkdir docs
touch scripts/script_a.py
touch docs/manuscript
touch docs/script_b.py
ls
```

In the list of files, you should see the `scripts` directory, but no `script_a`. Now execute
```
ls scripts
```

## Relative and Absolute paths
Sometimes, you'll need to access files from another location in the file hierarchy. With relative paths, you can use .. to access the parent directory, so `../../BashTest/source` goes up two directories, then down through BashTest and source. So you should be in Project1 now, if you change directory to scripts: `cd scripts` then `../docs` goes up one directories, then down through `docs`, or try `../../BashTest/source` if you have copied the provided folder. This can get cumbersome if you're not sure exactly how many times you need to go up.

Instead, there are absolute paths. On Unix systems, there is one root node for the file-system: `/`. All files are in subdirectories of root. Any pathname starting with `/` is an absolute path starting from the root.

Try out `ls /`

Another special location is your home directory. The short-form is `~/`. You can also short-form any user's home-directory with `~username/`.
Most of the time working with scripts, you should use relative paths, because one cannot assume the state of another's file system.

let's try moving script_b from docs to scripts, because that's not where it should be. We assume we are in scripts directory:
note: you can run `pwd` to make sure you're in the desired directory. if not, change directories before continuing
`mv ../docs/script_b.py script_b.py`


## Globbing

If you want to pass more than one filename as an argument, you can use *globbing*. The special patterns for globbing are:

- `*` Match any string of arbitrary length
- `?` Match any single character
- `[]` Match any of the characters within square brackets.

### challenge:
make a file named main.py in scripts directory.
Try copying every file with `script` to docs?
remove the files that have `a` from docs

## Getting more powerful

Some true strengths of the command line come from combining commands. This is the "Unix philosophy" of having many small programs that perform their jobs well. These units can be combined to perform more complicated tasks.

## Pipes (stdin/out)
Commands can be strung together with pipes `|`. Commands typically have an input (stdin) and an output (stdout). The pipe attaches the output of one command into the input of another.

This is easier to see with commands like `cat` and `head`. Try these out using the BashTest directory:

```
head animals
cat animals
cat animals | head
ls | head -n2
head
grep 'fish' animals | wc -l
```

Can you figure out how each of these commands behave from the above?

You can also redirect output into a file with `>` or `>>`. The former over-writes the file, while `>>` appends to the file if it exists. For example,

```
grep 'fish' animals > list-of-fish
```

Will create a new file with a list of fish. Files can also be used for `stdin` using the `<` character. The above command would be

```
grep fish < animals > list-of-fish
```

Or, with pipes,

```
grep fish < animals | wc -l > number-of-fish
```

Note that `<` appears after the first command, because each line must start with a command. What would happen if you tried `animals > grep fish`?

Another stream worth mentioning is `stderr` (for standard error), which is how most errors or warnings are reported. This can be accessed with `2>`, which is input redirection symbol.  For example, so save compiler errors for later, try
  gcc some-code.c -o my-program 2> log-file
(gcc: GNU Compiler Collection)

## Multiple commands in a line
You can also run multiple commands without piping their inputs/outputs together. There are a few ways characters for this:
- `;` separates commands like they are on separate lines
- `&&` does the next command if the previous one succeeds
- `||` does the next command if the previous one fails
- `&` runs the previous command in the "background"

## Variables
Bash happens to be a full scripting language (aka bash script). As part of that are variables. They can be assigned with `=`. Try the following:
```
    myOne=1
    myName=John
    mySubject = Physics
```

What happened in the last example? In bash, there cannot be a space between the variable name and `=`. Now let's try accessing our variables.
    echo myName

Why doesn't that work? Bash has no way of knowing whether `myName` is a variable name or string-literal, so it always assumes a string. To access variables, we use `$varname`.
```
    echo $myName
    echo $myOne
    echo $mySubject
```
Note that if a variable isn't defined, then it simply returns an empty string. Everything in bash is a string. Even numbers are strings which are cast to ints for arithmetic.

There are special variables called *environment variables* which are used by bash and other programs to affect behaviour. One of the most important ones is `$PATH`:
```
    echo $PATH
```

The path is a list of all directories to search for commands. To add a directory to your path,
```
    export PATH="${HOME}/.local/bin:${PATH}"
```
That adds the `~/.local/bin` directory to my path, so any programs installed there are now first-class commands in this bash session.

All defined environment variables can be found with the `env` command. For example,

    `env | sed 's/=.*$//'`

will print all defined variable names.

### challenge
`sed` (**s**tream **ed**itor**) performs functions like insertion, deletion, search and replace(substitution). find out what does the rest of the syntax means.  

## Loops
Repetitive tasks call for loops! Bash has loops:

```
for i in 1 2 3 4 5; do
    echo The value of i is $i
done
```

The basic syntax is
```
for variable_name in a_list; do
    [commands]
done
```

The list is just like an argument list to a command: each item is a string, separated by spaces. Try using different values in the for loop, or putting quotes around different items.

### Challenge
so, if you want to make a series of new directories (let's say 10) for datasets to populate later, instead of doing right click and make new folder, try do it in bash.
answer:
```
for num in $(seq 01 10); do
mkdir "daraset$num"
done
```

One common task I have is performing a command on each file in a directory. For example, consider adding a license preamble to every sourcefile in your project. If the license is in `LICENSE.txt`, then

```
for fn in *.py; do
    cat LICENSE.txt $fn > tmpfile
    mv tmpfile $fn
done
rm tmpfile
```

Unfortunately, there isn't a simple, universal way to prepend a file without a temporary file.

## Running scripts

Scripts are files that contain lists of commands, very much like scripts in Python, Ruby, R, Perl, etc. They can be run in much the same way.

    bash myscript.sh

Another trick is to use the "shebang" syntax at the beginning of a file

```
#!/bin/bash

echo "The first argument is $1"

echo "All of the arguments are"
for i in $*; do
    echo $i
done
```

If the file is made executable (`chmod u+x myscript.sh`), then it can be executed with `./myscript.sh`. You can take it one step further and insert it in your path.

The shebang syntax can be used for any interpreted language, like for Python:

    #!/usr/bin/env python

# Wrapping up
At first, using the command line might seem cumbersome, and like a lot to remember. But this is just like learning any language: at first you will be limited by your vocabulary, but with time and practice you'll be able to do much more.

A tools you may want to look into when working with more files/strings are:
 - Regular expressions. Used in tools like `grep` and `sed` are great for searching in strings/files.
 - `find` can do some really powerful things when working with files.
 - `xargs` creates/executes commands built from `stdin`

### challenge
Try these commands:
- If the output of a command is very long, use `less`:
     long-output-command | less

- You can then scroll up and down and quit less by typing `q`.

- Joining (concatenating) files with `cat`.
     cat file1 file2 > both-files

- Appending a line to a file
     echo "put this at the end" >> some-file

- Search and replace in a file
     sed -e 's/cat/dog/g' < animals > no-cats


## acknowledgments
Taken from UofT coders lesson, [Introduction to shells and the command-line with bash](https://github.com/UofTCoders/studyGroup/tree/gh-pages/lessons/misc/bash-intro/), by John Ladan
