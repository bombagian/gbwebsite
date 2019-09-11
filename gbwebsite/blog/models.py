from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

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
    # add author?

    post_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Landscape mode only; horizontal width between 1000px and 3000px.'
        )

    body = StreamField(
        [
            ('full_richtext', blocks.RichtextBlock()),
            ('quote_block', blocks.QuoteBlock()),
            ('image_with_caption', blocks.ImageWithCaption()),
        ],
        null=True,
        blank=True,
    )

    subtitle = models.CharField(blank=True, max_length=255)
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)
    date_published = models.DateTimeField(
        name="Date published",
        verbose_name="Date article published",
        blank=True,
        null=True,
        )

    content_panels = Page.content_panels + [
        FieldPanel('subtitle', classname="full"),
        FieldPanel('page_intro'),
        ImageChooserPanel('post_image'),
        StreamFieldPanel('body'),
        FieldPanel('Date published')
     ]

    promote_panels = Page.promote_panels + [
        FieldPanel('tags'),
     ]


class BlogIndex(Page):

    template = 'blog/blog_index.html'
    max_count = 1

    introduction = models.TextField(
        help_text='Text to describe the page',
        blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('introduction', classname="full"),
    ]

    # Speficies that only BlogPage objects can live under this index page
    subpage_types = ['BlogPage']

    # Defines a method to access the children of the page
    def children(self):
        return self.get_children().specific().live()

    # Overrides the context to list all child items, that are live, by the
    # date that they were published
    def get_context(self, request):
        context = super(BlogIndex, self).get_context(request)
        context['posts'] = BlogPage.objects.descendant_of(
            self).live()#.order_by('-date_published')
        return context

    # Returns the child BlogPage objects for this BlogPageIndex.
    # If a tag is used then it will filter the posts by tag.
    def get_posts(self, tag=None):
        posts = BlogPage.objects.live().descendant_of(self)
        if tag:
            posts = posts.filter(tags=tag)
        return posts

    def serve_preview(self, request, mode_name):
        # Needed for previews to work
        return self.serve(request)
