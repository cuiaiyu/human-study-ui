from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Answer, Question, Choice
from django.http import HttpResponse
from django.template import loader

class IndexView(generic.ListView):
    template_name = 'FEdit/index.html'
    context_object_name = 'latest_question_list'
    def get_queryset(self):
        return Question.objects.order_by('id')


class DetailView(generic.DetailView):
    model = Question
    template_name = 'FEdit/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'FEdit/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        print(request.POST)
        import pdb; pdb.set_trace()
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'FEdit/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        if (question.id + 1) < Question.objects.count():
            return HttpResponseRedirect(reverse('FEdit:vote', args=(question.id + 1,)))
        else:
            return HttpResponseRedirect(reverse('FEdit:results', args=(question.id,)))



def index(request):

    latest_question_list = Question.objects.order_by('id') #('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }

    if request.method == "POST":
        try:
            import pdb; pdb.set_trace()
            selects = []
            for question in latest_question_list:
                choice_id = request.POST['%d'%question.id]
                selected_choice =  question.choice_set.get(pk=choice_id)
                selects.append(selected_choice)
            for selected_choice in selects:
                selected_choice.votes += 1
                selected_choice.save()
            return HttpResponseRedirect(reverse('FEdit:results', args=(question.id,)))

        
        except (KeyError, Choice.DoesNotExist):
            # Redisplay the question voting form.
            return render(request, 'FEdit/index.html', {
                'latest_question_list': latest_question_list,
                'error_message': "You didn't select a choice for question %d." % question.id,
            })
    return render(request, 'FEdit/index.html', context)
