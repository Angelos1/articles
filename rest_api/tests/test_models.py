"""The model tests below are not exhaustive. It is just some examples to illustrate the TestCase library
All the tests will be successful except the one defined by the method 'test_title_max_length_MEANT_TO_FAIL' """

import datetime
from django.test import TestCase
from rest_api.models import Article, Author

class ArticleModelTest(TestCase):
    """Tests on the Article Model."""

    @classmethod
    def setUpTestData(cls):
        # This method runs only once to create the relevant objects (Article Model object)
        Article.objects.create(title='Big Bang', summary='Is the Big Bang a theory or reality',
                               content='loads of content...', published_status='a',
                               published_date=datetime.datetime(2020, 5, 17))

    """testing that the label of the published_status field is labelled as expected.
    If a verbose_name is not specified in the model it just replaces the underscore with spaces"""
    def test_published_status_label(self):
        article = Article.objects.get(id=1)
        field_label = article._meta.get_field('published_status').verbose_name
        self.assertEquals(field_label, 'published status')

    """testing that the label of the published_date field is labelled as expected"""
    def test_published_date_label(self):
        article=Article.objects.get(id=1)
        field_label = article._meta.get_field('published_date').verbose_name
        self.assertEquals(field_label, 'published date')

    """testing that the max_length of the title field satisfies our requirements"""
    def test_title_max_length(self):
        article = Article.objects.get(id=1)
        max_length = article._meta.get_field('title').max_length
        self.assertEquals(max_length, 200)

    """A test meant to fail just for illustration purposes of the TestCase library"""
    def test_title_max_length_MEANT_TO_FAIL(self):
        article = Article.objects.get(id=1)
        max_length = article._meta.get_field('title').max_length
        self.assertEquals(max_length, 300) # It fails because 200=!300

class AuthorModelTest(TestCase):
    """Tests on the Author Model."""

    @classmethod
    def setUpTestData(cls):
        # This method runs only once to create the relevant objects (Author Model object)
        Author.objects.create(first_name='Nick', last_name='Nicolaou')

    """testing that the admin panel display of the Author model is 'Author.last_name, Author.firstname' """
    def test_model_admin_display_is_last_name_comma_first_name(self):
        author = Author.objects.get(id=1)
        expected_object_name = f'{author.last_name}, {author.first_name}'
        self.assertEquals(expected_object_name, str(author))

