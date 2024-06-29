from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.title
    

class Choices:
    status = (
        (1, "Read"),
        (2, "Want To Read"),
        (3, "Did Not Finish"),
        (4, "Reading")
    )

class Status(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user_status = models.SmallIntegerField(default=1, choices=Choices.status)
    rating = models.IntegerField()
    review = models.CharField(max_length=5000)

    def __str__(self):
        return self.user_status