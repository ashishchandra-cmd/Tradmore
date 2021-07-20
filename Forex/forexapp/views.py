from typing import Counter
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.hashers import make_password,check_password
from forexapp.models import *
import requests
from pprint import PrettyPrinter
pp = PrettyPrinter()



class CustomerRegist(ViewSet):
    def create(self,request):
        data=request.data
        username1=data.get("phone")
        password1=data.get("password")
        fname=data.get("fullname")
        print(username1,password1,fname)

        if username1=='' or password1=='' or fname=='':
            response_data = {'response_code':200,'comments':'All fields are Required',"status": False}
            return Response(response_data)
        try:
            user_inst=User.objects.get(username=username1)
            response_data = {'response_code':200,'comments':'User Already Exist',"status": False}
            return Response(response_data)
        except :
            print("except")
            user_register=User(username=username1,password=make_password(password1),first_name=fname)
            user_register.save()
            response_data = {'response_code':200,'comments':'Registration successful',"status": True}
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


class Login(ViewSet):
    def create(self,request):
        data=request.data
        username=data.get('phone')
        password=data.get('password')
        try:
            user=User.objects.filter(username=data.get('phone'))
            user_password=data.get('password')
        except:
            user=None

        if user:
            if user_password:
                if user[0].check_password(user_password):
                    response_data = {'response_code':200,'comments':'login successfully',"status": True}
                    return Response(response_data)
                else:
                    response_data = {'response_code':200,'comments':'invalid password',"status": False}
                    return Response(response_data)
            else:
                response_data = {'response_code':200,'comments':'Please enter your password',"status": False}
                return Response(response_data)
        else:
            response_data = {'response_code':200,'comments':'Please Registrations First',"status": False}
            return Response(response_data)


class Logout_check(ViewSet):
    def list(self,request):
        logout(request)
        response_data = {'response_code':200,'comments':'logout is successful',"status": True}
        return Response(response_data) 


class ForexApi(ViewSet):
    def list(self,request):
        url = "https://marketdata.tradermade.com/api/v1/live"
        currency = "USDJPY,GBPUSD,UK100"
        api_key = "Er9M81VADh7MhjmebGaY"
        querystring = {"currency":currency,"api_key":api_key}
        r= requests.get(url, params=querystring)
        try:
            userdata=r.json()
            sending_data=[]
            sending_data.append(userdata)
            response_data = {"data":sending_data,'response_code':200,'comments':'data get',"status": True}
            return Response(response_data) 
        except:
            response_data = {'response_code':200,'comments':'no data get',"status": False}
            return Response(response_data)


