from django.urls import path
from . import views

urlpatterns = [
    path('view/', views.view, name = 'view'),
    path('mycourse/', views.mycourse, name = 'mycourse'),
    path('detail/<int:id>', views.detail, name = 'detail'),
]
