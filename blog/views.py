from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy,reverse
from .models import Post
from .forms import BlogForm 

class BlogListView(ListView):
	model=Post
	template_name="home.html"

class BlogDetailView(DetailView):
	model=Post
	form_class = BlogForm
	template_name="post_detail.html"
	success_url = reverse_lazy('post:post_detail')

class BlogCreateView(CreateView):
	model=Post
	form_class = BlogForm
	template_name="post_new.html"
	success_url = reverse_lazy('post:home')
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['value'] = '建立'
		context['title'] = '建立項目'
		return context

	# fields="__all__"

class BlogUpdateView(UpdateView):
	model=Post
	form_class = BlogForm
	template_name='post_edit.html'
	# success_url = reverse_lazy('post:home')

	def get_success_url(self, **kwargs):
		return reverse_lazy("post:post_detail", args=(self.object.id,))

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['value'] = '更新'
		context['title'] = '更新項目'
		return context

class BlogDeleteView(DeleteView):
	model=Post
	template_name="post_delete.html"
	success_url=reverse_lazy('post:home')

