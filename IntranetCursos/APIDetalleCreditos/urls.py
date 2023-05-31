from django.urls import path, include
from .models import TbDetalleCredito
from rest_framework import routers, serializers, viewsets,status
from rest_framework.response import Response
from APICursos.urls import CursosSerializer
from APICreditos.urls import CreditosSerializer
import datetime
import json
import pika 



# Serializers define the API representation.
class DetalleCreditoSerializer(serializers.HyperlinkedModelSerializer):
    CodigoCredito=CreditosSerializer()
    CodigoCurso=CursosSerializer()
    class Meta:
        model = TbDetalleCredito
        fields = ('CodigoDetalleCredito', 'Cantidad', 'CodigoCredito', 'CodigoCurso')

# ViewSets define the view behavior.
def RabitmqSend(rooting_key,message_body):
    
    log={
        "timestamp": datetime.datetime.now().isoformat(),
        "Level": rooting_key,
        "Message": json.dumps(message_body)
    }

    connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost", port=5672))
    channel = connection.channel()

    channel.queue_declare(queue="logs")
    channel.basic_publish(exchange='', routing_key="logs", body=json.dumps(log))
    
    connection.close()

class DetalleCreditoViewSet(viewsets.ModelViewSet):
    queryset = TbDetalleCredito.objects.all()
    serializer_class = DetalleCreditoSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        
        serializer.is_valid(raise_exception=True)
        self.perform_database_save(serializer) 

        RabitmqSend('creditos_queue_Post',serializer.validated_data)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_database_save(serializer)

        RabitmqSend('creditos_queue_Put', serializer.validated_data)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK, headers=headers)
    
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        RabitmqSend('creditos_queue_Get', serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        RabitmqSend('creditos_queue_Get_1', serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def perform_database_save(self, serializer):
        serializer.save() 

    

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register('TbDetalleCredito', DetalleCreditoViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path('', include(router.urls)),
]