"""
Definition of views.
"""

import os
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from django.apps import apps

from filed.song.models import Song, Podcast, Audiobook
from django.conf import settings

# def validate_data_song(audio_data):

@csrf_exempt
def home(request):
    data = {'status': True}
    return JsonResponse(data, status=200)

@csrf_exempt
def create_audio(request):
    data = {'status': False}
    request_data=json.loads(request.body)
    if request_data['type'] or request_data['data']:
        audio_type = request_data['type']
        audio_data = request_data['data']
        if audio_type == 'song':
            if ['duration', 'name'] == sorted(audio_data.keys()):
                name = audio_data['name']
                duration = audio_data['duration']
                obj = Song.objects.create(name=name, duration=duration)
                data['id'] = obj.id
                data['status'] = True
            else:
                data['msg'] 'Invalid song data.'
        elif audio_type == 'podcast':
            if ['duration', 'host', 'name', 'participants'] == sorted(audio_data.keys()):
                name = audio_data['name']
                duration = audio_data['duration']
                host = audio_data['host']
                participants = ",".join(audio_data['participants'][:10])
                obj = Podcast.objects.create(name=name, duration=duration, host=host, participants=participants)
                data['id'] = obj.id
                data['status'] = True
            else:
                data['msg'] 'Invalid podcast data.'
        elif audio_type == 'audiobook':
            if ['author', 'duration', 'narrator', 'title'] == sorted(audio_data.keys()):
                title = audio_data['title']
                author = audio_data['author']
                narrator = audio_data['narrator']
                duration = audio_data['duration']
                obj = Audiobook.objects.create(title=title, author=author, narrator=narrator, duration=duration)
                data['id'] = obj.id
                data['status'] = True
            else:
                data['msg'] 'Invalid audiobook data.'
        else:
            data = {'status': False, 'msg': 'Type not supported'}
    else:
        data = {'status': False, 'msg': 'Invalid Request data.'}
    return JsonResponse(data, status=200)

@csrf_exempt
def delete_audio(request, type, id):
    data = {'status': False}
    db_model = apps.get_model(settings.DB_MIGRATION, type.capitalize())
    if db_model:
        db_model.objects.filter(id=id).delete()
        data['status'] = True
    else:
        data = {'status': False, 'msg': 'Invalid Type.'}
    return JsonResponse(data, status=200)

@csrf_exempt
def update_audio(request, type, id):
    data = {'status': False}
    request_data=json.loads(request.body)
    if request_data['data']:
        audio_data = request_data['data']
        db_model = apps.get_model(settings.DB_MIGRATION, type.capitalize())
        if db_model:
            obj = db_model.objects.filter(id=id).first()
            if obj:
                data['status'] = True
                if type == 'song':
                    if ['duration', 'name'] == sorted(audio_data.keys()):
                        name = audio_data['name']
                        duration = audio_data['duration']
                        obj.update(name=name, duration=duration)
                    else:
                        data['msg'] 'Invalid song data.'
                elif type == 'podcast':
                    if ['duration', 'host', 'name', 'participants'] == sorted(audio_data.keys()):
                        name = audio_data['name']
                        duration = audio_data['duration']
                        host = audio_data['host']
                        participants = ",".join(audio_data['participants'][:10])
                        obj.update(name=name, duration=duration, host=host, participants=participants)
                    else:
                        data['msg'] 'Invalid podcast data.'
                elif type == 'audiobook':
                    if ['author', 'duration', 'narrator', 'title'] == sorted(audio_data.keys()):
                        title = audio_data['title']
                        author = audio_data['author']
                        narrator = audio_data['narrator']
                        duration = audio_data['duration']
                    obj.update(title=title, author=author, narrator=narrator, duration=duration)
                    else:
                        data['msg'] 'Invalid audiobook data.'
            else:
                data = {'status': False, 'msg': 'Invalid Id.'}
        else:
            data = {'status': False, 'msg': 'Invalid Type.'}
    else:
        data = {'status': False, 'msg': 'Invalid Request data.'}
    return JsonResponse(data, status=200)

@csrf_exempt
def get_audio(request, type, id):
    data = {'status': False}
    db_model = apps.get_model(settings.DB_MIGRATION, type.capitalize())
    if db_model:
        obj = db_model.objects.filter(id=id).first()
        if obj:
            data['status'] = True
            data['data'] = model_to_dict(obj)
        else:
            data = {'status': False, 'msg': 'Invalid Id.'}
    else:
        data = {'status': False, 'msg': 'Invalid Type.'}
    return JsonResponse(data, status=200)

@csrf_exempt
def get_all_audio(request, type):
    data = {'status': False}
    db_model = apps.get_model(settings.DB_MIGRATION, type.capitalize())
    if db_model:
        obj = db_model.objects.all()
        if obj:
            data['status'] = True
            data['data'] = list(obj.values())
        else:
            data = {'status': False, 'msg': 'Invalid Id.'}
    else:
        data = {'status': False, 'msg': 'Invalid Type.'}
    return JsonResponse(data, status=200)