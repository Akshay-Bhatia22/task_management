from .serializers import AccountSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import UserAccount
from django.contrib.auth.password_validation import validate_password

class NewAccount(APIView):
    permission_classes = (AllowAny,)
    
    # create a new account
    def post(self, request, format = None):

        serializer = AccountSerializer(data=request.data)
        user_email = request.data.get("email",)

        # checking if user already exists
        if UserAccount.objects.filter(email__iexact = user_email).exists():
            message = {'message':'User already exists. Please Log-In'}
            return Response(message, status=status.HTTP_401_UNAUTHORIZED)

        else:
            # validate_password throws exception for valdation errors
            if request.data.get('password',)=='':
                return Response({'message':'Please enter a password'},status=status.HTTP_403_FORBIDDEN)

            try:
                validate_password(request.data.get('password',))
                if serializer.is_valid():
                    serializer.save()
                    message=serializer.data
                    return Response(message, status=status.HTTP_200_OK)
                    
            except: 
                message = 'Please Enter a valid password.'
                return Response({'message': message},status=status.HTTP_400_BAD_REQUEST)
