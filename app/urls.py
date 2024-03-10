from django.contrib import admin
from django.urls import path
from auxiliar.views import AuxiliarCreateListView, AuxiliarRetriveUpdateDestroyView

from intervalo.views import IntervaloCreateListView
from intervalo.views import IntervaloRetriveUpdateDestroyView

from professor.views import ProfessorCreateListView
from professor.views import ProfessorRetriveUpdateDestroyView

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('professor/', ProfessorCreateListView.as_view()),
    path('professor/<int:pk>', ProfessorRetriveUpdateDestroyView.as_view()),

    path('intervalo/', IntervaloCreateListView.as_view()),
    path('intervalo/<int:pk>', IntervaloRetriveUpdateDestroyView.as_view()),

    path('auxiliar/', AuxiliarCreateListView.as_view()),
    path('auxiliar/<int:pk>', AuxiliarRetriveUpdateDestroyView.as_view()),

    path('authentication/token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('authentication/token/refresh/',
         TokenRefreshView.as_view(), name='token_refresh'),
    path('authentication/token/verify/',
         TokenVerifyView.as_view(), name='token_verify'),

]
