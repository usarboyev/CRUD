from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_form, name='add'),
    path('add-record/', views.add_rec, name='add_rec'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('update/update-record/<int:id>/', views.upd_rec, name='upd_rec')
]