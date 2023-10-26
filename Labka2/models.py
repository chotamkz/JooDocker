from django.db import models

# Create your models here.


class Book(models.Model):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.review_set = None

    title = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    publication_date = models.CharField(max_length=255)
    book_rating = models.IntegerField(blank=True, null=True)
    number_of_reviews = models.IntegerField(blank=True, null=True)
