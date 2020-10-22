from __future__ import unicode_literals
from django.shortcuts import render
# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.http import HttpResponse,Http404,JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.views import APIView
from django_backend.models import Placement_Team,Faculty,News,Event,Notice,TimeTable,LessonPlan,SelfLearning,StudentProjects,Acivementlist,StudentPublications,FacultyPublications,Branch,BranchSubjects,BranchSections,StudyMaterialMCQ,StudyMaterialAssignment,StudyMaterialQuestionPaper,StudyMaterialPresentation,LabResources,BranchSections,BranchSubjects
from django_backend.serializers import UserSerializer,FacultySerializer,MarqueeSerializer,DisclosureSerializer,GallerySerializer,NewsSerializer,EventSerializer,TimeTableSerializer,NoticeSerializer,LessonPlanSerializer,SelfLearningSerializer,AcivementlistSerializer,StudentPublicationsSerializer,FacultyPublicationsSerializer,StudentProjectsSerializer,StudyMaterialMCQSerializer,StudyMaterialPresentationSerializer,StudyMaterialQuestionPaperSerializer,StudyMaterialAssignmentSerializer,LabResourcesSerializer,BranchSectionSerializer,BranchSubjectsSerializer
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAdminUser,IsAuthenticated
from django_backend.CollegeAppPermission import IsFacultyAdmin
from rest_framework.authtoken.views import ObtainAuthToken



