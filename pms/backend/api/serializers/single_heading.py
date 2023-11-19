from rest_framework import serializers

class heading_TaskSerializer_single_task(serializers.Serializer):
    task = serializers.CharField()
    start = serializers.DateField(required=False)
    end = serializers.DateField(required=False)
    created = serializers.DateTimeField()
    updated = serializers.DateTimeField()

class heading_HeadingSerializer_single_task(serializers.Serializer):
    tasks = heading_TaskSerializer_single_task(many=True)

    heading = serializers.CharField()
    start = serializers.DateField(required=False)
    end = serializers.DateField(required=False)
    created = serializers.DateTimeField()
    updated = serializers.DateTimeField()


