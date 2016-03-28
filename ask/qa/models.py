from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
from django.contrib.auth.models import User

class Question (models.Model):
    title = models.CharField(max_length = 255)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(blank=True, default=0)
    author = models.ForeignKey(User)
    likes = models.ManyToManyField(User, related_name='likes_set')

    # Getting URL for request
    def get_url(self):
#        print 'try get url for question %s' % (self.id)
        return reverse('question', kwargs={'inid':self.id})
        #return reverse('question', args=[id])
        #return reverse('question')

class Answer (models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User)
    
