from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.urls import reverse


categories = (
    ('Projects', 'Projects'),
    ('Study', 'Study'),
    ('외부컨텐츠', '외부컨텐츠'),
)
class Post(models.Model):
    title = models.CharField(max_length=30)
    category = models.CharField(max_length=10, choices=categories, default='Study')
    content = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(allow_unicode=True, unique=True)

    class Meta:
        db_table = 'Posts'
        ordering = ('-created_date',)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home:post_detail', args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(args, kwargs)
    
    