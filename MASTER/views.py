from django.shortcuts import render
from rest_framework import viewsets

from MASTER.models import Kabupaten, Kecamatan ,Kelurahan
from MASTER.serializers import KecamatanSerializer, KelurahanSerializer, KabupatenSerializer


class KabupatenViewSet(viewsets.ModelViewSet):
    queryset = Kabupaten.objects.all()
    serializer_class = KabupatenSerializer


class KecamatanViewSet(viewsets.ModelViewSet):
    queryset = Kecamatan.objects.all()
    serializer_class = KecamatanSerializer


class KelurahanViewSet(viewsets.ModelViewSet):
    queryset = Kelurahan.objects.all()
    serializer_class = KelurahanSerializer

