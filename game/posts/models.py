from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
import datetime

from django.contrib.auth.models import User



# Create your models here.
SPORT_CHOICES = (
    ('basketball', 'Basketball'),
    ('soccer', 'Soccer'),
    ('volleyball', 'Volleyball'),
    ('frisbee', 'Ultimate Frisbee'),
    ('tennis', 'Tennis'),
)

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, related_name='creator')
    title = models.CharField(max_length=200)
    sport = models.CharField(max_length=20, choices=SPORT_CHOICES)
    description = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=100)
    city = models.CharField(max_length=50, null=True)
    capacity = models.IntegerField(default=10)
    time = models.TimeField(default=datetime.time(12, 00))
    created_date = models.DateTimeField(default=timezone.now)
    joined_users = models.ManyToManyField(User)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={"post_id": self.id})

    def get_sport_icon(self):
        sports = {'basketball': 'images/basketball.png', 'soccer': 'images/football.png', 'tennis': 'images/tennis.png', 'volleyball': 'images/volleyball.png', 
        'frisbee': 'images/frisbee.png'}
        icon_url = sports.get(self.sport)
        return icon_url

    def get_num_players(self):
        users = self.joined_users.all()
        num_players = len(users)+1
        return num_players

