from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
   # path('delete/<int:pk>/', views.delete, name="delete"),
    #path('delete/(?P<pk>)[\d]+)/$', views.delete, name="delete"),
    path('<int:pk>/delete', views.delete, name="delete"),
    path(r'^<int:pk>/update', views.update, name="update")

]