from django.urls import path
from .views import APICreditosViews
urlpatterns=[
    path('',APICreditosViews.as_view(),name='profesores_lists')
    #guia = path('<int:CodDocente>',APICreditosViews.as_view(), name='profesores_process')
]