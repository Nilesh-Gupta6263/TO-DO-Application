from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import logout


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.signup, name='signup'),
    path('loginn/', views.login_View, name='login'),
    path('todopage/', views.todo_view, name='todo'),
    path('delete/<int:id>/', views.delete_task, name='delete_task'),
    path('edit/<int:id>/', views.edit_task, name='edit_task'),
    path('logout/', views.logout_view, name='logout'),
]