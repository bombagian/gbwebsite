from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class TitleAndTextBlock(blocks.StructBlock):
    "title and nothing else"

    title = blocks.CharBlock(required=True, help_text='Add your title')
    text = blocks.TextBlock(required=True, help_text='Add additional text')


    class Meta: # noqa
        template = "streams/title_and_text_block.html"
        icon = "edit"
        label = "Title and Text"


class CardBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, help_text='Add your title')
    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=True)),
                ("title", blocks.CharBlock(required=True, max_length=40)),
                ("text", blocks.TextBlock(required=True, max_length=200)),
                ("button_page", blocks.PageChooserBlock(required=False)),
                ("button_url", blocks.URLBlock(required=False, help_text="if the button page above is selected, that will be used first")),
            ]
        )
    )

    class Meta:
        template = "streams/card_block.html"
        icon = "placeholder"
        label = "Staff Cards"


class RichtextBlock (blocks.RichTextBlock):

    class Meta:
        template = "streams/richtext_block.html"
        icon = "doc-full"
        label = "Full RichText"


class SimpleRichtextBlock (blocks.RichTextBlock):
    def __init__(self, required=True, help_text=None, editor='default', features=None, validators=(), **kwargs):
        super().__init__(**kwargs)
        self.features = [
            "bold",
            "italic",
            "link",
        ]

    class Meta:
        template = "streams/richtext_block.html"
        icon = "edit"
        label = "Simple RichText"


class QuoteBlock(blocks.StructBlock):

    text = blocks.TextBlock()
    quote_author = blocks.CharBlock(blank=True, required=False, label= "Author", help_text="e.g. Leonardo da Vinci")
    quote_source = blocks.CharBlock(blank=True, required=False, label= "Source", help_text="e.g. diary")

    class Meta:
        template = "streams/quote_block.html"
        icon = "openquote"


class ImageWithCaption(blocks.StructBlock):

    image = ImageChooserBlock(required=True)
    caption = blocks.CharBlock(required=False)
    attribution = blocks.CharBlock(required=False)

    class Meta:
        template = "streams/image_with_caption.html"
        icon = "image"
        