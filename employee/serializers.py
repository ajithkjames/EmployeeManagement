from rest_framework import serializers
from employee.models import Team, Project, Task


class TaskSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Task
        fields = ('title','content','assigner','assignee','project')
        read_only_fields = ('assigner',)

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('name','team','members')


class TeamSerializer(serializers.ModelSerializer):
    project_set = ProjectSerializer(many=True,read_only=True)

    class Meta:
        model = Team
        fields = ('name','lead','members','project_set')

