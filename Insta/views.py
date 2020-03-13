#from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from Insta.models import Post
#class-based view
class HelloWorld(TemplateView):
    template_name = 'test.html'

class PostsView(ListView):
    model = Post
    template_name = 'index.html'
