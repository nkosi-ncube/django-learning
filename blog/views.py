from django.views.generic.edit import CreateView
from django.views.generic import ListView,DetailView
from .models import Post
# Create your views here.
class BlogHomeView(ListView):
    model = Post
    template_name='home.html'
    context_object_name='all_blogs'

class BlogDetailView(DetailView):
    model=Post
    template_name='post_detail.html'   