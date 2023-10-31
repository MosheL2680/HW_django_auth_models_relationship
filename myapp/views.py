from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from .models import Product
from .serializers import ProductSerializer

# Create your views here.

@api_view(['POST'])
def register(req):
    User.objects.create_user(username=req.data["username"], password=req.data["password"])
    return Response({"user":"created successfuly"})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def products(req):
    return Response({f'welcome {req.user}, here are our products': ProductSerializer(Product.objects.all(), many=True).data})