from django.forms import CheckboxSelectMultiple

from django.template.loader import render_to_string
from django.utils.safestring import mark_safe

from camomilla.models import Media


class MediaSelectMultiple(CheckboxSelectMultiple):

    template_name = 'camomilla/widgets/media_select_multiple.html'

    def _build_choices(self, name, all_choices, choices_selected):
        choices = []
        for choice in all_choices:
            thumb_url = ''
            media_obj = Media.objects.get(id=choice[0])
            if media_obj.is_image and media_obj.thumbnail:
                thumb_url = media_obj.thumbnail.url
            choices.append({
                'thumb': thumb_url,
                'value': choice[0],
                'label': choice[1],
                'selected': True if choice[0] in choices_selected else False
            })
        return choices

    def render(self, name, value, attrs=None, choices=()):
        choices = self._build_choices(name, self.choices, value)
        html = render_to_string(
            self.template_name,
            {'name': name, 'choices': choices}
        )
        return mark_safe(html)
