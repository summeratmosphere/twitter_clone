from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm

def index(request):

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        # If the form is valid
        if form.is_valid():
            # Yes, Save
            form.save()
            
            # Redirect to Home
            return HttpResponseRedirect('/')
    
    # Get all posts, limit = 20
    posts = Post.objects.all().order_by('-created_at')[:20]

    # Show
    return render(request, 'posts.html', {'posts': posts})


def delete(request, post_id):
        # Find post
        post = Post.objects.get(id = post_id)
        post.delete()
        return HttpResponseRedirect('/')

def credits(request):
        return render(request, 'credits.html')

def edit(request, post_id):
  # Get requested tweet
  post = Post.objects.get(id = post_id)

  # If the method is POST
  if request.method == 'POST':
    form = PostForm(request.POST, request.FILES, instance=post)
  
    if form.is_valid():
      # Save and redirect to home
      form.save()
      return HttpResponseRedirect('/')
    else:
      print(form.errors)

  
  # Show editting screen
  form = PostForm
  return render(request, 'edit.html',
  {'post': post, 'form': form})

def like(request, post_id):
  post = Post.objects.get(id = post_id)
  print(post_id)
  post.like_count += 1
  post.save()
  return HttpResponseRedirect('/')


