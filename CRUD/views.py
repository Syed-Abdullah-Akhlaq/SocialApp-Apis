from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.generics import RetrieveAPIView
from .models import CRUD,Post
from .serializers import CRUDserializer,PostSerializer
from rest_framework import permissions 
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from django.db import connection

class CRUDviews(ListCreateAPIView):

    serializer_class = CRUDserializer
    permission_classes = (permissions.IsAuthenticated,)


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
    def get_queryset(self):
        return CRUD.objects.filter(owner = self.request.user)




class CRUDDetails(RetrieveUpdateDestroyAPIView):

    serializer_class = CRUDserializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = "id"
    
    def get_queryset(self):
        return CRUD.objects.filter(owner = self.request.user)


@api_view(['GET'])
def getOwner(request,owner):
    # print(request.data)
    # queryset = CRUD.objects.filter(owner = owner).order_by('-id')
    query=CRUD.objects.filter(owner = owner)
    a = CRUDserializer(query,many=True)
    # print(a)
    return Response(a.data)





class PostModelViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    def get_queryset(self):
        queryset = Post.objects.all()
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset
    # print('Return:',connection.queries)
    # print('No Of Queries:',len(connection.queries))






@api_view(['GET', 'POST'])
def home(request):
    student_data = Post.objects.all()
    print(type(student_data))
    data=PostSerializer(student_data,many=True).data
    print(type(data))
    for i in student_data:
        print(i.post)
    print('Return:',connection.queries)
    print('No Of Queries Student:',len(connection.queries))
    return Response({"data":data})
    # return render(request, 'NewQuerySets/home.html',{'students':student_data})