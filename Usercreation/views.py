import json
from sqlite3 import IntegrityError
from rest_framework import generics, permissions
from rest_framework.response import Response
from django.forms import ValidationError
from Usercreation.serializer import RegistrationSerializer,CampaignsSerializer, OrganizationSerializer
from rest_framework.authtoken.models import Token
from .models import Users
from rest_framework.views import APIView
from .serializer import  RegistrationSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import generics

# @api_view(["POST"])
# @permission_classes([AllowAny])
# def Register_Users(request):
#     try:
#         data = {}
#         serializer = RegistrationSerializer(data=request.data)
#         if serializer.is_valid():
#             user = Users.objects.filter(Email_Address = serializer.data['Email_Address'])
#             # user = Users.objects.get(password = serializer.data['password'])
#             token = Token.objects.get_or_create(user=user)[0].key
#             data["message"] = "user registered successfully"
#             data["email"] = user.Email_Address
#             data["name"] = user.name
#             data["token"] = token

#         else:
#             data = serializer.errors
        


#         return Response(data,{'status':200,'payload':serializer.data})
#     except IntegrityError as e:
#         account=Users.objects.get(user='')
#         account.delete()
#         raise ValidationError({"400": f'{str(e)}'})

#     except KeyError as e:
#         print(e)
#         raise ValidationError({"400": f'Field {str(e)} missing'})
@api_view(["POST"])
@permission_classes([AllowAny])
def Register_Users(request):
    try:
        data = []
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            account = serializer.save()
            account.is_active = True
            account.save()
            token = Token.objects.get_or_create(user=account)[0].key
            data["message"] = "user registered successfully"
            data["email"] = account.email
            data["username"] = account.username
            data["token"] = token

        else:
            data = serializer.errors


        return Response(data)
    except IntegrityError as e:
        account=Users.objects.get(username='')
        account.delete()
        raise ValidationError({"400": f'{str(e)}'})

    except KeyError as e:
        print(e)
        raise ValidationError({"400": f'Field {str(e)} missing'})


@api_view(["POST"])
@permission_classes([AllowAny])
def login_user(request):

        data = {}
        reqBody = json.loads(request.body)
        email1 = reqBody['Email_Address']
        password = reqBody['password']
        try:

            Account = Users.objects.get(Email_Address=email1)
        except BaseException as e:
            raise ValidationError({"400": f'{str(e)}'})

        token = Token.objects.get_or_create(user=Account)[0].key
        

        if Account:
            if Account.is_active:
                # login(request, Account)
                data["message"] = "user logged in"
                data["email_address"] = Account.Email_Address

                Res = {"data": data, "token": token}

                return Response(Res)

            else:
                raise ValidationError({"400": f'Account not active'})

        else:
            raise ValidationError({"400": f'Account doesnt exist'})





class OrganizationView(APIView):
    serializer_class = OrganizationSerializer
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class CampignsView(APIView):
    serializer_class =  CampaignsSerializer
    def post(self,request):
        serializer = self.serializer_class(data=request.data.id)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
