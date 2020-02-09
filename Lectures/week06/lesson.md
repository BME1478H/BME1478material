---
title: 'Command line Python and Git version control'
---
## Lesson objectives:

Part 1:
  - Understand the difference between running code in Jupyter Notebook command line
  - Use the values of command-line arguments in a program
  - Handle flags and files separately in a command-line program.
  - Read data from standard input in a program so that it can be used in a pipeline.
Part 2
  - Learn basics of version control using Git and GitHub
  - Create a repository
  - Track changes
  - Set up remotes
  - Sync repositories

# Command line python
The Jupyter Notebook and other interactive tools are great for prototyping code and exploring data, but we ultimately want to use our program in a pipeline to process many data files, run it with many different parameters, or combine it with other programs in the data analysis pipeline. The easiest way to do this effectively is often to turn our code into a standalone program that can be run in a shell terminal just like other command-line tools (Taschuk and Wilson, 2017).


> In this lesson we are switching from typing commands in a Python interpreter to typing commands in a shell terminal window (such as Git-bash).
> When you see a $ in front of a command that tells you to run that command in the shell rather than the Python interpreter.

Note before we start: positioning our terminal: open your terminal in the Project directory that we defined in the previous lesson
Project
|__code
|__data
and cd to the code directory.

## Command-Line Arguments
Using Atom (or any text editor of your choice), save the following commands in the a text file called `sys_version.py`:

```Bash
atom  `sys_version.py`
```
when open, copy these Python commands in the text file and hit save.

```Python
import sys
print ('version is', sys.version)
```

alternatively:
  - open Atom
  - hit `New File`,
  - type the above Python commands and
  - save it with `sys_version.py` name.

note: .py files are basically text files.

The first line imports a library called sys, which is short for “system”. It defines values such as `sys.version`, which describes which version of Python we are running. We can run this script from the command line like this:

```Bash
$ python sys_version.py
```
you will get an output that gives you the version of Python installed on your machine, something like this:

