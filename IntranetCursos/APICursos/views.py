from django.shortcuts import render
from django.views import View
from .models import TbCursos
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import Http404

class APICursosViews(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, CodigoCurso=''):
        if CodigoCurso != '':
            cursos = list(TbCursos.objects.filter(CodigoCurso=CodigoCurso).values()) 
            if len(cursos):
                cursos = cursos[0]
                datos = {'Cursos': cursos}
            else:
                raise Http404("Cursos no encontrados")
            return JsonResponse(datos)
        else:
            cursos = list(TbCursos.objects.values())
            if len(cursos) > 0:
                datos = {'Cursos': cursos}
            else:
                raise Http404("Cursos no encontrados")
            return JsonResponse(datos)

    def post(self, request):
        jd=json.loads(request.body)
        TbCursos.objects.create(CodigoCurso=jd['CodigoCurso'],NombreCurso=jd['NombreCurso'],
                                THCurso=jd['THCurso'],PreRequisitoCurso=jd['PreRequisitoCurso'],
                                CicloCurso=jd['CicloCurso'],CodigoProfesor_id=jd['CodigoProfesor'],TbEstado_id=jd['TbEstado'])
        datos={
                'messaje': 'Success'
            }
        return JsonResponse(datos)
    
    def put(self,request,CodigoCurso):
        jd=json.loads(request.body)
        cursos = list(TbCursos.objects.filter(CodigoCurso=CodigoCurso).values()) 
        if len(cursos):
            curs = TbCursos.objects.get(CodigoCurso=CodigoCurso)
            curs.CodigoCurso=jd['CodigoCurso']
            curs.NombreCurso=jd['NombreCurso']
            curs.THCurso=jd['THCurso']
            curs.PreRequisitoCurso=jd['PreRequisitoCurso']
            curs.CicloCurso=jd['CicloCurso']
            curs.CodigoProfesor_id=jd['CodigoProfesor']
            curs.TbEstado_id=jd['TbEstado']
            curs.save()
            datos={'messaje': 'Success'}
        else:
            raise Http404("Profesores no encontrados")
        return JsonResponse(datos)