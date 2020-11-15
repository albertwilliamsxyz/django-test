from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='projects_index'),
    path('<int:id>/', details, name='projects_details'),
]
