from django.db import models


class BaseModel(models.Model):
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

    def __str__(self):
        return self.title
