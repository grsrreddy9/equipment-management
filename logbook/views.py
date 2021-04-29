
from rest_framework.views import APIView
from rest_framework.response import Response
from Main.serializers import ProductSerializer , EquipmentSerializer
from Main.models import Manufacturer,Department,Product,Equipment
from .models import LogBook, CleanType
from .serializers import LogBookSerializer, CleanTypeSerializer

class LogBookView(APIView):

    # authentication_classes = [authentication.TokenAuthentication]
    #permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        log_book = LogBook.objects.all()
        log_book_serializer = LogBookSerializer(log_book, many=True)
        return Response(log_book_serializer.data)


    def post(self, request, format=None):
        log_book_serializer = LogBookSerializer(request.data)
        if (log_book_serializer.is_valid()):
            log_book_serializer.save()
            return Response(log_book_serializer.data, status=201)
        return Response(log_book_serializer.errors, status=400)


class CleanTypeView(APIView):

    def get(self, request, format=None):
        clean_types = CleanType.objects.all()
        clean_types_serializer = CleanTypeSerializer(clean_types, many=True)
        return Response(clean_types_serializer.data)



# Create your views here.
