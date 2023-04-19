from django.urls import path
from .views import ProfesorViews
urlpatterns=[
    path('profesores/',ProfesorViews.as_view(), name='profesores_lists'),
    path('profesores/<int:CodDocente>',ProfesorViews.as_view(), name='profesores_process')
]