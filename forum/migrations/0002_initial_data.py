from __future__ import unicode_literals
from django.db import migrations
from django.utils.text import slugify


def initial_topic(apps, schema_editor):
    topic = apps.get_model(app_label='forum', model_name='Topic')

    topic(author='John',
          subject='I like this forum!',
          slug=slugify('I like this forum!'),
          topic_message='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent id commodo turpis.'
                        ' Phasellus at congue ipsum. Aliquam congue mi at faucibus porttitor. Sed lectus magna, luctus'
                        ' ac felis a, ultricies tincidunt massa. Etiam sit amet convallis orci, eu pellentesque nisi.'
                        ' Pellentesque eu egestas arcu. Curabitur venenatis pulvinar diam, at ullamcorper nisi pharetra'
                        ' eleifend. '
          ).save()

    topic(author='Adam',
          subject='Where is course!',
          slug=slugify('Dude where is my course!'),
          topic_message='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent id commodo turpis.'
                        ' Phasellus at congue ipsum. Aliquam congue mi at faucibus porttitor. Sed lectus magna, luctus'
                        ' ac felis a, ultricies tincidunt massa. Etiam sit amet convallis orci, eu pellentesque nisi.'
                        ' Pellentesque eu egestas arcu. Curabitur venenatis pulvinar diam, at ullamcorper nisi pharetra'
                        ' eleifend. '
          ).save()

    topic(author='Kate',
          subject='about my account',
          slug=slugify('about my account'),
          topic_message='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent id commodo turpis.'
                        ' Phasellus at congue ipsum. Aliquam congue mi at faucibus porttitor. Sed lectus magna, luctus'
                        ' ac felis a, ultricies tincidunt massa. Etiam sit amet convallis orci, eu pellentesque nisi.'
                        ' Pellentesque eu egestas arcu. Curabitur venenatis pulvinar diam, at ullamcorper nisi pharetra'
                        ' eleifend. '
          ).save()

    topic(author='Pete',
          subject='What is going on?',
          slug=slugify('What is going on?'),
          topic_message='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent id commodo turpis.'
                        ' Phasellus at congue ipsum. Aliquam congue mi at faucibus porttitor. Sed lectus magna, luctus'
                        ' ac felis a, ultricies tincidunt massa. Etiam sit amet convallis orci, eu pellentesque nisi.'
                        ' Pellentesque eu egestas arcu. Curabitur venenatis pulvinar diam, at ullamcorper nisi pharetra'
                        ' eleifend. '
          ).save()

    topic(author='Leon',
          subject='Email not working',
          slug=slugify('Email not working'),
          topic_message='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent id commodo turpis.'
                        ' Phasellus at congue ipsum. Aliquam congue mi at faucibus porttitor. Sed lectus magna, luctus'
                        ' ac felis a, ultricies tincidunt massa. Etiam sit amet convallis orci, eu pellentesque nisi.'
                        ' Pellentesque eu egestas arcu. Curabitur venenatis pulvinar diam, at ullamcorper nisi pharetra'
                        ' eleifend. '
          ).save()


    topic(author='Layla',
          subject='Course start date',
          slug=slugify('Course start date'),
          topic_message='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent id commodo turpis.'
                        ' Phasellus at congue ipsum. Aliquam congue mi at faucibus porttitor. Sed lectus magna, luctus'
                        ' ac felis a, ultricies tincidunt massa. Etiam sit amet convallis orci, eu pellentesque nisi.'
                        ' Pellentesque eu egestas arcu. Curabitur venenatis pulvinar diam, at ullamcorper nisi pharetra'
                        ' eleifend. '
          ).save()


class Migration(migrations.Migration):
    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(initial_topic)
    ]
