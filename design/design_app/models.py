from django.db import models

class Post(models.Model):
    created = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        blank=False,
        null=False
    )

    update = models.DateTimeField(
        auto_now=True,
        editable=False,
        blank=False,
        null=False
    )

    first_name = models.CharField(
        max_length=10,
        blank=False,
        null=False
    )

    first_name_kana = models.CharField(
        max_length=10,
        blank=False,
        null=False
    )

    last_name = models.CharField(
        max_length=10,
        blank=False,
        null=False
    )

    last_name_kana = models.CharField(
        max_length=10,
        blank=False,
        null=False
    )

    call_num = models.CharField(
        max_length=15,
        blank=False,
        null=False
    )

    address = models.CharField(
        max_length=100,
        blank=False,
        null=False
    )

    def __str__(self):
        return self.first_name
