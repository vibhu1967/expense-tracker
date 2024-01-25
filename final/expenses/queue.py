from azure.storage.queue import QueueClient, BinaryBase64EncodePolicy, BinaryBase64DecodePolicy
from final.keyvault import *
from final.resources import *


def sendMessage(message):
    connection_str = gets_secerts(vault_url, "connstr")
    queue_name = "js-queue-items"
    stringMessage = str(message)
    queue_client = QueueClient.from_connection_string(
        connection_str, queue_name)
    queue_client.message_encode_policy = BinaryBase64EncodePolicy()
    queue_client.message_decode_policy = BinaryBase64DecodePolicy()
    message_bytes = stringMessage.encode('ascii')

    try:
        queue_client.create_queue()
        queue_client.send_message(
            queue_client.message_encode_policy.encode(content=message_bytes)
        )
    except:
        queue_client.send_message(
            queue_client.message_encode_policy.encode(content=message_bytes)
        )
