from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from .models import Product, News, Category
from datetime import datetime
from django.shortcuts import render
from django.views import View  # импортируем простую вьюшку
from django.core.paginator import Paginator  # импортируем класс, позволяющий удобно осуществлять постраничный вывод
from .filters import ProductFilter, NewsFilter  # импортируем недавно написанный фильтр
from .forms import ProductForm, NewsForm


# Create your views here.

# В отличие от дженериков, которые мы уже знаем, код здесь надо писать самому,
# переопределяя типы запросов (например гет или пост, вспоминаем реквесты из модуля C5)
class Products(ListView):
    model = Product
    template_name = 'products.html'
    context_object_name = 'products'
    ordering = ['-price']
    paginate_by = 1  # поставим постраничный вывод в один элемент
    #  form_class = ProductForm   # добавляем форм класс, чтобы получать доступ к форме через метод POST

    def get_context_data(self, **kwargs):  # забираем отфильтрованные объекты переопределяя
        # метод get_context_data у наследуемого класса (привет, полиморфизм, мы скучали!!!)
        context = super().get_context_data(**kwargs)
        context['filter'] = ProductFilter(self.request.GET, queryset=self.get_queryset())
        # вписываем наш фильтр в контекст
        context['categories'] = Category.objects.all()
        #  context['form'] = ProductForm()
        return context

    """def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)  # создаём новую форму, забиваем в неё данные из POST-запроса

        if form.is_valid():  # если пользователь ввёл всё правильно и нигде не ошибся, то сохраняем новый товар
            form.save()

        return super().get(request, *args, **kwargs)  # отправляем пользователя обратно на GET-запрос"""


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    queryset = Product.objects.all()


class ProductCreateView(CreateView):
    template_name = 'product_create.html'
    form_class = ProductForm


#  дженерик для редактирования объекта
class ProductUpdateView(UpdateView):
    template_name = 'product_detail.html'
    form_class = ProductForm

    # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте,
    # который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Product.objects.get(pk=id)


class ProductDeleteView(DeleteView):
    template_name = 'product_delete.html'
    queryset = Product.objects.all()
    success_url = '/products/'


""""
class ProductList(ListView):
    model = Product  # указываем модель, объекты которой мы будем выводить
    template_name = 'products.html'  # указываем имя шаблона, где будет лежать HTML,
    # в котором будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'products'  # это имя списка, в котором будут лежать все объекты,
    # его надо указать, чтобы обратиться к самому списку объектов через HTML-шаблон
    queryset = Product.objects.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['value1'] = None
        return context
"""


class NewsList(ListView):
    model = News
    template_name = 'news.html'
    context_object_name = 'news'
    ordering = ['-id']
    paginate_by = 1
    # form_class = NewsForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.today()
        context['filter'] = NewsFilter(self.request.GET, queryset=self.get_queryset())
        return context

    """def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

        return super().get(request, *args, **kwargs)"""

    """def post(self, request, *args, **kwargs):
        title = request.POST['title']
        text = request.POST['text']

        news = News(title=title, text=text)
        news.save()
        return super().get(request, *args, **kwargs)"""


class NewsCreateView(CreateView):
    template_name = 'news_create.html'
    form_class = NewsForm


class NewsDetailView(DetailView):
    model = News
    template_name = 'news_detail.html'
    queryset = News.objects.all()


class NewsUpdateView(UpdateView):
    template_name = 'news_detail.html'
    form_class = NewsForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return News.objects.get(pk=id)


class NewsDeleteView(DeleteView):
    template_name = 'news_delete.html'
    queryset = News.objects.all()
    success_url = '/news/'



