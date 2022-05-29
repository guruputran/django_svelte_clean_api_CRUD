from django.db import models
class Todo(models.Model):
    todoItem = models.CharField(max_length=200, blank=True, null=True)
    isCompleted = models.BooleanField(default=False)
        
    def __str__(self):
        return self.todoItem