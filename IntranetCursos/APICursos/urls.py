from django.urls import path
from .views import APICursosViews
urlpatterns=[
    path('',APICursosViews.as_view(),name='profesores_lists'),
    #guia = path('<int:CodDocente>',APICreditosViews.as_view(), name='profesores_process')
]