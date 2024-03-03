import datetime
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Choice, Question
from django.views import generic


class IndexView(generic.ListView):
    extra_context = {'title': 'ИМЯ-ВЫМЯ'}
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).exclude(choice=None).order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"
    extra_context = {'title': 'ИМЯ-ВЫМЯ'}

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"
    extra_context = {'title': 'ИМЯ-ВЫМЯ'}

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


def vote(question_id):
    return HttpResponse("You're voting on question %s." % question_id)


def print_year(year):
    now = datetime.datetime.now()
    return HttpResponse("You chose year ", year, "and time - ", now)


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))


def page_not_found():
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
