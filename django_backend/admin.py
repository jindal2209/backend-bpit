# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from django_backend.models import Placement_Team,Faculty,News,Event,Notice,TimeTable,LessonPlan,SelfLearning,StudentProjects,Acivementlist,StudentPublications,FacultyPublications,Branch,PhotoGallery,Disclosures,Marquee,BranchSubjects,StudentPlaced,Society,SocietyPics,Recruiters,LabResources,BranchSections,StudyMaterialMCQ, StudyMaterialAssignment,StudyMaterialQuestionPaper,StudyMaterialPresentation,Training,IndustrialToursAndWorkShops,ExpertTalksAndSeminar,NIRF
from django.contrib.auth.models import Permission

admin.site.register(Permission)
from rest_framework.authtoken.admin import TokenAdmin
TokenAdmin.raw_id_fields = ('user',)
   

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

UserAdmin.add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'first_name','last_name','email','password1', 'password2'),
        }),
    )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

@admin.register(Faculty)
class Facultyview(admin.ModelAdmin):
  list_display =('User','is_faculty_admin','designation',)
  list_filter =('branch','is_faculty_admin',)

@admin.register(LabResources)
class LabResourcesview(admin.ModelAdmin):
  pass

@admin.register(Branch)
class Branchview(admin.ModelAdmin):
  pass

@admin.register(PhotoGallery)
class PhotoGalaryview(admin.ModelAdmin):
   pass

@admin.register(Disclosures)
class Disclosuresview(admin.ModelAdmin):
   pass

@admin.register(Marquee)
class Marqueeview(admin.ModelAdmin):
   pass

# @admin.register(News)
# class Newsview(admin.ModelAdmin):
#    pass

@admin.register(Notice)
class Noticeview(admin.ModelAdmin):
  list_display = ('branch','examination_notice','display_to_home','date')
  list_filter = ('branch','examination_notice','display_to_home',)
  
@admin.register(TimeTable)
class Timetableviews(admin.ModelAdmin):
  list_display = ('branch',"branch_section","semester")
  list_filter = ('branch',"branch_section","semester")


@admin.register(LessonPlan)
class LessonPlanviews(admin.ModelAdmin):
  pass

@admin.register(SelfLearning)
class SelfLearningviews(admin.ModelAdmin):
  pass

@admin.register(StudentProjects)
class StudentProjectsviews(admin.ModelAdmin):
  pass

@admin.register(Acivementlist)
class Achievementlistview(admin.ModelAdmin):
  pass

@admin.register(StudentPublications)
class Studentpublicationview(admin.ModelAdmin):
  pass

@admin.register(StudyMaterialMCQ)
class studyMaterialview(admin.ModelAdmin):
  pass

@admin.register(StudyMaterialPresentation)
class studyMaterialview(admin.ModelAdmin):
  pass

@admin.register(StudyMaterialQuestionPaper)
class studyMaterialview(admin.ModelAdmin):
  pass

@admin.register(StudyMaterialAssignment)
class studyMaterialview(admin.ModelAdmin):
  pass

@admin.register(FacultyPublications)
class FacultyPublicationsview(admin.ModelAdmin):
  search_fields = ('User__first_name','User')
  list_display = ('User','branch',)
  list_filter = ('branch',)
  
@admin.register(News)
class NewsView(admin.ModelAdmin):
  list_display = ('branch','date')
  list_filter = ('branch','date')
  

@admin.register(Event)
class EventView(admin.ModelAdmin):
  list_display = ('branch','date')
  list_filter = ('branch','date')


# @admin.register(NBA)
# class NBAview(admin.ModelAdmin):
#   pass 

@admin.register(BranchSubjects)
class BranchSubjectsView(admin.ModelAdmin):
  list_display =('branch','subject_name',)
  list_filter = ('branch',)
 

@admin.register(BranchSections)
class NBAview(admin.ModelAdmin):
  pass 

@admin.register(StudentPlaced)
class StudentPlacedview(admin.ModelAdmin):
  pass 
@admin.register(Society)
class Societyview(admin.ModelAdmin):
  pass 
@admin.register(SocietyPics)
class SocietyPicsview(admin.ModelAdmin):
  pass 
@admin.register(Recruiters)
class Recruitersview(admin.ModelAdmin):
  search_fields = ('recruiter_name',)

# Society
admin.site.register(Training)

admin.site.register(IndustrialToursAndWorkShops)
admin.site.register(ExpertTalksAndSeminar)


@admin.register(Placement_Team)
class Placement_TeamView(admin.ModelAdmin):
  list_display =('User','is_placement_team_admin',)
  list_filter =('is_placement_team_admin',)

admin.site.register(NIRF)

