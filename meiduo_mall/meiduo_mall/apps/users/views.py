from django.shortcuts import render
from rest_framework.generics import CreateAPIView,GenericAPIView,RetrieveAPIView,UpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status,mixins
from rest_framework.permissions import IsAuthenticated

from . import serializers
from .models import User
from verifications.serializers import CheckImageCodeSerialzier
from .utils import get_user_by_account
import re


# Create your views here.


class UsernameCountView(APIView):
    """
    用户名数量
    """
    def get(self, request, username):
        """
        获取指定用户名数量
        """
        count = User.objects.filter(username=username).count()

        data = {
            'username': username,
            'count': count
        }

        return Response(data)


class MobileCountView(APIView):
    """
    手机号数量
    """
    def get(self, request, mobile):
        """
        获取指定手机号数量
        """
        count = User.objects.filter(mobile=mobile).count()

        data = {
            'mobile': mobile,
            'count': count
        }

        return Response(data)


class UserView(CreateAPIView):
    """
    用户注册
    """
    serializer_class = serializers.CreateUserSerializer


class SMSCodeTokenView(GenericAPIView):
    """获取发送短信验证码的凭据"""

    serializer_class = CheckImageCodeSerialzier


    def get(self,request,account):
        # 校验图片验证码
        serializers = self.get_serializer(data=request.query_params)
        serializers.is_valid(raise_exception=True)
        # 根据account查询User对象
        user = get_user_by_account(account)
        if user is None:
            return Response({"message":'用户不存在'},status=status.HTTP_404_NOT_FOUND)
        # 根据User对象的手机号生成access_token
        pass
        access_token = user.generate_send_sms_code_token()

        mobile = re.sub(r"(\d{3})\d{4}(\d{4})",r"\1****\2",user.mobile)

        return Response({
            'mobile':mobile,
            'access_token':access_token
        })


class PasswordTokenView(GenericAPIView):
    """
    用户帐号设置密码的token
    """
    serializer_class = serializers.CheckSMSCodeSerializer

    def get(self, request, account):
        """
        根据用户帐号获取修改密码的token
        """
        # 校验短信验证码
        serializer = self.get_serializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)

        user = serializer.user

        # 生成修改用户密码的access token
        access_token = user.generate_set_password_token()

        return Response({'user_id': user.id, 'access_token': access_token})


class PasswordView(mixins.UpdateModelMixin, GenericAPIView):
    """
    用户密码
    """
    queryset = User.objects.all()
    serializer_class = serializers.ResetPasswordSerializer

    def post(self, request, pk):
        return self.update(request, pk)


class UserDetailView(RetrieveAPIView):
    """用户详情信息
    /users/<pk>/

    /user/
    """
    # def get(self, request):
    #     request.user
    #
    # def post(self, request):

    # 在类视图对象中也保存了请求对象request
    # request对象的user属性是通过认证检验之后的请求用户对象
    # 类视图对象还有kwargs属性

    serializer_class = serializers.UserDetailSerializer
    # 补充通过认证才能访问接口的权限
    permission_classes = [IsAuthenticated]

    def get_object(self):
        """
        返回请求的用户对象
        :return: user
        """
        return self.request.user


class EmailView(UpdateAPIView):
    """
    保存邮箱
    /email/
    """
    serializer_class = serializers.EmailSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


    # def get_serializer(self, *args, **kwargs):
    #     return EmailSerialier(self.request.user, data=self.request.data)


class EmailVerifyView(APIView):
    """邮箱验证"""
    def get(self, request):
        # 获取token
        token = request.query_params.get('token')
        if not token:
            return Response({'缺少token'}, status=status.HTTP_400_BAD_REQUEST)

        # 校验  保存
        result = User.check_email_verify_token(token)

        if result:
            return Response({"message": "OK"})
        else:
            return Response({"非法的token"}, status=status.HTTP_400_BAD_REQUEST)




