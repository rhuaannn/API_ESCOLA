from django.contrib import admin
from django.urls import path

from intervalo.views import IntervaloCreateListView
from intervalo.views import IntervaloRetriveUpdateDestroyView

from professor.views import ProfessorCreateListView
from professor.views import ProfessorRetriveUpdateDestroyView


urlpatterns = [
    path('admin/', admin.site.urls),

    path('professor/', ProfessorCreateListView.as_view()),
    path('professor/<int:pk>', ProfessorRetriveUpdateDestroyView.as_view()),

    path('intervalo/', IntervaloCreateListView.as_view()),
    path('intervalo/<int:pk>', IntervaloRetriveUpdateDestroyView.as_view())
]
