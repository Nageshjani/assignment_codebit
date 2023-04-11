from .models import Product,CustomUser
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken


class CustomUserSerializer(serializers.ModelSerializer):
    _id = serializers.SerializerMethodField(read_only=True)


    class Meta:
        model = CustomUser
        fields = ['_id','first_name','last_name','email','is_superuser','token']
    
    def get__id(self, obj):
        return obj.id



class CustomUserSerializerWithToken(CustomUserSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = CustomUser
        fields = ['_id','first_name','last_name','email' ,'is_superuser','token']

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)
    



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'



