from django.urls import path
from .views import APIProfesorViews
urlpatterns=[
    path('',APIProfesorViews.as_view(),name='profesores_lists'),
    path('<int:CodigoDocente>',APIProfesorViews.as_view(), name='Pofesores_perId')
]