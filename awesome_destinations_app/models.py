from django.db import models


class Destination(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=100, default='Unknown')  # Provide default value here
    # other fields and methods
    description = models.TextField(default='Default description')
# Ensure this field is in your model
    image = models.ImageField(upload_to='destinations/', blank=True, null=True)  # New image field

    def __str__(self):
        # Generate a string for the image information
        image_info = f"Image: {self.image.url}" if self.image else "No image"
        # Return a formatted string for the model instance
        return f"{self.name} - {self.country}: {self.description[:50]} ({image_info})" # Adjust as needed
