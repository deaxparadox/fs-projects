from rest_framework import serializers

class task_HeadingSerializer_single_task(serializers.Serializer):
    heading = serializers.CharField()
    start = serializers.DateField(required=False)
    end = serializers.DateField(required=False)
    created = serializers.DateTimeField()
    updated = serializers.DateTimeField()

class task_TaskSerializers_single_task(serializers.Serializer):
    heading = task_HeadingSerializer_single_task()

    task = serializers.CharField()
    start = serializers.DateField(required=False)
    end = serializers.DateField(required=False)
    created = serializers.DateTimeField()
    updated = serializers.DateTimeField()