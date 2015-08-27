from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Kabupaten, Kecamatan, Kelurahan, KecamatanResource, KelurahanResource, KabupatenResource


class KabupatenAdmin(ImportExportModelAdmin):
    list_display = ['nama_kabupaten', 'keterangan']
    resource_class = KabupatenResource
    pass

admin.site.register(Kabupaten, KabupatenAdmin)


class KecamatanAdmin(ImportExportModelAdmin):
    list_display = ['nama_kecamatan', 'nama_kecamatan', 'keterangan']
    resource_class = KecamatanResource
    pass

admin.site.register(Kecamatan, KecamatanAdmin)


class KelurahanAdmin(ImportExportModelAdmin):
    list_display = ['nama_kecamatan', 'nama_kelurahan', 'keterangan']
    resource_class = KelurahanResource
    pass

admin.site.register(Kelurahan, KelurahanAdmin)
