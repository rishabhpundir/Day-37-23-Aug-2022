from rest_framework import serializers
from .models import Mail
from django.contrib.auth.models import User

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password')

class MailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mail
        fields = ['id', 'to_address', 'subject', 'message']
