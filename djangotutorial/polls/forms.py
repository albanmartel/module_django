from django import forms
from .models import Question, Choice

NB_MAX_CHOIX = 5


class NameForm(forms.Form):
    your_name = forms.CharField(label="Your name", max_length=100)


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)


class QuestionAddForm(forms.Form):
    question_text = forms.CharField(label='Question text')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for i in range(NB_MAX_CHOIX):
            self.fields[f"choice_{i}"] = forms.CharField(
                label=f"Choice #{i + 1}",
                max_length=200,
                required=False
            )


class VoteForm(forms.Form):

    def __init__(self, question_text, choices, *args, **kwargs):
        super(VoteForm, self).__init__(*args, **kwargs)
        self.fields['choice'] = \
            forms.ChoiceField(label=question_text,
                              widget=forms.RadioSelect,
                              choices=choices)
