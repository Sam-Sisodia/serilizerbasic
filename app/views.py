from django.shortcuts import render

# Create your views here.
from . models import *
from . serializer import*
from django.contrib.auth.models import User

from django.http import JsonResponse

from  django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.views import  APIView
from rest_framework import status
def userdata(request):
    user = User.objects.all()
    serializer= UserSerlizer(user,many=True)
    return JsonResponse(serializer.data,safe=False)

@csrf_exempt
def userpost(request):
    if request.method =="GET":
        data = Emp.objects.all()
        serializer = Empserializer(data,many=True)
        return JsonResponse(serializer.data,safe=False)



    elif request.method =="POST":                     #create must be implemate in this type post in serlizer
        data =JSONParser().parse(request)
        serializer = Empserializer(data = data, )
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data , safe=False)

        else:
            return JsonResponse(serializer.errors)


from rest_framework.response import Response

class course(APIView):

    def get(self,request,format=None):
        userdata = Course.objects.all()
        serializer = courseserializer(userdata, many=True)
        return Response((serializer.data))


    
    def post(self,request,format=None):
        serializer = courseserializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        else:
            return Response((serializer.errors))




class coursedetails(APIView):
    def get_course(self,pk):
        try:
            course = Course.objects.get(pk=pk)
            return course
        except Exception:
            return Response({"msg":"not found"})
     

    def get(self,request,pk):
        course = self.get_course(pk)
        serializer = courseserializer(course)
        return Response(serializer.data)

    
    def put(self,request,pk):
        user = self.get_course(pk)
        serializer = courseserializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


     
    def delete(self,request,pk):
        course = self.get_course(pk)
        course.delete()
        
        return Response(status=status.HTTP_200_OK)


            



    



