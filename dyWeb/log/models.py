from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.utils import timezone
import datetime

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

import time
# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=255, default="")

    def __str__(self):
        return self.name


class Tag(models.Model):
    title = models.CharField(max_length=255, default="")
    slug = models.SlugField(blank=True, default="")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Tag, self).save()


class Category(models.Model):
    title = models.CharField(max_length=255, default="")
    slug = models.SlugField(blank=True, default="")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save()


class Log(models.Model):
    title = models.CharField(max_length=255, default="")
    author_name = models.ForeignKey(
        Author, null=True, on_delete=models.PROTECT)
    contents = models.TextField(default="")
    slug = models.SlugField(blank=True, default="")
    tags = models.ManyToManyField(Tag)  # hashtag
    categories = models.ForeignKey(
        Category, null=True, on_delete=models.PROTECT)  # 分成 程式、美術等等的分類
    image = models.ImageField(default="", blank=True, upload_to="images")
    image_thumbnail = ImageSpecField(source='image',
                                     processors=[ResizeToFill(350, 200)], format='JPEG', options={'quality': 60})
    edit_time = models.DateTimeField(default=timezone.now)

    def timestamp(self):
        return self.latest_edit_time >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']
        db_table = "log"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Log, self).save()

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.slug)])
