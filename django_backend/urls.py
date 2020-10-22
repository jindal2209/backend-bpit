# from django.conf.urls import url,include
from django_backend.views import get_timetable,get_name,get_team,obtain_placement_auth_token,LabResourcesBranchListView,NoticeBranchListView,NewsBranchListView,EventBranchListView,TimeTableBranchListView,LessonPlanBranchListView,SelfLearningBranchListView,AcivementlistBranchListView,StudentProjectsBranchView,StudentPublicationsBranchListView,FacultyPublicationsBranchListView,FacultyBranchListView,create_user,NoticeForExamination,obtain_auth_token,get_branch,get_section,get_subject, StudyMaterialPresentationBranchListView,StudyMaterialQuestionPaperBranchListView,StudyMaterialAssignmentBranchListView,StudyMaterialMCQBranchListView,get_faculty,SectionListView,SubjectsListView,create_placement

from rest_framework import generics
from django_backend.serializers import PlacementFacultySerializer,IndustrialToursAndWorkShopsSerializer,TrainingSerializer ,UserSerializer,FacultySerializer,MarqueeSerializer ,DisclosureSerializer,GallerySerializer,NewsSerializer,EventSerializer,TimeTableSerializer, NoticeSerializer,LessonPlanSerializer, SelfLearningSerializer, AcivementlistSerializer,StudentPublicationsSerializer,FacultyPublicationsSerializer,StudentProjectsSerializer,StudentPlacedSerializer,SocietySerializer,RecruitersSerializer,NIRFSerializer,BranchSerializer,LabResourcesSerializer, StudyMaterialMCQSerializer,StudyMaterialPresentationSerializer,StudyMaterialQuestionPaperSerializer,StudyMaterialAssignmentSerializer,ExpertTalksAndSeminarSerializer

from django_backend.models import Placement_Team,IndustrialToursAndWorkShops,Faculty,News,Event,Notice,TimeTable,LessonPlan,SelfLearning,StudentProjects,Acivementlist,StudentPublications,FacultyPublications,Branch,PhotoGallery,Disclosures,Marquee,StudentPlaced,Society,SocietyPics,Recruiters,NIRF,LabResources,StudyMaterialMCQ, StudyMaterialAssignment,StudyMaterialQuestionPaper,StudyMaterialPresentation,Training,ExpertTalksAndSeminar
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAdminUser,IsAuthenticated
from django_backend.CollegeAppPermission import IsFacultyAdmin
from rest_framework.parsers import MultiPartParser, FormParser,JSONParser
from django.contrib.auth.models import User
from django.views.generic import RedirectView
from django.contrib import admin
from django.urls import path,include,re_path
from django.conf import settings
from django.conf.urls.static import static

     

idtobranchurls=[
    re_path(r'(?P<pk>[0-9]+)$', get_branch),
]

idtosectionsurls=[
    re_path(r'(?P<branch>[A-Za-z]+)$',SectionListView.as_view()),
    re_path(r'(?P<branchid>[0-9]+)/(?P<sectionid>[0-9]+)$', get_section)
]

idtosubjectsurls=[
    re_path(r'(?P<branch>[A-Za-z]+)$',SubjectsListView.as_view()),
    re_path(r'(?P<branchid>[0-9]+)/(?P<subjectid>[0-9]+)$', get_subject)
]

galleryurls=[  
    re_path(r'$',generics.ListAPIView.as_view(queryset=PhotoGallery.objects.all(),serializer_class=GallerySerializer)),
]

societyurls=[
    re_path(r'$',generics.ListAPIView.as_view(queryset=Society.objects.all(),serializer_class=SocietySerializer)),
]

studentplacedurls=[
    re_path(r'$',generics.ListAPIView.as_view(queryset=StudentPlaced.objects.all(),serializer_class=StudentPlacedSerializer)),
]

disclosureurls=[
    re_path(r'$',generics.ListAPIView.as_view(queryset=Disclosures.objects.all(),serializer_class=DisclosureSerializer))
]

marqueeurls=[
    re_path(r'$',generics.ListAPIView.as_view(queryset=Marquee.objects.all(),serializer_class=MarqueeSerializer))
]

