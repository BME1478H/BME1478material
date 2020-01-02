# Getting Your Computer Ready for BME1478H 

To code along during lessons and tutorials, or to complete assignments, you will need to set up your laptop/computer with the following software, and an up-to-date web browser.
1. Install Bash Shell
2. Install Git + Make a GitHub Account
3. Text Editor
4. Install Anaconda Python

Detailed instructions for various operating systems are included below.

These instructions were developed by [The Carpentries](https://carpentries.org/).

## 1. The Bash Shell

Bash is a commonly-used shell that gives you the power to do simple
tasks more quickly.

### Windows
[Video Tutorial](https://www.youtube.com/watch?v=339AEqk9c-8)

1.  Download the Git for Windows
    [installer](https://git-for-windows.github.io/).
2.  Run the installer and follow the steps below:
    1.  Click on \"Next\" four times (two times if you\'ve previously
        installed Git). You don\'t need to change anything in the
        Information, location, components, and start menu screens.
    2.  **From the dropdown menu select \"Use the `nano` editor by
        default\" and click on \"Next\".**
    3.  Ensure that \"Git from the command line and also from 3rd-party
        software\" is selected and click on \"Next\". (If you don\'t do
        this Git Bash will not work properly, requiring you to remove
        the Git Bash installation, re-run the installer and to select
        the \"Git from the command line and also from 3rd-party
        software\" option.)
    4.  Ensure that \"Use the native Windows Secure Channel library\" is
        selected and click on \"Next\".
    5.  Ensure that \"Checkout Windows-style, commit Unix-style line
        endings\" is selected and click on \"Next\".
    6.  **Ensure that \"Use Windows\' default console window\" is
        selected and click on \"Next\".**
    7.  Ensure that \"Enable file system caching\" and \"Enable Git
        Credential Manager\" are selected and click on \"Next\".
    8.  Click on \"Install\".
    9.  Click on \"Finish\".
3.  If your \"HOME\" environment variable is not set (or you don\'t know
    what this is):
    1.  Open command prompt (Open Start Menu then type `cmd` and press
        \[Enter\])
    2.  Type the following line into the command prompt window exactly
        as shown:

        `setx HOME "%USERPROFILE%"`

    3.  Press \[Enter\], you should see
        `SUCCESS: Specified value was saved.`
    4.  Quit command prompt by typing `exit` then pressing \[Enter\]

This will provide you with both Git and Bash in the Git Bash program.

### Mac OS
The default shell in some versions of macOS is Bash, and Bash is
available in all versions, so no need to install anything. You access
Bash from the Terminal (found in `/Applications/Utilities`). See the Git
installation [video
tutorial](https://www.youtube.com/watch?v=9LQhwETCdwY%20) for an example
on how to open the Terminal. You may want to keep Terminal in your dock
for this workshop.

To see if your default shell is Bash type `echo $SHELL` in Terminal and
press the enter/return key. If the message printed does not end with
\'/bash\' then your default is something else and you can run Bash by
typing `bash`.

### Linux
The default shell is usually Bash and there is usually no need to
install anything.

To see if your default shell is Bash type `echo $SHELL` in a terminal
and press the enter/return key. If the message printed does not end with
\'/bash\' then your default is something else and you can run Bash by
typing `bash`.


## 2. Git

GitHub browser compatibility is
given at https://help.github.com/articles/supported-browsers/

Git is a version control system that lets you track who made changes to
what when and has options for easily updating a shared or public version
of your code on [github.com](https://github.com/). You will need a
[supported web
browser](https://help.github.com/articles/supported-browsers/).

You will need an account at [github.com](https://github.com/) for parts
of the Git lesson. Basic GitHub accounts are free. We encourage you to
create a GitHub account if you don\'t have one already. Please consider
what personal information you\'d like to reveal. For example, you may
want to review these [instructions for keeping your email address
private](https://help.github.com/articles/keeping-your-email-address-private/)
provided at GitHub.

### Windows

Git should be installed on your computer as part of your Bash install
(described above).

### Mac OS

[Video Tutorial](https://www.youtube.com/watch?v=9LQhwETCdwY%20)

**For OS X 10.9 and higher**, install Git for Mac by downloading and
running the most recent \"mavericks\" installer from [this
list](http://sourceforge.net/projects/git-osx-installer/files/). Because
this installer is not signed by the developer, you may have to right
click (control click) on the .pkg file, click Open, and click Open on
the pop up window. After installing Git, there will not be anything in
your `/Applications` folder, as Git is a command line program. **For
older versions of OS X (10.5-10.8)** use the most recent available
installer labelled \"snow-leopard\" [available
here](http://sourceforge.net/projects/git-osx-installer/files/).

### Linux

If Git is not already available on your machine you can try to install
it via your distro\'s package manager. For Debian/Ubuntu run
`sudo apt-get install git` and for Fedora run `sudo dnf install git`.

### 3. Text Editor

When you\'re writing code, it\'s nice to have a text editor that is
optimized for writing code, with features like automatic color-coding of
key words. The default text editor on macOS and Linux is usually set to
Vim, which is not famous for being intuitive. If you accidentally find
yourself stuck in it, hit the Esc key, followed by :+Q+! (colon,
lower-case \'q\', exclamation mark), then hitting Return to return to
the shell.

### Windows
`nano` is a basic editor and the default that instructors use in the
workshop. It is installed along with Git.

Others editors that you can use are
[Notepad++](https://notepad-plus-plus.org/) or [Sublime
Text](https://www.sublimetext.com/). **Be aware that you must add its
installation directory to your system path.** Please ask your instructor
to help you do this.

### Mac OS
`nano` is a basic editor and the default that instructors use in the
workshop. See the Git installation [video
tutorial](https://www.youtube.com/watch?v=9LQhwETCdwY%20) for an example
on how to open nano. It should be pre-installed.

Others editors that you can use are
[BBEdit](https://www.barebones.com/products/bbedit/) or [Sublime
Text](https://www.sublimetext.com/).

### Linux 
`nano` is a basic editor and the default that instructors use in the
workshop. It should be pre-installed.

Others editors that you can use are
[Gedit](https://wiki.gnome.org/Apps/Gedit),
[Kate](https://kate-editor.org/) or [Sublime
Text](https://www.sublimetext.com/).


## 4. Anaconda Python

[Python](https://python.org) is a popular language for research
computing, and great for general-purpose programming as well. Installing
all of its research packages individually can be a bit difficult, so we
recommend [Anaconda](https://www.anaconda.com/distribution/), an
all-in-one installer.

**Please make sure you
install Python version 3.x** (e.g., 3.6 is fine, but not 2.7**).

We will teach Python using the [Jupyter Notebook](https://jupyter.org/),
a programming environment that runs in a web browser (Jupyter Notebook
will be installed by Anaconda). For this to work you will need a
reasonably up-to-date browser. The current versions of the Chrome,
Safari and Firefox browsers are all
[supported](https://jupyter-notebook.readthedocs.io/en/stable/notebook.html#browser-compatibility)
(some older browsers, including Internet Explorer version 9 and below,
are not).


### Windows

[Video Tutorial](https://www.youtube.com/watch?v=xxQ0mzZ8UvA)

1.  Open <https://www.anaconda.com/distribution/#download-section> with
    your web browser.
2.  Download the Anaconda for Windows installer with Python 3. (If you
    are not sure which version to choose, you probably want the 64-bit
    Graphical Installer *Anaconda3-\...-Windows-x86\_64.exe*)
3.  Install Python 3 by running the Anaconda Installer, using all of the defaults for installation.

### Mac OS
[Video Tutorial](https://www.youtube.com/watch?v=TcSAln46u9U)

1.  Open <https://www.anaconda.com/distribution/#download-section> with
    your web browser.
2.  Download the Anaconda Installer with Python 3 for macOS (you can
    either use the Graphical or the Command Line Installer).
3.  Install Python 3 by running the Anaconda Installer using all of the
    defaults for installation.

### Linux

1.  Open <https://www.anaconda.com/distribution/#download-section> with
    your web browser.
2.  Download the Anaconda Installer with Python 3 for Linux.\
    (The installation requires using the shell. If you aren\'t
    comfortable doing the installation yourself stop here and request
    help at the workshop.)
3.  Open a terminal window and navigate to the directory where the
    executable is downloaded (e.g., \`cd \~/Downloads\`).
4.  Type

        bash Anaconda3-

    and then press Tab to autocomplete the full file name. The name of
    file you just downloaded should appear.

5.  Press Enter. You will follow the text-only prompts. To move through
    the text, press Spacebar. Type `yes` and press enter to approve the
    license. Press Enter to approve the default location for the files.
    Type `yes` and press Enter to prepend Anaconda to your `PATH` (this
    makes the Anaconda distribution the default Python).
6.  Close the terminal window.

### Installing packages in Python

After Anaconda has been installed on your system,
you can use the command line `conda` package manager
or the GUI-driven `anaconda-navigator` to install Python packages.
For comprehensive instructions on both of these,
refer to the [official documentation](https://docs.continuum.io/anaconda/#navigator-or-conda).
Brief step-by-step instructions to get up and running with `conda` follow.

1. To install a new Python package from the Anaconda repositories,
   run this in terminal:  

   `conda install <package name>`  

   You can also use the `pip` package manager

    `pip install <package name>`

   but it will be easier to keep track of packages by sticking to one installation method.
2. Some packages are not available in the default Anaconda repositories.
   User contributed packaged are available in Anaconda "channels",
   use `anaconda search -t conda <package name>`,
   to find a channel with the desired package.
   To install this package,
   use `conda install -c <channel name> <package name>`.
   The [conda forge channel](https://conda-forge.github.io/) channel has many of the packages not in the default repositories.

[offical documentation]: https://docs.continuum.io/anaconda/#navigator-or-conda