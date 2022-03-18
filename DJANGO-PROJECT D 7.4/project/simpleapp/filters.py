from django_filters import FilterSet   # импортируем filterset, чем-то напоминающий знакомые дженерики
from .models import Product, News


# создаём фильтр
class ProductFilter(FilterSet):
    # Здесь в мета классе надо предоставить модель и указать поля,
    # по которым будет фильтроваться (т. е. подбираться) информация о товарах
    class Meta:
        model = Product
        """fields = ('name', 'category', 'price', 'quantity')  # поля, которые мы будем фильтровать
        # (т. е. отбирать по каким-то критериям, имена берутся из моделей)"""
        fields = {
            'name': ['icontains'],  # мы хотим чтобы нам выводило имя хотя бы отдалённо похожее на то,
                                    # что запросил пользователь
            'quantity': ['gt'],  # количество товаров должно быть больше или равно тому, что указал пользователь
            'price': ['lt'],  # цена должна быть меньше или равна тому, что указал пользователь
        }


class NewsFilter(FilterSet):
    class Meta:
        model = News
        fields = {
            'title': ['icontains'],
            'text': ['icontains'],
        }
