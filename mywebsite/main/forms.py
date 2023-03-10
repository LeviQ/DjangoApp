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

class CreateNewItemForList(forms.Form):
    name = forms.CharField(
        label="Name",
        max_length=200,
        widget=forms.TextInput(attrs={
            'style': 
                'width: 20%; padding: 10px;'
                'border: 1px solid #ddd; box-shadow: 2px 2px 5px #ddd; margin-right: 15px; margin-left: 5px;',
            'placeholder': 'Item Name',
        })
    )
    description = forms.CharField(
        label="Description",
        max_length=400,
        required=False,
        widget=forms.TextInput(attrs={
            'style': 
                'width: 30%; padding: 10px;'
                'border: 1px solid #ddd; box-shadow: 2px 2px 5px #ddd; margin-right: 15px; margin-left: 5px;',
            'placeholder': 'Item Description',
        })
    )
    completed = forms.BooleanField(label="Completed",required=False)

