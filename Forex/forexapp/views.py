from typing import Counter
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.hashers import make_password,check_password
from forexapp.models import *

##################CustomerRegister start #######################



class CustomerRegister(ViewSet):
    def create(self,request):
        data=request.data
        username1=data.get("name")
        password1=data.get("password")
        phone1=data.get("phone")
        # print(username1,password1,phone1)
        if username1=='' or password1=='' or phone1=='':
            response_data = {'response_code':200,'comments':'all fields is required',"status": False}
            return Response(response_data)
        try:
            user1=User(username=username1,password=make_password(password1))
            user1.save()
            user_inst=User.objects.get(username=username1)#instance
            servive=Customer(user=user_inst,phone=phone1)
            servive.save()
            customer_inst=Customer.objects.get(user=user_inst)
            sending_data=[]
            userdata={'id':user_inst.id,'name':user_inst.username,'phone':customer_inst.phone}
            sending_data.append(userdata)
            response_data = {'user_data':sending_data,'response_code':200,'comments':'register is succeefull',"status": True}
            return Response(response_data)
        except :
            user_inst=User.objects.get(username=username1)#instance
            customer_inst=Customer.objects.get(user=user_inst)
            sending_data=[]
            userdata={'id':user_inst.id,'name':user_inst.username,'phone':customer_inst.phone}
            sending_data.append(userdata)
            response_data = {'user_data':sending_data,'response_code':200,'comments':'All ready created',"status": False}
        return Response(response_data)

######################CustomerRegister end #######################

#################### start login api ####################
class Login_check(ViewSet):
    def create(self,request):
        data=request.data
        username1=data.get('name')
        password1=data.get('password')
        if username1=='' or password1=='':
            response_data = {'response_code':200,'comments':'all fields is required',"status": False}
            return Response(response_data)
        user1=authenticate(username=username1,password=password1)
        if user1 is not None:
            user_det=User.objects.get(username=username1)
            user_reg=Customer.objects.get(user=user_det)
            sending_data=[]
            userdata={'id':user_det.id,'name':user_det.username,'phone':user_reg.phone}
            sending_data.append(userdata)
            response_data = {'user_data':sending_data,'response_code':200,'comments':'login',"status": True}
            return Response(response_data)     
        else:
            response_data = {'response_code':200,'comments':'user is not login',"status": False}
            return Response(response_data)
        #################### end login api ####################




############################start logout api ####################


class Logout_check(ViewSet):
    def list(self,request):
        logout(request)
        response_data = {'response_code':200,'comments':'logout is successful',"status": True}
        return Response(response_data) 
