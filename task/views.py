from django.shortcuts import render
from .models import Task
from .serializers import TaskSerializer
from rest_framework import viewsets 
from rest_framework.generics import  (ListAPIView , CreateAPIView, UpdateAPIView , 
                                      DestroyAPIView , RetrieveAPIView , ListCreateAPIView ,
                                      RetrieveUpdateDestroyAPIView , )
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination




# Paginatsiya klassi
class TaskPagination(PageNumberPagination):
    page_size = 2  # Har bir sahifada 5 ta element bo‘ladi



# viewsets bunda  CRUD  hammasi bor  

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    pagination_class = TaskPagination

 

# genericlar bilan  [5 ta url chiqarishimiz kerak] 

class TaskCreateView(CreateAPIView):
    """ BU view yangi task qoshish uchun"""
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskUpdateView(UpdateAPIView):
    """ BU view taskni update qilish uchun"""
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDeleteView(DestroyAPIView):
    """ BU view taskni delet qilish uchun"""
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)

        data={
            'status': True ,
            'msg' : 'Task ochirildi'
        }
        return Response(data=data)

class TaskLIstView(ListAPIView):
    """ BU view barcha tasklarni korsatadi"""
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    pagination_class = TaskPagination

class TaskRetrieveView(RetrieveAPIView):
    """ BU view taskni ozini toliq korish uchun"""
    queryset = Task.objects.all()
    serializer_class = TaskSerializer



#generic more [ faqat ikkita url chiqarib ishlasak boladi]

class TaskListCreateView(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer 

class TaskRetrieveUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)

        data={
            'status': True ,
            'msg' : 'Task ochirildi'
        }
        return Response(data=data)



#  ApiView  bilan 

class TaskCreateApiView(APIView):
    """ BU view yangi task qoshish uchun"""
    def post(self , request):
        serializer = TaskSerializer( data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = {
             'status' : True ,
             'msg' : 'Task yaratildi' ,
             'data' : serializer.data
         }
        return Response(data = data)
     
class TaskUpdateApiView(APIView):
    """ BU view taskni update qilish uchun"""
    def patch(self , request , pk):
        try:
            task = Task.objects.get(id=pk)  # Task mavjudligini tekshiramiz
        except Task.DoesNotExist:
            data = {
                'status' : False ,
                'msg' : "Task topilmadi" ,
            }
            return Response(data= data)
        serializer = TaskSerializer(task , data=request.data , partial=True)
        if serializer.is_valid():
            serializer.save()
            data = {
                'status' : True ,
                'msg' : "Task o'zgartirildi" ,
                'data' : serializer.data
            }
            return Response(data=data)

class TaskDeletApiView(APIView):
    """ BU view taskni delet qilish uchun"""
    def delete(self , request , pk):
        try:
            task = Task.objects.get(id=pk)
        except Task.DoesNotExist:
            data = {
                'status' : False ,
                'msg' : "Task topilmadi" ,
            }
            return Response(data= data)
        task.delete()
        data = {
            'status' : True ,
            'msg' : "Task o'chirildi" ,
            }
        return Response(data=data)

class TaskListApiView(APIView):
    """ BU view barcha tasklarni korsatadi"""
    def get(self , request):
        task = Task.objects.all()
        paginator = TaskPagination()
        paginated_task = paginator.paginate_queryset(task , request)
        serializer = TaskSerializer(paginated_task , many=True)
        return paginator.get_paginated_response(serializer.data)

class TaskRetrieveApiView(APIView):
    """ BU view taskni ozini toliq korish uchun"""
    def get(self , request , pk):
        try:
            task = Task.objects.get(id=pk)
        except Task.DoesNotExist:
            data = {
                'status' : False ,
                'msg' : "Task topilmadi" ,
            }
            return Response(data=data)
        serializer = TaskSerializer(task )
        return Response(serializer.data)

        

        
