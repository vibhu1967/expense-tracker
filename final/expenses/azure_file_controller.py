
from io import BytesIO
from pathlib import Path
import uuid
from azure.storage.blob import BlobServiceClient

from final.settings import Connection_string, Container_name, Storage_account_key, Storage_account_name


storage_account_key = Storage_account_key
storage_account_name = Storage_account_name
connection_string = Connection_string
container_name = Container_name


def upload_file_to_blob(file):
    blob_service_client = BlobServiceClient.from_connection_string(
        connection_string)
    blob_client = blob_service_client.get_blob_client(
        container=container_name, blob=file)
    file_prefix = uuid.uuid4().hex
    ext = Path(file.name).suffix
    file_name = f"{file_prefix}{ext}"
    file_content = file.read()
    file_io = BytesIO(file_content)
    blob_client.upload_blob(data=file_io)
    file_object = file_name
    print("file uploaded to", file_object, file)

    return file_object
