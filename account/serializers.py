from rest_framework import serializers
from account.models import User,Skill
from employee.serializers import TeamSerializer,ProjectSerializer


class SkillSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Skill
        fields = ('name',)


class UserSerializer(serializers.ModelSerializer):

    skills = SkillSerializer(many=True)
    team_set = TeamSerializer(many=True ,read_only=True)
    project_set = ProjectSerializer(many=True,read_only=True)

    class Meta:
        model = User
        fields = ('username','password','first_name','empid','age','teamlead','skills','team_set','project_set')
        extra_kwargs = {
            'password': {'write_only': True, 'required':False}
        }

    def create(self, validated_data):
        skills_data = validated_data.pop('skills')
        print skills_data, "####"
        user = User.objects.create_user(**validated_data)
        for skill_data in skills_data:
            print skill_data
            skill = Skill.objects.create(**skill_data)
            user.skills.add(skill)
        return user

    def update(self, instance, validated_data):
        if validated_data.get('password'):
            instance.set_password(validated_data.get('password'))
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.age = validated_data.get('age', instance.age)
        instance.teamlead = validated_data.get('teamlead', instance.teamlead)
        skills_data = validated_data.pop('skills')
        instance.skills.clear()
        for skill_data in skills_data:
            skill = Skill.objects.create(**skill_data)
            instance.skills.add(skill)
        instance.save()
        return instance