from django.urls import include, path, re_path

from apps.api import views


urlpatterns = [
    # AUTH
    path('accounts/password/reset/', views.ResetPassword.as_view(), name='api_account_reset_password'),
    path('accounts/signup/', views.SignUp.as_view(), name='api_account_signup'),
    path('accounts/login/', views.Login.as_view(), name='api_account_login'),
    path('accounts/login/facebook/', views.FacebookLogin.as_view(), name='api_account_login_fb'),

    # TOKEN
    path('accounts/refresh/token/', views.RefreshToken.as_view(), name='api_refresh_token'),
    path('accounts/pushtoken/', views.AppRegistrationAPI.as_view(), name='api_token'),
    path('accounts/login/convert_token/', views.ConvertToken.as_view(), name='api_account_login_convert_token'),

    # MESSAGE
    path('notification/send/', views.SendPushNotification.as_view(), name='api_notification_send_push_notification'),
    path('card/real/create/', views.CadCartao.as_view(), name='api_card_real_create'),
    path('card/vigente/create/', views.CadVigente.as_view(), name='api_card_vigente_create'),
    path('transacao/list/', views.TransacaoList, name='api_transacao_list'),

    # SERVICES
    re_path(r'^cep/(?P<cep>\w+)/$', views.AddressAPI.as_view(), name='api_address'),
]
