import datetime
import logging
import pyodbc
from datetime import date

import azure.functions as func


def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    if mytimer.past_due:
        logging.info('The timer is past due!')

    query = 'SELECT TOP (1000) * FROM [dbo].[expenses_expenses] '
    connection_string = "Driver={ODBC Driver 17 for SQL Server};Server=tcp:assessmentserverget.database.windows.net,1433;Database=vaibhavdb;Uid=dbadmin;Pwd=Admin123;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"

    # Uncomment below line when use username and password for authentication
    conn = pyodbc.connect(connection_string)

    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    d1 = 1

    for row in rows:
        current_date = date.today()
        if row.approval_status == "Pending" and abs(row.date-current_date).days > d1:
            cursor.execute(
                "update [dbo].[expenses_expenses] set approval_status=? where id=?", "Rejected", row.id)
            cursor.execute(
                "update [dbo].[expenses_expenses] set approved_by=? where id=?", "auto-rejected", row.id)
    cursor.commit()

    logging.info('Python timer trigger function ran at %s', utc_timestamp)