from django.urls import path, include
from .models import TbCursos
from rest_framework import routers, serializers, viewsets
from APIProfesor.urls import ProfesorSerializer

from .models import TbEstado

class TbEstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbEstado
        fields = ('IdEstado', 'Estado')

# Serializers define the API representation.
class CursosSerializer(serializers.HyperlinkedModelSerializer):
    CodigoProfesor=ProfesorSerializer()
    FkEstado=TbEstadoSerializer()

    class Meta:
        model = TbCursos
        fields = ('CodigoCurso', 'NombreCurso', 'THCurso', 'PreRequisitoCurso', 'CicloCurso', 'CodigoProfesor','FkEstado')

# ViewSets define the view behavior.
class CursosViewSet(viewsets.ModelViewSet):
    queryset = TbCursos.objects.all()
    serializer_class = CursosSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register('TbCursos', CursosViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path('', include(router.urls)),
]