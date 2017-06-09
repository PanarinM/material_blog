from django.db import models
from solo.models import SingletonModel
from redactor.fields import RedactorField
from utils import get_file_path


class Core(SingletonModel):
    logo = models.ImageField(upload_to=get_file_path)
    footer = RedactorField()
    about = RedactorField()