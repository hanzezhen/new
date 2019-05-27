# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2019-05-27 07:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='equipment',
            fields=[
                ('eid', models.AutoField(primary_key=True, serialize=False, verbose_name='编号')),
                ('ename', models.CharField(max_length=50, verbose_name='设备名')),
                ('eshiyanshi', models.CharField(max_length=50, verbose_name='实验室')),
                ('eguanliyuan', models.CharField(max_length=50, verbose_name='管理人')),
                ('ezhuangtai', models.CharField(max_length=20, verbose_name='状态')),
                ('exianshi', models.DecimalField(decimal_places=1, default=100.0, max_digits=10, verbose_name='限时')),
                ('ejieshao1', models.CharField(blank=True, max_length=500, verbose_name='介绍第一段')),
                ('ejieshao2', models.CharField(blank=True, max_length=500, verbose_name='介绍第二段')),
                ('ejieshao3', models.CharField(blank=True, max_length=500, verbose_name='介绍第三段')),
            ],
            options={
                'verbose_name_plural': '设备',
                'verbose_name': '设备',
                'db_table': 'equipment',
            },
        ),
        migrations.CreateModel(
            name='quanxian',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qeid', models.ForeignKey(db_column='qeid', on_delete=django.db.models.deletion.PROTECT, to='myapp.equipment', verbose_name='设备')),
            ],
            options={
                'verbose_name_plural': '权限',
                'verbose_name': '权限',
                'db_table': 'quanxian',
            },
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('spk', models.AutoField(primary_key=True, serialize=False, verbose_name='编号')),
                ('sid', models.CharField(max_length=30, unique=True, verbose_name='用户名')),
                ('sname', models.CharField(max_length=20, verbose_name='姓名')),
                ('semail', models.CharField(blank=True, max_length=50, verbose_name='邮箱')),
                ('stelephone', models.CharField(blank=True, max_length=30, verbose_name='电话')),
                ('isshenhe', models.BooleanField(default=False, verbose_name='已审')),
                ('time', models.DateField(default=django.utils.timezone.now, verbose_name='注册时间')),
                ('password', models.CharField(max_length=50, verbose_name='密码')),
                ('time_use', models.DecimalField(decimal_places=1, default=0.0, max_digits=10, verbose_name='用时')),
                ('istongguo', models.BooleanField(default=False, verbose_name='审核通过')),
                ('isstudent', models.BooleanField(default=True, verbose_name='是否组内')),
            ],
            options={
                'verbose_name_plural': '学生',
                'verbose_name': '学生',
                'db_table': 'student',
            },
        ),
        migrations.CreateModel(
            name='teacher',
            fields=[
                ('tid', models.AutoField(primary_key=True, serialize=False, verbose_name='编号')),
                ('tname', models.CharField(max_length=20, verbose_name='姓名')),
                ('temail', models.CharField(blank=True, max_length=50, verbose_name='邮箱')),
                ('ttelephone', models.CharField(blank=True, max_length=30, verbose_name='电话')),
            ],
            options={
                'verbose_name_plural': '老师',
                'verbose_name': '老师',
                'db_table': 'teacher',
            },
        ),
        migrations.CreateModel(
            name='weiyuecishu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=0, verbose_name='违约次数')),
                ('ysid', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='myapp.student')),
            ],
            options={
                'verbose_name_plural': '违约次数',
                'verbose_name': '违约次数',
                'db_table': 'weiyue',
            },
        ),
        migrations.CreateModel(
            name='xitongxinxi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yuyueshichang', models.IntegerField(default=14, verbose_name='预约提前天数')),
                ('quxiaoyuyue', models.IntegerField(default=1, verbose_name='取消预约提前')),
            ],
            options={
                'verbose_name_plural': '系统信息',
                'verbose_name': '系统信息',
                'db_table': 'xitongxinxi',
            },
        ),
        migrations.CreateModel(
            name='yuyue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ydate', models.DateField(verbose_name='预约日期')),
                ('ytimestart', models.CharField(max_length=30, verbose_name='开始时间')),
                ('shichang', models.DecimalField(decimal_places=1, max_digits=5, verbose_name='时长')),
                ('yuyuebeizhu', models.CharField(blank=True, max_length=200, verbose_name='备注')),
                ('shiyanfankui', models.CharField(blank=True, max_length=200, verbose_name='实验反馈')),
                ('isqiandao', models.BooleanField(default=False, verbose_name='违约')),
                ('yeid', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='myapp.equipment')),
                ('ysid', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='myapp.student')),
            ],
            options={
                'verbose_name_plural': '预约',
                'verbose_name': '预约',
                'db_table': 'yuyue',
            },
        ),
        migrations.AddField(
            model_name='student',
            name='steacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='myapp.teacher', verbose_name='老师'),
        ),
        migrations.AddField(
            model_name='quanxian',
            name='qsid',
            field=models.ForeignKey(db_column='qsid', on_delete=django.db.models.deletion.PROTECT, to='myapp.student', verbose_name='学生'),
        ),
        migrations.AlterUniqueTogether(
            name='quanxian',
            unique_together=set([('qsid', 'qeid')]),
        ),
    ]
