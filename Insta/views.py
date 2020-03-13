#from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from Insta.models import Post
#class-based view
class HelloWorld(TemplateView):
    template_name = 'test.html'

class PostsView(ListView):
    # generate object list
    model = Post
    template_name = 'index.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
