
from django.urls import path
from . import views # . is because views is the same folder(blog)

app_name = 'blog'
urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    path('<int:blog_id>/', views.detail, name='detail'),
]
