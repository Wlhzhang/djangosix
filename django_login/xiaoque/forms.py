from django import forms

from xiaoque.models import AddTask


class TaskForm(forms.ModelForm):
    class Meta:
        model = AddTask
        fields = (
            'task_id',
            'task_name',
            'inspect_line',
            'inspect_user',
            'state',
            'pole_beg',
            'pole_end',
            'df_username',
            'df_date',
        )