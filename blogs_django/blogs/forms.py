from django import forms
from django.core.validators import MaxLengthValidator
from django.utils.translation import gettext_lazy as _
from .models import Post


class PostForm(forms.ModelForm):
    """
    label_tag: Renders the field's label wrapped in a <label> tag.
    value: Retrieves the current value of the field.
    id_for_label: Returns the HTML ID attribute for the field's label.
    errors: Returns a list of validation errors for the field.
    is_hidden: Indicates whether the field is a hidden input.
    name: Returns the name attribute of the field.
    auto_id: Generates an automatic ID for the field.
    css_classes: Returns a string containing CSS classes for the field.
    help_text: Returns the help text associated with the field.
    field: Returns the field object itself.
    """

    class Meta:
        model = Post
        fields = [
            'title', 'content', 'status', 'image'
        ]
        # labels = {
        #     'title': _('Title'),
        #     'content': _('Content'),
        #     'status': _('Status'),
        #     'image': _('Image'),
        # }
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'title': 'title'
                }
            ),
            'content': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),
            'status': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'image': forms.FileInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].required = True
        # self.fields['title'].validators.append(MaxLengthValidator(15))
        # self.fields['content'].validators.append(MaxLengthValidator(150))
