from django.db import models
from django.contrib.auth.models import User

# ユーザのプロフィール情報を保存するモデル
# ユーザモデル本体に変更を加えたくないので別個に作成
# pkはユーザモデルと同じになるように設定

class User_profile(models.Model):
    User_id = models.OneToOneField(to=User,primary_key=True, on_delete=models.CASCADE)
    handlename = models.CharField(max_length=15)
    introduction = models.CharField(max_length=255)
    icon = models.CharField(max_length=40, null=True, blank=True)
    image = models.ImageField(upload_to="user/", null=True, blank=True)

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
    image = models.ImageField(upload_to='image/event_image', verbose_name='イベント画像', null=True, blank=True, default='../media/image/backgroundimage/green.jpg')
    background_color = (
        ('../media/image/backgroundimage/green.jpg','green'),
        ('../media/image/backgroundimage/pink.jpg','pink'),
        )
    background= models.CharField(max_length=40, choices=background_color)



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