facultyurls=[
    re_path(r'create$',generics.ListCreateAPIView.as_view(queryset=Faculty.objects.all(),serializer_class=FacultySerializer,permission_classes=(IsAuthenticated,IsFacultyAdmin,))),
    re_path(r'placement_create$',generics.ListCreateAPIView.as_view(queryset=Placement_Team.objects.all(),serializer_class=PlacementFacultySerializer,permission_classes=(IsAuthenticated,IsFacultyAdmin,))),
]

# nbaurls=[
#     re_path(r'$',generics.ListAPIView.as_view(queryset=NBA.objects.all(),serializer_class=NBASerializer)),
# ]

nirfurls=[
    re_path(r'$',generics.ListAPIView.as_view(queryset=NIRF.objects.all(),serializer_class=NIRFSerializer)),
]

labresurls=[  
    re_path(r'(?P<pk>[0-9]+)$',generics.RetrieveUpdateDestroyAPIView.as_view(queryset=LabResources.objects.all(),serializer_class=LabResourcesSerializer,permission_classes=(IsAuthenticatedOrReadOnly,IsFacultyAdmin,),parser_classes = (MultiPartParser, FormParser,JSONParser))),
    re_path(r'$',generics.ListCreateAPIView.as_view(queryset=LabResources.objects.all(),serializer_class=LabResourcesSerializer,permission_classes=(IsAuthenticatedOrReadOnly,IsFacultyAdmin,),parser_classes = (MultiPartParser, FormParser,JSONParser))) ,
]

noticeurls=[
    re_path(r'examination$',NoticeForExamination.as_view()),
    re_path(r'(?P<pk>[0-9]+)$',generics.RetrieveUpdateDestroyAPIView.as_view(queryset=Notice.objects.all(),serializer_class=NoticeSerializer,permission_classes=(IsAuthenticatedOrReadOnly,IsFacultyAdmin,),parser_classes = (MultiPartParser, FormParser,JSONParser))),
    re_path(r'$',generics.ListCreateAPIView.as_view(queryset=Notice.objects.all(),serializer_class=NoticeSerializer,permission_classes=(IsAuthenticatedOrReadOnly,IsFacultyAdmin,),parser_classes = (MultiPartParser, FormParser,JSONParser))) ,
]

newsurls=[
    re_path(r'(?P<pk>[0-9]+)$',generics.RetrieveUpdateDestroyAPIView.as_view(queryset=News.objects.all(),serializer_class=NewsSerializer,permission_classes=(IsAuthenticatedOrReadOnly,IsFacultyAdmin,),parser_classes = (MultiPartParser, FormParser,JSONParser))),
    re_path(r'$',generics.ListCreateAPIView.as_view(queryset=News.objects.all(),serializer_class=NewsSerializer,permission_classes=(IsAuthenticatedOrReadOnly,IsFacultyAdmin,),parser_classes = (MultiPartParser, FormParser,JSONParser))) ,
]

eventsurls=[
    re_path(r'(?P<pk>[0-9]+)$',generics.RetrieveUpdateDestroyAPIView.as_view(queryset=Event.objects.all(),serializer_class=EventSerializer,permission_classes=(IsAuthenticatedOrReadOnly,IsFacultyAdmin,),parser_classes = (MultiPartParser, FormParser,JSONParser))),
    re_path(r'$',generics.ListCreateAPIView.as_view(queryset=Event.objects.all(),serializer_class=EventSerializer,permission_classes=(IsAuthenticatedOrReadOnly,IsFacultyAdmin,),parser_classes = (MultiPartParser, FormParser,JSONParser))) ,
]

studentprojecturls=[
    re_path(r'(?P<pk>[0-9]+)$',generics.RetrieveUpdateDestroyAPIView.as_view(queryset=StudentProjects.objects.all(),serializer_class=StudentProjectsSerializer,permission_classes=(IsAuthenticatedOrReadOnly,IsFacultyAdmin,),parser_classes =(MultiPartParser, FormParser,JSONParser))),
    re_path(r'$',generics.ListCreateAPIView.as_view(queryset=StudentProjects.objects.all(),serializer_class=StudentProjectsSerializer,permission_classes=(IsAuthenticatedOrReadOnly,IsFacultyAdmin,),parser_classes = (MultiPartParser, FormParser,JSONParser))) ,
]

