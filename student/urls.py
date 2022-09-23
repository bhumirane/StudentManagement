
from django.contrib import admin
from django.urls import path
from student import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>',views.view_student, name='view_student'),
    path('add/', views.adda, name='add'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('delete/<int:id>/', views.delete, name='delete'),

]