```text
version is 3.6.5 |Anaconda, Inc.| (default, Mar 29 2018, 13:32:41) [MSC v.1900 64 bit (AMD64)]
```
> Note for Windows users: if you get an error or no output, it's probably because of a conflict with the Python that is added into the Windows Store.
> type "manage app execution aliases" into the Windows search prompt and disable the store versions of Python. see [here](https://stackoverflow.com/questions/56974927/permission-denied-trying-to-run-python-on-windows-10) for more info.

Let's create another file called `argv_list.py` and save the following text to it.

```Python
import sys
print('sys.argv is', sys.argv)
```

The strange name `argv` stands for “argument values”. Whenever Python runs a program, it takes all of the values given on the command line and puts them in the list `sys.argv` so that the program can determine what they were. If we run this program with no arguments:

```text
sys.argv is ['argv_list.py']
```
the only thing in the list is the full path to our script, which is always `sys.argv[0]`. If we run it with a few arguments, however:

```Python
$ python argv_list.py first second third
```
then Python adds each of those arguments to that magic list.

```text
sys.argv is ['argv_list.py', 'first', 'second', 'third']
```
With this in hand, let’s continue with the example of data analysis for our inflammation study. Here we may want a program that reads a dataset and prints the average inflammation per patient.

Let's change directory to our data folder: `cd ../data`

 The first step is to write a function that outlines our implementation. Open a new file in Atom, named `stats_01.py` (remember that you have set Atom as the default editor in bash and you can open it right there)

 ```Bash
 $ atom ../code/stats_01.py
 ```
and copy the following and save:

```python
import sys
import numpy


def average_inflammation():
    script = sys.argv[0]
    filename = sys.argv[1]
    data = numpy.loadtxt(filename, delimiter=',')
    print('running ', script)
    for row_mean in numpy.mean(data, axis=1):
        print(row_mean)
```
This function gets the name of the script from `sys.argv[0]`, because that’s where it’s always put, and the name of the file to process from `sys.argv[1]`.

let's run this:

```Bash
$ python ../code/stats_01.py inflammation-01.csv
```
There is no output because we have defined a function, but haven’t actually called it. Similar to when we defined a function in a cell in Jupyter Notebook and execute the cell, which we have seen that nothing happens. Let's add a call to the `average_inflammation` function to our script:

```Bash
$ atom ../code/stats_02.py
```

```Python
import sys
import numpy


def average_inflammation():
    script = sys.argv[0]
    filename = sys.argv[1]
    data = numpy.loadtxt(filename, delimiter=',')
    print('running ', script)
    for row_mean in numpy.mean(data, axis=1):
        print(row_mean)

if __name__ == '__main__':
   average_inflammation()
```
Why is the call to our function is in an if statement and what does it mean?
`__name__ ` is a special built-in variable in Python: when a python script is run directly this variable is set as `__main__`, and when the script is imported within another script, the `__name__` variable is set to the name of that script (e.g. here 'stats_01'). When we import a script, we don't necessarily expect an output from the function(s) in the script, we import the script to call the functions later (recall we import numpy and then use the functions later). But when we run the script directly, we want to call and see the outputs of the functions. Therefore, we put the call for the function in a conditional statement to only be executed when the script is run directly:

```Python
if __name__ == '__main__':
    `whatever function that produces output`
````

now run that in terminal for one of the inflammation datasets:

```Bash
$ python ../code/stats_02.py inflammation-01.csv
```
```text
running  ../code/stats_02.py
5.45
5.425
6.1
5.9
5.55
6.225
5.975
6.65
6.625
6.525
6.775
5.8
6.225
5.75
5.225
6.3
6.55
5.7
5.85
6.55
5.775
5.825
6.175
6.1
5.8
6.425
6.05
6.025
6.175
6.55
6.175
6.35
6.725
6.125
7.075
5.725
5.925
6.15
6.075
5.75
5.975
5.725
6.3
5.9
6.75
5.925
7.225
6.15
5.95
6.275
5.7
6.1
6.825
5.975
6.725
5.7
6.25
6.4
7.05
5.9
```
For the rest of the tutorial we're going to use the small*.csv files in the data set, since showing 60 lines of output per file makes the tutorial messy. These files only contain three days of data for two patients. we can easily see the whole content in the terminal:

```Bash
$ cat small-01.csv
```
```text
0,0,1
0,1,2
```
and running our script for one of them:

```Bash
$ python ../code/stats_01.py small-01.csv
```

```text
running  stats_01.py
0.3333333333333333
1.0
```
Using small data files as input also allows us to check our results more easily: here, for example, we can see that our program is calculating the mean correctly for each line, whereas we were really taking it on faith before. This is yet another rule of programming: test the simple things first.

## Handling Multiple Files
The next step is to teach our program how to handle multiple files.
We want our program to process each file separately, so we need a loop that executes once for each filename. If we specify the files on the command line, the filenames will be in `sys.argv`, but we need to be careful: `sys.argv[0]` will always be the name of our script, rather than the name of a file. We also need to handle an unknown number of filenames, since our program could be run for any number of files.

The solution to both problems is to loop over the contents of `sys.argv[1:]`. The ‘1’ tells Python to start the slice at location 1, so the program’s name isn’t included; since we’ve left off the upper bound, the slice runs to the end of the list, and includes all the filenames. Let's modify our script and call it `stats_03.py`:

```Python
import sys
import numpy


def average_inflammation():
    script = sys.argv[0]
    for filename in sys.argv[1:]:
        print('running ', script, 'for ', filename)
        data = numpy.loadtxt(filename, delimiter=',')
        for row_mean in numpy.mean(data, axis=1):
            print(row_mean)

if __name__ == '__main__':
   average_inflammation()
```
and run it:

```Bash
$ python ../code/stats_03.py small-01.csv small-02.csv
```
```text
running  ../code/stats_03.py for  small-01.csv
0.3333333333333333
1.0
running  ../code/stats_03.py for  small-02.csv
13.666666666666666
11.0
```

## Handling Command-Line Flags
The next step is to teach our program to pay attention to the `--min`, `--mean`, and `--max` flags. These always appear before the names of the files, so we modify further as below and call it `stats_04.py`:

```Python
import sys
import numpy


def stats_inflammation(): # note that we changed the name of the function only to be more descriptive of the what it is doing
    script = sys.argv[0]
    action = sys.argv[1]
    filenames = sys.argv[2:]

    for filename in filenames:
#        print('running ', script, 'for ', filename) and we can also disable this line since it's giving us redundant info
        data = numpy.loadtxt(filename, delimiter=',')

        if action == '--min':
            values = numpy.min(data, axis=1)
        elif action == '--mean':
            values = numpy.mean(data, axis=1)
        elif action == '--max':
            values = numpy.max(data, axis=1)

        for val in values:
            print(val)

if __name__ == '__main__':
   stats_inflammation()
```
and it works:

```Bash
python ../code/stats_04.py --max small-01.csv
```

```text
1.0
2.0
```
but there are several things wrong with it:

1. `stats_inflammation` is too large to read comfortably.

2. If we do not specify at least two additional arguments on the command-line, one for the flag and one for the filename, but only one, the program will not throw an exception but will run. It assumes that the file list is empty, as `sys.argv[1]` will be considered the action, even if it is a filename. Silent failures like this are always hard to debug.

2. The program should check if the submitted action is one of the three recognized flags.

This version checks that action is one of the allowed flags before doing any processing, so that the program fails fast, and then runs our stats function on each file in a loop. We save this version as `stats_05.py`

```Python
import sys
import numpy


def main():
    script = sys.argv[0]
    action = sys.argv[1]
    filenames = sys.argv[2:]
    assert action in ['--min', '--mean', '--max'], \
           'Action is not one of --min, --mean, or --max: ' + action
    for filename in filenames:
        stats_inflammation(filename, action)


def stats_inflammation(filename,action):
        # print('running ', script, 'for ', filename)
        data = numpy.loadtxt(filename, delimiter=',')

        if action == '--min':
            values = numpy.min(data, axis=1)
        elif action == '--mean':
            values = numpy.mean(data, axis=1)
        elif action == '--max':
            values = numpy.max(data, axis=1)

        for val in values:
            print(val)

if __name__ == '__main__':
   main()
```
This is four lines longer than its predecessor, but broken into more digestible chunks of 8 and 12 lines.

## Handling Standard Input
The next thing our program has to do is read data from standard input if no filenames are given so that we can put it in a pipeline, redirect input to it, and so on.

We can do this by using `sys.stdin` which is how "standard input" is handled in Python. Standard input is a file-like object, which as it's name suggests is the standard communication channel between a program and it's environment. When we use piping the program uses the standard input channel to transfer input from one command to another (or when we use < and the name of a file, the program opens the file, and uses the standard input for transfer, instead of reading the file).
So, we now need to rewrite the program so that it loads data from `sys.stdin` if no filenames are provided. Luckily, `numpy.loadtxt` can handle either a filename or an open file as its first parameter, so we don’t actually need to change our stats function, Only `main` changes. we call this stats_06.py:

```Python
import sys
import numpy


def main():
    script = sys.argv[0]
    action = sys.argv[1]
    filenames = sys.argv[2:]
    assert action in ['--min', '--mean', '--max'], \
           'Action is not one of --min, --mean, or --max: ' + action
    if len(filenames) == 0:
        stats_inflammation(sys.stdin, action)
    else:
        for filename in filenames:
            stats_inflammation(filename, action)


def stats_inflammation(filename,action):
        # print('running ', script, 'for ', filename)
        data = numpy.loadtxt(filename, delimiter=',')

        if action == '--min':
            values = numpy.min(data, axis=1)
        elif action == '--mean':
            values = numpy.mean(data, axis=1)
        elif action == '--max':
            values = numpy.max(data, axis=1)

        for val in values:
            print(val)

if __name__ == '__main__':
   main()
```

Let's try it out:

```Bash
$ python ../code/stats_06.py --max < small-01.csv
```

```text
1.0
2.0
```
> ## Challenge:
Write a command-line program that does addition and subtraction:
$ python arith.py add 1 2


So far we have created several versions of our script called stats_01.py, stats_02.py, and stats_03.py, etc. We wouldn’t do this in real life: instead, we would have one file called stats.py that we committed to version control every time we got an enhancement working.

# Version Control with Git
Git is a version control system. Version control systems start with a base version of the document (our stats_01.py) and then record changes you make each step of the way. You only need to have one file, which shows you the most recent version, but you always can rewind on each change you made, and revive the document at each phase.

This is very helpful for not cluttering your workspace with redundant copies of the same work but at the same time keep track of the history of your work to go back in time at any point you need. It is also very helpful when multiple people are working on the same document (e.g. code) since a version control system also keeps track of who made the changes.

A version control system is automatic in the sense that when it's called, it automatically keeps track of changes (what) and metadata of the changes (who and when), which all together make up a "repository". But, it's you who have to operate it. So you have to create a repository and you have to decide which changes you want to keep a history of. For this, you have to run certain Git commands.

There are two main commands:
- `git init`: to create a repository
- `git add`: to mark the changes that we want to keep track of
- `git commit`: to actually create a version of the state of change
as seen in ![Figure](git-staging-area.png)


## Creating a repository
first cd to code directory and create a repository there. We said we want to have only one file for the stats code and apply the improvements on that, so let's rename the first file we made:

```Bash
$ cd ../code
mv stats_01.py stats.py
```
create a repository:
```Bash
$ git init
```

We can check that everything is set up correctly by asking Git to tell us the status of our project:

```Bash
$ git status
```
```Text
On branch master
Untracked files:
  (use "git add <file>..." to include in what will be committed)

        argv_list.py
        stats.py
        stats_02.py
        stats_03.py
        stats_04.py
        stats_05.py
        stats_06.py
        sys_version.py

nothing added to commit but untracked files present (use "git add" to track)
```
## Tracking changes
 keep track of our first version of stats, and the two other separate functions we have created.

```Bash
$ git add argv_list.py sys_version.py stats.py
```
if we run `git status` again:

```Text
On branch master

Initial commit

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)

        new file:   argv_list.py
        new file:   stats.py
        new file:   sys_version.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)

        stats_02.py
        stats_03.py
        stats_04.py
        stats_05.py
        stats_06.py

