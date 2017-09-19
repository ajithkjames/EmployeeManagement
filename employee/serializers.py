from rest_framework import serializers
from account.models import User
from employee.models import Team, Project, Task


class BaseUserSerializer(serializers.ModelSerializer):
    skills = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name',
        many=True
     )

    class Meta:
        model = User
        fields = ('username','first_name','empid','age','teamlead','skills')


class ProjectSerializer(serializers.ModelSerializer):
    members = BaseUserSerializer(many=True,read_only=True)
    class Meta:
        model = Project
        fields = ('name','team','members')


class ProjectCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ('name','team','members')


class TeamSerializer(serializers.ModelSerializer):
    project_set = ProjectSerializer(many=True,read_only=True)
    members = BaseUserSerializer(many=True,read_only=True)
    class Meta:
        model = Team
        fields = ('name','lead','members','project_set')


class TeamCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = ('name','lead','members')


class TaskSerializer(serializers.ModelSerializer):
    assignee = BaseUserSerializer(read_only=True)
    project = ProjectSerializer(read_only=True)

    class Meta:
        model = Task
        fields = ('title','content','assignee','project')


class TaskCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('title','content','assignee','project')