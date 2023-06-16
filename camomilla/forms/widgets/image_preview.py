from django.template.loader import render_to_string
from django.forms.widgets import TextInput
from django import forms

class ImagePreviewWidget(forms.widgets.Widget):
    template_name = 'defaults/widgets/image_preview.html'

    def render(self, name, value, attrs=None, renderer=None):
        if value is None:
            value = ''
        model_instance = self.attrs.get('instance')    
        context = {
            'widget': {
                'name': name,
                'value': value,
                'attrs': attrs,
            },
            'self': model_instance,
            
        }
        return self._render(self.template_name, context, renderer)    