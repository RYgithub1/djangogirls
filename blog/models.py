from django.db import models
from django.conf import settings
from django.utils import timezone



POST_TYPE_CHOICE = (('lifestyle', 'Lifestyle'),
                            ('anime', 'Anime'),
                            ('nature', 'Nature'))



class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    # CharField needs limit, unlike TextField()
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    # Add post type.
    post_type = models.CharField(choices=POST_TYPE_CHOICE, max_length=20, default='lifestyle')
    # When changed model, Need both maikemigrations and migrate.
    # SAMPLE
    # flag = models.CharField(max_length=200, default='1')


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title