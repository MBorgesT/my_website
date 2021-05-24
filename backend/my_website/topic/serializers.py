from rest_framework import serializers, fields
from .models import Topic


class TopicSerializer(serializers.ModelSerializer):

	class Meta:
		model = Topic
		fields = '__all__'
