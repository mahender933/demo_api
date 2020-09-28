from django.db import models


class Exam(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.name}"


class SubCategory(models.Model):
    name = models.CharField(max_length=150)
    exam = models.ForeignKey(Exam, null=True, blank=True, related_name='sub_category', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.exam} -> {self.name}"

    class Meta:
        verbose_name_plural = 'Sub Category'


class Subject(models.Model):
    name = models.CharField(max_length=150)
    exam = models.ForeignKey(Exam, null=True, blank=True, on_delete=models.DO_NOTHING, related_name='subject')
    sub_cat = models.ForeignKey(SubCategory, null=True, blank=True, on_delete=models.DO_NOTHING, related_name='subject')

    def __str__(self):
        return f"{self.name}"


class Topic(models.Model):
    name = models.CharField(max_length=150)
    subject = models.ForeignKey(Subject, null=True, blank=True, related_name='topics', on_delete=models.CASCADE)
    # subtopic = models.ForeignKey('self', null=True, blank=True, related_name='subtopics', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.subject} -> {self.name}"

