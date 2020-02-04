# Generated by Django 2.1.2 on 2020-02-03 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LMS', '0003_auto_20200203_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='Designation',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Employee', 'Employee'), ('Manager', 'Manager'), ('HR', 'HR'), ('Permanent', 'Permanent'), ('Probationary', 'Probationary'), ('Limited_term', 'Limited-term'), ('Temporary', 'Temporary')], max_length=10),
        ),
        migrations.AlterField(
            model_name='employee',
            name='Gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Employee', 'Employee'), ('Manager', 'Manager'), ('HR', 'HR'), ('Permanent', 'Permanent'), ('Probationary', 'Probationary'), ('Limited_term', 'Limited-term'), ('Temporary', 'Temporary')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='Worktype',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Employee', 'Employee'), ('Manager', 'Manager'), ('HR', 'HR'), ('Permanent', 'Permanent'), ('Probationary', 'Probationary'), ('Limited_term', 'Limited-term'), ('Temporary', 'Temporary')], max_length=15),
        ),
    ]
