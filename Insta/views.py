#from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from Insta.models import Post
# for signup feature
from django.contrib.auth.forms import UserCreationForm

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

def blog_detail_view(request,primary_key):
    try:
        post = Post.objects.get(pk=primary_key)
    except Post.DoesNotExist:
        raise Http404('We are sorry... but this page does not exist')
    return render(request,'post_detail.html', context = {'post':post})


class PostCreateView(CreateView):
    model = Post
    template_name = 'post_create.html'
    fields = '__all__'

class PostUpdateView(UpdateView):
    model = Post
    template_name = 'post_update.html'
    fields = ["title"]

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    # prevent early jump before deletion complete
    success_url = reverse_lazy("posts")

class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy("login")
