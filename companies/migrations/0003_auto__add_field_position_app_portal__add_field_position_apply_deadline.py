# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Position.app_portal'
        db.add_column(u'companies_position', 'app_portal',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=500, blank=True),
                      keep_default=False)

        # Adding field 'Position.apply_deadline'
        db.add_column(u'companies_position', 'apply_deadline',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)


        # Changing field 'Position.start_date'
        db.alter_column(u'companies_position', 'start_date', self.gf('django.db.models.fields.DateField')(null=True))

    def backwards(self, orm):
        # Deleting field 'Position.app_portal'
        db.delete_column(u'companies_position', 'app_portal')

        # Deleting field 'Position.apply_deadline'
        db.delete_column(u'companies_position', 'apply_deadline')


        # Changing field 'Position.start_date'
        db.alter_column(u'companies_position', 'start_date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2013, 10, 29, 0, 0)))

    models = {
        u'companies.company': {
            'Meta': {'object_name': 'Company'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'companies.contact': {
            'Meta': {'object_name': 'Contact'},
            'company': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['companies.Company']", 'null': 'True', 'symmetrical': 'False'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        },
        u'companies.position': {
            'Meta': {'object_name': 'Position'},
            'app_portal': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'apply_deadline': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['companies.Company']"}),
            'date_noted': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['companies']