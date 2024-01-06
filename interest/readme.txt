Set up the virtual environment
  we use pip install venv
  Activate the virtual environment

Configuring Django
  from the venv we install django 
  we create a project in django using django-admin
  we create an application in django using manage.py
  from the second folder with the same name as the project we install our application in the installed apps section in the settings.py
  from settings.py you specify where your static and template files should be found
  still from settings you specify the urls for login and login redirection
  if you going to use crispy_bootstrap you also list it in the installed apps section(dont forget to install it using pip)
  for the first time run migrate for the installed apps in django(this will for you a database)
  create an administrative user
  then run your server using manage.py

Serving custom templates and static files
  create a directory in the apps directory called 'static' for  the 'images','css' and 'javascript'
  create a 'templates' directory in the project direcory for the html files

  from the urls files of the projects directory specify to django to use the urls in your application
  from the urls file in the app we determine the url string and how it will be responded to by the 'view'
  (we attach a url request string to its coresponding view for response)
  note. some views are in-built in djang we just need to re-use them e.g the 'login' and 'logout'
  url is a way/route to reach a file(html)

  
  