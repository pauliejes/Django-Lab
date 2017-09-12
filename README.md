# Django-Lab
Instructions for the first Django lab. Highpoint Computer Science Club

## 1) Create new directory in linus-public for your ComputerScienceClub labs
Now make one more directory inside ComputerScienceClub labs (Or whatever you called it) for the Django lab we're doing today. After that, cd into the Django directory you just made.
I will be referring to the ComputerScienceClub labs folder as <cscLabs> and the Django folder as <django>

## 2) Now we install pip in a local directory without root/sudo access.
a. Download pip from an online repository : `wget https://bootstrap.pypa.io/get-pip.py`

b. Install the downloaded package into a local directory : `python get-pip.py --user`
   This installs pip to your local directory `(.local/bin)`.

c. To use `pip` anywhere : `PATH=$PATH:~/.local/bin` followed by `source ~/.bashrc` to apply the changes.

## 3) Install Django
Navigate back to the <django> directory inside your <cscLabs> labs directory. Once there, run `pip install --user Django` (we add `--user` since we cannot install Django system-wide on linus-public).

## 4) Start Project

Now we start our project with `django-admin startproject djangoLab`

`djangoLab/ - Simple container, Call whatever you want.
    manage.py - Lets you interact with your project via the command line.
    djangoLab/ - Actual project directory.
        __init__.py - Tells python this is a Python package.
        settings.py - Settings for the project.
        urls.py - URL rules. Django docs aptly describes as your table of contents.
        wsgi.py - WSGI magic begins here. Worry about this when it comes time to actually deploy to a server.`
