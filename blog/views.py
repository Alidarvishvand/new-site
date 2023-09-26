from django.shortcuts import render,get_object_or_404
from blog.models import Post,Comment
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from blog.forms import CommentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def blog_view(request,cat_name=None,author_username=None):
  posts = Post.objects.filter(status=1)
  if cat_name: 
      posts = posts.filter(category_name=cat_name)
  if author_username:
      posts = posts.filter(author__username=author_username)
  posts = Paginator(posts,2)
  try:
    page_number = request.GET.get('page')
    posts = posts.get_page(page_number)
  except PageNotAnInteger:  
    posts = posts.get_page(1) 
  except EmptyPage:
    posts = posts.get_page(1) 
  context = {'posts': posts}
  return render(request,'blog/blog-home.html',context)



def blog_single(request,pid):
  if request.method == 'POST':
     form = CommentForm(request.POST)
     if form.is_valid():
        form.save()
        messages.add_message(request,messages.SUCCESS,'your ticket submited successfully')
     else:
        messages.add_message(request,messages.ERROR,'your ticket didnt submited successfully')
     
  comments = Comment.objects.filter(post=pid).order_by('-created_date') 
  posts = Post.objects.filter(status=1)
  post = get_object_or_404(posts,pk=pid)
  form = CommentForm
  context = {'post':post,'comments':comments,'form':form}
  return render (request,'blog/blog-single.html',context) 


def test (request):
  #post = Post.objects.get(id=pid)
 # post = get_object_or_404(Post,pk=pid)
  #context = {'post':post}
  return render (request,'test.html')

def blog_category(request,cat_name):
  posts = Post.objects.filter(status=1)
  posts = posts.filter(category__name=cat_name)
  context  = {'posts':posts}
  return render(request,'blog/blog-home.html',context)


def blog_search(request):
   posts = Post.objects.filter(status=1)
   if request.method == 'GET':
      if s := request.GET.get('s'):
         posts = posts.filter(content__contains=request.GET.get('s'))


   context = {'posts':posts}
   return render(request,'blog/blog-home.html',context)