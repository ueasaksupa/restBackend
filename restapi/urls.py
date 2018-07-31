from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token
from . import views

urlpatterns = [
    path('portfolios', views.PortfolioList.as_view()),
    path('portfolios/<int:pk>', views.PortfolioDetail.as_view()),
    path('users', views.UserList.as_view()),
    path('users/<int:pk>', views.UserDetail.as_view()),
    path('api-token-auth/', obtain_jwt_token),
]