```

Let's commit our changes:

```Bash
$ git commit -m "start stats code"
```

```Text
[master (root-commit) 440c19e] start stats code
 3 files changed, 26 insertions(+)
 create mode 100644 argv_list.py
 create mode 100644 stats_01.py
 create mode 100644 sys_version.py
```
When we run `git commit`, Git takes everything we have told it to save by using `git add` and stores a copy permanently inside the special .git directory. This permanent copy is called a commit (or revision) and its short identifier is 440c19e. Your commit may have another identifier.

We use the -m flag (for “message”) to record a short, descriptive, and specific comment that will help us remember later on what we did and why. If we just run `git commit` without the -m option, Git will launch whatever other editor we configured as 'core.editor' so that we can write a longer message.

Good commit messages start with a brief (<50 characters) statement about the changes made in the commit. Generally, the message should complete the sentence “If applied, this commit will” .

If we run `git status` now:
```Text
On branch master
Untracked files:
  (use "git add <file>..." to include in what will be committed)

        stats_02.py
        stats_03.py
        stats_04.py
        stats_05.py
        stats_06.py

nothing added to commit but untracked files present (use "git add" to track)
```
It tells everything that was added to be tracked is up-to-date (and there are some untracked files we want to ignore for now).

If we want to know what we’ve done recently, we can ask Git to show us the project’s history using `git log`:

```Text
commit be2d45d60960a51a9b50343e0a63e8ca3bdd9a5c
Author: SaraMati <sara.mahallati@gmail.com>
Date:   Fri Feb 7 01:06:54 2020 -0500

    start stats code
