from rest_framework import serializers
from assignments.models import Assignment,Question,Answers
from courses.models import Course,Subject
# from forums.models import Form,Comments
from schools.models import School

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ()
        model = Course
        
class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ()
        model = Assignment
        
class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ()
        model = Subject       

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ()
        model = School    
        
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ()
        model = Question    