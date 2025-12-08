from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    

    def __str__(self):
        return f"{self.id} - {self.name}"
    

class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
    done = models.BooleanField(default=False)
    deadline = models.DateTimeField(null=True, blank=True)
    priority = models.IntegerField(choices=[(1, 'Low'), (2, 'Medium'), (3, 'High')], null=True, blank=True)

    owner = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='todos', null=True, blank=True)
    def __str__(self):
        return f"{self.id} - {self.title}"
    
