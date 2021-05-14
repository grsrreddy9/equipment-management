from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import (
    ProductSerializer,
    EquipmentSerializer,
    DepartmentSerializer,
    ManufacturerSerializer,
    UserSerializer,
    ProductGranulationSerializer,
    RoomSerializer
)
from .models import (
    Manufacturer,
    Department,
    Product,
    Equipment,
    User,
    ProductGranulation,
    Room,
)

class DepartmentView(APIView):
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        department = Department.objects.all()
        department_serializer = DepartmentSerializer(department, many=True)

        return Response(department_serializer.data)

    def post(self, request, format=None):
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
        data = request.data
        # department = Department.objects.get(id=data.department)
        # generated_id = department.name[0:3] + "abc"
        # data['equipment_id'] = generated_id
        serializer = EquipmentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class UsersView(APIView):
    def get(self, request, format=None):
        user_id = request.query_params.get('id')
        if (user_id):
            user = User.objects.get(id=user_id)
            user_serializer = UserSerializer(user)
            print(user_serializer.data)
        else:
            users = User.objects.all()
            user_serializer = UserSerializer(users, many=True)
        return Response(user_serializer.data)


class RoomView(APIView):
    def get(self, request, format=None):
        rooms = Room.objects.all()
        room_serializer = RoomSerializer(rooms, many=True)
        return Response(room_serializer.data)


class ProductGranulationView(APIView):
    def get(self, request, format=None):
        product_details = ProductGranulation.objects.all()
        product_details_serializer = ProductGranulationSerializer(
            product_details, many=True
        )
        data = product_details_serializer.data
        for index in range(len(data)):
            product = Product.objects.get(id=data[index]['product'])
            product_serializer = ProductSerializer(product)
            equipments = Equipment.objects.filter(id__in=data[index]['equipment'])
            equipment_serializer = EquipmentSerializer(equipments, many=True)
            room = Room.objects.get(id=data[index]['room'])
            room_serializer = RoomSerializer(room)
            data[index]['product'] = product_serializer.data
            data[index]['equipment'] = equipment_serializer.data
            data[index]['room'] = room_serializer.data
        return Response(data)

    def post(self, request, format=None):
        data = request.data
        serializer = ProductGranulationSerializer(data=data, fields=('batch_number', 'equipment',  'product', 'room', 'start_time'))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

