from rest_framework import serializers

from app.models.headings import Heading
from app.models.tasks import Task

# 
# Model Serializers
# 
class HeadingModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Heading
        fields = ["heading", "created", "updated", "start", "end"]



class TaskModelSerializers(serializers.ModelSerializer):
    heading = HeadingModelSerializers()
    class Meta:
        model = Task
        fields = "__all__"

# 
# Relational Model  Serializers
# 
class TaskModel_Serializers_2(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['task', 'start', 'end', 'created', 'updated']

class HeadingModelSerializers_2(serializers.ModelSerializer):
    tasks = TaskModel_Serializers_2(many=True)
    class Meta:
        model = Heading
        fields = ["id", "heading", "start", "end", "created", "updated","tasks"]


