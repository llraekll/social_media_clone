# R-Soultions
## Python 
![alt tag](https://github.com/llraekll/r-shortlinks/blob/main/images/python.png)

## Django
![alt tag](https://github.com/llraekll/r-shortlinks/blob/main/images/dj1.png)

# https://r-solutions.herokuapp.com/ 


A python app built on the framework Django, this is a clone of stack overflow performing all the actions such as 
* User sign-up
* User sign-in
* User sign-out
* User profiles can be viewed
* User profiles can also be edited
Users can perform actions such as 
* Ask question
* View questions asked
* Edit the questions asked
* Answer the questions asked
* Voting the question

![alt tag](https://github.com/llraekll/r_solutions/blob/main/images/home.png)

This repo can be installed by following the steps below

```bash
    django-admin startproject "name"
    git clone git@github.com:llraekll/r_solutions.git
    pip install -r requirements.txt
```


![alt tag](https://github.com/llraekll/FastAPI/blob/main/images/Heroku.png)
### Deploy on Heroku
```bash
    pip install whitenoise
```
In settings settings.py add 

```bash
    MIDDLEWARE = [
    # ...
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    # ...
]
```
Want forever-cacheable files and compression support? Just add this to your settings.py:

```bash
    STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
``` 
In wsgi.py file add whitenoise as application

```bash
    import os
    from whitenoise import WhiteNoise

    from django.core.wsgi import get_wsgi_application

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'r_solutions.settings')

    application = get_wsgi_application()
    application = WhiteNoise(application)
```

* Create a Procfile mentioning the app’s web server
```bash
    web: gunicorn r_solutions.wsgi --log-file - 
```

* Create a requirements.txt file for Heroku to identify the language
* Ensure there are no unused libraries mentioned in the source code
* Add and commit source code, create a Heroku remote as mentioned on Heroku
* Deploy your code 

```bash
    git add --all
    git commit -am "comment"
    git push heroku main
```

![alt tag](https://github.com/llraekll/r_solutions/blob/main/images/profile.png)
![alt tag](https://github.com/llraekll/r_solutions/blob/main/images/questions.png)
![alt tag](https://github.com/llraekll/r_solutions/blob/main/images/view.png)
