from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from examination.models import Exam, Subject
from . serializers import ExamSerializer, SubjectSerializer, SubCategorySerializer, TopicSerializer


@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'API Overview': 'api/',
        'Exam List': 'exam-list/',
        'Subject List': 'subject-list/',
        'Add Exam': 'add-exam/',
        'Add Sub Category': 'add-category/',
        'Add Subject': 'add-subject/',
        'Add Topic': 'add-topic/',
        'Exam Hierarchy': 'show-hierarchy/<int:exam_id>/'
    }
    return Response(api_urls)


@api_view(['GET'])
def exams_list(request):
    """
    List of all exams
    """
    serialized = ExamSerializer(Exam.objects.all(), many=True)
    return Response(serialized.data)


@api_view(['GET'])
def subject_list(request):
    """
    List of all subjects
    """
    serialized = SubjectSerializer(Subject.objects.all(), many=True)
    return Response(serialized.data)


@api_view(["POST", "GET"])
def add_exam(request):
    """
    Adds a new exam object.
    """
    if request.method == "GET":
        return Response(status=status.HTTP_200_OK, data={
            "info": "Adds an exam",
            "request_method": "POST",
            "payload_example": {
                "name": "(str) Exam Name"
            }
        })
    if request.data:
        exam = ExamSerializer(data=request.data)
        if exam.is_valid():
            exam.save()
            return Response(status=status.HTTP_201_CREATED, data={"msg": f"Created Successfully"})
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=exam.errors)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"msg": "Empty Payload"})


@api_view(["POST", "GET"])
def add_category(request):
    """
    Adds a new category object for a particular exam.
    """
    if request.method == "GET":
        return Response(status=status.HTTP_200_OK, data={
            "info": "Adds a category for a particular exam.",
            "request_method": "POST",
            "payload_example": {
                "name": "(str) Sub Category Name",
                "exam": "(int) Exam primary key for which this subcategory would be assigned to"
            }
        })
    if request.data:
        sub_cat = SubCategorySerializer(data=request.data)
        if sub_cat.is_valid():
            sub_cat.save()
            return Response(status=status.HTTP_201_CREATED, data={"msg": f"Created Successfully"})
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=sub_cat.errors)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"msg": "Empty Payload"})


@api_view(["POST"])
def add_subject(request):
    """
    Adds a subject to an Exam object or a SubCategory object
    """

    if request.method == "GET":
        return Response(status=status.HTTP_200_OK, data={
            "info": "Adds a category for a particular exam.",
            "request_method": "POST",
            "payload_example": {
                "name": "(str) Subject Name",
                "exam": "(int) Exam primary key for which this subject would be assigned to",
                "sub_cat": "(int) Subcategory primary key for which this subject would be assigned to"
            }
        })
    serializer = SubjectSerializer(data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_200_OK, data={"msg": "Updated Successfully"})
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)


@api_view(['POST', 'GET'])
def add_topic(request):
    """
    Add a topic to a specific subject object using its primary key
    """
    if request.method == "GET":
        return Response(status=status.HTTP_200_OK, data={
            "info": "Adds a topic for a particular subject object.",
            "request_method": "POST",
            "payload_example": {
                "name": "(str) Topic Name",
                "subject": "(int) Subject primary key for which this topic would be assigned to",
            }
        })
    serializer = TopicSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_200_OK, data={"msg": "Updated Successfully"})
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)


@api_view(['GET'])
def show_hierarchy(request, exam_id):
    response = list()
    subject = Subject.objects.select_related('exam').select_related('sub_cat').filter(exam__id=exam_id)
    for sub in subject:
        response.append(f"{sub.exam.name} > {sub.sub_cat.name if sub.sub_cat else ''} > {sub.name} "
                        f"> {', '.join([topic.name for topic in sub.topics.all()])}")
    return Response(status=status.HTTP_200_OK, data=response)
