from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

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


class RoomView(generic.DetailView):
    model = BetRoom
    template_name = 'bets/room.html'

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