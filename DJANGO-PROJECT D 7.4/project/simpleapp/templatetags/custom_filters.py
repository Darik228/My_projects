from django import template
import random


register = template.Library()   # если мы не зарегистрируем наши фильтры,
# то Django никогда не узнает, где именно их искать, и фильтры потеряются
#  {% load custom_filters %}.
@register.filter(name='multiply') # регистрируем наш фильтр под именем multiply,
# чтоб django понимал, что это именно фильтр, а не простая функция
def multiply(value, arg):  # первый аргумент здесь — это то значение, к которому надо применить фильтр,
# второй аргумент это аргумент фильтра, т. е. примерно следующее будет в шаблоне value|multiply:arg
   if isinstance(value, str) and isinstance(arg, int):
      return str(value) * arg  # возвращаемое функцией значение — это то значение, которое подставится к нам в шаблон
   else:
      raise ValueError(f'Нельзя умножить {type(value)} на {type(arg)}')


@register.filter(name='censor')
def censor(value):
   chars = ["*", "#", "%", "&", "?", "@", "£"]
   bad_words = ["блять", "бля", "сука", "далбаеб", "пидр", "пидарас", "гандон", "хуй", "пизда", "ебан"]
   if isinstance(value, str):
      value = value.lower().split(' ')
      for word in value:
         if word in bad_words:
            temp = random.sample(chars, len(word))
            replaced_word = ''.join(temp)
            value = [x.replace(word, replaced_word) for x in value]
      return ' '.join(map(str, value)).capitalize()