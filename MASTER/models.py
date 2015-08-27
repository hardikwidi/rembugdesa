from django.db import models
from import_export import resources


class Kabupaten(models.Model):
    nama_kabupaten = models.CharField(max_length=100)
    keterangan = models.CharField(max_length=500)

    createtime = models.DateTimeField(auto_now_add=True, auto_now=False)
    updatetime = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.nama_kabupaten

class KabupatenResource(resources.ModelResource):
    class Meta:
        model = Kabupaten


class Kecamatan(models.Model):
    nama_kabupaten = models.ForeignKey(Kabupaten)
    nama_kecamatan = models.CharField(max_length=100)
    keterangan = models.CharField(max_length=500)

    createtime = models.DateTimeField(auto_now_add=True, auto_now=False)
    updatetime = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.nama_kecamatan


class KecamatanResource(resources.ModelResource):
    class Meta:
        model = Kecamatan


class Kelurahan(models.Model):
    nama_kecamatan = models.ForeignKey(Kecamatan)
    nama_kelurahan = models.CharField(max_length=100)
    keterangan = models.CharField(max_length=500)

    createtime = models.DateTimeField(auto_now_add=True, auto_now=False)
    updatetime = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.nama_kelurahan


class KelurahanResource(resources.ModelResource):
    class Meta:
        model = Kelurahan
