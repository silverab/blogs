from django.contrib import admin
from .models import Category, LeftPost, RightPost, CenterPost, MiniCenterPost, AsiaPost, AfricaPost, EuropePost, NorthAmericaPost



admin.site.register(Category)

class NorthAmericaPostAdmin(admin.ModelAdmin):
	list_display = ['title', 'category', 'created', 'author']
	prepopulated_fields = {'slug': ('title',)}
	list_filter = ['category', 'created','updated']
	class Meta:
		model = NorthAmericaPost

admin.site.register(NorthAmericaPost, NorthAmericaPostAdmin)

class EuropePostAdmin(admin.ModelAdmin):
	list_display = ['title', 'category', 'created', 'author']
	prepopulated_fields = {'slug': ('title',)}
	list_filter = ['category', 'created','updated']
	class Meta:
		model = EuropePost

admin.site.register(EuropePost, EuropePostAdmin)

class AfricaPostAdmin(admin.ModelAdmin):
	list_display = ['title', 'category', 'created', 'author']
	prepopulated_fields = {'slug': ('title',)}
	list_filter = ['category', 'created','updated']
	class Meta:
		model = AfricaPost

admin.site.register(AfricaPost, AfricaPostAdmin)

class AsiaPostAdmin(admin.ModelAdmin):
	list_display = ['title', 'category', 'created', 'author']
	prepopulated_fields = {'slug': ('title',)}
	list_filter = ['category', 'created','updated']
	class Meta:
		model = AsiaPost

admin.site.register(AsiaPost, AsiaPostAdmin)

class LeftPostAdmin(admin.ModelAdmin):
	list_display = ['title', 'category', 'created', 'author']
	prepopulated_fields = {'slug': ('title',)}
	list_filter = ['category', 'created','updated']
	class Meta:
		model = LeftPost

admin.site.register(LeftPost, LeftPostAdmin)

class CenterPostAdmin(admin.ModelAdmin):
	list_display = ['title', 'category', 'created', 'author']
	prepopulated_fields = {'slug': ('title',)}
	list_filter = ['category', 'created','updated']
	class Meta:
		model = CenterPost

admin.site.register(CenterPost, CenterPostAdmin)

class MiniCenterPostAdmin(admin.ModelAdmin):
	list_display = ['title', 'category', 'created', 'author']
	prepopulated_fields = {'slug': ('title',)}
	list_filter = ['category', 'created','updated']
	class Meta:
		model = MiniCenterPost

admin.site.register(MiniCenterPost, MiniCenterPostAdmin)

class RightPostAdmin(admin.ModelAdmin):
	list_display = ['title', 'category', 'created', 'author']
	prepopulated_fields = {'slug': ('title',)}
	list_filter = ['category', 'created','updated']
	class Meta:
		model = RightPost

admin.site.register(RightPost, RightPostAdmin)