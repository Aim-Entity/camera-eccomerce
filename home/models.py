from django.db import models


class Contact(models.Model):
    fullname = models.CharField(max_length=95)
    email = models.EmailField(max_length=125)

    message = models.TextField(max_length=450)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Name: {self.fullname} Read: {self.read}"
