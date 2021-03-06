from django import forms
from django.forms import ModelForm
from. models import *

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = [
            'r_number',
            'r_name',
            'seating_capacity'
        ]
    def clean(self):
        cleaned_data = self.cleaned_data
        r_number = cleaned_data.get('r_number')
        r_name = cleaned_data.get('r_name')
        qs = Room.objects.filter(r_number__iexact=r_number)
        qs1 = Room.objects.filter(r_name__iexact=r_name)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
            qs1 = qs1.exclude(pk=self.instance.pk)
        if qs.exists() or qs1.exists():
            raise forms.ValidationError("This Room already exists.")
        return cleaned_data

class InstructorForm(ModelForm):
    class Meta:
        model = Instructors
        fields = [
            'Ins_id',
            'Ins_name'
        ]
    def clean(self):
        cleaned_data = self.cleaned_data
        Ins_id = cleaned_data.get('Ins_id')
        qs = Instructors.objects.filter(Ins_id__iexact=Ins_id)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError("This Instructor already exists.")
        return cleaned_data
        
class SubjectForm(ModelForm):
    class Meta:
        model = Subject
        fields = ['sj_id', 'sj_name', 'sj_ins','max_numb_students']

    def clean(self):
        cleaned_data = self.cleaned_data
        sj_id = cleaned_data.get('sj_id')
        sj_name = cleaned_data.get('sj_name')
        qs = Subject.objects.filter(sj_id__iexact=sj_id)
        qs1 = Subject.objects.filter(sj_name__iexact=sj_name)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
            qs1 = qs1.exclude(pk=self.instance.pk)
        if qs.exists() or qs1.exists():
            raise forms.ValidationError("This Subject already exists.")
        return cleaned_data
        

class ShiftForm(ModelForm):
    class Meta:
        model = Shift
        fields = ['sid','time','day']

    def clean(self):
        cleaned_data = self.cleaned_data
        sid = cleaned_data.get('sid')
        time = cleaned_data.get('time')
        day = cleaned_data.get('day')
        qs = Shift.objects.filter(sid__iexact=sid)
        qs1 = Shift.objects.filter(time__iexact=time)
        qs2 = Shift.objects.filter(day__iexact=day)
        if self.instance:  # not sure if it should be self.instance.pk
            qs = qs.exclude(pk=self.instance.pk)
            qs1 = qs1.exclude(pk=self.instance.pk)
            qs1 = qs1.exclude(pk=self.instance.pk)
        if qs.exists() and qs1.exists() and qs2.exists():
            raise forms.ValidationError("This Shift already exists.")

        """ This is the form's clean method, not a particular field's clean method """
        time = cleaned_data.get("time")
        day = cleaned_data.get("day")
        if Shift.objects.filter(time=time, day=day).count() > 0:
           del cleaned_data["time"]
           del cleaned_data["day"]
           raise forms.ValidationError("Time and Day combination already exists.")
        return cleaned_data

class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = ['dept_name', 'subjects']

    def clean(self):
        cleaned_data = self.cleaned_data
        dept_name = cleaned_data.get('dept_name')
        qs = Department.objects.filter(dept_name__iexact=dept_name)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError("This department already exists.")
        return cleaned_data

class SectionForm(ModelForm):
    class Meta:
        model = Section
        fields = ['section_id', 'department', 'classes_in_week']
    def clean(self):
        cleaned_data = self.cleaned_data
        section_id = cleaned_data.get('section_id')
        department = cleaned_data.get('department')
        qs = Section.objects.filter(section_id__iexact=section_id)
        qs1 = Section.objects.filter(department__dept_name__iexact=department)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
            qs1 = qs1.exclude(pk=self.instance.pk)
            print(qs,qs1)
        if qs.exists() and qs1.exists():
            raise forms.ValidationError("This section already exists.")
        print('Cleaned data: ',cleaned_data)
        return cleaned_data
