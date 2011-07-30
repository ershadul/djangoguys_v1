from django.db import models
from tags.models import Tag

class Post(models.Model):
    pub_date = models.DateTimeField(auto_now_add=True)
    mod_date = models.DateTimeField(auto_now=True)
    headline = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, db_index=True, unique=True)
    body_text = models.TextField()
    n_comments = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    tags = models.ManyToManyField(Tag, null=True, blank=True)
    is_published = models.BooleanField(default=0)
    
    def __unicode__(self):
        return self.headline

    def get_absolute_url(self):
        return '/%s/%s/%s/%s' % (str(self.pub_date.year), str(self.pub_date.month), str(self.pub_date.day), self.slug)