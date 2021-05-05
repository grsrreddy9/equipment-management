from rest_framework.views import APIView
from rest_framework.response import Response
from Main.models import User
from Main.serializers import UserSerializer
from .models import LogBook, CleanType, CleaningDetail
from .serializers import LogBookSerializer, CleanTypeSerializer, CleaningDetailSerializer


class LogBookView(APIView):

    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        log_book = LogBook.objects.all()
        log_book_serializer = LogBookSerializer(log_book, many=True)
        return Response(log_book_serializer.data)

    def post(self, request, format=None):
        log_book_serializer = LogBookSerializer(data=request.data)
        if log_book_serializer.is_valid():
            log_book_serializer.save()
            return Response(log_book_serializer.data, status=201)
        return Response(log_book_serializer.errors, status=400)


class CleanTypeView(APIView):
    def get(self, request, format=None):
        clean_types = CleanType.objects.all()
        clean_types_serializer = CleanTypeSerializer(clean_types, many=True)
        return Response(clean_types_serializer.data)


class CleaningDetailsView(APIView):
    def get(self, request, format=None):
        cleaning_details = CleaningDetail.objects.all()
        serializer = CleaningDetailSerializer(cleaning_details, many=True)
        data = serializer.data
        for index in range(len(data)):
            clean_type = CleanType.objects.get(id=data[index]['clean_type'])
            clean_type_serializer = CleanTypeSerializer(clean_type)
            equipment_cleaned_by = User.objects.get(id=data[index]['equipment_cleaned_by'])
            equipment_cleaned_by_serializer = UserSerializer(equipment_cleaned_by)
            room_cleaned_by = User.objects.get(id=data[index]['room_cleaned_by'])
            room_cleaned_by_serializer = UserSerializer(room_cleaned_by)
            data[index]['clean_type'] = clean_type_serializer.data
            data[index]['equipment_cleaned_by'] = equipment_cleaned_by_serializer.data
            data[index]['room_cleaned_by'] = room_cleaned_by_serializer.data
        return Response(data)

    def post(self, request, format=None):
        serializer = CleaningDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
