from django.db import models
from users.models import User
from redactor.fields import RedactorField


class Category(models.Model):
    name = models.CharField(max_length=40)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return "{}".format(self.name).upper()


class InterestTag(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return "{}".format(self.name).upper()


class BlogPost(models.Model):
    title = models.CharField(max_length=40)
    author = models.ForeignKey(User, related_name="post_author")
    text = RedactorField(verbose_name=u'Blog Post')
    category = models.ForeignKey(Category, related_name="post_category")
    tags = models.ManyToManyField(InterestTag, related_name="post_tags", blank=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("title", "author")

    def __str__(self):
        return "{} {} {}".format(self.title, self.author, self.category)


class BlogPostComment(models.Model):
    email = models.EmailField()
    author = models.CharField(max_length=40)
    text = RedactorField(verbose_name=u'Comment')
    post = models.ForeignKey(BlogPost)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("email", "author")

    def __str__(self):
        return "{} {} {}".format(self.author, self.email, self.post)
