# Instructions

Instructions for interacting with the articles app

## Getting Started

These instructions will guide you to:
* clone the repository
* install required Python packages for running the articles app 
* run the app in developer mode and call the endpoint
* run the unit tests
* interact with the admin panel in order to write, update and delete records.

### Clone the repository
Choose a destination folder you want to clone the repository to (e.g. *destination_folder*).
```
$ cd destination_folder
$ git clone git@github.com:Angelos1/articles.git
```

### Python packages to be installed

Install Django. Run the following command:
```
$ pip install django
```
We will also need Django REST Framework, so let’s get that installed.
Run the following command:

```
$ pip install djangorestframework
```

### Run the app and call the endpoint

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

#### Pagination implementation
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

### Running the unit tests

The tests are located inside the tests/test_models.py file and they are not exhaustive.

It is just some examples to illustrate the *TestCase* library.

All the tests will be successful except the one defined by the method *'test_title_max_length_MEANT_TO_FAIL'* (again for illustration purposes)

To run the tests execute the following command:
```
$ py manage.py test --verbosity 2
```
You can observe that all the tests are successful except the *'test_title_max_length_MEANT_TO_FAIL'*

*--verbosity 2* is used in order to display more information for the tests (the default verbosity is 1)


### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
