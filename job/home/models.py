from django.db import models


class Link(models.Model):
    email = models.CharField(
        max_length = 250,
        verbose_name = "Email",
    )

    def __str__(self):
        return self.email

    class Meta:
        db_table = "email"
        verbose_name = "Email"
        verbose_name_plural = "Emails"