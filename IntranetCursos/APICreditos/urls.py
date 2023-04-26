from django.urls import path
from .views import CreditoViews

urlpatterns=[
    path('',CreditoViews.as_view(), name='creditos_lists'),
    path('<int:CodCredito>',CreditoViews.as_view(), name='creditos_process')
]