import azure.functions as func
from datetime import datetime
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient


def main(mytimer: func.TimerRequest) -> None:
    account_url = "https://assessmentstgacc.blob.core.windows.net/"
    default_credential = "eiyYAT6BkNDxxQ1KSFDEjkJ87GXUvAqO1By/bW1m0WTN0MWp5PSFrDYw0lAfHza17CCpUEYYTNhp+AStufDnyw=="
    today = datetime.utcnow()
    blob_service_client = BlobServiceClient(
        account_url, credential=default_credential)
    blob_container = blob_service_client.get_container_client(
        container="vaibhav-expense")
    blob_list = blob_container.list_blobs()
    for b in blob_list:
        last_modified = b.last_modified
        last_modified = last_modified.replace(tzinfo=None)
        difference = today-last_modified
        minutes = difference.total_seconds() / 60
        if minutes > 15:
            print("yes", minutes)
            print(b.blob_tier)
            blob = BlobClient(container_name="vaibhav-expense",
                              blob_name=b.name, account_url=account_url, credential=default_credential)
            blob.set_standard_blob_tier(standard_blob_tier="Archive")
            print(b.blob_tier)
        else:
            print("No", minutes)
        print(b.name)
