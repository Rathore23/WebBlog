import io

from django.core.files.base import ContentFile
from django.db import models
from django.contrib.auth.models import User
from PIL import Image


STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class CommonInfo(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(CommonInfo):
    STATUS = (
        (0, "Private"),
        (1, "Public")
    )

    title = models.CharField(max_length=15, unique=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_posts'
    )
    content = models.TextField(max_length=300)
    status = models.IntegerField(choices=STATUS, default=1)
    image = models.ImageField(upload_to='post/', default='post/blogs_img.jpeg')

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Open the original image
        img = Image.open(self.image)
        # Create a BytesIO object to hold the compressed image data
        output = io.BytesIO()
        # Compress the image and save it to the BytesIO object
        img.save(output, format='JPEG', quality=30)  # Adjust quality as needed
        # Get the size of the compressed image data
        size = output.tell()
        # If the compressed image is smaller than the original, update the image field
        if size < self.image.size:
            # Set the file pointer to the beginning of the BytesIO object
            output.seek(0)
            # Update the image field with the compressed image data
            self.image = ContentFile(output.getvalue(), name=self.image.name)
        # Call the parent class's save method to save the model instance
        super().save(*args, **kwargs)
