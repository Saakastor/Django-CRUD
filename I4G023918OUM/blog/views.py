from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import blog

# Create your views here.
class PostListView(ListView):
    model = post

class PostCreateView(CreateView):
    model = Post
fields = "__all__"
success_url  = reverse_lazy("blog:all")

class PostDetailView(DetailView):
    model = post

class  PostUpdateView(UpdateView):
    model = Post
fields = "__all__"
success_url  = reverse_lazy("blog:all")

class  PostDeleteView(DeleteView):
    model = Post
fields = "__all__"
success_url  = reverse_lazy("blog:all")