from django import forms    

class CreateNewList(forms.Form):
    name = forms.CharField(
        label="Name",
        max_length=200,
        widget=forms.TextInput(attrs={
            'style': 
                'width: 50%; padding: 10px;'
                'border: 1px solid #ddd; box-shadow: 2px 2px 5px #ddd; margin-right: 15px; margin-left: 5px;',
            'placeholder': 'List Name',
        })
    )
    check = forms.BooleanField(
        label="Completed",
        required=False,
        widget=forms.CheckboxInput(attrs={
            'style': 
                'margin-left: 5px; margin-right: 15px;',
            'cursor': 'pointer',
        })
    )
