from .models import Students
# from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt




# Create your views here.
# def index(r): 
#     return "hello"
# index()

class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'
    def create(self, validated_data):
        user = self.context['user']
        print(user)
        return Students.objects.create(**validated_data,user=user)

# register staff
@api_view(['POST'])
def register(request):
    user = User.objects.create_user(
                username=request.data['username'],
                email=request.data['email'],
                password=request.data['password']
            )
    user.is_active = True
    user.is_staff = True
    user.save()
    return Response("new user born")



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['username'] = user.username
        # ...
        return token
 
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

# @api_view(['GET'])
@permission_classes([IsAuthenticated])
class MyStudentsView(APIView):
    def get(self, request, id=-1):  # axios.get
        if int(id) > -1:
            my_model = Students.objects.get(id=id)
            serializer = StudentsSerializer(my_model, many=False)
        else:
            # my_model = Students.objects.all()
            my_model = request.user.students_set.all()
            serializer = StudentsSerializer(my_model, many=True)
        return Response(serializer.data)


    def post(self, request):  # axios.post
        print(request.user)
        serializer = StudentsSerializer(data=request.data, context={'user': request.user})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, id):  # axios.put
        my_model = Students.objects.get(id=id)
        serializer = StudentsSerializer(my_model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, id):  # axios.delete
        my_model = Students.objects.get(id=id)
        my_model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)