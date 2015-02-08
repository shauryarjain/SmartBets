from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
import random
import requests

from bets.models import User, BetRoom, Option, Bet

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'bets/index.html'
    # context_object_name = 'latest_betroom_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return BetRoom.objects.filter(
        date_created__lte=timezone.now()
    ).order_by('-date_created')[:5]


class CreateRoom(generic.TemplateView):
    model = BetRoom
    template_name = 'bets/create.html'


class RoomView(generic.TemplateView):
    model = BetRoom
    template_name = 'bets/room.html'

def room_view(request, url):
    venmo_auth = request.GET.get('access_token')
    try:
        room = BetRoom.objects.get(url=url)
        
    except:
        # Redisplay the question voting form.
        return render(request, 'bets/room.html', {
            'question': b,
            'error_message': "You didn't select a choice.",
        })
    else:
        return render(request, 'bets/room.html', {
            'bet_room': room.room_name,
            'bet_room_id': room.pk,
            'venmo_auth': venmo_auth,
            'options': room.options.all(),
            'bets': room.bets.all(),
            'url': url
            })

def make_bet(request):
    betroom = BetRoom.objects.get(pk=int(request.POST.get('betroom_id')))
    r = requests.post('https://api.venmo.com/v1/payments', data={
        'access_token': request.POST.get('access'),
        'phone': '8184066164',
        'note': 'Bet placed on {}'.format(request.POST.get('choice')),
        'amount': request.POST.get('amount'),
        })
    print {'access_token': request.POST.get('access'),
        'phone': '8184066164',
        'note': 'Bet placed on {}'.format(request.POST.get('choice')),
        'amount': float(request.POST.get('amount'))}
    print r.json()
    response = r.json()['data']['actor']['username']
    b = Bet(date_created=timezone.now(),
            betroom_id = int(request.POST.get('betroom_id')),
            from_id=response,
            to_id='shaurya-jain',
            bet_type='PAY_IN',
            bet_option=Option.objects.get(pk=int(request.POST.get('choice'))),
            name=request.POST.get('name'),
            amount=request.POST.get('amount')
            )
    b.save()
    return render(request, 'bets/room.html', {
            'bet_room': betroom.room_name,
            'bet_room_id': betroom.pk,
            'venmo_auth': venmo_auth,
            'options': betroom.options.all(),
            'bets': betroom.bets.all(),
            'url': urls
            })


def make_betroom(request):
    rand = ''.join(random.choice('0123456789abcdefghijklmnopqrstuvwxyz') for i in range(12))
    try: 
        print '1'*80
        b = BetRoom(room_name=request.POST['name'], 
                    date_created=timezone.now(),
                    password=request.POST['pw'], 
                    is_active=True, 
                    url=rand
                    )
        b.save()
        options = [i for i in request.POST.keys() if 'option' in i]
        for x in options:
            o = Option(betroom=b,
                       option_name=request.POST[x]
                       )
            o.save()
        print '8'*80
    except:
        # Redisplay the question voting form.
        return render(request, 'bets/room.html', {
            'question': b,
            'error_message': "You didn't select a choice.",
        })
    else:
        print '3'*80
        b.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('room', args=[rand]))

# def vote(request, question_id):
#     p = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = p.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'bets/detail.html', {
#             'question': p,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('results', args=(p.id,)))