from django.contrib import admin

from website.models import Boardmember, BlogPost
# , Album, Photo
# Register your models here.

class BoardMemberAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name',               {'fields': ['member_fname', 'member_lname', 'member_nName']}),
        ('Postiion', {'fields': ['position']}),
        ('Major/Minor', {'fields': ['major_minor']}),
        ('Year', {'fields': ['year']}),
        ('Why ASA', {'fields': ['why_ASA']}),
        ('Fave Mem', {'fields': ['fave_mem']}),
        ('Fun Fact', {'fields': ['fun_fact']}),
    ]

class BlogPostAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Title',               {'fields': ['title']}),
        ('Body',               {'fields': ['body']}),
        ('created', {'fields': ['created']}),
        ('Image'  , {'fields' : ['picture']})   
    ]



admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Boardmember, BoardMemberAdmin)


# class PhotoInline(admin.TabularInline):
#     model = Photo
#     extra = 3


# class AlbumAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,               {'fields': ['album_name']}),
#         ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
#     ]
#     inlines = [PhotoInline]
#     list_display = ('album_name', 'pub_date', 'was_published_recently')
#     list_filter = ['pub_date']
#     search_fields = ['album_name']

# admin.site.register(Album, AlbumAdmin)