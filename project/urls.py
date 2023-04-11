

from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from app.views import MyTokenObtainPairView,CustomUserCreateAPIView, ProductCreateAPIView,ProductListCreateAPIView, ProductRetrieveUpdateDestroyAPIView

  
  
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',CustomUserCreateAPIView.as_view(),name='register'),
    path('login/', MyTokenObtainPairView.as_view(),
         name='login'),


    path('products/create/', ProductCreateAPIView.as_view(), name='product-create'),
    path('products/', ProductListCreateAPIView.as_view(), name='product-list'),
    path('products/<int:_id>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-detail'),
    path('api/token/',
         jwt_views.TokenObtainPairView.as_view(),
         name ='token_obtain_pair'),

    path('api/token/refresh/',
         jwt_views.TokenRefreshView.as_view(),
         name ='token_refresh'),
         
    



]

