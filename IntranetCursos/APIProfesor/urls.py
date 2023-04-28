from django.urls import path, include
from .models import TbProfesor
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class ProfesorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TbProfesor
        fields = '__all__'

# ViewSets define the view behavior.
class ProfesorViewSet(viewsets.ModelViewSet):
    queryset = TbProfesor.objects.all()
    serializer_class = ProfesorSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register('TbProfesor', ProfesorViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path('', include(router.urls))
]