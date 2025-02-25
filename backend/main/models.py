from django.db.models import (
    TextField, ImageField, URLField, BooleanField,
    ManyToManyField, Model, ForeignKey, CASCADE, CharField
)


class Skill(Model):
    title = CharField(max_length=100)
    is_published = BooleanField(blank=True, default=False)

    def __str__(self):
        return self.title


class Project(Model):
    title = CharField(max_length=100)
    is_published = BooleanField(blank=True, default=False)
    description = TextField()
    image = ImageField(upload_to='projects/', blank=True)
    url = URLField(blank=True)
    github = URLField(blank=True)
    is_commercial = BooleanField(default=False)
    skills = ManyToManyField(
        Skill, through='ProjectSkill', related_name='projects'
    )

    def __str__(self):
        return self.title


class ProjectSkill(Model):
    project = ForeignKey(Project, on_delete=CASCADE)
    skill = ForeignKey(Skill, on_delete=CASCADE)


class Employer(Model):
    title = CharField(max_length=100)
    is_published = BooleanField(blank=True, default=False)
    image = ImageField(upload_to='projects/', blank=True)
    url = URLField(blank=True)

    def __str__(self):
        return self.title
