# Generated by Django 3.1.3 on 2021-04-06 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('desc', models.CharField(max_length=500, verbose_name='用例描述')),
                ('code', models.TextField(max_length=30000, verbose_name='代码')),
                ('creator_nickname', models.CharField(max_length=64, verbose_name='创建人昵称')),
                ('project_id', models.IntegerField(verbose_name='项目id')),
            ],
            options={
                'db_table': 'case',
            },
        ),
        migrations.CreateModel(
            name='CaseResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('case_id', models.IntegerField(verbose_name='用例id')),
                ('result', models.CharField(max_length=50, verbose_name='运行结果')),
                ('elapsed', models.CharField(max_length=50, verbose_name='耗时')),
                ('output', models.TextField(default='', verbose_name='输出日志')),
                ('run_env', models.CharField(max_length=20, verbose_name='运行环境')),
                ('run_user_nickname', models.CharField(max_length=64, verbose_name='运行用户昵称')),
                ('run_time', models.DateTimeField(auto_now=True, verbose_name='运行时间')),
            ],
            options={
                'db_table': 'case_result',
            },
        ),
        migrations.CreateModel(
            name='Fixture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('name', models.CharField(max_length=100, verbose_name='fixture名称')),
                ('desc', models.CharField(default='', max_length=500, verbose_name='fixture描述')),
                ('code', models.TextField(max_length=30000, verbose_name='代码')),
                ('creator_nickname', models.CharField(max_length=64, verbose_name='创建人昵称')),
                ('project_id', models.IntegerField(verbose_name='项目id')),
            ],
            options={
                'db_table': 'fixture',
            },
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='测试计划名称')),
                ('project_id', models.IntegerField(verbose_name='项目id')),
            ],
            options={
                'db_table': 'plan',
            },
        ),
        migrations.CreateModel(
            name='PlanCase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_id', models.IntegerField(max_length=50, verbose_name='测试计划id')),
                ('case_id', models.IntegerField(verbose_name='用例id')),
            ],
            options={
                'db_table': 'plan_case',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='项目名称')),
                ('env_config', models.CharField(max_length=100, verbose_name='环境配置')),
            ],
            options={
                'db_table': 'project',
            },
        ),
        migrations.CreateModel(
            name='EnvVar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('name', models.CharField(max_length=50, verbose_name='变量名')),
                ('value', models.CharField(max_length=100, verbose_name='变量值')),
                ('desc', models.CharField(default='', max_length=200, verbose_name='描述')),
                ('project_id', models.IntegerField(verbose_name='项目id')),
                ('env_name', models.CharField(max_length=20, verbose_name='环境名称')),
            ],
            options={
                'db_table': 'env_var',
                'unique_together': {('project_id', 'env_name', 'name')},
            },
        ),
    ]