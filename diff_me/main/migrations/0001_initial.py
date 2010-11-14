# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Diff'
        db.create_table('main_diff', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('base58_id', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('original', self.gf('django.db.models.fields.TextField')()),
            ('original_revision', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('modified', self.gf('django.db.models.fields.TextField')()),
            ('modified_revision', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('private', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Diff'])),
        ))
        db.send_create_signal('main', ['Diff'])


    def backwards(self, orm):
        
        # Deleting model 'Diff'
        db.delete_table('main_diff')


    models = {
        'main.diff': {
            'Meta': {'object_name': 'Diff'},
            'base58_id': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
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
