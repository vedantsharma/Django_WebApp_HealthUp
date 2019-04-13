from django.db import models

class Prescription(models.Model):
    title = models.CharField(max_length=100)
    patient = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='prescription/pdfs/')
    cover = models.ImageField(upload_to='prescription/covers/', null=True, blank=True)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.pdf.delete()
        self.cover.delete()
        super(self).delete(*args, **kwargs)

