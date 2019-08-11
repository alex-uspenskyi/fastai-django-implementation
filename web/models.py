from django.db import models
from django.contrib.postgres.fields import JSONField
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.utils.text import slugify
from django.db import models
from datetime import datetime
from PIL import Image
from io import BytesIO
import sys, os

class Request(models.Model):
    photo = models.ImageField(upload_to='uploads/%Y/%m/')
    ip = models.GenericIPAddressField()
    date = models.DateTimeField(default=datetime.now)
    scores = JSONField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            name, extension = os.path.splitext(self.photo.name)
            im = Image.open(self.photo)
            if not im.mode == 'RGB':
                im = im.convert('RGB')
            output = BytesIO()
            im.thumbnail( (800,800) )
            im.save(output, format='JPEG', quality=90)
            output.seek(0)
            self.photo = InMemoryUploadedFile(output,'ImageField', "%s.jpg" %slugify(name), 'image/jpeg', sys.getsizeof(output), None)
    
        super(Request, self).save(*args, **kwargs)