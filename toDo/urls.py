from api import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('toDoAPI/', views.to_do_api),
    path('toDoAPI/<int:time>', views.to_do_api)
]
