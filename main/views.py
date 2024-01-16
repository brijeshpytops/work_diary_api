from .models import task
from .serializers import taskSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def taskListAPI(request):
    if request.method == 'GET':
        querySet = task.objects.all()
        serializer = taskSerializer(querySet, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = taskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def taskDetailAPI(request):
    if request.method == 'GET':
        pass
    if request.method == 'PUT':
        pass
    if request.method == 'PATCH':
        pass
    if request.method == 'DELETE':
        pass