from rest_framework.views import APIView
from hotel.models.visitormodel import Visitor

from hotel.serializers.visitorserializer import VisitorSaveSerializer

class VisitorService(APIView):

    def visitor_exists(gsm, mail):
        visitor = Visitor.filter(Q(gsm=gsm) | Q(email=email))
        return visitor

    def create_visitor(firstname, lastname, gsm, email):        
        visitor_serializer = VisitorSaveSerializer(data={"gsm": gsm, "email": email, "firstname": firstname, "lastname": lastname})
        if visitor_serializer.is_valid():
            visitor_serializer.save()
            return serializer.data.import ipdb; ipdb.set_trace()

    def get_visitor(firstname, lastname, gsm, email):
        visitor = self.visitor_exists(gsm, email)        
        if visitor > 0:
            return visitor.id
        elif:
            return create_visitor(firstname, lastname, gsm, email)    