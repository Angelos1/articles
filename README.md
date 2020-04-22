# Instructions

Instructions for running interacting with the *articles* Django app.

These instructions will guide you to:
* clone the repository
* install required Python packages for running the articles app 
* run the app in developer mode and call the endpoint
* run the unit tests
* interact with the admin panel in order to write, update and delete records.

## Clone the repository
Choose a destination folder you want to clone the repository to (e.g. *destination_folder*).
```
$ cd destination_folder
$ git clone git@github.com:Angelos1/articles.git
```

## Python packages to be installed

Install Django. Run the following command:
```
$ pip install django
```
We will also need Django REST Framework, so let’s get that installed.
Run the following command:

```
$ pip install djangorestframework
```

## Run the app and call the endpoint

Change your directory to the root of the cloned repository.
```
$ cd articles
```
Run the app on your PC with the following command:

```
$ py manage.py runserver
```
If the above command doesn't work try:
```
$ python3 manage.py runserver
```

Once you have the app up and running on your PC go to your browser and call the 
endpoint [localhost:8000/api/articles/](localhost:8000/api/articles/) 

Pagination is implemented with *PAGE_SIZE:2* (for testing purposes on a small data set of 5 articles). That 
is why you are not retrieving all the records.

You can see *Next* and *Previous* links to navigate to the next and previous pages of the pagination respectively.

You can also change the page size through the *PAGE_SIZE* configuration in the *articles/settings.py* file.

### Pagination implementation
The pagination is implemented through the *CustomCursorPagination* class in the *paginations.py* file and through the below 
code which is written in the *articles/settings.py* file.

```
# comment this out to deactivate pagination
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'paginations.CustomCursorPagination', # custom pagination class defined in paginations.py
    'PAGE_SIZE': 2,
}
```

You can comment out this piece of code in order to deactivate pagination and have all the articles returned when calling 
the endpoint.

## Running the unit tests

The tests are located inside the tests/test_models.py file and they are not exhaustive.

It is just some examples to illustrate the *TestCase* library.

All the tests will be successful except the one defined by the method *'test_title_max_length_MEANT_TO_FAIL'* (again for illustration purposes)

To run the tests execute the following command:
```
$ py manage.py test --verbosity 2
```
You can observe that all the tests are successful except the *'test_title_max_length_MEANT_TO_FAIL'*

*--verbosity 2* is used in order to display more information for the tests (the default verbosity is 1)


## Admin Panel

A user interface for the admin that can be used to store update & delete *Articles*, *Authors* and *Categories*

From your browser go to [http://localhost:8000/admin/](http://localhost:8000/admin/) and you will be directed in a login interface.

To log in use the following credentials:
```
Username: cocoon
Password: cocoon
```
After logging in you can see the Models (Articles, Authors, Categories) of the *articles* app under the REST_API section.

Click on the Articles model and see its records.

The app is already populated with records because it is connected with an SQLite 
database which is located in the file *db.sqlite3* in the base directory of the project.

It is the default database that a Django app uses if another database is not defined and it is set in the below piece 
of code which is located in *articles/settings.py*
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```
I populated this database so that you can find some records in for your convenience. 

You can add Articles by clicking the ADD ARTICLE+ button. Fill the required fields and press SAVE.

If you want to update an article just click on the article title and update any fields and press save.
