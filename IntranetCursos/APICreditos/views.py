import pika
import json
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import TbCreditos
from .serializers import CreditosSerializer

class CreditosViewSet(viewsets.ModelViewSet):
    queryset = TbCreditos.objects.all()
    serializer_class = CreditosSerializer

    def perform_create(self, serializer):
        # Connect to RabbitMQ
        connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost", port=5672))
        channel = connection.channel()

        # Declare the queue
        channel.queue_declare(queue='creditos_queue')

        # Convert validated_data to a JSON string
        message_body = json.dumps(serializer.validated_data)

        # Publish the creditos data to the queue
        channel.basic_publish(exchange='', routing_key='creditos_queue', body=message_body)

        # Close the connection
        connection.close()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_database_save(serializer)  # Save data to the database
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def perform_database_save(self, serializer):
        serializer.save()  # Save the data to the database
