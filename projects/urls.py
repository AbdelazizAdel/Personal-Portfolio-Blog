from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_index_view, name='project_index'),
    path('<int:id>/', views.project_details_view, name='project_details'),
]