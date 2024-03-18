# Generated by Django 4.2.11 on 2024-03-16 16:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('coparentbot', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parentingplan',
            name='parent1_name',
        ),
        migrations.RemoveField(
            model_name='parentingplan',
            name='parent2_name',
        ),
        migrations.AddField(
            model_name='conversation',
            name='moderator_response',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='changerequest',
            name='parenting_plan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='coparentbot.parentingplan'),
        ),
        migrations.AlterField(
            model_name='conflictscore',
            name='parenting_plan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='coparentbot.parentingplan'),
        ),
        migrations.AlterField(
            model_name='conversation',
            name='parenting_plan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='coparentbot.parentingplan'),
        ),
        migrations.AlterField(
            model_name='demeritpoint',
            name='parenting_plan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='coparentbot.parentingplan'),
        ),
        migrations.AlterField(
            model_name='visitation',
            name='parenting_plan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='coparentbot.parentingplan'),
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='conversation',
            name='intended_parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='intended_messages', to='coparentbot.parent'),
        ),
        migrations.AddField(
            model_name='parentingplan',
            name='parent1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent1_plans', to='coparentbot.parent'),
        ),
        migrations.AddField(
            model_name='parentingplan',
            name='parent2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent2_plans', to='coparentbot.parent'),
        ),
        migrations.AlterField(
            model_name='conversation',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='coparentbot.parent'),
        ),
        migrations.AlterField(
            model_name='demeritpoint',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent_points', to='coparentbot.parent'),
        ),
    ]