from django.urls import path
from basicApp import views

# Set Template Tagging
app_name = 'basicApp'

urlpatterns = [
    path('relative/', views.relative, name='relative'),
    path('page2', views.page2, name='page2')
]
