
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProductSerializer , EquipmentSerializer , DepartmentSerializer, ManufacturerSerializer, UserSerializer, ProductGranulationSerializer
from .models import  Manufacturer ,Department ,Product ,Equipment, User, ProductGranulation
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

class ManufacturerView(APIView):

    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        manufacturers = Manufacturer.objects.all()
        manufacturer_serializer = ManufacturerSerializer(manufacturers, many=True)
        return Response(manufacturer_serializer.data)

    def post(self, request, format=None):
       # data = JSONParser().parse(request)
        serializer = ManufacturerSerializer(data=request.data)

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
        print(request.data)
        data = request.data
        # department = Department.objects.get(id=data.department)
        # generated_id = department.name[0:3] + "abc"
        # data['equipment_id'] = generated_id
        serializer = EquipmentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        print("Errors: *******************")
        print(serializer.errors)
        print("Errors: ######################")
        return Response(serializer.errors, status=400)


class UserView(APIView):
    def get(self, request, format=None):
        users = User.objects.all()
        user_serializer = UserSerializer(users, many=True)
        return Response(user_serializer.data)


class ProductGranulationView(APIView):
    def get(self, request, format=None):
        product_details = ProductGranulation.objects.all()
        product_details_serializer = ProductGranulationSerializer(product_details, many=True)
        return Response(product_details_serializer.data)



# Create your views here.
