from rest_framework import permissions
from django_backend.models import Faculty,Placement_Team

class IsFacultyAdmin(permissions.BasePermission):
	message="It does not seems like you are Faculty admin"
	def has_permission(self,request,view):
		if request.method in permissions.SAFE_METHODS:
			return True
		try:  
			faculty_member=Faculty.objects.get(User=request.user) 
		except:
			try:
				placement_member=Placement_Team.objects.get(User=request.user)
				if(placement_member.is_placement_team_admin):
					 return True  
			except:
					 return False
		if(faculty_member.is_faculty_admin):
			return True
		else:
			return False    
