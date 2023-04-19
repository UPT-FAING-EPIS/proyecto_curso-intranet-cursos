from django.shortcuts import render
from django.views import View
from .models import Creditos2
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

class CreditoViews(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self , request,CodCredito=0):
        if(CodCredito>0):
            creditos = list(Creditos2.objects.filter(CodCredito=CodCredito).values()) 
            if len(creditos)>0:
                creditos = creditos[0]
                datos = {'companies': creditos}
            else:
                datos = {'message: ': "creditos no found..."}
            return JsonResponse(datos)
        else:
            creditos = list(Creditos2.objects.values())
            if len(creditos)>0:
                datos = {'companies': creditos}
            else:
                datos = {'message: ': "creditos no found..."}
            return JsonResponse(datos)
    
    def post(self, request):
        jd=json.loads(request.body)
        Creditos2.objects.create(TipCredito=jd['TipCredito'])
        datos={
                'messaje': 'Success'
            }
        return JsonResponse(datos)
    
    def put(self,request,CodCredito):
        jd=json.loads(request.body)
        creditos = list(Creditos2.objects.filter(CodCredito=CodCredito).values()) 
        if len(creditos)>0:
            cred = Creditos2.objects.get(CodCredito=CodCredito)
            cred.TipCredito=jd['TipCredito']
            
            cred.save()
            datos={'messaje': 'Success'}
        else:
            datos = {'message: ': "creditos no found..."}
        return JsonResponse(datos)