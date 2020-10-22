# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager

class Branch(models.Model):
    branch_name = models.CharField(max_length=10, unique=True, blank=True)

    def __str__(self):
        return self.branch_name

class BranchSubjects(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    subject_name = models.CharField(max_length=100, unique=True, blank=True) 

    class Meta:
        verbose_name_plural = "Branch Subjects"

class BranchSections(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    section = models.CharField(max_length=100, blank=True)

    class Meta:
        unique_together = [['branch', "section"]]
        verbose_name_plural = "Branch Sections"

    def __str__(self):
        return self.branch.branch_name + " - " + self.section

class PhotoGallery(models.Model):
    title = models.CharField(max_length=50)
    photo = models.ImageField(upload_to="Images/")

class Disclosures(models.Model):
    disclosure_title = models.CharField(max_length=500,default="")
    disclosures = models.FileField(upload_to="Diclosures/")
    date = models.DateField(null=False)

class Marquee(models.Model):
    marquee_text = models.TextField()
    
    def save(self):
        marquee=Marquee.objects.all()
        marquee.delete()
        super(Marquee,self).save()

class News(models.Model):
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE)
    title = models.CharField(max_length=350)
    news = models.FileField(upload_to="News/")
    date = models.DateField()

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-date']
        verbose_name_plural = 'News'



class Event(models.Model): 
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE)
    title = models.CharField(max_length=350)
    events = models.FileField(upload_to="Events/")
    date = models.DateField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date'] 

class Notice(models.Model):
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE)
    examination_notice = models.BooleanField(default=True)
    display_to_home = models.BooleanField(default=True)
    title = models.CharField(max_length=250)
    notices = models.FileField(upload_to="Notices/")
    date = models.DateField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date']


class TimeTable(models.Model):
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE)
    branch_section = models.ForeignKey(BranchSections,on_delete=models.CASCADE)
    semester = models.IntegerField(blank=True,null=False,default=1)
    time_table = models.FileField(upload_to="TimeTable/")

class LessonPlan(models.Model):
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE)
    subject = models.ForeignKey(BranchSubjects,on_delete=models.CASCADE)
    LecturePlan = models.FileField(upload_to="LessonPlans/")

class SelfLearning(models.Model):
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE)
    SLLecturePlan = models.CharField(max_length=200)

class StudentProjects(models.Model):
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE)
    Project_title = models.CharField(max_length=200)
    project_pic = models.ImageField(upload_to="ProjectsPic/")
    description = models.TextField(null=False)

class Acivementlist(models.Model): 
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE)
    acivement = models.CharField(max_length=2000)

class StudentPublications(models.Model):
    title = models.TextField(null=False)
    authors = models.TextField(null=False)  #change to True
    branch=models.ForeignKey(Branch,on_delete=models.CASCADE)
    venue = models.CharField(max_length=300,null=False)
    conference_name = models.CharField(max_length=200,null=False)
    year = models.IntegerField(null=False)

class StudyMaterialMCQ(models.Model):   
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE)
    subject = models.ForeignKey(BranchSubjects,on_delete=models.CASCADE)
    MCQ = models.FileField(upload_to="StudyMaterial/Mcq")

class StudyMaterialAssignment(models.Model):   
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE)
    subject = models.ForeignKey(BranchSubjects,on_delete=models.CASCADE)
    Assignment = models.FileField(upload_to="StudyMaterial/Assignment")


class StudyMaterialQuestionPaper(models.Model):   
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE)
    subject = models.ForeignKey(BranchSubjects,on_delete=models.CASCADE)
    QuestionPaper = models.FileField(upload_to="StudyMaterial/Quespaper")


class StudyMaterialPresentation(models.Model):   
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE)
    subject = models.ForeignKey(BranchSubjects,on_delete=models.CASCADE)
    presentation = models.FileField(upload_to="StudyMaterial/Presentation")

class FacultyPublications(models.Model):
    User = models.ForeignKey(User,on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE)
    paper_title = models.TextField()
    indexing = models.CharField(max_length=100)
    year = models.IntegerField()
    isbn_no = models.CharField(max_length=200,null=True,blank=True)
    volume = models.CharField(max_length=100,null=True,blank=True)
    journal = models.CharField(max_length=2000,null=True,blank=True)

   


# users
class Faculty(models.Model):
    User = models.OneToOneField(User,on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE)
    # order = models.IntegerField()
    profile_pic = models.ImageField(upload_to="Faculty/ProfilePics/")
    is_faculty_admin = models.BooleanField(default=True)
    designation = models.CharField(max_length=30) 
    Qualification = models.CharField(max_length=200)
    Experience = models.CharField(max_length=100)
    speacialization = models.CharField(max_length=200)
    nation_Publications = models.IntegerField(default=0)
    international_publication = models.IntegerField(default=0)
    date_of_joining = models.DateField(auto_now_add=True,blank=True) 
    faculty_publication_url = models.URLField(max_length=400,blank=True)
    
    class Meta:
        ordering = ['-date_of_joining']  

# placement stuff
class Placement_Team(models.Model):
    User = models.OneToOneField(User,on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to="PlacementFaculty/ProfilePics/")
    Phone_Number = models.IntegerField()
    designation = models.CharField(max_length=30)
    is_placement_team_admin = models.BooleanField(default=True)
    date_of_joining = models.DateField(auto_now_add=True,null=False) 

# class NBA(models.Model):   # remove it
#     NBA_title = models.CharField(max_length=500,default="")
#     NBA_file = models.FileField(upload_to="NBA/")




class SocietyPics(models.Model):
    society_pics = models.ImageField(upload_to="Society/Pics")

class Society(models.Model):
    society_name = models.CharField(max_length=100)
    description = models.TextField(max_length=3000)
    pics = models.ManyToManyField(SocietyPics)

class NIRF(models.Model):
    nirf_name = models.CharField(max_length=2000)
    date_of_upload = models.DateField()
    file = models.FileField(upload_to="NIRF")

class LabResources(models.Model):
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    pic = models.ImageField(upload_to="LabResources/")



class Recruiters(models.Model):
    recruiter_name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to="Recruiters/Logo/") 

    def __str__(self):
        return self.recruiter_name

class Training(models.Model):   # may raise error in future
    description = models.TextField()
    date_of_upload = models.DateField(null=False)
    company = models.CharField

class ExpertTalksAndSeminar(models.Model):
    date_of_upload = models.DateField()
    description = models.CharField(max_length=1000,blank=True)
    data = models.FileField(upload_to="ExpertTalksAndSeminar/")
    class Meta:
        ordering = ['-date_of_upload']


class IndustrialToursAndWorkShops(models.Model):
    description = models.TextField()
    date = models.DateField()
    company = models.CharField(max_length=300,blank=True,null=False)
    branch = models.CharField(max_length=300,blank=True,null=False)
    participants = models.IntegerField(default=0,null=False)

    class Meta:
        ordering = ["-date"]

class StudentPlaced(models.Model):
    date_of_upload = models.DateField()
    batch = models.CharField(max_length=20)
    data = models.FileField(upload_to="Students/Placedment/")
    branch = models.CharField(max_length=50,blank=True,null=False)
    class Meta:
        ordering = ['-date_of_upload']  