from django import template
from blog.models import Post
register = template.Library()

@register.simple_tag(name = 'totalposts')

def function():
    posts = Post.objects.filter(status=1).count()
    return posts

@register.simple_tag(name = 'posts')

def function():
    posts = Post.objects.filter(status=1)
    return posts
@register.filter
def snippet(value):
    return value[:100]

@register.inclusion_tag('blog/blog-popular-posts.html')
def latestposts(args=3):
    posts = Post.objects.filter(status=1).order_by('published_date')[:args]
    return {'posts':posts}