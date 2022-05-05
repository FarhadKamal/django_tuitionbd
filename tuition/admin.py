from ntpath import join
from django.contrib import admin
from django.utils import timezone
from django.utils.html import format_html
from .models import Contact, Post, Subject, Class_in
admin.site.site_title= 'TutionBD Admin Panel'
admin.site.site_header= 'TutionBD Admin Panel'
admin.site.index_title=''
admin.site.register(Contact)

admin.site.register(Subject)
admin.site.register(Class_in)
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    # fields=('user','title')
    # exclude=('user','title',)
    list_fileter=('title',)
    readonly_fields=('slug',)
    list_display=('user','title_html_display','created_at','salary','created_since','get_subjects')
    search_fields=('title',)
    filter_horizontal=('subject','class_in')
    list_editable=('salary',)
    list_display_link=('title')
    actions=('change_salary_3000',)

    def title_html_display(self,obj):
        return format_html(f'<span style="font-size:20px; color:blue">{obj.title}</span>')

    def get_subjects(self,obj):
        return ", ".join([p.name for p in  obj.subject.all()])
    get_subjects.short_description="Subjects"

    def created_since(self,Post):
        diff= timezone.now() - Post.created_at
        return diff.days
    created_since.short_description="Since created"
    def change_salary_3000(self,request,queryset):
        count=queryset.update(salary=3000)
        self.message_user(request,'{} posts updated'.format(count))
    change_salary_3000.short_description="change salary"
admin.site.register(Post,PostAdmin)
