from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Event(models.Model):
    eventtitle = models.CharField(max_length=100)
    eventdate = models.DateTimeField(null=True, blank=True)
    eventlength = models.DurationField(null=True, blank=True)
    location = models.CharField(max_length=255)
    agenda = models.CharField(max_length=255)
    good = models.IntegerField(null=True, blank=True,default=0)
    read = models.IntegerField(null=True, blank=True,default=0)
    author = models.ForeignKey(User, to_field='id', on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='image/event_image', verbose_name='イベント画像', null=True, blank=True)
    background_color = (
        ('green','green'),
        ('pink','pink'),
        )
    background= models.CharField(max_length=10, choices=background_color)



    def __str__(self):
        return self.eventtitle

    class Meta:
        db_table = 'Event'

class Backgroundimage(models.Model):
    event_pk = models.ForeignKey(Event, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='background/')
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title