# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Collection.type'
        db.add_column('www_collection', 'type',
                      self.gf('django.db.models.fields.CharField')(default='V', max_length=20),
                      keep_default=False)

        # Adding field 'Collection.label'
        db.add_column('www_collection', 'label',
                      self.gf('django.db.models.fields.CharField')(max_length=20, null=True),
                      keep_default=False)

        # Adding field 'Collection.location'
        db.add_column('www_collection', 'location',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255),
                      keep_default=False)

        # Adding field 'Collection.created'
        db.add_column('www_collection', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2013, 1, 21, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Collection.edited'
        db.add_column('www_collection', 'edited',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2013, 1, 21, 0, 0), blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Collection.type'
        db.delete_column('www_collection', 'type')

        # Deleting field 'Collection.label'
        db.delete_column('www_collection', 'label')

        # Deleting field 'Collection.location'
        db.delete_column('www_collection', 'location')

        # Deleting field 'Collection.created'
        db.delete_column('www_collection', 'created')

        # Deleting field 'Collection.edited'
        db.delete_column('www_collection', 'edited')


    models = {
        'www.collection': {
            'Meta': {'object_name': 'Collection'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'edited': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '20'})
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