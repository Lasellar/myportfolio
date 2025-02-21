from django.contrib.admin import register, ModelAdmin, TabularInline

from .models import Project, Skill, Employer, ProjectSkill


class SkillInline(TabularInline):
    model = ProjectSkill
    extra = 1


@register(Project)
class ProjectAdmin(ModelAdmin):
    inlines = (SkillInline,)
    list_display = ('title', 'url', 'github', 'is_published')
    list_display_links = ('title',)
    list_editable = ('is_published',)


@register(Skill)
class SkillAdmin(ModelAdmin):
    list_display = ('title', 'is_published')
    list_display_links = ('title',)
    list_editable = ('is_published',)


@register(Employer)
class EmployerAdmin(ModelAdmin):
    list_display = ('title', 'url', 'is_published')
    list_display_links = ('title',)
    list_editable = ('is_published',)
