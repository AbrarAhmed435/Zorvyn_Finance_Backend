from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from django.shortcuts import get_object_or_404
from rest_framework import permissions,status
from .serializers import RegisterUserSerializer,LoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics


class RegisterView(generics.CreateAPIView):
    serializer_class=RegisterUserSerializer


class LoginView(APIView):
    permission_classes=[permissions.AllowAny]

    def post(self,request):
        serializer=LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user=serializer.validated_data['user']
        refresh=RefreshToken.for_user(user)
        return Response({ 
            "access":str(refresh.access_token),
            "refresh":str(refresh)
        },status=status.HTTP_200_OK)
    
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status, permissions
# from django.shortcuts import get_object_or_404
# from .models import User
from .serializers import RoleUpdateSerializer


class UpdateUserRoleView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, pk):
        # 🔥 Only admin can do this
        if request.user.role != 'admin':
            return Response(
                {"error": "Only admin can change roles"},
                status=status.HTTP_403_FORBIDDEN
            )

        user = get_object_or_404(User, pk=pk)

        serializer = RoleUpdateSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)

