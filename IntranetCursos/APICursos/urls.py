from django.urls import path
from .views import APICursosViews
urlpatterns=[
    path('',APICursosViews.as_view(),name='Cursos_lists'),
    path('<str:CodigoCurso>',APICursosViews.as_view(), name='Cursos_perCod')
]