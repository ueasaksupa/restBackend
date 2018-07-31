from django.urls import path
from . import views

urlpatterns = [
    path('portfolios', views.portfolio_list),
    path('portfolios/<int:pk>', views.portfolio_detail),
]