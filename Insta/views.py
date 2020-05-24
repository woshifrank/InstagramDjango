#from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from Insta.models import Post
# for signup feature
from Insta.forms import CustomUserCreationForm
# for mixin
from django.contrib.auth.mixins import LoginRequiredMixin

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


class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    template_name = 'post_create.html'
    fields = '__all__'
    login_url = 'login'

class PostUpdateView(LoginRequiredMixin,UpdateView):
    model = Post
    template_name = 'post_update.html'
    fields = ["title"]
    login_url = 'login'

class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    template_name = 'post_delete.html'
    # prevent early jump before deletion complete
    success_url = reverse_lazy("posts")
    login_url = 'login'

class SignUp(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy("login")