timetableurls=[
    re_path(r'(?P<pk>[0-9]+)$',generics.RetrieveUpdateDestroyAPIView.as_view(queryset=TimeTable.objects.all(),serializer_class=TimeTableSerializer,permission_classes=(IsAuthenticatedOrReadOnly,IsFacultyAdmin,),parser_classes = (MultiPartParser, FormParser,JSONParser))),
    re_path(r'$',generics.CreateAPIView.as_view(queryset=TimeTable.objects.all(),serializer_class=TimeTableSerializer,permission_classes=(IsAuthenticated,IsFacultyAdmin,),parser_classes = (MultiPartParser, FormParser,JSONParser))),
]

lessonplaneurls=[
    re_path(r'(?P<pk>[0-9]+)$',generics.RetrieveUpdateDestroyAPIView.as_view(queryset=LessonPlan.objects.all(),serializer_class=LessonPlanSerializer,permission_classes=(IsAuthenticatedOrReadOnly,IsFacultyAdmin,),parser_classes = (MultiPartParser, FormParser,JSONParser))),
    re_path(r'$',generics.CreateAPIView.as_view(queryset=LessonPlan.objects.all(),serializer_class=LessonPlanSerializer,permission_classes=(IsAuthenticated,IsFacultyAdmin,),parser_classes = (MultiPartParser, FormParser,JSONParser))) ,
]

selflearningurls=[
    re_path(r'(?P<pk>[0-9]+)$',generics.RetrieveUpdateDestroyAPIView.as_view(queryset=SelfLearning.objects.all(),serializer_class=SelfLearningSerializer,permission_classes=(IsAuthenticatedOrReadOnly,IsFacultyAdmin,),parser_classes = (MultiPartParser, FormParser,JSONParser))),
    re_path(r'$',generics.CreateAPIView.as_view(queryset=SelfLearning.objects.all(),serializer_class=SelfLearningSerializer,permission_classes=(IsAuthenticated,IsFacultyAdmin,),parser_classes = (MultiPartParser, FormParser,JSONParser))) ,
]

achievementlisturls=[
    re_path(r'$',generics.ListAPIView.as_view(queryset=Acivementlist.objects.all(),serializer_class=AcivementlistSerializer)),
]

studentpuburls=[
    re_path(r'(?P<pk>[0-9]+)$',generics.RetrieveUpdateDestroyAPIView.as_view(queryset=StudentPublications.objects.all(),serializer_class=StudentPublicationsSerializer,permission_classes=(IsAuthenticatedOrReadOnly,IsFacultyAdmin,),parser_classes = (MultiPartParser, FormParser,JSONParser))),
    re_path(r'$',generics.ListCreateAPIView.as_view(queryset=StudentPublications.objects.all(),serializer_class=StudentPublicationsSerializer,permission_classes=(IsAuthenticatedOrReadOnly,IsFacultyAdmin,),parser_classes = (MultiPartParser, FormParser,JSONParser))) ,
]

facultypuburls=[
    re_path(r'(?P<pk>[0-9]+)$',generics.RetrieveUpdateDestroyAPIView.as_view(queryset=FacultyPublications.objects.all(),serializer_class=FacultyPublicationsSerializer,permission_classes=(IsAuthenticatedOrReadOnly,IsFacultyAdmin,),parser_classes = (MultiPartParser, FormParser,JSONParser))),
    re_path(r'$',generics.ListCreateAPIView.as_view(queryset=FacultyPublications.objects.all(),serializer_class=FacultyPublicationsSerializer,permission_classes=(IsAuthenticatedOrReadOnly,IsFacultyAdmin,),parser_classes = (MultiPartParser, FormParser,JSONParser))) ,
]

