from django.urls import path
from . import views   # . means currrent parkage i.e products.
# it can also be writen as from products import views, views is a module inside products parkage



urlpatterns=[
    path('', views.index),
    path('news', views.news),
    path('sales', views.sales)
]