```

`git log` lists all commits made to a repository in reverse chronological order. The listing for each commit includes the commit’s full identifier (which starts with the same characters as the short identifier printed by the git commit command earlier), the commit’s author, when it was created, and the log message Git was given when the commit was created.

Let's reiterate what we did when building our code, phase two was to add the conditional statement to the code (you can open stats_02.py and copy paste). Save stats.py and run 'git status' again:

```Bash
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

        modified:   stats.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)

        stats_02.py
        stats_03.py
        stats_04.py
        stats_05.py
        stats_06.py

no changes added to commit (use "git add" and/or "git commit -a")
```
The last line is the key phrase: “no changes added to commit”. We have changed this file, but we haven’t told Git we will want to save those changes (which we do with `git add`) nor have we saved them (which we do with `git commit`). So let’s do that now. It is good practice to always review our changes before saving them. We do this using `git diff`. This shows us the differences between the current state of the file and the most recently saved version:

```Text
diff --git a/stats.py b/stats.py
index 63f7904..ea3d82f 100644
--- a/stats.py
+++ b/stats.py
@@ -9,3 +9,6 @@ def average_inflammation():
     print('running ', script)
     for row_mean in numpy.mean(data, axis=1):
         print(row_mean)
+
+if __name__ == '__main__':
+   average_inflammation()
```
The output is cryptic because it is actually a series of commands for tools like editors and patch telling them how to reconstruct one file given the other. If we break it down into pieces:

- The first line tells us that Git is producing output similar to the Unix diff command comparing the old and new versions of the file.
- The second line tells exactly which versions of the file Git is comparing; 63f7904 and ea3d82f are unique computer-generated labels for those versions.
- The third and fourth lines once again show the name of the file being changed.
- The remaining lines are the most interesting, they show us the actual differences and the lines on which they occur. In particular, the + marker in the first column shows where we added a line.
After reviewing our change, it’s time to commit it:

```Bash
$ git commit -m "add call to function"
```
```text
On branch master
Changes not staged for commit:
        modified:   stats.py

