import re
from django.db import models
from django.contrib import admin


COLLECTION_TYPES = (
    ('V', 'Videos'),
    ('A', 'Audio'),
    ('P', 'Pictures'),
)


class DlnaSettings(models.Model):
    version = models.IntegerField()
    friendly_name = models.CharField(max_length=50, help_text="Name that the DLNA server presents to clients.", verbose_name="Server Name")
    port = models.IntegerField(verbose_name="Server Port")
    model_name = models.CharField(max_length=50, help_text="Server model name that is reported to clients.")
    model_number = models.IntegerField(help_text="Server model number that is reported to clients.")
    serial = models.CharField(max_length=50, help_text="Serial number the server reports to clients.")
    album_art_names = models.TextField(help_text="List of file names to look for when searching for album art. Names should be delimited with a forward slash (\"/\").")
    created = models.DateTimeField(auto_now_add=True)
    hash_id = models.CharField(max_length=32)

    _settings_file = '/Users/kylederkacz/minidlna.conf'
    _line_regex = r'^\s*\#?\s*([\w\_]+)\s*=\s*(.*)$\n'

    def load_settings(self):
        with open(self._settings_file, 'r') as f:
            settings = re.findall(self._line_regex, f.read(), re.MULTILINE)
            for setting, value in settings:
                if hasattr(self, setting):
                    setattr(self, setting, value)

    def save_settings(self):
        pass

    def has_changed(self):
        pass


class Collection(models.Model):
    type = models.CharField(max_length=20, choices=COLLECTION_TYPES)
    label = models.CharField(max_length=20, help_text="An internal label that is used to help you identify the collection. This value is not sent to the client.", null=True)
    location = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "{0} ({1})".format(self.location, self.type)

    _settings_file = '/Users/kylederkacz/minidlna.conf'
    # media_dir=V,/media/Media/Movies
    _line_regex = r'^\s*media\_dir\s*=\s*([APV]),(.*)$\n'

    @classmethod
    def load_collections(cls):
        collections = []
        with open(cls._settings_file, 'r') as f:
            settings = re.findall(cls._line_regex, f.read(), re.MULTILINE)
            for type, location in settings:
                collections.append(Collection(type=type, location=location))
        return collections


class Drive(models.Model):
    uuid = models.CharField(max_length=50)
    location = models.CharField(max_length=25)
    file_system = models.CharField(max_length=20)
    label = models.CharField(max_length=100, null=True)


admin.site.register(DlnaSettings)
admin.site.register(Collection)
