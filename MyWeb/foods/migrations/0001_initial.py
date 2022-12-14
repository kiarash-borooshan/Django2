# Generated by Django 3.2.8 on 2022-08-08 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100, verbose_name='نام غذا')),
                ('Description', models.CharField(max_length=50, verbose_name='توضیحات')),
                ('Rate', models.IntegerField(verbose_name='امتیاز')),
                ('Price', models.BigIntegerField(verbose_name='قیمت')),
                ('Time', models.IntegerField(verbose_name='زمان لازم')),
                ('Pub_date', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ')),
                ('Photo', models.ImageField(upload_to='foods/image/', verbose_name='تصویر')),
            ],
        ),
    ]
