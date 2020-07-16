from django.db import models
from django.utils import timezone
from main_app import User
from .image_helpers import Thumbnail
# Create your models here.


class Comment(models.Model):
    author = models.ForeignKey(User)
    #title = models.CharField(max_length=250)
    text = models.TextField(max_length=5000, blank=True)
    timestamp = models.DateTimeField(default=timezone.now)
    image = models.ImageField(blank = True, upload_to = 'discussion/comments')
    thumbnail = models.ImageField(blank = True, upload_to = 'discussion/thumbnails')
    #votes = models.ManyToManyField(Vote)
    #vote_count = models.IntegerField(default = 0)

    def generate_thumbnail(self):
        try:
            image_generator = Thumbnail(source=self.image)
            modified_image_file = image_generator.generate()
            dest = open(self.image.path, 'wb')
            dest.write(modified_image_file.read())
            dest.close()
        except:
            pass


class Submission(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=250)
    text = models.TextField(max_length=5000, blank=True)
    timestamp = models.DateTimeField(default=timezone.now)
    image = models.ImageField(blank = True, upload_to = 'discussion/submissions')
    thumbnail = models.ImageField(blank = True, upload_to = 'discussion/thumbnails')
    comments = models.ManyToManyField(Comment)
    #votes = models.ManyToManyField(Vote)
    #vote_count = models.IntegerField(default = 0)

    def generate_thumbnail(self):
        try:
            image_generator = Thumbnail(source=self.image)
            modified_image_file = image_generator.generate()
            dest = open(self.image.path, 'wb')
            dest.write(modified_image_file.read())
            dest.close()
        except:
            pass


class Discussion(models.Model):
    submissions = models.ManyToManyField(Submission)
