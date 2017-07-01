from rest_framework.serializers import ModelSerializer
from .models import Experience, Skills, About, Education

class ExperiencesSerializer(ModelSerializer):

    class Meta:
        model = Experience
        fields = '__all__'

class AboutSerializer(ModelSerializer):

    class Meta:
        model = About
        fields = '__all__'

class SkilsSerializer(ModelSerializer):

    class Meta:
        model = Skills
        fields = '__all__'

class EducationSerializer(ModelSerializer):

    class Meta:
        model = Education
        fields = '__all__'

