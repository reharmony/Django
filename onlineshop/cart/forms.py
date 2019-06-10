from django import forms # 폼을 만드는 클래스

class AddProductForm(forms.Form):
    quantity = forms.IntegerField()
    is_update = forms.BooleanField(required = False,
                                   initial = False, widget = forms.HiddenInput)
    # 넘길 값으로 폼 안에 넣어야 하는데 화면에는 숨기고 싶을 때 HiddenInput사용
    # HTML에서는 <input type="hidden"> 방식으로 숨김

