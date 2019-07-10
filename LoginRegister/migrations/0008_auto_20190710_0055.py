# Generated by Django 2.1.10 on 2019-07-10 00:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LoginRegister', '0007_auto_20190709_2057'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['-c_time'], 'verbose_name': '云盘用户', 'verbose_name_plural': '云盘用户'},
        ),
        migrations.AlterField(
            model_name='confirmstring',
            name='c_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='认证时间'),
        ),
        migrations.AlterField(
            model_name='confirmstring',
            name='code',
            field=models.CharField(max_length=256, verbose_name='确认码'),
        ),
        migrations.AlterField(
            model_name='confirmstring',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='LoginRegister.User', verbose_name='认证用户'),
        ),
        migrations.AlterField(
            model_name='user',
            name='c_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='注册时间'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='邮箱'),
        ),
        migrations.AlterField(
            model_name='user',
            name='has_confiremed',
            field=models.BooleanField(default=False, verbose_name='验证状态'),
        ),
        migrations.AlterField(
            model_name='user',
            name='imgpath',
            field=models.CharField(default='moren/moren123.jpg', max_length=80, verbose_name='头像'),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=128, unique=True, verbose_name='用户名'),
        ),
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(max_length=128, verbose_name='昵称'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=256, verbose_name='密码'),
        ),
        migrations.AlterField(
            model_name='user',
            name='uid',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='id'),
        ),
    ]
