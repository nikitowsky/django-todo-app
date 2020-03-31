from django.db import models


class BaseModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.full_clean()
        super(BaseModel, self).save(*args, **kwargs)


class Tag(BaseModel):
    title = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.title


class Todo(BaseModel):
    title = models.CharField(max_length=255)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)

    class Meta:
        ordering = ['created_at']

    def add_tag(self, title):
        """ Add tag to a Todo """
        if title is None:
            raise ValueError('Title is required')

        tag, created = Tag.objects.get_or_create(title=title)

        if not created:
            tag = Tag.objects.get(title=tag)

        self.tags.add(tag)

        return tag

    def __str__(self):
        return self.title
