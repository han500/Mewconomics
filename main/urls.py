from django.urls import path

from . import views

app_name = 'main'
urlpatterns = [
    path('', views.home, name='home'),
    path('extra/', views.extra, name='extra'),
    path('essays/', views.essays, name='essays'),
    path('essays/<str:chapter>/<str:subtopic>/', views.show_essay, name='essay'),
]