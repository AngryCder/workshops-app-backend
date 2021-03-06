# Generated by Django 2.2.6 on 2020-02-11 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0009_remove_userprofile_is_admin'),
        ('workshop', '0010_auto_20200211_0929'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='council',
            name='joint_secy',
        ),
        migrations.RemoveField(
            model_name='council',
            name='secy',
        ),
        migrations.AddField(
            model_name='council',
            name='gensec',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='council_gensec', to='authentication.UserProfile', verbose_name='General Secretary'),
        ),
        migrations.AddField(
            model_name='council',
            name='joint_gensec',
            field=models.ManyToManyField(blank=True, related_name='council_joint_gensec', to='authentication.UserProfile', verbose_name='Joint General Secretary'),
        ),
        migrations.AlterField(
            model_name='club',
            name='joint_secy',
            field=models.ManyToManyField(blank=True, related_name='club_joint_secy', to='authentication.UserProfile', verbose_name='Joint Secretary'),
        ),
        migrations.AlterField(
            model_name='club',
            name='secy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='club_secy', to='authentication.UserProfile', verbose_name='Secretary'),
        ),
    ]
