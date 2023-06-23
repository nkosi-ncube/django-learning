from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.views.generic import ListView,DetailView
from .models import Post
from django.urls import reverse_lazy
# Create your views here.
class BlogHomeView(ListView):
    model = Post
    template_name='home.html'
    context_object_name='all_blogs'

class BlogDetailView(DetailView):
    model=Post
    template_name='post_detail.html'   


#Below are the CRUD operations -create,read,update and delete
class BlogNewPostView(CreateView):
    model=Post
    template_name='post_new.html'
    fields=['title','author','body']
    
class BlogUpdateView(UpdateView):
    model=Post
    template_name='post_edit.html'
    fields=['title','body',]    

class BlogDeleteView(DeleteView):
    model=Post
    template_name='post_delete.html'
    success_url=reverse_lazy('home')    