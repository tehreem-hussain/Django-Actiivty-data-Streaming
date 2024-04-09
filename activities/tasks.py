from azure.eventhub import EventHubProducerClient, EventData
from django.conf import settings  # To access your Azure credentials

def send_event_to_azure(summary_data):
    producer = EventHubProducerClient.from_connection_string(
        conn_str=settings.AZURE_EVENT_HUB_CONNECTION_STRING,
        eventhub_name=settings.AZURE_EVENT_HUB_NAME
    )
    event_data = EventData(body=summary_data)
    with producer:
        producer.send_batch([event_data])
