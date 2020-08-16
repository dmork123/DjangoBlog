from django.shortcuts import render
from django.views.generic import ListView
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


# class based views
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']  # orders the post from newwest to oldests


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
