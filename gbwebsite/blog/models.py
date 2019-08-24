from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel

from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

from streams import blocks
# Create your models here.


class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey('BlogPage', on_delete=models.CASCADE, related_name='tagged_items')


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
            ('quote_block', blocks.QuoteBlock()),
            ('image_with_caption', blocks.ImageWithCaption()),
        ],
        null=True,
        blank=True,
    )

    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)

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

    promote_panels = Page.promote_panels + [
        FieldPanel('tags'),
     ]
