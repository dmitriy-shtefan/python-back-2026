from django import forms


class TeacherQuestionForm(forms.Form):
    name = forms.CharField(max_length=100, label="Імʼя")
    email = forms.EmailField(label="Email")
    question = forms.CharField(
        label="Питання",
        min_length=10,
        widget=forms.Textarea
    )

    def clean_question(self):
        question = self.cleaned_data['question']
        if "???" in question:
            raise forms.ValidationError("Сформулюйте питання без повтору ???.")

        return question