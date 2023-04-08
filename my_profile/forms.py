from django import forms

class UploadForm(forms.Form):
    file = forms.FileField()

    def clean_file(self):
        uploaded_file = self.cleaned_data['file']
        # Perform validation on the uploaded file here
        return uploaded_file
