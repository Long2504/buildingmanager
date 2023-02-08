
from django import forms
from .models import Floor


class FloorForm(forms.ModelForm):
    name = forms.CharField(
        label='Name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Name'
            }
        )
    )
    capacity = forms.IntegerField(
        widget=forms.IntegerField(
            attrs={
                'class': 'form-control',
                'placeholder': 'số lượng người'
            }
        )
    )
    status = forms.CharField(("Chưa thuê"),("Đã thuê"),("Đang sửa chửa"))
    area = forms.IntegerField(
        widget=forms.IntegerField(
            attrs={'class': 'form-control'}
        )
    )
    deleted_flag = forms.BooleanField()
    image = forms.ImageField(
        widget=forms.FileInput()
        
    )

    class Meta:
        model = Student
        fields = [
            'code',
            'name',
            'address',
            'email',
            'department']

    def clean_code(self, *args, **kwargs):
        new_code = self.cleaned_data.get('code')
        if not new_code.isnumeric():
            raise forms.ValidationError('The code should be digit only!')
        return new_code

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        if not email.endswith("dut.udn.vn"):
            raise forms.ValidationError(
                'The email should be end with dut.udn.vn!')
        return email
