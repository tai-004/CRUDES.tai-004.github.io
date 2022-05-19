from django.urls import path

from . import views

urlpatterns = [
    #127.0.0.1:8000/pessoas/
    path('', views.index, name='index'),
    
    #127.0.0.1:8000/pessoas/88
    path('<int:pessoa_id>/', views.detail, name='detail'),
    
    #127.0.0.1:8000/pessoas/excluir/888
    path('excluir/<int:pessoa_id>/', views.excluir, name='excluir'),
    
    #127.0.0.1:8000/pessoas/criar
    path('criar/', views.criar, name='criar'),
    
    #127.0.0.1:8000/pessoas/editar/88
    path('editar/<int:pessoa_id>/', views.editar, name='editar'),
    
    path('template/', views.template, name="template")
]