from django.urls import path
from .views import CreditoViews
urlpatterns=[
    path('creditos/',CreditoViews.as_view(), name='creditos_lists'),
    path('creditos/<int:CodCredito>',CreditoViews.as_view(), name='creditos_process')
]