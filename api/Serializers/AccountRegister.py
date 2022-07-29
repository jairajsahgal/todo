from rest_framework import serializers
from api.Model.Account import Account, User
from django.db.models import Q
from django.utils.translation import gettext_lazy as _
from .utils import check_password

class RegisterAccountSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=100,error_messages={"required":"Password not given!"})
    class Meta:
        model = Account
        fields = ['username','email','password']
        extra_kwargs = {'password':{'write_only':True},}
    
    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        username = attrs.get('username')

        if email and password and username:
            if User.objects.filter(Q(username=attrs.get('username')) | Q(email=attrs.get('email'))).exists():
                msg = _("Account already exists!")
                raise serializers.ValidationError(msg,code="Duplicate")
            elif not check_password(password=password):
                msg = _("Password doesn't meet conditions")
                raise serializers.ValidationError(msg,code="Unsecure Password")
            else:
                userObject = User.objects.create_user(username=username,password=password)
        else:
            msg = _("Credentials not given properly.")
            raise serializers.ValidationError(msg,code="Improper Credentials")
        attrs["user"]=userObject
        return attrs