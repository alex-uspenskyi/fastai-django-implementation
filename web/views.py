from fastai.vision import learner, open_image, load_learner
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from .forms import MainForm
from .models import Request
from django.utils.translation import gettext_lazy as _
import os

classes = ['ant', 'bedbug', 'beetle', 'cockroach', 'flea', 'louse', 'moth', 'spider', 'tick', 'woodlouse']
labels = [_('ant'), _('bedbug'), _('beetle'), _('cockroach'), _('flea'), _('louse'), _('moth'), _('spider'), _('tick'), _('woodlouse')]

def index(request):
    result = False
    if request.method == 'POST' and request.FILES:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        form = MainForm({'ip': ip}, request.FILES)
        if form.is_valid():
            model = form.save()
            img = open_image(settings.BASE_DIR + model.photo.url)
            learn = load_learner(os.path.join(settings.BASE_DIR, 'fastai'))
            pred_class,pred_idx,outputs = learn.predict(img)
            scores = sorted(zip(classes, outputs.data.tolist()), key=lambda kv: kv[1], reverse=True)
            model.scores = dict(scores)
            model.save(update_fields=["scores"])
            result = list(scores[0]) + [_(scores[0][0])]
            print(result)
    else:
        form = MainForm()

    return render(request, 'web/index.html', {'form': form, 'result': result, 'labels': labels})