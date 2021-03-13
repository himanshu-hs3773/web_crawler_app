from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('css/', include('web_crawler_app.urls')),
    path('search/', views.new_search, name='new_search'),
]
