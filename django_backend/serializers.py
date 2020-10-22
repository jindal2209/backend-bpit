from rest_framework import serializers
from django.contrib.auth.models import User
from django_backend.models import Placement_Team,Faculty,News,Event,Notice,TimeTable,LessonPlan,SelfLearning,StudentProjects,Acivementlist,StudentPublications,FacultyPublications,Branch,PhotoGallery,Disclosures,Marquee,StudentPlaced,Society,SocietyPics,Recruiters,NIRF,Branch,LabResources,StudyMaterialMCQ,StudyMaterialAssignment,StudyMaterialQuestionPaper,StudyMaterialPresentation,BranchSections,BranchSubjects,Training,IndustrialToursAndWorkShops,ExpertTalksAndSeminar


class  UserSerializer(serializers.ModelSerializer):
  class Meta:
    model=User
    fields=("username","password","first_name","last_name","email","pk")

  def create(self, validated_data):
      user = super(UserSerializer, self).create(validated_data)
      user.set_password(validated_data['password'])
      user.save()
      return user

class BranchSerializer(serializers.ModelSerializer):
  class Meta:
     model=Branch
     fields=("branch_name",)

class  FacultySerializer(serializers.ModelSerializer):
  class Meta:
    model=Faculty
    fields=(
          "User",       
          "branch",
          "profile_pic",
          "is_faculty_admin",
          "designation",
          "Qualification",
          "Experience",
          "speacialization",
          "nation_Publications",
          "international_publication",
          "date_of_joining",
          "faculty_publication_url",

        )

class  PlacementFacultySerializer(serializers.ModelSerializer):
  class Meta:
    model=Placement_Team
    fields=(
          "User",       
          "branch",
          "profile_pic",
          "designation",
          "date_of_joining",
          "Phone_Number",
        )

class MarqueeSerializer(serializers.ModelSerializer):
  class Meta:
   model=Marquee
   fields=('marquee_text',)    

class LabResourcesSerializer(serializers.ModelSerializer):
  class Meta:
   model=LabResources
   fields="__all__"  


class DisclosureSerializer(serializers.ModelSerializer):
  class Meta:
   model=Disclosures
   fields="__all__"


class BranchSectionSerializer(serializers.ModelSerializer):
  class Meta:
   model=BranchSections
   fields="__all__"   

class BranchSubjectsSerializer(serializers.ModelSerializer):
  class Meta:
   model=BranchSubjects
   fields="__all__"   

class  GallerySerializer(serializers.ModelSerializer):
  class Meta:
    model=PhotoGallery
    fields="__all__"

#facultystuff
class  NewsSerializer(serializers.ModelSerializer):
  class Meta:
    model=News
    fields="__all__"



class  EventSerializer(serializers.ModelSerializer):
  class Meta:
    model=Event
    fields="__all__"


class TimeTableSerializer(serializers.ModelSerializer):
  class Meta:
   model=TimeTable
   fields="__all__"



class  NoticeSerializer(serializers.ModelSerializer):
  class Meta:
    model=Notice
    # fields = ('branch','examination_notice','display_to_home','title','date')
    fields="__all__"


class  LessonPlanSerializer(serializers.ModelSerializer):
  class Meta:
    model=LessonPlan
    fields="__all__"
    

class  SelfLearningSerializer(serializers.ModelSerializer):
  class Meta:
    model=SelfLearning
    fields="__all__"
    

class  AcivementlistSerializer(serializers.ModelSerializer):
  class Meta:
    model=Acivementlist
    fields="__all__"
       

    
class  StudentPublicationsSerializer(serializers.ModelSerializer):
  class Meta:
    model=StudentPublications
    fields="__all__"
    


class  StudyMaterialMCQSerializer(serializers.ModelSerializer):
  class Meta:
    model=StudyMaterialMCQ
    fields="__all__"

class  StudyMaterialPresentationSerializer(serializers.ModelSerializer):
  class Meta:
    model=StudyMaterialPresentation
    fields="__all__"  

class  StudyMaterialQuestionPaperSerializer(serializers.ModelSerializer):
  class Meta:
    model=StudyMaterialQuestionPaper
    fields="__all__"


class  StudyMaterialAssignmentSerializer(serializers.ModelSerializer):
  class Meta:
    model=StudyMaterialAssignment
    fields="__all__"



class FacultyPublicationsSerializer(serializers.ModelSerializer):
  class Meta:
   model=FacultyPublications
   fields="__all__" 
   


class StudentProjectsSerializer(serializers.ModelSerializer):
  class Meta:
   model=StudentProjects
   fields="__all__"
      

# class NBASerializer(serializers.ModelSerializer):
#   class Meta:
#     model=NBA
#     fields="__all__"


class StudentPlacedSerializer(serializers.ModelSerializer):
  class Meta:
    model=StudentPlaced
    fields="__all__"

class  SocietySerializer(serializers.ModelSerializer):
  class Meta:
    model=Society
    fields="__all__"
    


class RecruitersSerializer(serializers.ModelSerializer):
  class Meta:
   model=Recruiters
   fields="__all__"   

class SocietyPicsSerializer(serializers.ModelSerializer):
  class Meta:
   model=SocietyPics
   fields="__all__" 

class NIRFSerializer(serializers.ModelSerializer):
  class Meta:
   model=NIRF
   fields="__all__"

class TrainingSerializer(serializers.ModelSerializer):
  class Meta:
    model = Training
    fields = "__all__"

class IndustrialToursAndWorkShopsSerializer(serializers.ModelSerializer):
  class Meta:
    model = IndustrialToursAndWorkShops
    fields = '__all__'

class ExpertTalksAndSeminarSerializer(serializers.ModelSerializer):
  class Meta:
    model = ExpertTalksAndSeminar
    fields = '__all__'