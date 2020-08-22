from rest_framework import serializers
from .models import Project, Pledge
#No text field in rest framework for serializer

class ProjectSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField(max_length=400)
    description = serializers.CharField(max_length=400)
    goal = serializers.IntegerField()
    image = serializers.URLField()
    is_open = serializers.BooleanField()
    date_created = serializers.DateTimeField()
    owner = serializers.ReadOnlyField(source='owner.username')
    def create(self, validated_data):
        return(Project.objects.create(**validated_data))


class PledgeSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    amount = serializers.IntegerField()
    comment = serializers.CharField(max_length=400)
    anonymous = serializers.BooleanField()
    supporter = serializers.CharField(max_length=400)
    project_id = serializers.IntegerField()

    def create(self,validated_data):
        return Pledge.objects.create(**validated_data)


class ProjectDetailSerializer(ProjectSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)




