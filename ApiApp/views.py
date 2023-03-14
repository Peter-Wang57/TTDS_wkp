from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
import pymongo;
from bson.json_util import dumps
from ApiApp.tfidf import TFIDF
from ApiApp.getresults import get_results
from django.core.files.storage import default_storage
from django.http import HttpResponse

# Create your views here.


def home(request):
    return HttpResponse("Home Page")

def search(request):
    return HttpResponse("search")

client = pymongo.MongoClient("mongodb+srv://zhou:0219@cluster0.kwwqk4a.mongodb.net/?retryWrites=true&w=majority")
db = client['test']



@csrf_exempt
def my_view(request):
    query = request.GET.get('name')
    age = request.GET.get('age')
    print(query)

    result = TFIDF(query)
    print(result[0:100])
    data = get_results(result[0:100])
    return JsonResponse(data, safe=False)
    # Return the result as JSON
    # return HttpResponse(json.dumps(result), content_type='application/json')
    return HttpResponse('Hello, {}! You are {} years old.'.format(query, age))

    print(http_string_value)

    if request.method=='GET':
        departments = Department.find_all()
        return HttpResponse(dumps(departments), content_type='application/json')
    else:
        response_data = {'message': 'Invalid request method'}
        return JsonResponse(response_data, status=405)

# @csrf_exempt
# def departmentApi(request,id=0):
#     if request.method=='GET':
#         departments = Departments.objects.all()
#         departments_serializer=DepartmentSerializer(departments,many=True)
#         return JsonResponse(departments_serializer.data,safe=False)
#     elif request.method=='POST':
#         department_data=JSONParser().parse(request)
#         departments_serializer=DepartmentSerializer(data=department_data)
#         if departments_serializer.is_valid():
#             departments_serializer.save()
#             return JsonResponse("Added Successfully",safe=False)
#         return JsonResponse("Failed to Add",safe=False)
#     elif request.method=='PUT':
#         department_data=JSONParser().parse(request)
#         department=Departments.objects.get(DepartmentId=department_data['DepartmentId'])
#         departments_serializer=DepartmentSerializer(department,data=department_data)
#         if departments_serializer.is_valid():
#             departments_serializer.save()
#             return JsonResponse("Updated Successfully",safe=False)
#         return JsonResponse("Failed to Update")
#     elif request.method=='DELETE':
#         department=Departments.objects.get(DepartmentId=id)
#         department.delete()
#         return JsonResponse("Deleted Successfully",safe=False)

# @csrf_exempt
# def employeeApi(request,id=0):
#     if request.method=='GET':
#         employees = Employees.objects.all()
#         employees_serializer=EmployeeSerializer(employees,many=True)
#         return JsonResponse(employees_serializer.data,safe=False)
#     elif request.method=='POST':
#         employee_data=JSONParser().parse(request)
#         employees_serializer=EmployeeSerializer(data=employee_data)
#         if employees_serializer.is_valid():
#             employees_serializer.save()
#             return JsonResponse("Added Successfully",safe=False)
#         return JsonResponse("Failed to Add",safe=False)
#     elif request.method=='PUT':
#         employee_data=JSONParser().parse(request)
#         employee=Employees.objects.get(EmployeeId=employee_data['EmployeeId'])
#         employees_serializer=EmployeeSerializer(employee,data=employee_data)
#         if employees_serializer.is_valid():
#             employees_serializer.save()
#             return JsonResponse("Updated Successfully",safe=False)
#         return JsonResponse("Failed to Update")
#     elif request.method=='DELETE':
#         employee=Employees.objects.get(EmployeeId=id)
#         employee.delete()
#         return JsonResponse("Deleted Successfully",safe=False)

# @csrf_exempt
# def SaveFile(request):
#     file=request.FILES['file']
#     file_name=default_storage.save(file.name,file)
#     return JsonResponse(file_name,safe=False)


# client = pymongo.MongoClient("mongodb+srv://zhou:0219@cluster0.kwwqk4a.mongodb.net/?retryWrites=true&w=majority")
# db = client['test']

# class Department:
#     collection = db['ApiApp_departments']

#     @classmethod
#     def find_all(cls):
#         return cls.collection.find()

#     @classmethod
#     def find_by_id(cls, id):
#         return cls.collection.find_one({'id': id})

# # class Employee:
# #     collection = db['employees']

# #     @classmethod
# #     def find_all(cls):
# #         return cls.collection.find()

# #     @classmethod
# #     def find_by_id(cls, id):
# #         return cls.collection.find_one({'id': id})