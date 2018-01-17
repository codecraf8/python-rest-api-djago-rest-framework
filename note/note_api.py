from rest_framework import serializers
from .models import Note
from rest_framework import viewsets

class NoteSerialiser(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Note
        fields = ('id', 'title', 'description', 'created_at', 'created_by', 'priority')


class NoteViewSet(viewsets.ModelViewSet):

    queryset = Note.objects.all()
    serializer_class = NoteSerialiser