studymaterialurls=[
    re_path(r'mcq/(?P<pk>[0-9]+)$',generics.RetrieveUpdateDestroyAPIView.as_view(queryset=StudyMaterialMCQ.objects.all(),serializer_class=StudyMaterialMCQSerializer,permission_classes=(IsAuthenticatedOrReadOnly,IsFacultyAdmin,),parser_classes = (MultiPartParser, FormParser,JSONParser))),
    re_path(r'mcq/$',generics.CreateAPIView.as_view(queryset=StudyMaterialMCQ.objects.all(),serializer_class=StudyMaterialMCQSerializer, permission_classes=(IsAuthenticated,IsFacultyAdmin,),parser_classes = (MultiPartParser, FormParser,JSONParser))) ,
    re_path(r'assignment/(?P<pk>[0-9]+)$',generics.RetrieveUpdateDestroyAPIView.as_view(queryset=StudyMaterialAssignment.objects.all(),serializer_class=StudyMaterialAssignmentSerializer,permission_classes=(IsAuthenticatedOrReadOnly,IsFacultyAdmin,),parser_classes = (MultiPartParser, FormParser,JSONParser))),
    re_path(r'assignment/$',generics.CreateAPIView.as_view(queryset=StudyMaterialAssignment.objects.all(),serializer_class=StudyMaterialAssignmentSerializer,permission_classes=(IsAuthenticated,IsFacultyAdmin,),parser_classes = (MultiPartParser, FormParser,JSONParser))) ,
    re_path(r'question-paper/(?P<pk>[0-9]+)$',generics.RetrieveUpdateDestroyAPIView.as_view(queryset=StudyMaterialQuestionPaper.objects.all(),serializer_class=StudyMaterialQuestionPaperSerializer,permission_classes=(IsAuthenticatedOrReadOnly,IsFacultyAdmin,),parser_classes = (MultiPartParser, FormParser,JSONParser))),
    re_path(r'question-paper/$',generics.CreateAPIView.as_view(queryset=StudyMaterialQuestionPaper.objects.all(),serializer_class=StudyMaterialQuestionPaperSerializer,permission_classes=(IsAuthenticated,IsFacultyAdmin,),parser_classes = (MultiPartParser, FormParser,JSONParser))) ,
    re_path(r'presentation/(?P<pk>[0-9]+)$',generics.RetrieveUpdateDestroyAPIView.as_view(queryset=StudyMaterialPresentation.objects.all(),serializer_class=StudyMaterialPresentationSerializer,permission_classes=(IsAuthenticatedOrReadOnly,IsFacultyAdmin,),parser_classes = (MultiPartParser, FormParser,JSONParser))),
    re_path(r'presentation/$',generics.CreateAPIView.as_view(queryset=StudyMaterialPresentation.objects.all(),serializer_class=StudyMaterialPresentationSerializer,permission_classes=(IsAuthenticated,IsFacultyAdmin,),parser_classes = (MultiPartParser, FormParser,JSONParser))) ,
]

userurls=[
    # re_path(r'create$',generics.ListCreateAPIView.as_view(queryset=User.objects.all(),serializer_class=UserSerializer)),
    re_path(r'create$',create_user),
    re_path(r'create/placement$',create_placement),
    # re_path(r'placement_create$',generics.ListCreateAPIView.as_view(queryset=Placement_Team.objects.all(),serializer_class=PlacementFacultySerializer,permission_classes=(IsAuthenticated,IsFacultyAdmin,))),

]

