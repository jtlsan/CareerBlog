from django.db import models
from ckeditor.fields import RichTextField


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
    
    