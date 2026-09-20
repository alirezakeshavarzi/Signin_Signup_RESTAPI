
from django.contrib import admin
from django.urls import path
from django.urls import path

from rest_framework_simplejwt import views as jwt_views




from rest_sign_in_out.views import Rigister, UserInfo, Hello

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', Rigister.as_view()),
    path('myinfo/', UserInfo.as_view()),

    path('hello_test/', Hello.as_view(), name='hello'),


    # get first access token for user
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),

    # when a user's token expires, they are given a new token here.
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

]
