from django import forms


class GetListed(forms.Form):
    name = forms.CharField(
        label="Business Name"
    )
    description = forms.CharField(
        widget=forms.Textarea,
        label="Description",
        required=False
    )
    address1 = forms.CharField(
        label="Address Line 1"
    )
    address2 = forms.CharField(
        label="Address Line 2",
        required=False
    )
    town = forms.CharField(
        label="Town",
        required=False
    )
    open_time = forms.TimeField(
        label="Opening Time",
        required=False
    )
    close_time = forms.TimeField(
        label="Closing Time",
        required=False
    )
    contact1 = forms.CharField(
        label="Contact Name 1",
        required=False
    )
    phone1 = forms.CharField(
        max_length=12,
        label="Phone Number 1",
        required=False
    )
    contact2 = forms.CharField(
        label="Contact Name 2",
        required=False
    )
    phone2 = forms.CharField(
        max_length=12,
        label="Phone Number 2",
        required=False
    )
    latitude = forms.FloatField(
        label="Latitude",
        required=False
    )
    longitude = forms.FloatField(
        label="Longitude",
        required=False
    )
    CARDINAL_POINTS = (
        ('None', 'None'),
        ('North', 'North'),
        ('East', 'East'),
        ('South', 'South'),
        ('West', 'West'),
        ('Central', 'Central')
    )
    cardinal_point = forms.ChoiceField(
        choices=CARDINAL_POINTS,
        required=False
    )
    email = forms.EmailField(
        label="Email",
        required=False
    )
    website = forms.URLField(
        label="Website",
        required=False
    )
    facebook = forms.URLField(
        label="Facebook",
        required=False
    )
    notes = forms.CharField(
        label="Notes",
        widget=forms.Textarea,
        required=False
    )