branchurls=[
    re_path(r'(?P<branch>[A-Za-z]+)/notice$',NoticeBranchListView.as_view()),
    re_path(r'(?P<branch>[A-Za-z]+)/faculty$',get_faculty),
    re_path(r'(?P<branch>[A-Za-z]+)/news$',NewsBranchListView.as_view()),
    re_path(r'(?P<branch>[A-Za-z]+)/events$',EventBranchListView.as_view()),
    re_path(r'(?P<branch>[A-Za-z]+)/student-projects$',StudentProjectsBranchView.as_view()),
    # re_path(r'(?P<branch>[A-Za-z]+)/time-table$',TimeTableBranchListView.as_view()),
    re_path(r'(?P<branch>[A-Za-z]+)/time-table$',get_timetable),
    re_path(r'(?P<branch>[A-Za-z]+)/lesson-plan$',LessonPlanBranchListView.as_view()),
    re_path(r'(?P<branch>[A-Za-z]+)/self-learning$',SelfLearningBranchListView.as_view()),
    re_path(r'(?P<branch>[A-Za-z]+)/student-publication$',StudentPublicationsBranchListView.as_view()),
    re_path(r'(?P<branch>[A-Za-z]+)/student-projects$',StudentProjectsBranchView.as_view()),
    re_path(r'(?P<branch>[A-Za-z]+)/faculty-publication$',get_name),
    # re_path(r'(?P<branch>[A-Za-z]+)/faculty-publication$',FacultyPublicationsBranchListView.as_view()),
    re_path(r'(?P<branch>[A-Za-z]+)/study-material/mcq$',StudyMaterialMCQBranchListView.as_view()),
    re_path(r'(?P<branch>[A-Za-z]+)/study-material/assignment$',StudyMaterialAssignmentBranchListView.as_view()),
    re_path(r'(?P<branch>[A-Za-z]+)/study-material/presentation$',StudyMaterialPresentationBranchListView.as_view()),
    re_path(r'(?P<branch>[A-Za-z]+)/study-material/question-paper$',StudyMaterialQuestionPaperBranchListView.as_view()),
    re_path(r'(?P<branch>[A-Za-z]+)/lab-resources$',LabResourcesBranchListView.as_view()),
]

placementurls = [
    re_path(r'team$',generics.ListCreateAPIView.as_view(queryset=Placement_Team.objects.all(),serializer_class=PlacementFacultySerializer,permission_classes=(IsAuthenticatedOrReadOnly,IsFacultyAdmin),parser_classes = (MultiPartParser, FormParser,JSONParser))),
    re_path(r'teams$',get_team),

    # StudentPlaced
    re_path(r'^student-placed$', generics.ListCreateAPIView.as_view(queryset=StudentPlaced.objects.all(),serializer_class=StudentPlacedSerializer,permission_classes=(IsAuthenticatedOrReadOnly,IsFacultyAdmin))),
    re_path(r'^student-placed/(?P<pk>[0-9]+)$',generics.RetrieveUpdateDestroyAPIView.as_view(queryset=StudentPlaced.objects.all(),serializer_class=StudentPlacedSerializer,permission_classes=(IsAuthenticatedOrReadOnly,IsFacultyAdmin,),parser_classes = (MultiPartParser, FormParser,JSONParser))),

    # Training
    re_path(r'^trainings$', generics.ListCreateAPIView.as_view(queryset=Training.objects.all(),serializer_class=TrainingSerializer,permission_classes=(IsAuthenticatedOrReadOnly,IsFacultyAdmin))),
    re_path(r'^trainings/(?P<pk>[0-9]+)$',generics.RetrieveUpdateDestroyAPIView.as_view(queryset=Training.objects.all(),serializer_class=TrainingSerializer,permission_classes=(IsAuthenticatedOrReadOnly,IsFacultyAdmin,),parser_classes = (MultiPartParser, FormParser,JSONParser))),


    # Recruiters
    # re_path(r'^recruiters$', include(recruitersurls)),
    re_path(r'^recruiters/(?P<pk>[0-9]+)$',generics.RetrieveUpdateDestroyAPIView.as_view(queryset=Recruiters.objects.all(),serializer_class=RecruitersSerializer,permission_classes=(IsAuthenticatedOrReadOnly,IsFacultyAdmin,),parser_classes = (MultiPartParser, FormParser,JSONParser))),
    re_path(r'^recruiters', generics.ListCreateAPIView.as_view(queryset=Recruiters.objects.all(),serializer_class=RecruitersSerializer,permission_classes=(IsAuthenticatedOrReadOnly,IsFacultyAdmin))),

    # IndustrialToursAndWorkShops
    re_path(r'^industrial-tour-and-workshop$',generics.ListCreateAPIView.as_view(queryset=IndustrialToursAndWorkShops.objects.all(),serializer_class=IndustrialToursAndWorkShopsSerializer,permission_classes=(IsAuthenticatedOrReadOnly,IsFacultyAdmin))),
    re_path(r'^industrial-tour-and-workshop/(?P<pk>[0-9]+)$',generics.RetrieveUpdateDestroyAPIView.as_view(queryset=IndustrialToursAndWorkShops.objects.all(),serializer_class=IndustrialToursAndWorkShopsSerializer,permission_classes=(IsAuthenticatedOrReadOnly,IsFacultyAdmin,),parser_classes = (MultiPartParser, FormParser,JSONParser))),

    # ExpertTalksAndSeminar
    re_path(r'^expert-talk-seminar$',generics.ListCreateAPIView.as_view(queryset=ExpertTalksAndSeminar.objects.all(),serializer_class=ExpertTalksAndSeminarSerializer,permission_classes=(IsAuthenticatedOrReadOnly,IsFacultyAdmin))),
    re_path(r'^expert-talk-seminar/(?P<pk>[0-9]+)$',generics.RetrieveUpdateDestroyAPIView.as_view(queryset=ExpertTalksAndSeminar.objects.all(),serializer_class=ExpertTalksAndSeminarSerializer,permission_classes=(IsAuthenticatedOrReadOnly,IsFacultyAdmin,),parser_classes = (MultiPartParser, FormParser,JSONParser))),
    
]

