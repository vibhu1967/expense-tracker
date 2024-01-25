import logging
import json
import logging
import os
import pyodbc
import struct
import azure.functions as func
import datetime
from datetime import date


def main(msg: func.QueueMessage) -> None:

    logging.info('Python queue trigger function processed a queue item: %s',
                 msg.get_body().decode('utf-8'))

    d1 = 30

    # Uncomment below line when use username and password for authentication
    query = 'SELECT TOP (1000) * FROM [dbo].[expenses_expenses] '
    connection_string = "Driver={ODBC Driver 18 for SQL Server};Server=tcp:assessmentserverget.database.windows.net,1433;Database=vaibhavdb;Uid=dbadmin;Pwd=Admin123;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"

    # Uncomment below line when use username and password for authentication
    conn = pyodbc.connect(connection_string)

    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()

    for row in rows:
        current_time = date.today()
        print(current_time, row.date)
        if row.approval_status == "Pending" and abs(row.date-current_time).days > d1:
            cursor.execute(
                "update [dbo].[expenses_expenses] set approval_status where id=?", "Rejected", row.id)
            cursor.execute(
                "update [dbo].[expenses_expenses] set approved_by=? where id=?", "auto-rejected", row.id)
        if row.approval_status == "Pending" and row.amount <= 500 and abs(row.date-current_time).days < d1:
            cursor.execute(
                "update [dbo].[expenses_expenses] set approval_status=? where id=?", "Approved", row.id)
            cursor.execute(
                "update [dbo].[expenses_expenses] set approved_by=? where id=?", "auto-approved", row.id)

    cursor.commit()
