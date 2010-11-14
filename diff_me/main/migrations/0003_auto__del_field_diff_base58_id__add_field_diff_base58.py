# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Diff.base58_id'
        db.delete_column('main_diff', 'base58_id')

        # Adding field 'Diff.base58'
        db.add_column('main_diff', 'base58', self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Adding field 'Diff.base58_id'
        db.add_column('main_diff', 'base58_id', self.gf('django.db.models.fields.CharField')(default=0, max_length=50), keep_default=False)

        # Deleting field 'Diff.base58'
        db.delete_column('main_diff', 'base58')


    models = {
        'main.diff': {
            'Meta': {'object_name': 'Diff'},
            'base58': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'modified': ('django.db.models.fields.TextField', [], {}),
            'modified_revision': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'original': ('django.db.models.fields.TextField', [], {}),
            'original_revision': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Diff']"}),
            'private': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['main']
