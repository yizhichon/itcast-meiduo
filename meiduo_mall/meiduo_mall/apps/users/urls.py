from django.urls import path,re_path
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.routers import DefaultRouter

from . import views

urlpatterns = [
    path('users/', views.UserView.as_view()),
    re_path(r'usernames/(?P<username>\w{5,20})/count/', views.UsernameCountView.as_view()),
    re_path(r'mobiles/(?P<mobile>1[345789]\d{9})/count/', views.MobileCountView.as_view()),
    path('authorizations/', views.UserAuthorizationView.as_view()), # 登录,获取JWT token
    re_path(r'^accounts/(?P<account>\w{4,20})/sms/token/$', views.SMSCodeTokenView.as_view()),  # 获取发送短信验证码的token
    re_path(r'^accounts/(?P<account>\w{4,20})/password/token/$', views.PasswordTokenView.as_view()),  # 获取修改密码的token
    re_path(r'^users/(?P<pk>\d+)/password/$', views.PasswordView.as_view()),  # 重置密码的
    path('user/', views.UserDetailView.as_view()),  # 用户个人中心数据
    path('emails/', views.EmailView.as_view()),  # 发送邮件
    path('emails/verification/', views.EmailVerifyView.as_view()),  # 更新邮箱
    path('browse_histories/', views.UserHistoryView.as_view())

]

router = DefaultRouter()
router.register('addresses', views.AddressViewSet, base_name='addresses')

urlpatterns += router.urls
