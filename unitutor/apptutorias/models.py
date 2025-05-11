from django.db import models

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
      telefono = models.CharField(max_length=15, blank=True, null=True)
      rol = models.CharField(max_length=10, choices=[('ESTUDIANTE', 'Estudiante'), ('DOCENTE', 'Docente')], blank=True, null=True)

      def __str__(self):
          return self.username