recruitersurls=[
    re_path(r'$',generics.ListCreateAPIView.as_view(queryset=Recruiters.objects.all(),serializer_class=RecruitersSerializer,permission_classes=(IsAuthenticatedOrReadOnly,IsFacultyAdmin))),
    re_path(r'^(?P<pk>[0-9]+)$',generics.RetrieveUpdateDestroyAPIView.as_view(queryset=Recruiters.objects.all(),serializer_class=RecruitersSerializer,permission_classes=(IsAuthenticatedOrReadOnly,IsFacultyAdmin,),parser_classes = (MultiPartParser, FormParser,JSONParser))),
]


mainurls = [
    re_path(r'^auth-token/placement', obtain_placement_auth_token),
    re_path(r'^auth-token/', obtain_auth_token),
    re_path(r'^faculty/', include(facultyurls)),
    re_path(r'^placement/', include(placementurls)),
    re_path(r'^gallery/',include(galleryurls)),
    re_path(r'^disclosures/',include(disclosureurls)),
    re_path(r'^marquee/',include(marqueeurls)),
    re_path(r'^notice/', include(noticeurls)),
    re_path(r'^news/', include(newsurls)),
    re_path(r'^events/', include(eventsurls)),
    re_path(r'^time-table/',include(timetableurls)), 
    re_path(r'^lesson-plan/',include(lessonplaneurls)), 
    re_path(r'^self-learning/',include(selflearningurls)),
    re_path(r'^student-projects/', include(studentprojecturls)),
    re_path(r'^achievement-list/',include(achievementlisturls)), 
    re_path(r'^student-publications/',include(studentpuburls)), 
    re_path(r'^faculty-publications/',include(facultypuburls)),
    re_path(r'^study-material/',include(studymaterialurls)),
    re_path(r'^user/',include(userurls)),
    # re_path(r'^nba/',include(nbaurls)),
    re_path(r'^society/',include(societyurls)),
    re_path(r'^student-placed/',include(studentplacedurls)),
    re_path(r'^recruiters/',include(recruitersurls)),
    re_path(r'^nirf/',include(nirfurls)),
    re_path(r'^branch/',include(idtobranchurls)),
    re_path(r'^section/',include(idtosectionsurls)),
    re_path(r'^subject/',include(idtosubjectsurls)),
    re_path(r'^departments/',include(branchurls)),
    re_path(r'^lab-resources/',include(labresurls)),
    re_path(r'^(?!/?static/)(?!/?media/)(?P<path>.*\..*)$',RedirectView.as_view(url='/static/%(path)s', permanent=False)), 
]


urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^api/',include(mainurls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json'])
