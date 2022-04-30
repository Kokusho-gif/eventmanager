from django import forms
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

import bootstrap_datepicker_plus.widgets as datetimepicker
from PIL import Image

from .models import Event

class UserUpdateForm(forms.ModelForm):
    """ユーザー情報更新フォーム"""
    class Meta:
        model = User
        fields = ('username', 'last_name','first_name','email','password')

class EventCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(EventCreateForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['author'].required = False

    class Meta:
        model = Event
        fields = ('eventtitle','eventdate','location','agenda','author','image','background')
        widgets={
            'eventtitle':forms.Textarea(attrs={'cols':80,'rows':1}),
            'eventdate':datetimepicker.DatePickerInput(
                options = {
                     "format": "MM/DD/YYYY HH:mm", # moment date-time format
                     "showClose": True,
                     "showClear": True,
                     "showTodayButton": True,
                }
            ),
            'location':forms.Textarea(attrs={'cols':80,'rows':1}),
            'agenda':forms.Textarea(attrs={'cols':80,'rows':10}),
            'author':forms.HiddenInput(),
        }
        error_messages = {
            'eventtitle':{
                'max_length':_('Title is too long')
            }
        }

