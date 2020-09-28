from django.urls import path, include


app_name = "exam"
urlpatterns = [
    path('api/', include('examination.api.urls'))
]

