from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('reporter/new', views.new_reporter, name='new reporter'),
    path('reporter/edit', views.edit_reporter, name='edit reporter name'),
]
