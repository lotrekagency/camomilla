from django import forms
from camomilla.models import Media
from .widgets import ImagePreviewWidget

class MediaModelForm(forms.ModelForm):

    image_preview = forms.Field(widget=ImagePreviewWidget())
    
    class Meta:
        model = Media
        fields = '__all__'
        widgets = {
            'image_preview': ImagePreviewWidget(),
        }

    def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance')
        super().__init__(*args, **kwargs)
        self.fields['image_preview'].widget.attrs['instance'] = instance    
