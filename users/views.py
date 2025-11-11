from .serializers import UserRegisterSerializer
# from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



class RegisterView(APIView):
    
    def post(self, request, *args, **kwargs):
        serializer = UserRegisterSerializer(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            data = {
                'id':user.id,
                'full_name': user.full_name,
                'email': user.email
            }
            return Response(data, status= status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)






# class UserLoginView(APIView):
#     def post(self, request):
#         serializer = UserLoginSerializer(data=request.data)
#         if serializer.is_valid():
#             email = serializer.validated_data['email']
#             password = serializer.validated_data['password']
#             user = authenticate(email=email, password=password)
            
#             if user:
#                 return Response({"message": "Login successful!"})
#             else:
#                 return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
