from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.
class TaskStatus(models.TextChoices):
    PENDING="PE","Pending"
    COMPLETED="CO","Completed"
    DROPPED="DR","Dropped"
class Tag(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=255)

    def __str__(self):
        return  self.name


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content=models.TextField()
    created_at=models.DateTimeField(default=timezone.now())
    completed_at=models.DateTimeField(null=True)
    deadline=models.DateTimeField( null=True, blank=True)
    status=models.CharField(choices=TaskStatus.choices,default=TaskStatus.PENDING,max_length=2)
    tags=models.ManyToManyField(Tag, null=True, blank=True)


    def __str__(self):
        return self.content

    def get_all_tags(self,delimeter=', '):
        return delimeter.join(tag.name for tag in self.tags.all())
        #using list comprehension and used strings join to join all the tags

