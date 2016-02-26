from django.db import models

# Create your models here.

class Gr(models.Model):
    text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    via = models.URLField(blank=True)

    # Model Method
    def total_likes(self):
        return self.like_set.count()
class Like(models.Model):
    gr = models.ForeignKey(Gr)
