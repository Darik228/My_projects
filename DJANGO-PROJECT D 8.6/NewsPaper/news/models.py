from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    rating = models.FloatField(default=0.0)

    user = models.OneToOneField(User, on_delete=models.CASCADE,)

    def update_rating(self, updated_rating):
        self.rating = updated_rating
        self.save()

    def __str__(self):
        return self.user.username


class Category(models.Model):
    category_name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return str(self.category_name)


class Post(models.Model):
    article = 'AR'
    news = 'NW'
    TITLE_CHOICES = [
        (article, 'Статья'),
        (news, 'Новость')
    ]

    publication = models.CharField(max_length=2, choices=TITLE_CHOICES, default=article)
    date_of_creation = models.DateTimeField(auto_now_add=True)
    heading = models.CharField(max_length=100)
    text = models.TextField()
    rating = models.FloatField(default=0.0)

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, through='PostCategory')

    def like(self):
        self.rating += 1.0
        self.save()

    def dislike(self):
        self.rating -= 1.0
        self.save()

    def preview(self):
        return f'{self.text[:125]}...'

    def get_absolute_url(self):
        return f'/news/{self.id}'


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')


class Comment(models.Model):
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    rating = models.FloatField(default=0.0)

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def like(self):
        self.rating += 1.0
        self.save()

    def dislike(self):
        self.rating -= 1.0
        self.save()
