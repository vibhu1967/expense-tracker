
from rest_framework import serializers
from .models import Expenses


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expenses
        fields = "__all__"

        def create(self, validated_data):
            return Expenses.objects.create(**validated_data)

        def update(self, instance, validated_data):
            Expenses.objects.filter(id=instance.id).update(**validated_data)
            return Expenses.objects.get(id=instance.id)
