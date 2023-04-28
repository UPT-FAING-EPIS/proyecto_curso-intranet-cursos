from django.urls import path, include
from .models import TbCreditos
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class CreditosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TbCreditos
        fields = '__all__'

# ViewSets define the view behavior.
class CreditosViewSet(viewsets.ModelViewSet):
    queryset = TbCreditos.objects.all()
    serializer_class = CreditosSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register('TbCreditos', CreditosViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path('', include(router.urls))
]