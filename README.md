# Sample-Json-app
A Django application with User and Activity models to populate the database with some dummy values and to serve that data in JSON format

**1.)Uploading your code from GitHub to PythonAnywhere

The code stored in the GitHUb can be cloned it from a Bash Console of PythonAnywhere:

$ git clone https://github.com/DheerajS777/Sample-Json-app.git

**2.)Create a virtualenv and install Django and any other requirements:

$ mkvirtualenv myenv --python=/usr/bin/python3.6 
(myenv)$ pip install django
or, if you have a requirements.txt:
(myenv)$ cd Sample-Json-app
(myenv)/Sample-Json-app $ pip install -r requirements.txt


Click on the Files Tab and Upload file 'Test JSON.json' in the directory "/home/dheeraj321/"

**3.)Create a Web app with Manual Config

Head over to the Web tab and create a new web app, choosing the "Manual Configuration" option and the right version of Python (the same one you used to create your virtualenv).

Once that's done, enter the name of your virtualenv in the Virtualenv section on the web tab and click OK.

Enter the path to your project folder in the Code section on the web tab, eg /home/"myusername"/Sample-Json-app in Source code and Working directory.

Enter the virtualenv path in the virtualenv section of the web tab, eg/home/"mysername"/.virtualenvs/myenv
***4.) Edit the WSGI file:

Click on the WSGI file link, and it will take you to an editor where you can change it.

Delete everything except the Django section and then uncomment that section. Your WSGI file should look something like this:

... +++++++++++ DJANGO +++++++++++
import os
import sys

path = '/home/myusername/mysite'
if path not in sys.path:
    sys.path.insert(0, path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'


from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


Save the file, then go and hit the Reload button for your domain. (You'll find one at the top right of the wsgi file editor, or you can go back to the main web tab)


***5.)Database Setup

a.)Click on the Databases tab and enter the new MySQL password and click initialize MySQL and then enter the database name and click create database.
b.)Under files,click Sample-Json-app/FullThrottle/settings.py and replace the DATABASE's user,password,host,name with the new the username,password,hostname and database name of previoulsy created database.

...DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'dheeraj321$UserData',
        'USER': 'dheeraj321',
        'PASSWORD': 'root1234',
        'HOST': 'dheeraj321.mysql.pythonanywhere-services.com',

   }

c.)Also update the user,host and password in the mysql.connector statement in the views.py file of User and Activity app
d.)Except __init__.py,clear all the migration files in all the apps(User,Activity and Index)

**6.) Making the migrations on Bash Console.

(myenv)Sample-Json-app $ python manage.py makemigrations
...Operations to perform:
  Apply all migrations: Activity, User, admin, auth, contenttypes, sessions
Running migrations:
  Applying Activity.0001_initial... OK
  Applying Activity.0002_auto_20200520_0653... OK
  Applying User.0001_initial... OK
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying sessions.0001_initial... OK
(myenv)/Sample-Json-app $ python manage.py makemigrations
Migrations for 'Activity':
  Activity/migrations/0001_initial.py
    - Create model Activity_Data
Migrations for 'User':
  User/migrations/0001_initial.py
    - Create model UserModel
    
**7.) Reload the Web App.

Click on the Web tab and reload the alreadt created web and click on the host link above the reload button

The web host shows the contents of the given sample JSON file.

There are two links, one for the Modified Used data which is stored in JSON format and the other one for Modified ActivityPeriod data which is also stored in JSON format.



