from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import ToDoModel
from .serializers import ToDoSerializers

# Create your views here.
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def to_do_api(request, time=None):
    if request.method == 'GET':
        if time is not None:
            to_do = get_object_or_404(ToDoModel, time = time)
            serializer = ToDoSerializers(to_do)
            return Response(serializer.data)

        to_do_list = ToDoModel.objects.all()
        serializer = ToDoSerializers(to_do_list, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ToDoSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Posted'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        to_do = get_object_or_404(ToDoModel, pk=time)
        serializer = ToDoSerializers(to_do, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PATCH':
        to_do = get_object_or_404(ToDoModel, pk=time)
        serializer = ToDoSerializers(to_do, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data Updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        to_do = get_object_or_404(ToDoModel, pk=time)
        to_do.delete()
        return Response({'msg': 'Data Deleted'}, status=status.HTTP_204_NO_CONTENT)
