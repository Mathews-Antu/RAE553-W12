from flask import *
from flask_restful import Resource, Api
import json
app = Flask(__name__)
api = Api(app)

students = [
    {
        'name': 'Amal Mathews',
        'ID': '201AEM021',
        'course': 1,
        'group no': 1
    },
    {
        'name': 'Sadi Kamla',
        'ID': '210ADB101',
        'course': 3,
        'group no': 2
    }
]

jsonDataTemp = []

@app.route('/')
def home():
    return "HomePage";

#searching for students
@app.route('/student/<string:name>')
def getStusdent(name):
    for student in students:
        if(student['name'] == name):
            return json.dumps(student, indent=4, separators=(',', ': '))
    return "Student not found"

@app.route('/studentbyid/<string:id>')
def getStusdentbyID(id):
    for student in students:
        if(student['ID'] == id):
            return json.dumps(student, indent=4, separators=(',', ': '))
    return "Student ID not found"

@app.route('/student', methods=['POST'])
def addStudent():
    data = request.json
    print (data);
    for student in students:
        if(student['ID'] == data['ID'] or student['name'] == data['name']):
            return "This student already registered!"
    students.append(data)
    return json.dumps(data, indent=4, separators=(',', ': '))

@app.route('/student/ShowAll')
def showAllStudents():
    return json.dumps(students, indent=4, separators=(',', ': '))

@app.route('/student/<string:name>/delete', methods=['DELETE'])
def deleteStudent(name):
    i=0;
    while(i<len(students)):
        if(students[i]['name'] == name):
            students.pop(i);
            return "Deleted"
        i+=1;
    return "Student Not Found!"
app.run(port=5000);
