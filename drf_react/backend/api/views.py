from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer


class LCApiView(APIView):
    def get(self, request):
        query = Student.objects.all()
        serializer = StudentSerializer(query, many = True)
        return Response(data = serializer.data, status=status.HTTP_200_OK)