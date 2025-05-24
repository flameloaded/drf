from .serializers import StudentSerializer, EmployeeSerialiazer
from blogs.serializer import BlogSerializer, CommentSerializer
from students.models import Student
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from employee.models import Employee
from django.http import Http404
from rest_framework import mixins,generics,viewsets
from django.shortcuts import render, get_object_or_404
from blogs.models import Blog, Comment
from blogs.serializer import CommentSerializer
from .paginations import CustomPagination
from django_filters.rest_framework import DjangoFilterBackend
from employee.filters import EmployeeFilter

@api_view(['GET', 'POST'])
def studentView(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def StudentDetailView(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serialier = StudentSerializer(student)
        return Response(serialier.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serialier = StudentSerializer(student, data=request.data)
        if  serialier.is_valid():
            serialier.save()
            return Response(serialier.data,status=status.HTTP_200_OK)
        return Response(serialier.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# class Employees(APIView):
#     def get(self, request):
#         employees = Employee.objects.all()
#         serializer = EmployeeSerialiazer(employees, many = True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     def post(self, request):
#         serializer = EmployeeSerialiazer(data= request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class EmployeeDetail(APIView):
#     def get_object(self,pk):
#         try:
#             return Employee.objects.get(pk=pk)
#         except Employee.DoesNotExist:
#             raise Http404
        
#     def get(self, request, pk):
#         employee = self.get_object(pk)
#         serializer = EmployeeSerialiazer(employee)
#         return Response(serializer.data,status=status.HTTP_200_OK)
    
#     def put(self, request, pk):
#         employee = self.get_object(pk)
#         serializer = EmployeeSerialiazer(employee, data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status.HTTP_200_OK)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk):
#         employee = self.get_object(pk)
#         employee.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# Mixinns
# class Employees(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerialiazer

#     def get(self,request):
#         return self.list(request)
    
#     def post(self,request):
#         return self.create(request)
    
# class EmployeeDetail(mixins.RetrieveModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerialiazer

#     def get(self, request, pk):
#         return self.retrieve(request, pk)
    
#     def put(self, request, pk):
#         return self.update(request,pk)
    
#     def delete(self, request, pk):
#         return self.destroy(request, pk)


#Generics Vies
# class Employees(generics.ListCreateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerialiazer


# class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerialiazer
#     lookup_field = 'pk'

# class EmployeeViewset(viewsets.ViewSet):
#     def list(self, request):
#         queryset = Employee.objects.all()
#         serializer = EmployeeSerialiazer(queryset,many=True)
#         return Response(serializer.data)
    
#     def create(self, request):
#         serializer = EmployeeSerialiazer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors)
    
#     def retrieve(self, request, pk=None):
#         employee = get_object_or_404(Employee,pk=pk)
#         serializer = EmployeeSerialiazer(employee)
#         return Response(serializer.data,status=status.HTTP_200_OK)
    
#     def update(self, request, pk=None):
#         employee = get_object_or_404(Employee,pk=pk)
#         serializer = EmployeeSerialiazer(employee, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)
    
#     def delete(self, request, pk=None):
#         employee = get_object_or_404(Employee, pk=pk)
#         employee.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

class EmployeeViewset(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerialiazer
    pagination_class = CustomPagination
    filterset_class = EmployeeFilter

class BlogViews(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class CommentViews(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'pk'


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'pk'
