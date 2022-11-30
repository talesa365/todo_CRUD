
# import the standard Django Model
# from built-in library
from django.forms import ModelForm
from todo_app.models import Comment, Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["description"]
        
class CommentForm(ModelForm):
    #Pull the description column from the Task model into a form
    class Meta:
        model = Comment
        fields = ["body"]
#the form will get created with a task. we need to pull that task out and keep track of it

#the form will get created with a task. we need to pull that task out and keep track of it

    def _init_(self, *args, **kwargs):
        task = kwargs.pop('task_object')
        super()._init_(*args, **kwargs)
    
  #self.instance is the comment we are creating with this form  
        self.instance.task = task
        self.fields['body'].label = ''
    
    