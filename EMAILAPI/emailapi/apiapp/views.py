from django.shortcuts import render
from django.core.mail import send_mail, EmailMessage
from .models import Mail
from .serializers import RegisterSerializer, MailSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

# Create your views here.

class MailView(ListCreateAPIView):
    queryset = Mail.objects.all()
    serializer_class = MailSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def create(self, request, *args, **kwargs):
        serializer = MailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
        response = super(MailView, self).create(request, *args, **kwargs)
        send_mail(
        subject=data['subject'], 
        message=data['message'], 
        recipient_list=[data['to_address']], 
        from_email='thephoenixxperson@gmail.com', 
        fail_silently=False)
        return response

# Register API
class RegisterView(GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response({
        "user": 'new user registered successfully!',
        "Token": token.key,
        })
