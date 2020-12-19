from django.db import models
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel

from cabins.core import get_app_site_string, get_image_model_string
from cabins.core.models import Orderable, SeriailizerMixin
from cabins.page import get_page_string


class SiteContent(SeriailizerMixin, ClusterableModel):
    site = models.OneToOneField(
        get_app_site_string(),
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='site_content'
    )
    logo = models.ForeignKey(
        get_image_model_string(),
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='site_logo'
    )
    navigation = models.ManyToManyField(
        get_page_string(),
    )
    footer_content = models.TextField()

    site_phone = models.CharField(max_length=16)
    site_email = models.EmailField(max_length=255)


class SocialMedia(Orderable):
    site = ParentalKey(
        SiteContent,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='social_media'
    )
    name = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )
    url = models.URLField(
        max_length=255,
        blank=True,
        null=True
    )
    icon = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )
