from django.contrib import admin

# Register your models here.
""" from projects.models import Project, Position, ApplicationList, ApplicationRequest


class ApplicationListAdmin(admin.ModelAdmin):
    list_filter = ['acceptor']
    list_display = ['acceptor']
    search_fields = ['acceptor']
    readonly_fields = ['acceptor']

    class Meta:
        model = ApplicationList

admin.site.register(ApplicationList, ApplicationListAdmin)


class ApplicationRequestAdmin(admin.ModelAdmin):
    list_filter = ['sender', 'receiver']
    list_display = ['sender', 'receiver']
    search_fields = ['sender__username', 'receiver__username']

    class Meta:
        model = ApplicationRequest

admin.site.register(ApplicationRequest, ApplicationRequestAdmin)

class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',),}


admin.site.register([Project, Position]) """
