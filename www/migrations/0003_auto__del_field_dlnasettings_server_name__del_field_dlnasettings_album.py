# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'DlnaSettings.server_name'
        db.delete_column('www_dlnasettings', 'server_name')

        # Deleting field 'DlnaSettings.album_art'
        db.delete_column('www_dlnasettings', 'album_art')

        # Adding field 'DlnaSettings.friendly_name'
        db.add_column('www_dlnasettings', 'friendly_name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50),
                      keep_default=False)

        # Adding field 'DlnaSettings.album_art_names'
        db.add_column('www_dlnasettings', 'album_art_names',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)

        # Adding field 'DlnaSettings.hash_id'
        db.add_column('www_dlnasettings', 'hash_id',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=32),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'DlnaSettings.server_name'
        db.add_column('www_dlnasettings', 'server_name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50),
                      keep_default=False)

        # Adding field 'DlnaSettings.album_art'
        db.add_column('www_dlnasettings', 'album_art',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)

        # Deleting field 'DlnaSettings.friendly_name'
        db.delete_column('www_dlnasettings', 'friendly_name')

        # Deleting field 'DlnaSettings.album_art_names'
        db.delete_column('www_dlnasettings', 'album_art_names')

        # Deleting field 'DlnaSettings.hash_id'
        db.delete_column('www_dlnasettings', 'hash_id')


    models = {
        'www.collection': {
            'Meta': {'object_name': 'Collection'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'www.dlnasettings': {
            'Meta': {'object_name': 'DlnaSettings'},
            'album_art_names': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'friendly_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'hash_id': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'model_number': ('django.db.models.fields.IntegerField', [], {}),
            'port': ('django.db.models.fields.IntegerField', [], {}),
            'serial': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'version': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['www']