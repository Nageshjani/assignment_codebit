from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,IsAdminUser


from rest_framework.mixins import ListModelMixin,RetrieveModelMixin,CreateModelMixin,DestroyModelMixin,UpdateModelMixin
from rest_framework.generics import GenericAPIView
from .models import Product,CustomUser
from .serializers import ProductSerializer,CustomUserSerializerWithToken

from app.pagination import CustomePagination
from django.db.models import Q

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user:CustomUser):
        token=super().get_token(user)
        token['email']=user.email
        return token
    
    

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class CustomUserCreateAPIView(CreateModelMixin,GenericAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializerWithToken

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ProductCreateAPIView(CreateModelMixin,GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes=[IsAdminUser]
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class ProductListCreateAPIView(ListModelMixin,GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class=CustomePagination
    #permission_classes=[IsAdminUser]




    def get_queryset(self):
        queryset = super().get_queryset()
        name_filter = self.request.query_params.get('name', None)
        category_filter = self.request.query_params.get('category', None)
        brand_filter = self.request.query_params.get('brand', None)
        if name_filter or category_filter or brand_filter:
            filters = Q()
            if name_filter:
                filters &= Q(name__icontains=name_filter)
            if category_filter:
                filters &= Q(category__icontains=category_filter)
            if brand_filter:
                filters &= Q(brand__icontains=brand_filter)
            queryset = queryset.filter(filters)
        return queryset
    
    


    def get(self, request, *args, **kwargs):
        # Handle the ordering parameter
        ordering = request.query_params.get('ordering')
        if ordering:
            self.queryset = self.queryset.order_by(ordering)
        return self.list(request, *args, **kwargs)
    

class ProductRetrieveUpdateDestroyAPIView(RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin,GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = '_id'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

