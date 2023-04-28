from django.urls import path, include
from .models import TbDetalleCredito
from rest_framework import routers, serializers, viewsets
from APICursos.urls import CursosSerializer
from APICreditos.urls import CreditosSerializer

# Serializers define the API representation.
class DetalleCreditoSerializer(serializers.HyperlinkedModelSerializer):
    CodigoCredito=CreditosSerializer()
    CodigoCurso=CursosSerializer()
    class Meta:
        model = TbDetalleCredito
        fields = ('CodigoDetalleCredito', 'Cantidad', 'CodigoCredito', 'CodigoCurso')

# ViewSets define the view behavior.
class DetalleCreditoViewSet(viewsets.ModelViewSet):
    queryset = TbDetalleCredito.objects.all()
    serializer_class = DetalleCreditoSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register('TbDetalleCredito', DetalleCreditoViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path('', include(router.urls)),
]