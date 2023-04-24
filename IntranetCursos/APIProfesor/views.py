from django.shortcuts import render
from django.views import View
from .models import TbProfesor
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import Http404

class APIProfesorViews(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self , request,CodigoDocente=0):
        if(CodigoDocente>0):
            profesores = list(TbProfesor.objects.filter(CodigoDocente=CodigoDocente).values()) 
            if len(profesores)>0:
                profesores = profesores[0]
                datos = {'Profesores': profesores}
            else:
                raise Http404("Profesores no encontrados")
            return JsonResponse(datos)
        else:
            profesores = list(TbProfesor.objects.values())
            if len(profesores)>0:
                datos = {'Profesores': profesores}
            else:
                raise Http404("Profesores no encontrados")
            return JsonResponse(datos)
    
    def post(self, request):
        jd=json.loads(request.body)
        TbProfesor.objects.create(NombreDocente=jd['NombreDocente'],ApellidoDocente=jd['ApellidoDocente'],
                                EmailDocente=jd['EmailDocente'],NumeroDocente=jd['NumeroDocente'],
                                DireccionDocente=jd['DireccionDocente'])
        datos={
                'messaje': 'Success'
            }
        return JsonResponse(datos)
    
    def put(self,request,CodigoDocente):
        jd=json.loads(request.body)
        profesores = list(TbProfesor.objects.filter(CodigoDocente=CodigoDocente).values()) 
        if len(profesores)>0:
            prof = TbProfesor.objects.get(CodigoDocente=CodigoDocente)
            prof.NombreDocente=jd['NombreDocente']
            prof.ApellidoDocente=jd['ApellidoDocente']
            prof.EmailDocente=jd['EmailDocente']
            prof.NumeroDocente=jd['NumeroDocente']
            prof.DireccionDocente=jd['DireccionDocente']
            prof.save()
            datos={'messaje': 'Success'}
        else:
            raise Http404("Profesores no encontrados")
        return JsonResponse(datos)