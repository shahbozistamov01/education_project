from django.db import models
from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from head_page.models import Room, Topic, Message


class RoomSerializers(ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'
