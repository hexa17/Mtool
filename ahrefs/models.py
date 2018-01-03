from django.db import models

# Create your models here.
class AhrefsRank(models.Model):
    url = models.CharField(max_length=255, null=True, blank=True)
    ahrefs_rank = models.FloatField(null=True, default=0)

    def __str__(self):
        return self.url

class AhrefsBacklinks(models.Model):
    url_from = models.CharField(max_length=255, null=True, blank=True)
    url_to = models.CharField(max_length=255, null=True, blank=True)
    ahrefs_rank = models.IntegerField(null=True, default=0)
    domain_rating = models.IntegerField(null=True, default=0)
    ip_from = models.CharField(max_length=255, null=True, blank=True)
    links_internal = models.IntegerField(null=True, default=0)
    links_external = models.IntegerField(null=True, default=0)
    page_size = models.IntegerField(null=True, default=0)
    encoding = models.CharField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    first_seen = models.DateTimeField(max_length=255, null=True, default=0)
    last_visited = models.DateTimeField(max_length=255, null=True, default=0)
    prev_visited = models.DateTimeField(max_length=255, null=True, default=0)
    original = models.BooleanField(default=True)
    link_type = models.CharField(max_length=255, null=True, blank=True)
    redirect = models.IntegerField(null=True, default=0)
    nofollow = models.BooleanField(default=True)
    alt = models.CharField(max_length=255, null=True, blank=True)
    anchor = models.CharField(max_length=255, null=True, blank=True)
    text_pre = models.CharField(max_length=255, null=True, blank=True)
    text_post = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.url_to