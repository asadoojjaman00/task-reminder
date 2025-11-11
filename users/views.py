
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken, TokenError


from .serializers import UserRegisterSerializer, CustomObtainTokenSerializer

class RegisterView(APIView):
    permission_classes = [AllowAny]
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



class CustomLoginView(TokenObtainPairView):
    serializer_class = CustomObtainTokenSerializer

class CustomRefreshView(TokenRefreshView):
    pass 

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get('refresh')
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(
                {"detail": 'Successfully logout'},
                status= status.HTTP_205_RESET_CONTENT
            )
        except TokenError:
            return Response(
                {"detail": 'Invalid or Expired token'},
                status= status.HTTP_400_BAD_REQUEST
            )

