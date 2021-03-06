# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('country', models.SmallIntegerField(default=2, choices=[(1, b'Nigeria'), (2, b'Kenya')])),
                ('location', models.SmallIntegerField(default=84, choices=[(1, b'Abia'), (2, b'Abuja'), (3, b'Adamawa'), (4, b'Akwa Ibom'), (5, b'Anambra'), (6, b'Bauchi'), (7, b'Bayelsa'), (8, b'Benue'), (9, b'Borno'), (10, b'Cross River'), (11, b'Delta'), (12, b'Ebonyi'), (13, b'Edo'), (14, b'Ekiti'), (15, b'Enugu'), (16, b'Gombe'), (17, b'Imo'), (18, b'Jigawa'), (19, b'Kaduna'), (20, b'Kano'), (21, b'Katsina'), (22, b'Kebbi'), (23, b'Kogi'), (24, b'Kwara'), (25, b'Lagos'), (26, b'Nassarawa'), (27, b'Niger'), (28, b'Ogun'), (29, b'Ondo'), (30, b'Osun'), (31, b'Oyo'), (32, b'Plateau'), (33, b'Rivers'), (34, b'Sokoto'), (35, b'Taraba'), (36, b'Yobe'), (37, b'Zamfara'), (38, b'Mombasa'), (39, b'Kwale'), (40, b'Kilifi'), (41, b'Tana River'), (42, b'Lamu'), (43, b'Taita-Taveta'), (44, b'Garissa'), (45, b'Wajir'), (46, b'Mandera'), (47, b'Marsabit'), (48, b'Isiolo'), (49, b'Meru'), (50, b'Tharaka-Nithi'), (51, b'Embu'), (52, b'Kitui'), (53, b'Machakos'), (54, b'Makueni'), (55, b'Nyandarua'), (56, b'Nyeri'), (57, b'Kirinyaga'), (58, b"Murang'a"), (59, b'Kiambu'), (60, b'Turkana'), (61, b'West Pokot'), (62, b'Samburu'), (63, b'Trans-Nzoia'), (64, b'Uasin Gishu'), (65, b'Elgeyo-Marakwet'), (66, b'Nandi'), (67, b'Baringo'), (68, b'Laikipia'), (69, b'Nakuru'), (70, b'Narok'), (71, b'Kajiado'), (72, b'Kericho'), (73, b'Bomet'), (74, b'Kakamega'), (75, b'Vihiga'), (76, b'Bungoma'), (77, b'Busia'), (78, b'Siaya'), (79, b'Kisumu'), (80, b'Homa Bay'), (81, b'Migori'), (82, b'Kisii'), (83, b'Nyamira'), (84, b'Nairobi')])),
                ('occupation', models.TextField(default=b'', blank=True)),
                ('phonenumber', models.CharField(default=b'', max_length=20, blank=True)),
                ('intlnumber', models.CharField(default=b'', max_length=20, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
