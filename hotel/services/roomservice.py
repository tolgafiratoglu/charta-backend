from serializers.roomvisitorserializer import RoomVisitorSerializer

from models.roomvisitormodel import RoomVisitor

class RoomService():

    @classmethod
    def save_visitor_to_room(self, room, visitor):
        if room > 0 && visitor > 0:
            serializer = RoomVisitorSerializer(data={"room": room, "visitor": visitor})
            if serializer.is_valid():
                room_visitor = serializer.save()
                return room_visitor.pk
        else:
            return False        
