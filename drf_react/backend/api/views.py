from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer


class ListCreateAPIView(APIView):
    def get(self, request):
        query = Student.objects.all()
        serializer = StudentSerializer(query, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = StudentSerializer(data = request.data)
        if not serializer.is_valid():
            return Response({'message':'Post Unsuccessful'}, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    
class RetriveUpdateDeleteAPIView(APIView):
    def get(self, request, pk):
        try:
            query = Student.objects.get(pk = pk)
        except Student.DoesNotExist:
            return Response({'message':'Record Not Found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = StudentSerializer(query)
        return Response(serializer.data, status=status.http_)
    
    def put(self, request, pk):
        query = Student.objects.get(pk = pk)
        if not query:
            return Response({'message':'No Such Record'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = StudentSerializer(query, request.data)
        if not serializer.is_valid():
            return Response({'message': 'Update Unsuccessful'}, status=status.HTTP_304_NOT_MODIFIED)
        
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    
    
    def patch(self, request, pk):
        query = Student.objects.get(pk = pk)
        if not query:
            return Response({'message':'No Such Record'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = StudentSerializer(query, request.data, partial = True)
        if not serializer.is_valid():
            return Response({'message': 'Update Unsuccessful'}, status=status.HTTP_304_NOT_MODIFIED)
        
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

   
    
    def delete(self, request, pk):
        student = Student.objects.get(pk = pk)
        if not student:
            return Response({'message': 'Record Not Found'}, status=status.HTTP_404_NOT_FOUND)
        student.delete()
        return Response({'message': 'Deleted Successfully'}, status=status.HTTP_204_NO_CONTENT)