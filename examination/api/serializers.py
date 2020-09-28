from examination.models import Exam, Subject, SubCategory, Topic
from rest_framework import serializers


class SubjectSerializer(serializers.ModelSerializer):
    exam = serializers.PrimaryKeyRelatedField(queryset=Exam.objects.all(), required=False)
    sub_cat = serializers.PrimaryKeyRelatedField(queryset=SubCategory.objects.all(), required=False)

    class Meta:
        model = Subject
        fields = ['id', 'name', 'exam', 'sub_cat']

    def validate(self, data):
        if not any([data.get('sub_cat'), data.get('exam')]):
            raise serializers.ValidationError("Either exam or sub category primary key is required.")
        return data


class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ['id', 'name']


class SubCategorySerializer(serializers.ModelSerializer):
    exam = serializers.PrimaryKeyRelatedField(queryset=Exam.objects.all())

    class Meta:
        model = SubCategory
        fields = ['id', 'name', 'exam']


class TopicSerializer(serializers.ModelSerializer):
    subject = serializers.PrimaryKeyRelatedField(queryset=Subject.objects.all(), required=True)

    class Meta:
        model = Topic
        fields = ['name', 'subject']
