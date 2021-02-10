from rest_framework.permissions import BasePermission
from .models import anonymousUser
class AnonymousPermission(BasePermission):
    
    def has_permission(self, request, view):
       try:
        username=request.session['username']
        isAnonymous=anonymousUser.objects.get(username=username)
        if request.method=="GET":
            return True
        else:
            return False    
      
        
       except anonymousUser.DoesNotExist: 
           return True
        
        