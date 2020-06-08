import django_mongoengine

from django.contrib import messages
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from mongoengine import DoesNotExist
from rest_framework.views import APIView

from rest_framework_mongoengine.generics import CreateAPIView,GenericAPIView
from rest_framework.response import Response
from rest_framework import status
#from django.contrib.auth import get_user_model
from .models import User
from .serializers import UserLoginSerializer, UserCreateSerializer

#User = get_user_model()

class UserRegister(CreateAPIView):
    serializer_class=UserCreateSerializer
    queryset = User.objects.all()

class UserLogin(GenericAPIView):
    serializer_class=UserLoginSerializer

    def get_queryset(self):
        return User.objects.all()

    def post(self,request, *args, **kwargs):
        # email = request.POST('email')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=request.POST['username'])
            print(user)
            if user['password']== password:
                user.backend = 'django_mongoengine.auth.MongoEngineBackend'
                login(request, user)
                request.session.set_expiry(60 * 60 * 1)  # 1 hour timeout
                "return"
                return HttpResponse("Login Successful!!!!!!!!!!!")  # redirect('index')
            else:
                print
                "malament"
                messages.add_message(request, messages.ERROR, u"Incorrect login name or password !")
        except DoesNotExist:
            messages.add_message(request, messages.ERROR, u"Incorrect login name or password !")
        return redirect('/loginapi/')
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid():
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class UserLogout(APIView):

    def post(self, request): # NOT TESTED
         logout(request)
         return redirect('/loginapi/')
        #return redirect('/registerapi/')




# #util
# def extractDataFromPost(request):
#     rawData = request.body.replace('false', 'False')
#     rawData = rawData.replace('true', 'True')
#     rawData = rawData.replace('null', 'None')
#     return eval(rawData)
#
# #util
# def jsonResponse(responseDict):
#     return HttpResponse(simplejson.dumps(responseDict), mimetype='application/json')
#
# def createUser(request):
#     data = extractDataFromPost(request)
#
#     email = data["email"]
#     password = data["password"]
#     user_type = data["user_type"]
#
#     try:
#         user = CustomUser.objects.get(username=email)
#         return jsonResponse({'error':True, 'message': 'Email já cadastrado'})
#     except CustomUser.DoesNotExist:
#         user = CustomUser.create_user(email, password, email)
#         user.favorites = []
#         user.save()
#         user = authenticate(username=email, password=password)
#         user.backend = 'mongoengine.django.auth.MongoEngineBackend'
#         login(request, user)
#         request.session.set_expiry(3600000) # 1 hour timeout
#         del user.password
#         return HttpResponse(simplejson.dumps(user.toJSON()))





