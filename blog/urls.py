from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_index_view, name='blog_index'),
    path('<int:id>/', views.blog_details_view, name='blog_details'),
    path('<category>', views.blog_category_view, name='blog_category'),
]