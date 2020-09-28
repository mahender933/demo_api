# API Demo

RESTful microservice which gives following functionalities - 

* Stores the list of exams and their subcategories. An exam can have N-levels of sub-categories. Sub-categories can be optional, for example - 

* There is an exam called GATE and it can have sub-categories such as “Computer Science Engineering”, “Mechanical Engineering”, “Electrical Engineering”, etc. But exams like CAT, GMAT, IIT don’t have any sub-categories. (Note - Mains and Advance are papers of IIT, not sub-category).

* Give functionality to add subject and topics under an exam. Subjects can always be added under the lowest sub-category of an exam. In absence of sub-category, it can be added under exam. A topic can have child-topics up to N-level. 
Hierarchy should be: Exam > Sub-category > Subject > Topics

* Example - 
**Exam > Sub-category > Subject > Topic**

## Installation
* Install requirements
    `pip install -r requirements.txt`
* Change directory to where `manage.py` resides and Run migrations
    `python manage.py makemigrations`
    `python manage.py migrate`
* Run Server 
    `python manage.py runserver`
* Test by going to `http://localhost:8000/exam/api/`

## Endpoints 
* Api overview - `http://localhost:8000/exam/api/`
* Exam List:  `http://localhost:8000/exam/api/exam-list/`
* Subject List: `http://localhost:8000/exam/api/subject-list/`
* Add Exam: `http://localhost:8000/exam/api/add-exam/`
    * ```
      Method Allowed : POST
      Payload Example: {
            "name": "(str) Exam Name"
        }
        ```
* Add Sub Category: `http://localhost:8000/exam/api/add-category/`
    * ```
        Method Allowed : POST
        "payload_example": {
            "name": "(str) Sub Category Name",
            "exam": "(int) Exam primary key for which this subcategory would be assigned to"
        }
    ```
* Add Subject: `http://localhost:8000/exam/api/add-subject/`
    * ```
        Method Allowed : POST
        Payload Example: {
            "name": "(str) Subject Name",
            "exam": "(int) Exam primary key for which this subject would be assigned to",
            "sub_cat": "(int) Subcategory primary key for which this subject would be assigned to"
        }
    ```
* Add Topic: `http://localhost:8000/exam/api/add-topic/`
    * ```
        Method Allowed : POST,
        Payload Example: {
            "name": "(str) Topic Name",
            "subject": "(int) Subject primary key for which this topic would be assigned to",
        }
    ```
* Exam Hierarchy: `http://localhost:8000/exam/api/show-hierarchy/<int:exam_id>/`
