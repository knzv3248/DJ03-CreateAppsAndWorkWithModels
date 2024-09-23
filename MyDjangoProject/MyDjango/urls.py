# Следующие 2 строки необходимы для работы со статическими файлами
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('new', views.new, name='pagenews'),
    path('data', views.my_data, name='pagedata'),
    path('test', views.my_tests, name='pagetest'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # Строка для работы со статическими файлами в соответствии с документацией Django
