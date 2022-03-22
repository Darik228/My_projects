from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from .models import Author, Category, Post, Comment, PostCategory
from .filters import PostFilters
from .forms import PostForm


class PostList(ListView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'posts'
    paginate_by = 1
    # form_class = PostForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PostForm()
        return context


class PostSearch(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'posts'
    ordering = ['-rating']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilters(self.request.GET, queryset=self.get_queryset())
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    queryset = Post.objects.all()


class PostCreateView(CreateView):
    template_name = 'post_create.html'
    form_class = PostForm


class PostUpdateView(UpdateView):
    template_name = 'post_detail.html'
    form_class = PostForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class PostDeleteView(DeleteView):
    template_name = 'post_delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'