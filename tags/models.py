from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(max_length=128, unique=True, db_index=True)
    post_count = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name
