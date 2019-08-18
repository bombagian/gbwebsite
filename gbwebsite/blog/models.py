from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel

from streams import blocks
# Create your models here.


class BlogPage(Page):

    template = 'blog/blog_page.html'

    page_intro = models.TextField(
        help_text="Page intro",
        max_length=140,
        blank=True
    )
    # add photo of author

    body = StreamField(
        [
            ('full_richtext', blocks.RichtextBlock()),
        ],
        null=True,
        blank=True,
    )
    """
    date_published = models.DateField(
        name="Date published",
        verbose_name="Date article published",
        blank=True,
        null=True
        )
    """
    content_panels = Page.content_panels + [
        FieldPanel('page_intro'),
        StreamFieldPanel('body'),
        # FieldPanel('Date published'),
     ]
