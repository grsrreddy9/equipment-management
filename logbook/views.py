
from rest_framework.views import APIView
from rest_framework.response import Response
from Main.serializers import ProductSerializer , EquipmentSerializer
from Main.models import Manufacturer,Department,Product,Equipment

class LogBook(APIView):

  # authentication_classes = [authentication.TokenAuthentication]
   #permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        products = Product.objects.all()
        equipments = Equipment.objects.all()

        product_serializer = ProductSerializer(products, many=True)
        equipment_serializer = EquipmentSerializer(equipments, many=True)
        return Response(equipment_serializer.data)


# Create your views here.
