
from pathlib import Path
from django.http import JsonResponse
from rest_framework.views import APIView, Response
from expenses.azure_file_controller import upload_file_to_blob

from expenses.models import Expenses
from expenses.queue import sendMessage
from expenses.serializers import ExpenseSerializer


class Expense(APIView):

    def post(self, request):
        data = request.data
        serializer = ExpenseSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        file = request.FILES['image']
        ext = Path(file.name).suffix
        new_file = upload_file_to_blob(file)
        data['image'].name = new_file
        serializer.save()
        Expenses(category=request.data.get('category'), date=request.data.get('date'), amount=request.data.get(
            'amount'), comments=request.data.get('comments'), image=request.data.get('image'), approval_status='Pending').save()

        latest_obj_id = str(Expenses.objects.latest('id').id)
        sendMessage(latest_obj_id)
        return JsonResponse(serializer.data)

    def get(self, request, id=None):
        if id:
            item = Expenses.objects.get(id=id)
            serializer = ExpenseSerializer(item)
            return Response(serializer.data)

        items = Expenses.objects.all()
        serializer = ExpenseSerializer(items, many=True)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        model_id = kwargs.get("id", None)
        if not model_id:
            return JsonResponse({"error": "method /PUT/ not allowed"})
        try:
            instance = Expenses.objects.get(id=model_id)
        except:
            return JsonResponse({"error": "Object does not exist"})

        serializer = ExpenseSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse(serializer.data)


class Approved(APIView):
    def get(self, request):
        items = Expenses.objects.filter(approval_status="Approved")
        serializer = ExpenseSerializer(items, many=True)
        return Response(serializer.data)


class Pending(APIView):
    def get(self, request):
        items = Expenses.objects.filter(approval_status="Pending")
        serializer = ExpenseSerializer(items, many=True)
        return Response(serializer.data)


class Rejected(APIView):
    def get(self, request):
        items = Expenses.objects.filter(approval_status="Rejected")
        serializer = ExpenseSerializer(items, many=True)
        return Response(serializer.data)
