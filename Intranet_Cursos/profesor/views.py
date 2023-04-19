from django.shortcuts import render
from django.views import View
from .models import Profesor
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

class ProfesorViews(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self , request,CodDocente=0):
        if(CodDocente>0):
            profesores = list(Profesor.objects.filter(CodDocente=CodDocente).values()) 
            if len(profesores)>0:
                profesores = profesores[0]
                datos = {'companies': profesores}
            else:
                datos = {'message: ': "Profesores no found..."}
            return JsonResponse(datos)
        else:
            profesores = list(Profesor.objects.values())
            if len(profesores)>0:
                datos = {'companies': profesores}
            else:
                datos = {'message: ': "Profesores no found..."}
            return JsonResponse(datos)
    
    def post(self, request):
        jd=json.loads(request.body)
        Profesor.objects.create(NomDocente=jd['NomDocente'],ApeDocente=jd['ApeDocente'],
                                EmaDocente=jd['EmaDocente'],NumDocente=jd['NumDocente'],
                                DirDocente=jd['DirDocente'])
        datos={
                'messaje': 'Success'
            }
        return JsonResponse(datos)
    
    def put(self,request,CodDocente):
        jd=json.loads(request.body)
        profesores = list(Profesor.objects.filter(CodDocente=CodDocente).values()) 
        if len(profesores)>0:
            prof = Profesor.objects.get(CodDocente=CodDocente)
            prof.NomDocente=jd['NomDocente']
            prof.ApeDocente=jd['ApeDocente']
            prof.EmaDocente=jd['EmaDocente']
            prof.NumDocente=jd['NumDocente']
            prof.DirDocente=jd['DirDocente']
            prof.save()
            datos={'messaje': 'Success'}
        else:
            datos = {'message: ': "Profesores no found..."}
        return JsonResponse(datos)