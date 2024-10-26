from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializer


@api_view(['GET'])
def get_books(request):
    obj = Book.objects.all()
    serializer = BookSerializer(obj, many = True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_book(request):
    serializer = BookSerializer(data = request.data)
    if not serializer.is_valid():
        return Response({'message':'Invalid Request'}, status=status.HTTP_400_BAD_REQUEST)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)