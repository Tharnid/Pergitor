from django.db import models

# Create your models here.

class Gr(models.Model):
    text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    via = models.URLField(blank=True)

    # Model Method
    def total_likes(self):
        return self.like_set.count()

    def __unicode__(self):
        return self.text[:50]    # trims to 50 characters via slice mwhahaha
class Like(models.Model):
    gr = models.ForeignKey(Gr)
