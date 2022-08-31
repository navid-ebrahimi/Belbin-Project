from import_export import resources
from .models import *

class QuestionResource(resources.ModelResource):
    class meta:
        model = Questions

class OptionsResource(resources.ModelResource):
    class meta:
        model = Options