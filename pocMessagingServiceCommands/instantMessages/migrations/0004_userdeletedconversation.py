# Generated by Django 4.2.4 on 2023-08-26 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instantMessages', '0003_userremovedparticipanttoconversation_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDeletedConversation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=100)),
                ('conversation_id', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
