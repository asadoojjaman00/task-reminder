from rest_framework.views import APIView
# from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
# in app module : 
from .serializers import TaskSerializer
from .models import Task


# user own task view and create view : 


class TaskListView(APIView):
    
    # user own tasks list view
    def get(self , request):
        task = Task.objects.filter(user = request.user)
        serializer = TaskSerializer(task, many = True)
        return Response(serializer.data)
    
    # user create own task

    def post(self, request):
        serializer = TaskSerializer(data =request.data, context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class TaskDetailView(APIView):

    # helper method for find user own task

    def get_object(self , pk , user):
        try:
            return Task.objects.get(pk = pk, user = user)
        except Task.DoesNotExist:
            return None

    # get one exact task 
    
    def get(self, request, pk):
        task = self.get_object(pk, request.user)
        if not task:
            return Response({"error":'task not found or unauthorized'}, status= status.HTTP_404_NOT_FOUND)
        serializer = TaskSerializer(task)
        return Response(serializer.data)
    
    # edit existing task

    def put(self , request, pk):
        task = self.get_object(pk, request.user)
        if not task:
            return Response({"error":'task not found or unauthorized'}, status= status.HTTP_404_NOT_FOUND)
        serializer = TaskSerializer(task , data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    
    # delete one existing task 

    def delete(self, request, pk):
        task = self.get_object(pk, request.user)
        if not task:
            return Response({"errors": 'task not found or unauthorized'}, status=status.HTTP_404_NOT_FOUND)
        task.delete()
        return Response({"message": 'task deleted successfully'}, status=status.HTTP_204_NO_CONTENT)



