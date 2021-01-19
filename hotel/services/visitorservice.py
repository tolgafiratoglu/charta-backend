from rest_framework.views import APIView
from hotel.models.visitormodel import Visitor
from django.db.models import Q

from hotel.serializers.visitorserializer import VisitorSaveSerializer

class VisitorService():

    @classmethod
    def visitor_exists(self, gsm, email):
        visitor = Visitor.objects.filter(Q(gsm=gsm) | Q(email=email))
        return visitor

    @classmethod
    def create(self, firstname, lastname, gsm, email):        
        visitor_serializer = VisitorSaveSerializer(data={"gsm": gsm, "email": email, "firstname": firstname, "lastname": lastname})
        if visitor_serializer.is_valid():
            visitor = visitor_serializer.save()
            return visitor.pk
        else:
            return False  

    @classmethod
    def get_visitor(self, firstname, lastname, gsm, email):
        visitor = self.visitor_exists(gsm, email)        
        if visitor.count() > 0:
            return visitor.first()
        else:
            return self.create(firstname, lastname, gsm, email)    