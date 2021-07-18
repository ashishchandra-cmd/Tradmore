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




class Login(ViewSet):
    def create(self,request):
        data=request.data
        username1=data.get('phone')
        password1=data.get('password')
        if username1=='' or password1=='':
            response_data = {'response_code':200,'comments':'all fields is required',"status": False}
            return Response(response_data)
        user1=authenticate(username=username1,password=password1)
        if user1 is not None:
            user_det=User.objects.get(username=username1)
            sending_data=[]
            userdata={'id':user_det.id,'phone':user_det.username,'fullname':user_det.first_name}
            sending_data.append(userdata)
            response_data = {'user_data':sending_data,'response_code':200,'comments':'login',"status": True}
            return Response(response_data)     
        else:
            response_data = {'response_code':200,'comments':'fill currect phone and password',"status": False}
            return Response(response_data)


class CustomerRegist(ViewSet):
    def create(self,request):
        data=request.data
        username1=data.get("phone")
        password1=data.get("password")
        fname=data.get("fullname")
        # print(username1,password1,phone1)
        if username1=='' or password1=='' or fname=='':
            response_data = {'response_code':200,'comments':'all fields is required',"status": False}
            return Response(response_data)
        try:
            user1=User(username=username1,password=make_password(password1),first_name=fname)
            user1.save()
            user_inst=User.objects.get(username=username1)#instance
            sending_data=[]
            userdata={'id':user_inst.id,'phone':user_inst.username,'fullname':user_inst.first_name}
            sending_data.append(userdata)
            response_data = {'user_data':sending_data,'response_code':200,'comments':'register is succeefull',"status": True}
            return Response(response_data)
        except :
            user_inst=User.objects.get(username=username1)#instance
            sending_data=[]
            userdata={'id':user_inst.id,'phone':user_inst.username,'fullname':user_inst.first_name}
            sending_data.append(userdata)
            response_data = {'user_data':sending_data,'response_code':200,'comments':'All ready created',"status": False}
        return Response(response_data)

    def list(self,request):
        user_obj=User.objects.all()
        if user_obj:
            dat_dict={}
            data_list=[]
            for x in user_obj:
                dat_dict={'user_id':x.id,'user_phone':x.username,'user_name':x.first_name}
                data_list.append(dat_dict)
            user_dict={"user_details":data_list,'response_code':200,'comments':'all list of user',"status": True}
            return Response(user_dict)
        else:
            user_dict={'response_code':200,'comments':'no details of user',"status": False}
            return Response(user_dict)