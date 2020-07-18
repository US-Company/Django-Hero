import uuid as uuid_lib #pip install uuid
# from django.utils.encoding import python_2_unicode_compatible
from django.db import models

# Create your models here

#@python_2_unicode_compatible # For Python 3.5+ and 2.7
class Table(models.Model):
    id = models.UUIDField(
        db_index=True, default=uuid_lib.uuid4, editable=False, unique=True,
        primary_key=True
    )
    name_table = models.CharField(max_length=255)
    background_table = models.ImageField(upload_to='media')

    def __str__(self):
        return str(self.name_table)

    #def get_absolute_url(self):
        #return reverse('name_url', kwargs={'pk': self.pk})

    class Meta:
        #abstract = True
        ordering = ['name_table',]
        verbose_name_plural = 'Table'

#@python_2_unicode_compatible # For Python 3.5+ and 2.7
class Color(models.Model):
    uuid = models.UUIDField(db_index=True, default=uuid_lib.uuid4, editable=False)
    name_color = models.CharField(max_length=255)
    code_color = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name_color)

    #def get_absolute_url(self):
        #return reverse('name_url', kwargs={'pk': self.pk})

    class Meta:
        #abstract = True
        ordering = ['name_color',]
        verbose_name_plural = 'Colors'

#@python_2_unicode_compatible # For Python 3.5+ and 2.7
class Label(models.Model):
    uuid = models.UUIDField(db_index=True, default=uuid_lib.uuid4, editable=False)
    name_label = models.CharField(max_length=255)
    color_label = models.ForeignKey(Color, on_delete=models.CASCADE, \
                                  related_name='color_label')

    def __str__(self):
        return str(self.name_label)

    #def get_absolute_url(self):
        #return reverse('name_url', kwargs={'pk': self.pk})

    class Meta:
        #abstract = True
        ordering = ['name_label',]
        verbose_name_plural = 'Label'


#@python_2_unicode_compatible # For Python 3.5+ and 2.7
class CheckList(models.Model):
    uuid = models.UUIDField(db_index=True, default=uuid_lib.uuid4, editable=False)
    name_checklist = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name_checklist)

    #def get_absolute_url(self):
        #return reverse('name_url', kwargs={'pk': self.pk})

    class Meta:
        #abstract = True
        ordering = ['name_checklist',]
        verbose_name_plural = 'CheckList'

#@python_2_unicode_compatible # For Python 3.5+ and 2.7
class Item(models.Model):
    uuid = models.UUIDField(db_index=True, default=uuid_lib.uuid4, editable=False)
    name_item = models.CharField(max_length=255)
    check_item = models.BooleanField(default=False)
    list_item = models.ForeignKey(Table, on_delete=models.CASCADE, \
                                  related_name='ReName')

    def __str__(self):
        return str(self.name_item)

    #def get_absolute_url(self):
        #return reverse('name_url', kwargs={'pk': self.pk})

    class Meta:
        #abstract = True
        ordering = ['name_item',]
        verbose_name_plural = 'Item'


