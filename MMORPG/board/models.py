from django.db import models
from django.urls import reverse


#class Comment(models.Model):
#    text = models.TextField()


class Category(models.Model):
    text = models.CharField(max_length=60, unique=True)

    def __str__(self):
        return self.text.title()


class Ad(models.Model):
    title = models.CharField(max_length=100, unique=True)
    text = models.TextField()
    #file = models.FileField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    #comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.title.title()}: {self.text[:20]}'

    def get_absolute_url(self):
        return reverse('ad_detail', args=[str(self.id)])



