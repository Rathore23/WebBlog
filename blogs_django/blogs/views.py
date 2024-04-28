import time

from django.db import reset_queries, connection
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.http import HttpResponseForbidden
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
    DetailView,
    TemplateView,
)

from blogs_django.blogs.forms import PostForm
from blogs_django.blogs.models import Post


# Create your views here.
class AboutUsView(TemplateView):
    template_name = 'other_templates/about_us.html'


class ContactUsView(TemplateView):
    template_name = 'other_templates/contact_us.html'


class HomeView(ListView):
    queryset = Post.objects.all().order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 3

    def get_queryset(self):

        queryset = Post.objects.all()
        if self.request.GET.get('search') is not None:
            query = self.request.GET.get('search')
            queryset = queryset.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(author__username=query)
            )
        return queryset.order_by('-created_on')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PostForm()  # Add the PostForm to the context
        return context


class PostCreateView(CreateView):
    model = Post
    # template_name = 'index.html'
    # fields = ['title', 'content', 'status', 'image']
    form_class = PostForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blogs/post_update_1.html'
    # pk_url_kwarg = "pk"
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # Ensure the current user is the author of the post before updating
        if form.instance.author == self.request.user:
            return super().form_valid(form)
        else:
            return HttpResponseForbidden(
                "You do not have permission to update this post."
            )


class PostDeleteView(DeleteView):
    model = Post
    pk_url_kwarg = "pk"
    template_name = 'blogs/post_confirm_delete.html'
    success_url = reverse_lazy('home')


class PostDetailsView(DetailView):
    model = Post
    pk_url_kwarg = "pk"
    template_name = 'blogs/post_details.html'
    context_object_name = 'post'
