# Django-Lab
Instructions for the first Django lab. Highpoint Computer Science Club

## 1) Create new directory in linus-public for your club labs

   Lets start by making a new directory in linus-public for these labs. Next make another directory inside your clubLabs directory (Or whatever you called it) for the Django lab we're doing today. After that, cd into the new Django directory.
   - I will be referring to these new directories as <clubLabs>, and <django>

## 2) Install pip.

   We will need to install pip in a local directory since we do not have root access to linus-public. Here are the steps:

   - a. Download pip from an online repository : `wget https://bootstrap.pypa.io/get-pip.py`

   - b. Install the downloaded package into a local directory : `python get-pip.py --user` This installs pip to your local directory `(.local/bin)`.

   - c. To use `pip` anywhere : `PATH=$PATH:~/.local/bin` followed by `source ~/.bashrc` to apply the changes.

## 3) Installing Django on linus

   Navigate back to the `<django>` directory inside your `<cscLabs>` labs directory. Once there, run

      - `pip install --user Django`

   Here we are adding `--user` since we cannot install Django system-wide on linus-public due to our lack of admin privileges).

## 4) Creating a Project.

   In this step we will need to pick a name for the project. You will see that I have named mine `djangoLab`. Create your project using:

    - `django-admin startproject djangoLab`.

   This creates a directory with the name of your project, in my case - `<djangoLab>`. Inside will be another with the same name - `<djangoLab>`, as well as a file named `manage.py`. For simplicity, I will be calling the first djangoLab directory - `<djangoLab>(1)`, and the second `<djangoLab>(2)`. `manage.py` will allow easier interaction with your project via the command line. In the second `<djangoLab>` directory we will be focusing mainly on two files there named `settings.py`, and `urls.py`.

   ```
     ~ General structure of a Django project ~

       I) <djangoLab> - Simple container, Call whatever you want.  

           A) manage.py - Lets you interact with your project via the command line.
           B) <djangoLab> - Actual project directory.

               1) __init__.py - Tells python this is a Python package.
               2) settings.py - Settings for the project.
               3) urls.py - URL rules. Django docs aptly describes as your table of contents.
               4) wsgi.py - WSGI magic begins here. Worry about this when it comes time to actually deploy to a server.
   ```


Currently we should have our website, called `djangoLab`. Our next step will be creating an app. With Django, a website is an app, or more commonly a collection of apps. But before all of that, we should navigate to `<djangoLab>(1)` and run `python manage.py runserver 0.0.0.0:XXXX`. This starts running the local development server, which you should be able to access at `http://127.0.0.1:XXXX`.


## 5) Creating an app.

   Make your way to the `<djangoLab>(1)` directory. We will start our first `djangoLab` app by running:

      `python manage.py startapp personal`

   We can now see a directory named `personal`. In here, we see a lot of similar files, and some new ones:

```
      I) `<personal>`

         A) `<migrations>`
         	1) __init__.py
         	2) admin.py
         	3) apps.py
         	4) models.py
         	5) tests.py
         	6) views.py
```

   https://pythonprogramming.net/first-site-django-python-tutorial/?completed=/django-web-development-with-python-intro/

##