Untracked files:
        stats_02.py
        stats_03.py
        stats_04.py
        stats_05.py
        stats_06.py

no changes added to commit
```
Whoops: Git didn't commit because we didn’t use git add first. Let’s fix that:

```Bash
$ git add stats.py
$ git commit -m "add call to function"
```
```Text
[master 7892f47] add call to function
 1 file changed, 3 insertions(+)
 ```
now that we have copied the contents of stats_02.py, we can delete that file.
```Bash
$ rm stats_02.py
git status
```
```Text
On branch master
Untracked files:
  (use "git add <file>..." to include in what will be committed)

        stats_03.py
        stats_04.py
        stats_05.py
        stats_06.py

nothing added to commit but untracked files present (use "git add" to track)
```
if we run `git log`:
```Text
commit 7892f474a6315fa5e40888f5473b39193c8cfdac
Author: SaraMati <sara.mahallati@gmail.com>
Date:   Fri Feb 7 01:30:53 2020 -0500

    add call to function

commit be2d45d60960a51a9b50343e0a63e8ca3bdd9a5c
Author: SaraMati <sara.mahallati@gmail.com>
Date:   Fri Feb 7 01:06:54 2020 -0500

    start stats code

```

stats_02.py was removed without a trace, because it was never added to the staging area to be tracked.

## recovering old versions
from log we know the specific identifier of each phase (i.e. commit). We can restore them using `git checkout` commit:

```Bash
$ git checkout be2d45
```
note that we don't need to write the long string of the identifier.
now if you open the file, or run `cat stats.py` in the terminal, you can see that the file contains only the first phase of the code. If we want to go back to the latest version, we use `git checkout HEAD` this is the same as using it's identifier.


In the same manner, we can copy the full code into stats.py and remove the redundant files.
You can do this as a challenge.

> ## Challenge
1) add a line to one of the stats scripts you haven't tracked. it can be a simple comment.
run git status and see what happens.
2) copy the final version of the code in stats.py, and commit. remove extra files and run the status.
3) add a comment to stats.py and check the status, then add and commit to familiarize yourself with the way it looks when everything is up to date and there are no untracked files.

## Github
Although command line Git is very useful, GitHub allows for easy use of Git for
collaborative purposes using a primarily point-and-click interface, in addition
to providing a web-based hosting service for Git repositories (or 'repos').

To sync the repository across different computers and to collaborate with
others, Git is often used via [GitHub](http://www.github.com), a web-based
service that hosts Git repositories. In the spirit of 'working open' and
ensuring scientific reproducibility, it has also become increasingly common for
scientists to upload scripts and related files to GitHub for others to use.

### Creating a fork
The repos that have already been created can be thought of as 'main repos',
which will contain the 'primary' version of the repo at any given point in
time. However, instead of directly uploading and editing files right within
this main repo itself, we will begin by _forking_ the repo. When a given user
forks a repo, GitHub creates a user-specific copy of the repo and all its
files.
go to the [class repo](https://github.com/BME1478H/Winter2020class). So far we have been using the issue section for asking questions from the TAs. The repo contains the same codes we worked on today.

To fork this repo for yourself, navigate to the repo's page and click on the 'Fork'
button at the top right of the page. Following a brief load screen, GitHub will
redirect you to your new, forked repo.

#### Having a local repository of what you forked
You want to have a version of this repository on your computer to work with, that is called your `local repository`. The repository in your Github account is usually called `origin`, and the one your forked from is called `upstream`. The relationship and commands between the different repositories are shown in below figure (note that similar commands are used on the side of the owner of the main repo (the upstream) which we don't show in this Figure)
![Github remotes and local](github.png){ width=50% }

Head to your fork on GitHub, and click on the green 'Clone or
download' button on the right side of the page. This yields a link
to your fork. Copy this link to your clipboard.

Next, open a bash shell, and navigate over to whichever folder you would
like a copy of your repo to be saved in. Then, run:

```
git clone [repo link]
```

With the link in place of `[repo link]`. This process, known as _cloning_, will
create a new folder in your current working directory that contains the
contents of your fork. Enter this new folder with `cd` and type `git status` to
make sure the repo has been cloned properly. `git status` should output that
the branch is even with `origin/master`, indicating that it is currently the
same as the current state of your fork.

To get your fork up to date with the main repo, you next have to add a _remote_
linking to the main repo. Head to your group's repo and once again click
on 'Clone or download' to grab its link. Then, using the main repo link, run:

```
git remote add upstream [repo link]
```

Once this is done, run:

```
git remote -v
```

to get a list of existing remotes. This should return four links, two of which
are labelled `origin` and two of which are labelled `upstream`.

#### Keeping your fork up to date
If there are changes in the class repo, you want to keep your local (and your Github repo, origin) synced. so you have to _fetch_ the new changes that are in the main repo.

```
git fetch upstream
```

Once the edits have been downloaded, merge them into your local repo:

```
git merge upstream/master
```
Note:
The `git pull` command combines two other commands, `git fetch` and `git merge`.

Your local copy is now even with the main repo! do
```
git push origin master
```
to also update your cloud version.

what if you modify the code further?
You can push these changes to the GitHub version of your fork:

```
git push origin master
```

and if you want to also add this wonderful modification you made for all the class, you have to do this:
if you go to your repo on Github, you see that it says 'This branch is 1 commit ahead of BME1478H:master.' and a sign for "Pull request". In this way you are requesting the owner of the upstream repo to sync (i.e. pull) your changes. you create a `pull request` and based on the settings of that repo, either you or the owner can merge your pull request. a very useful feature is to ask for a `review` on your pull request, which you can learn on your own, along more terms that are useful to know, such as `branch`, `conflict`, etc.
a good resource is the [software carpentry lesson](http://swcarpentry.github.io/git-novice/).


# Supplementary material
It's a good practice to use Python’s `argparse` library to take arguments and parameters into our program. We will modify our code slightly to use this library, but you can learn how to even make the code more efficient by reading [Python's official documentation](https://docs.python.org/3/library/argparse.html)

Notice that the library takes care of reading the arguments passed in from a pipeline command-line and we can comment those section out of our code.

```Python
import sys
import numpy
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('infile', nargs = '?', type=argparse.FileType('r'), default=sys.stdin)
    parser.add_argument('--stat', type = str)
    args = parser.parse_args()

    action = args.stat
    filename = args.infile
    assert action in ['min', 'mean', 'max'], \
           'Action is not one of min, mean, or max: ' + action
    # if len(filenames) == 0:
    #     stats_inflammation(sys.stdin, action)
    # else:
    #     for filename in filenames:
    stats_inflammation(filename, action)


def stats_inflammation(filename,action):
        data = numpy.loadtxt(filename, delimiter=',')

        if action == 'min':
            values = numpy.min(data, axis=1)
        elif action == 'mean':
            values = numpy.mean(data, axis=1)
        elif action == 'max':
            values = numpy.max(data, axis=1)

        for val in values:
            print(val)

if __name__ == '__main__':
   main()
```
we can run our script as below:

```Bash
$ python ../code/stats.py --stat 'min' < small-01.csv
```
or
```Bash
$ python ../code/stats.py --stat 'max' small-01.csv
```
