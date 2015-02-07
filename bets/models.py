import datetime

from django.db import models
from django.utils import timezone

BET_CHOICES = (
    ('PAY_IN', 'Pay In'), 
    ('PAY_OUT', 'Pay Out'),
)

# Create your models here.
class User(models.Model):
    access_token = models.CharField(max_length=100)
    # question_text = models.CharField(max_length=200)
    # pub_date = models.DateTimeField('datepublished')
    def __unicode__(self):
        return self.question_text
    # def was_published_recently(self):
    #     return self.pub_date <= timezone.now() - datetime.timedelta(days=1)
    # was_published_recently.admin_order_field = 'pub_date'
    # was_published_recently.boolean = True
    # was_published_recently.short_description = 'Published recently?'

class BetRoom(models.Model):
    room_name = models.CharField(max_length=255)
    date_created = models.DateTimeField('datecreated')
    password = models.CharField(max_length=50)
    is_active = models.BooleanField(default=False)
    url = models.CharField(max_length=255)
    # question = models.ForeignKey(Question)
    # choice_text = models.CharField(max_length=200)
    # votes = models.IntegerField(default=0)
    def __unicode__(self):
        return self.url

class Option(models.Model):
    betroom = models.ForeignKey(BetRoom, related_name='options')
    option_name = models.CharField(max_length=255)
    def __unicode__(self):
        return self.option_name

class Bet(models.Model):
    date_created = models.DateTimeField('datecreated')
    betroom_id = models.ForeignKey(BetRoom, related_name='bets')    
    from_id = models.CharField(max_length=255)
    to_id = models.CharField(max_length=255)
    bet_type = models.CharField(max_length=20, choices=BET_CHOICES)
    bet_option = models.ForeignKey(Option, related_name='transactions')
    name = models.CharField(max_length=255)
