# Django-Lab
Instructions for the first Django lab. Highpoint Computer Science Club

## 1.) Create new directory in linus-public for your ComputerScienceClub labs
Make one more directory inside ComputerScienceClub labs (Or whatever you called it) for the Django lab we're doing today. After that, cd into the Django directory you just made.

## 2.) Install and use pip in a local directory without root/sudo access.
a. Download pip from an online repository : `wget https://bootstrap.pypa.io/get-pip.py`

b. Install the downloaded package into a local directory : `python get-pip.py --user`
   This installs pip to your local directory `(.local/bin)`.

c. Now you may navigate to this directory `(cd .local/bin)` and then use `pip` or better set your $PATH variable
   this directory to use `pip` anywhere : `PATH=$PATH:~/.local/bin` followed by `source ~/.bashrc` to apply the changes.
