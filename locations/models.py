from django.db import models


class Location(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Name",
        blank=True
    )
    description = models.TextField(
        max_length=None,
        verbose_name="Description",
        blank=True
    )
    address1 = models.CharField(
        max_length=255,
        verbose_name="Address Line 1",
        blank=True
    )
    address2 = models.CharField(
        max_length=255,
        verbose_name="Address Line 2",
        blank=True
    )
    town = models.CharField(
        max_length=255,
        verbose_name="Town",
        blank=True
    )
    open_time = models.TimeField(
        max_length=None,
        verbose_name="Opening Time",
        blank=True,
        null=True
    )
    close_time = models.TimeField(
        max_length=None,
        verbose_name="Closing Time",
        blank=True,
        null=True
    )
    contact1 = models.CharField(
        max_length=255,
        verbose_name="Contact Name 1",
        blank=True
    )
    phone1 = models.CharField(
        max_length=12,
        verbose_name="Phone Number 1",
        blank=True,
        null=True
    )
    contact2 = models.CharField(
        max_length=255,
        verbose_name="Contact Name 2",
        blank=True
    )
    phone2 = models.CharField(
        max_length=12,
        verbose_name="Phone Number 2",
        blank=True,
        null=True
    )
    latitude = models.FloatField(
        max_length=None,
        verbose_name="Latitude",
        blank=True,
        null=True
    )
    longitude = models.FloatField(
        max_length=None,
        verbose_name="Longitude",
        blank=True,
        null=True
    )
    D = 'None'
    N = 'North'
    E = 'East'
    S = 'South'
    W = 'West'
    C = 'Central'
    CARDINAL_POINTS = (
        (D, 'None'),
        (N, 'North'),
        (E, 'East'),
        (S, 'South'),
        (W, 'West'),
        (C, 'Central')
    )
    cardinal_point = models.CharField(
        max_length=7,
        choices=CARDINAL_POINTS,
        default=D,
        verbose_name="Cardinal Point"
    )
    email = models.EmailField(
        max_length=255,
        verbose_name="Email",
        blank=True
    )
    website = models.URLField(
        max_length=255,
        verbose_name="Website",
        blank=True
    )
    facebook = models.URLField(
        max_length=255,
        verbose_name="Facebook",
        blank=True
    )
    notes = models.TextField(
        max_length=None,
        verbose_name="Notes",
        blank=True
    )

    def __str__(self):
        return self.name
