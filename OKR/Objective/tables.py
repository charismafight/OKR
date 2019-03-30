import django_tables2 as tables
from django_tables2.utils import A
from .models import Objective


class ObjectiveTable(tables.Table):
    class Meta:
        model = Objective
        template_name = 'django_tables2/bootstrap.html'

    # link columns parameter means url name
    key_result = tables.LinkColumn('key_result_detail', args=[A('pk')])
    id = tables.LinkColumn('key_result_detail', args=[A('pk')])
