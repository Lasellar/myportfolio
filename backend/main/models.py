from django.db.models import (
    TextField, ImageField, URLField, BooleanField,
    ManyToManyField, Model, ForeignKey, CASCADE
)

from .mixins import ModelMixin


class Skill(ModelMixin):
    pass


class Project(ModelMixin):
    description = TextField()
    image = ImageField(upload_to='projects/', blank=True)
    url = URLField(blank=True)
    github = URLField(blank=True)
    is_commercial = BooleanField(default=False)
    skills = ManyToManyField(
        Skill, through='ProjectSkill', related_name='projects'
    )


class ProjectSkill(Model):
    project = ForeignKey(Project, on_delete=CASCADE)
    skill = ForeignKey(Skill, on_delete=CASCADE)


class Employer(ModelMixin):
    image = ImageField(upload_to='projects/', blank=True)
    url = URLField(blank=True)
