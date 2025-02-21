from django.db.models import (
    Model, CharField, BooleanField
)


class ModelMixin(Model):
    title = CharField(max_length=100)
    is_published = BooleanField(blank=True, default=False)

    def __str__(self):
        return self.title
