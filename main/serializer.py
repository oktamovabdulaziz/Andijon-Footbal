from rest_framework import serializers
from .models import *


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = "__all__"


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = "__all__"


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = "__all__"


class ArenaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Arena
        fields = "__all__"
    arena_photo = PhotoSerializer(many=True)



class SponsorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsors
        fields = "__all__"


class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = "__all__"


class NewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewDetail
        fields = "__all__"


class PressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Press
        fields = "__all__"


class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = "__all__"


class AdviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advice
        fields = "__all__"


class TrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Training
        fields = "__all__"


class ArenaHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ArenaHistory
        fields = "__all__"

