
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
        product_names = []
        equipment_ids = []
        for equipment in equipment_serializer.data:
            equipment_ids.append(equipment['equipment_id'])
        for product in product_serializer.data:
            product_names.append(product['product_name'])
        resp = {"equipment_ids": equipment_ids, "product_names": product_names}
        return Response(resp)



# Create your views here.
