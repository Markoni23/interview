from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=100)
    imageUrl = models.URLField(blank=True, null=True)

    @property
    def short_name(self):
        return self.name.split()[0]

    def __str__(self):
        return self.name


class Exercise(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    startTime = models.TimeField()
    endTime = models.TimeField()
    place = models.CharField(max_length=50)
    weekDay = models.IntegerField()
