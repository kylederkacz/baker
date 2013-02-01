# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'DlnaSettings'
        db.create_table('www_dlnasettings', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('version', self.gf('django.db.models.fields.IntegerField')()),
            ('server_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('port', self.gf('django.db.models.fields.IntegerField')()),
            ('model_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('model_number', self.gf('django.db.models.fields.IntegerField')()),
            ('serial', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('album_art', self.gf('django.db.models.fields.TextField')()),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('www', ['DlnaSettings'])

        # Adding model 'Collection'
        db.create_table('www_collection', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('www', ['Collection'])


    def backwards(self, orm):
        # Deleting model 'DlnaSettings'
        db.delete_table('www_dlnasettings')

        # Deleting model 'Collection'
        db.delete_table('www_collection')


    models = {
        'www.collection': {
            'Meta': {'object_name': 'Collection'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'www.dlnasettings': {
            'Meta': {'object_name': 'DlnaSettings'},
            'album_art': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'model_number': ('django.db.models.fields.IntegerField', [], {}),
            'port': ('django.db.models.fields.IntegerField', [], {}),
            'serial': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'server_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'version': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['www']