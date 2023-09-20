from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Category(models.Model):
    name=models.CharField( max_length=255)

    def __str__(self) :
        return self.name
# Create your models here.
class Post(models.Model):
    image=models.ImageField(upload_to='blog/',default='blog/default.jpg')
    author=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length=255)
    content =models.TextField()
    #tag
    category = models.ManyToManyField(Category)
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(null=False)
    created_date = models.DateTimeField (auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(null=True)

    class Meta:
           ordering= ['-created_date']
    def __str__(self):
        return  self.title
    

    def snippets(self):
            return self.content[:100] + "..."
    

    def get_absolute_url(self):
     return reverse('blog:single',kwargs={'pid':self.id})
