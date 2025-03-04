from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'  # modeldagi barcha malumotlarni olib Json korinishda taqdim qiladi
        