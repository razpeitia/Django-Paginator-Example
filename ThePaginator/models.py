from django.db import models

class Post(models.Model):
    timestamp = models.DateTimeField()
    text = models.TextField()

    def __unicode__(self):
        return u'%.50s' % (self.text,)
