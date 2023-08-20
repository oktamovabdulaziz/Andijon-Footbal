from .serializer import *
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, ListCreateAPIView, \
    UpdateAPIView, RetrieveUpdateDestroyAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, DestroyAPIView
from rest_framework.response import Response


class NewsView(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def list(self, request):
        query = self.queryset.all().order_by("-id")[:3]
        ser_data = NewsSerializer(query, many=True).data
        return Response({"data": ser_data})


class VideoView(ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


class TableView(ListAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer


class PlayerView(ListAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class ProductView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class PhotoView(ListAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer


class ArenaView(ListAPIView):
    queryset = Arena.objects.all()
    serializer_class = ArenaSerializer

    def list(self, request):
        query = self.queryset.last()
        ser_data = ArenaSerializer(query).data
        return Response({"data": ser_data})


class SponsorsView(ListAPIView):
    queryset = Sponsors.objects.all()
    serializer_class = SponsorsSerializer


class InfoView(ListAPIView):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer

    def list(self, request):
        query = self.queryset.last()
        ser = self.serializer_class(query).data
        return Response({"data": ser})


class NewDetailView(ListAPIView):
    queryset = NewDetail.objects.all()
    serializer_class = NewDetailSerializer


class PressView(ListAPIView):
    queryset = Press.objects.all()
    serializer_class = PressSerializer


class ClubView(ListAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer

    def list(self, request):
        query = self.queryset.last()
        ser = self.serializer_class(query).data
        return Response({"data": ser})


class AdviceView(ListAPIView):
    queryset = Advice.objects.all()
    serializer_class = AdviceSerializer

    def list(self, request):
        query = self.queryset.all().order_by("-id")[:4]
        ser = AdviceSerializer(query, many=True).data
        return Response({"data": ser})


class TrainingView(ListAPIView):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer

    def list(self, request):
        query = self.queryset.last()
        ser = self.serializer_class(query).data
        return Response({"data": ser})


class ArenaHistoryView(ListAPIView):
    queryset = ArenaHistory.objects.all()
    serializer_class = ArenaHistorySerializer

    def list(self, request):
        query = self.queryset.last()
        ser = self.serializer_class(query).data
        return Response({"data": ser})
