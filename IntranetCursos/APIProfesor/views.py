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

    def get(self , request,CodigoProfesor=0):
        if(CodigoProfesor>0):
            profesores = list(TbProfesor.objects.filter(CodigoProfesor=CodigoProfesor).values()) 
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
        TbProfesor.objects.create(NombreProfesor=jd['NombreProfesor'],ApellidoProfesor=jd['ApellidoProfesor'],EmailProfesor=jd['EmailProfesor'],NumeroProfesor=jd['NumeroProfesor'],DireccionProfesor=jd['DireccionProfesor'])
        datos={
                'messaje': 'Success'
            }
        return JsonResponse(datos)
    
    def put(self,request,CodigoProfesor):
        jd=json.loads(request.body)
        profesores = list(TbProfesor.objects.filter(CodigoProfesor=CodigoProfesor).values()) 
        if len(profesores)>0:
            prof = TbProfesor.objects.get(CodigoProfesor=CodigoProfesor)
            prof.NombreProfesor=jd['NombreProfesor']
            prof.ApellidoProfesor=jd['ApellidoProfesor']
            prof.EmailProfesor=jd['EmailProfesor']
            prof.NumeroProfesor=jd['NumeroProfesor']
            prof.DireccionProfesor=jd['DireccionProfesor']
            prof.save()
            datos={'messaje': 'Success'}
        else:
            raise Http404("Profesores no encontrados")
        return JsonResponse(datos)