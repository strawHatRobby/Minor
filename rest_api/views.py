from rest_framework import generics
from assignments.models import Assignment,Question,Answers
from courses.models import Course,Subject
from forums.models import Form,Comments
from schools.models import School
from serializers import CourseSerializer,AssignmentSerializer,SubjectSerializer,SchoolSerializer,QuestionSerializer


class ListCreateCourse(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    
class RetrieveUpdateDestroyCourse(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    
class ListCreateAssignment(generics.ListCreateAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    
class RetrieveUpdateDestroyAssignment(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = AssignmentSerializer
    
class ListCreateSubject(generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    
class RetrieveUpdateDestroySubject(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    
class ListCreateSchool(generics.ListCreateAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    
class RetrieveUpdateDestroySchool(generics.RetrieveUpdateDestroyAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    
class ListCreateQuestion(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    
class RetrieveUpdateDestroyQuestion(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer