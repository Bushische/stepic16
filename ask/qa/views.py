from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from models import Question
from models import Answer
from datetime import date
from django.core.paginator import Paginator, EmptyPage
from forms import AskForm, AnswerForm

# Create your views here.
from django.http import HttpResponse

def test(request, *args, **kwargs):
    return HttpResponse('OK')

# fill db with information
def filldb(request, cou):
    for x in range(0, int(cou)):
        q = Question(title = "Question #"+str(x),
                     text = "Just a question with number "+str(x))
        q.rating = x
        q.author_id = 1
        q.added_at = date(2016, 03, 1+x)
        q.save()
        q.added_at = date(2016, 03, 1+x)
        for y in range(1, x+2):
            a = Answer(text = "answer #"+str(y)+" for question #"+str(x))
            a.author_id = 1
            q.answer_set.add(a)
        q.save()
    return HttpResponse("OK")

# show info for one question
def showquestion(request, inid):
    try:
        que = Question.objects.get(id = inid)
    except Question.DoesNotExist:
        print "Question with id=%s was not found" % (inid)
        raise Http404

    form = AnswerForm(initial={'question': inid})
    return render(request, "qa/onequest.html",
                  {'question' : que,
                   'answers' : que.answer_set.all(),
                   'form': form,
                   })

# prepare common part of all objs
def prepareAndShow(request, ques, paginatorUrl):
    
    limit = 10
    try:
        page = request.GET.get('page', 1)
        if not(page):
            page = 1
    except ValueError as e:
        page = 1
    print '%s 2: %s'% (paginatorUrl, page)
    paginator = Paginator(ques, limit)
    paginator.baseurl = paginatorUrl #'/popular/?page='
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    # page = paginator.page(page) # Page
    return render(request, 'qa/popular.html', {
        'ques':  page.object_list,
        'paginator': paginator,
        'page': page,
    })

# show popular questioins
def showpopular(request):
    print 'showpopular 1'
    ques = Question.objects.all()
    ques = ques.order_by('-rating')
    return prepareAndShow(request, ques, '/popular/?page=')

# show questioins ordered by Id desc
def showbyid(request):
    print 'showbyid 1'
    ques = Question.objects.all()
    ques = ques.order_by('-id')
    return prepareAndShow(request, ques, '/?page=')

#========================================

# Add new Question
def question_add(request):
    if request.method == "POST":
        form = AskForm(request.POST)
    #   form = AskForm(initial={'question': question_id})
        if form.is_valid():
            ques = form.save()
            url = ques.get_url()
            print 'redirect to %s' % (url)
            return HttpResponseRedirect(url)
        print 'qa if but not valid'
    else:
        form = AskForm()
        print 'qa else'
    return render(request, 'qa/question_add.html', {'form': form})

# Add new Answer
def answer_add(request):
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answ = form.save()
            print 'try get url from answer %s' % (answ)
            url = answ.question.get_url()
            print 'redirect to %s' % (url)
            return HttpResponseRedirect(url)
        print 'answer_add if but not valid'
    else:
        form = AnswerForm()
        print 'answer add else'
    return Http404


"""
# show info for one question
def showquestion1(request, inid):
    print 'start showquestion with inid = %s' % (inid)
    try:
        try:
            print '1: '
            que = Question.objects.get(id=inid)
            print '2: ' + que.title
        except Question.DoesNotExist:
            print '4:'
            raise Http404
        except Exception as e:
            print '%s (%s)' % (e.message, type(e))
            raise Http404
        print '3:'
        return render(request, 'qa/index.html', {
            'question' : que,
            'title' : que.title,
            'text' : que.text,
             
            })
    except Exception as e:
        print 'EXC2: %s (%s)' % (e.message, type(e))
    return HttpResponse("not OK")
#    return render(request, "OK")
"""

"""
    
<html>
<head>QA</head>
<body>
<h1>{{ question.title }}</h1>
<p>{{ question.text }}</p>


</body>
</html>
"""
