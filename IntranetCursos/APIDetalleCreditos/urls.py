from django.urls import path
from .views import APIDetalleCreditosViews
urlpatterns=[
    path('',APIDetalleCreditosViews.as_view(),name='DetalleCreditos_lists'),
    #guia = path('<int:CodDocente>',APICreditosViews.as_view(), name='profesores_process')
]