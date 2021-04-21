
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProductSerializer , EquipmentSerializer , DepartmentSerializer
from .models import  Manufacturer ,Department ,Product ,Equipment
from rest_framework.parsers import JSONParser

class DepartmentView(APIView):

    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        department = Department.objects.all()


        department_serializer = DepartmentSerializer(department, many=True)

        return Response(department_serializer.data)

    def post(self, request, format=None):
       # data = JSONParser().parse(request)
        serializer = DepartmentSerializer(data=request.data)

        print(request.data)
        if serializer.is_valid():

            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class ProductView(APIView):

        # authentication_classes = [authentication.TokenAuthentication]
        # permission_classes = [permissions.IsAdminUser]

        def get(self, request, format=None):
            product = Product.objects.all()

            product_serializer = ProductSerializer(product, many=True)

            return Response(product_serializer.data)

        def post(self, request, format=None):
            # data = JSONParser().parse(request)
            serializer = ProductSerializer(data=request.data)

            print(request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)


class EquipmentView(APIView):

    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        equipment = Equipment.objects.all()

        equipment_serializer = EquipmentSerializer(equipment, many=True)

        return Response(equipment_serializer.data)

    def post(self, request, format=None):
        # data = JSONParser().parse(request)
        serializer = EquipmentSerializer(data=request.data)

        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
# Create your views here.
