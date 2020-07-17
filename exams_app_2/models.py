from django.db import models
from main_app.models import User
from django.utils import timezone
from .image_helpers import Thumbnail
from django.urls import reverse_lazy, reverse
import main_app
from .emailing import send_email
# Create your models here.

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete = models.PROTECT)
    #title = models.CharField(max_length=250)
    text = models.TextField(max_length=5000, blank=True)
    timestamp = models.DateTimeField(default=timezone.now)
    image = models.ImageField(blank = True, upload_to = 'discussion/comments')
    #thumbnail = models.ImageField(blank = True, upload_to = 'discussion/thumbnails')
    #votes = models.ManyToManyField(Vote)
    #vote_count = models.IntegerField(default = 0)

    def resize_image(self):
        try:
            image_generator = Resize_1080(source=self.image)
            modified_image_file = image_generator.generate()
            dest = open(self.image.path, 'wb')
            dest.write(modified_image_file.read())
            dest.close()
        except:
            pass

class Submission(models.Model):
    author = models.ForeignKey(User, on_delete = models.PROTECT)
    title = models.CharField(max_length=250)
    text = models.TextField(max_length=5000, blank=True)
    timestamp = models.DateTimeField(default=timezone.now)
    image = models.ImageField(blank = True, upload_to = 'discussion/submissions')
    #thumbnail = models.ImageField(blank = True, upload_to = 'discussion/thumbnails')
    comments = models.ManyToManyField(Comment)
    #votes = models.ManyToManyField(Vote)
    #vote_count = models.IntegerField(default = 0)


    def resize_image(self):
        try:
            image_generator = Resize_1080(source=self.image)
            modified_image_file = image_generator.generate()
            dest = open(self.image.path, 'wb')
            dest.write(modified_image_file.read())
            dest.close()
        except:
            pass

    def activity(self):
        new_activity = main_app.models.Activity(
            content = f"""{self.author.first_name} posted on {self.exam_set.all()[0].name} discussion page: {self.title}""",
            url = reverse('exams_app_2:exam_discussion', kwargs = {'exampk': self.exam_set.all()[0].pk,}),
            author = self.author,
            is_ece = self.exam_set.all()[0].is_ece,
            is_ee = self.exam_set.all()[0].is_ee,
            is_tutorial = self.exam_set.all()[0].is_tutorial,
        )
        new_activity.save()

    def notify(self):
        send_email(self)


    class Meta:
        ordering = ['-pk']



class Item(models.Model):
    item_number = models.PositiveSmallIntegerField()
    answer = models.CharField(max_length = 5)
    bonus = models.BooleanField(default = False)
    skip = models.BooleanField(default = False)

    def __str__(self):
        return str(self.item_number) + ' ' + self.answer

    class Meta:
        ordering = ['item_number']

class AnswerSheet(models.Model):
    user = models.ForeignKey(User, on_delete = models.PROTECT)
    items = models.ManyToManyField(Item)
    score = models.PositiveSmallIntegerField(null = True, blank = True)
    percentage = models.FloatField(null = True, blank = True)
    date_submitted = models.DateField(null = True, blank = True)
    first_take = models.BooleanField(default = False)

    def __str__(self):
        return self.user.first_name +','+ self.user.last_name + ',' + str(self.score) + '% ' + str(self.date_submitted)

    class Meta:
        ordering = ['-score']

class AnswerKey(models.Model):
    items = models.ManyToManyField(Item)

class ExamFile(models.Model):
    name = models.CharField(max_length = 50, blank = True)
    file = models.FileField(upload_to = 'exams_app_2/examfiles')

    is_ece = models.BooleanField(default = False)
    is_ee = models.BooleanField(default = False)
    is_tutorial = models.BooleanField(default = False)
    is_accessible = models.BooleanField(default = False)

class Exam(models.Model):
    author = models.ForeignKey(User, null = True, on_delete = models.PROTECT)
    name = models.CharField(max_length = 50)
    description = models.CharField(max_length = 100, blank = True)
    is_ece = models.BooleanField(default = False)
    is_ee = models.BooleanField(default = False)
    is_tutorial = models.BooleanField(default = False)
    is_accessible = models.BooleanField(default = False)
    files = models.ManyToManyField(ExamFile)
    answer_key = models.ForeignKey(AnswerKey, on_delete = models.CASCADE, null = True)
    answer_sheets = models.ManyToManyField(AnswerSheet)
    thumbnail = models.ImageField(upload_to = 'exams_app_2/thumbnails')
    is_done = models.BooleanField(default = False)
    timestamp = models.DateTimeField(null=True)
    submissions = models.ManyToManyField(Submission)

    """exam_stats"""
    has_stats = models.BooleanField(default = False)
    percent_as = models.CharField(max_length = 2000, null = True, blank = True)
    percent_bs = models.CharField(max_length = 2000, null = True, blank = True)
    percent_cs = models.CharField(max_length = 2000, null = True, blank = True)
    percent_ds = models.CharField(max_length = 2000, null = True, blank = True)
    percent_corrects = models.CharField(max_length = 2000, null = True, blank = True)
    item_labels = models.CharField(max_length = 2000, null = True, blank = True)

    def __str__(self):
        return self.name

    def compute_stats(self):
        percent_as = []
        percent_bs = []
        percent_cs = []
        percent_ds = []
        percent_corrects = []
        item_labels = []

        for i in range(1,101):
            count_a = 0
            count_b = 0
            count_c = 0
            count_d = 0
            count_correct = 0
            for sheet in self.answer_sheets.all():
                for item in sheet.items.filter(item_number = i):
                    if item.answer == 'a':
                        count_a = count_a + 1
                    elif item.answer == 'b':
                        count_b = count_b + 1
                    elif item.answer == 'c':
                        count_c = count_c + 1
                    elif item.answer == 'd':
                        count_d = count_d + 1
                    else:
                        pass

                    answer = self.answer_key.items.filter(item_number = i)[0].answer
                    if item.answer == answer:
                        count_correct = count_correct + 1

            total = count_a + count_b + count_c + count_d
            if not total == 0:
                percent_as.append(int(count_a * 100/ total))
                percent_bs.append(int(count_b * 100/ total))
                percent_cs.append(int(count_c * 100/ total))
                percent_ds.append(int(count_d * 100/ total))
                percent_corrects.append(int(count_correct * 100/ total))

        i = 1
        for item in self.answer_key.items.all():
            item_labels.append(str(i) + ', '+ str(item.answer))
            i = i + 1

        self.percent_as = percent_as
        self.percent_bs = percent_bs
        self.percent_cs = percent_cs
        self.percent_ds = percent_ds
        self.percent_corrects = percent_corrects
        self.item_labels = item_labels
        self.has_stats = True
        self.save()

    def compute_topnotchers(self):

        top_scores = (self.answer_sheets.all()
                             .order_by('-score')
                             .values_list('score', flat=True)
                             .distinct())
        top_records = (self.answer_sheets.all()
                              .order_by('-score')
                              .filter(score__in=top_scores[:10]))

        return top_records
