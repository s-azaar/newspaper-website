from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Article


class ArticleListView(LoginRequiredMixin, ListView):
    template_name = 'articles_list.html'
    model = Article


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = 'articles_delete.html'
    model = Article
    success_url = reverse_lazy('articles_list')

    def test_func(self):  # new
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleDetailView(LoginRequiredMixin, DetailView):
    template_name = 'articles_detail.html'
    model = Article


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'articles_edit.html'
    model = Article
    fields = ('title', 'body')

    def test_func(self):  # new
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'articles_new.html'
    fields = ('title', 'body')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
