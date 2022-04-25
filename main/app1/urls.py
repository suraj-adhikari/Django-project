from django.urls import path
from app1 import views

urlpatterns = [
   path('showme/',views.showme),
    path('index/',views.index),
    path('home/',views.home),
    path('Form/',views.Form),
    path('create/',views.create_view),
    path('data/',views.data_view),
    path('detail/<id>/',views.detail_view),
    # path('api/',include(router.urls)),
]