class CustomObtainAuthToken(ObtainAuthToken):
  def post(self, request, *args, **kwargs):
    serializer = self.serializer_class(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    token, created = Token.objects.get_or_create(user=user)
    return Response({'token': token.key,
                      'user_id':user.pk,
                      'username':user.username,
                      'firstname':user.first_name,
                      'lastname':user.last_name,
                      'branch':user.faculty.branch.pk,
                      'is_faculty_admin':user.faculty.is_faculty_admin})

obtain_auth_token = CustomObtainAuthToken.as_view()


class PlacementObtainAuthToken(ObtainAuthToken):
  def post(self,request,*args,**kwargs):
    serializer = self.serializer_class(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    token, created = Token.objects.get_or_create(user=user)
    return Response({'token': token.key,
                      'user_id':user.pk,
                      'username':user.username,
                      'firstname':user.first_name,
                      'lastname':user.last_name,
                      'branch':user.placement_team.branch.pk,
                      'is_placement_team_admin':user.placement_team.is_placement_team_admin})

obtain_placement_auth_token = PlacementObtainAuthToken.as_view()

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

def get_faculty(request,branch):
  branch=branch.upper()
  branchobj=Branch.objects.get(branch_name=branch)
  faculty=Faculty.objects.filter(branch=branchobj)
  main_list=[]
  update_dict={}
  for a in faculty:
        update_dict={
        "username":a.User.username,
        "firstname":a.User.first_name,
        "lastname":a.User.last_name,
        "email":a.User.email,
        "branch":a.branch.branch_name,
        "profile_pic":a.profile_pic.url,
        "designation":a.designation,
        "Qualification":a.Qualification,
        "Experience":a.Experience,
        "speacialization":a.speacialization,
        "nation_Publications":a.nation_Publications,
        "international_publication":a.international_publication,
        "publication_url":a.faculty_publication_url,
        # "order":a.order,
        }
        main_list.append(update_dict)
  return  JsonResponse(main_list,safe=False)   

def get_team(request):
  team=Placement_Team.objects.all()
  main_list=[]
  update_dict={}
  for a in team:
        update_dict={
        "username":a.User.username,
        "firstname":a.User.first_name,
        "lastname":a.User.last_name,
        "email":a.User.email,
        "profile_pic":a.profile_pic.url,
        "designation":a.designation,
        "Phone_Number":a.Phone_Number,
        # "order":a.order,
        }
        main_list.append(update_dict)
  return  JsonResponse(main_list,safe=False)  
    


def get_section(request,branchid,sectionid):
  try:
    print("b")
    branch=Branch.objects.get(pk=branchid)
    print("b1")
    section_obj=BranchSections.objects.get(branch=branch,pk=sectionid)
    return HttpResponse(section_obj.section) 
  except:
     print("exce")
     raise Http404

def get_subject(request,branchid,subjectid):
  try:
    branch=Branch.objects.get(pk=branchid)
    subject_obj=BranchSubjects.objects.filter(branch=branch,pk=subjectid).get() 
  except:
     raise Http404
  return    HttpResponse(subject_obj.subject_name) 

def get_branch(request,pk):
  try:
      branch=Branch.objects.get(pk=pk)
  except:
      raise Http404
  return HttpResponse(branch.branch_name)  



@api_view(['POST'])
@permission_classes((IsAuthenticated,IsFacultyAdmin,))
def create_user(request):
  # if request.method == 'GET':
  #   user = User
  #   serialized = UserSerializer()
  #   return Response(serialized.data)
  
  if request.method == 'POST':
    serialized = UserSerializer(data=request.data)
    if serialized.is_valid():
        serialized.save()
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes((IsAuthenticated,IsFacultyAdmin,))
def create_placement(request):
  if request.method == 'POST':
    serialized = UserSerializer(data=request.data)
    if serialized.is_valid():
        serialized.save()
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)


class NoticeBranchListView(generics.ListAPIView):
  serializer_class=NoticeSerializer
  def get_queryset(self):
       branch=self.kwargs['branch'].upper()
       return Notice.objects.filter(branch__branch_name=branch)  

class NewsBranchListView(generics.ListAPIView):
  serializer_class=NewsSerializer
  def get_queryset(self):
       branch=self.kwargs['branch'].upper()
       return News.objects.filter(branch__branch_name=branch) 

class EventBranchListView(generics.ListAPIView):
  serializer_class=EventSerializer
  def get_queryset(self):
       branch=self.kwargs['branch'].upper()
       return Event.objects.filter(branch__branch_name=branch) 

class TimeTableBranchListView(generics.ListAPIView):
  permission_classes = (IsAuthenticatedOrReadOnly,)
  serializer_class=TimeTableSerializer
  def get_queryset(self):
       branch=self.kwargs['branch'].upper()
       return TimeTable.objects.filter(branch__branch_name=branch) 

@api_view(['GET'])
def get_timetable(request,branch):
  branch = branch.upper()
  list_obj = TimeTable.objects.filter(branch__branch_name=branch)
  main_list = []
  for i in list_obj:
    d = {}
    d["branch"] = i.branch.branch_name
    d["branch_section"] = i.branch_section.section
    d["semester"] = i.semester
    d["time_table"] = i.time_table.url   #"http://127.0.0.1:8000"+i.time_table.url    #locally
    main_list.append(d)
  return JsonResponse(main_list,safe=False)

class SectionListView(generics.ListAPIView):
  serializer_class=BranchSectionSerializer
  def get_queryset(self):
       branch=self.kwargs['branch'].upper()
       return BranchSections.objects.filter(branch__branch_name=branch) 

class SubjectsListView(generics.ListAPIView):
  serializer_class=BranchSubjectsSerializer
  def get_queryset(self):
       branch=self.kwargs['branch'].upper()
       return BranchSubjects.objects.filter(branch__branch_name=branch) 

class LessonPlanBranchListView(generics.ListAPIView):
  serializer_class=LessonPlanSerializer
  def get_queryset(self):
       branch=self.kwargs['branch'].upper()
       return LessonPlan.objects.filter(branch__branch_name=branch) 

class SelfLearningBranchListView(generics.ListAPIView):
  serializer_class=SelfLearningSerializer
  def get_queryset(self):
       branch=self.kwargs['branch'].upper()
       return SelfLearning.objects.filter(branch__branch_name=branch) 

class AcivementlistBranchListView(generics.ListAPIView):
  serializer_class=AcivementlistSerializer
  def get_queryset(self):
       branch=self.kwargs['branch'].upper()
       return Acivementlist.objects.filter(branch__branch_name=branch)
       

class StudentProjectsBranchView(generics.ListAPIView):
  serializer_class=StudentProjectsSerializer
  def get_queryset(self):
       branch=self.kwargs['branch'].upper()
       return StudentProjects.objects.filter(branch__branch_name=branch) 

class StudentPublicationsBranchListView(generics.ListAPIView):
  serializer_class=StudentPublicationsSerializer
  def get_queryset(self):
       branch=self.kwargs['branch'].upper()
       return StudentPublications.objects.filter(branch__branch_name=branch) 

    
class FacultyPublicationsBranchListView(generics.ListAPIView):
  serializer_class=FacultyPublicationsSerializer
  def get_queryset(self):
       branch=self.kwargs['branch'].upper()
       return FacultyPublications.objects.filter(branch__branch_name=branch)

def get_name(request,branch):
  branch=branch.upper()
  list_obj = FacultyPublications.objects.filter(branch__branch_name=branch)
  main_list = []
  for i in list_obj:
    d = {}
    d["paper_title"] = i.paper_title
    d["indexing"] = i.indexing
    d["year"] = i.year
    d["isbn_no"] = i.isbn_no
    d["volume"] = i.volume
    d["journal"] = i.journal
    d["name"] = i.User.first_name + " " + i.User.last_name
    main_list.append(d)
  return JsonResponse(main_list,safe=False)



class StudyMaterialQuestionPaperBranchListView(generics.ListAPIView):
  serializer_class=StudyMaterialQuestionPaperSerializer
  def get_queryset(self):
       branch=self.kwargs['branch'].upper()
       return StudyMaterialQuestionPaper.objects.filter(branch__branch_name=branch)

class StudyMaterialAssignmentBranchListView(generics.ListAPIView):
  serializer_class=StudyMaterialAssignmentSerializer
  def get_queryset(self):
       branch=self.kwargs['branch'].upper()
       return StudyMaterialAssignment.objects.filter(branch__branch_name=branch)

class StudyMaterialMCQBranchListView(generics.ListAPIView):
  serializer_class=StudyMaterialMCQSerializer
  def get_queryset(self):
       branch=self.kwargs['branch'].upper()
       return StudyMaterialMCQ.objects.filter(branch__branch_name=branch)
             
class FacultyBranchListView(generics.ListAPIView):
  serializer_class=FacultySerializer
  def get_queryset(self):
       branch=self.kwargs['branch'].upper()
       return Faculty.objects.filter(branch__branch_name=branch)      

class NoticeForExamination(generics.ListAPIView):
  serializer_class=NoticeSerializer
  def get_queryset(self):
       return Notice.objects.filter(examination_notice=True)


class StudyMaterialPresentationBranchListView(generics.ListAPIView):
  serializer_class=StudyMaterialPresentationSerializer
  def get_queryset(self):
       branch=self.kwargs['branch'].upper()
       return StudyMaterialPresentation.objects.filter(branch__branch_name=branch)



class LabResourcesBranchListView(generics.ListAPIView):
  serializer_class=LabResourcesSerializer
  def get_queryset(self):
       branch=self.kwargs['branch'].upper()
       return LabResources.objects.filter(branch__branch_name=branch)


