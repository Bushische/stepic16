from django import forms
from models import Question
from models import Answer

class AskForm(forms.Form):
    title = forms.CharField(max_length=100)
    text  = forms.CharField(widget=forms.Textarea)

#    hidden = forms.CharField(widget=forms.HiddenInput())

    def clean(self):
        text = self.cleaned_data['text']
        if not text:    #.is_valid()
            raise forms.ValidationError('question text is wrong', code=12)
        return self.cleaned_data

    def save(self):
        print 'AskF save: (%s)' % (self.cleaned_data)
        quest = Question(**self.cleaned_data)
        quest.author_id = 1
        quest.save()
        return quest

class AnswerForm(forms.Form):
#    title = forms.CharField(max_length=100)
    text  = forms.CharField(widget=forms.Textarea)
    # hiddent question id field
    question = forms.IntegerField(widget=forms.HiddenInput())

    def clean(self):
        text = self.cleaned_data['text']
        if not text: #.is_valid()
            raise forms.ValidationError('answer text is wrong', code=12)
        return self.cleaned_data

    def save(self):
        # getting Question by ID
        print 'AnswerF save: %s (%s)' % ( self.cleaned_data, self.cleaned_data['question'])
        q_id = int(self.cleaned_data['question'])
        quest = Question.objects.get(id = q_id)
        #ans = Answer(**self.cleaned_data)
        ans = Answer(text = self.cleaned_data['text'])
        ans.author_id = 1
        quest.answer_set.add(ans)
        quest.save()
        return ans
