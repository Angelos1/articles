from django.db import models
from django.urls import reverse
import uuid
from django.contrib.auth.models import User
from datetime import date

class Article(models.Model):
    """Model representing an article."""
    title = models.CharField(max_length=200)

    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the article')

    #Check content lenght
    content = models.TextField(help_text='Enter the article content')

    #The keys from the key/value pair below are stored in the db and the values are displayed in the admin area
    STATUS_CODES = (
        ('n', ' None'),
        ('nc', 'Needs Content'),
        ('nr', 'Needs Review'),
        ('a', 'Approved'),
    )
    published_status = models.CharField(
        max_length=2,
        choices=STATUS_CODES, # this is where the status field takes its values from
        blank=True,
        default='n',
        help_text='Article status',
    )

    published_date = models.DateField(null=True, blank=True)

    # ManyToManyField used under the assumption that news_category can contain many articles. Articles can have many Categories.
    category = models.ManyToManyField('Category', help_text='Select a genre for this book')

    # Foreign Key used because the assumption is that we can only have one author, but one author can have multiple articles
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """String for representing the Article object."""
        return self.title

class Author(models.Model):
    """Model representing an author."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):
        """String for representing the Author object."""
        return f'{self.last_name}, {self.first_name}'

class Category(models.Model):
    """Model representing article category."""
    name = models.CharField(max_length=200, help_text='Enter an article category (e.g. Sports)')

    def __str__(self):
        """String for representing the Category object."""
        return self.name