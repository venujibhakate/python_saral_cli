import requests
import json
import pprint

saralUrl = "http://saral.navgurukul.org/api"


def saralRequest(Url):
    request = requests.get(Url)
    response = request.json()
    return response
coursesUrl = saralUrl+"/courses"
coursesResponse = saralRequest(coursesUrl)
# pprint.pprint (coursesResponse)

listCourses = []
def coursesFunction():
    index = 0
    while index < len(coursesResponse["availableCourses"]):
        coursesEx = coursesResponse["availableCourses"][index]
        coursesName = coursesEx["name"]
        coursesId = coursesEx["id"]
        listCourses.append(coursesId)
        print index+0, coursesName, coursesId
        index = index + 1

coursesFunction()

print "............................................."

selectCourse = int(raw_input("Select The Course:-"))
selectCourseId = listCourses[selectCourse]
print(selectCourseId)

exerciseUrl = "{0}/{1}/exercises".format(coursesUrl, selectCourseId)
exerciseSlugList = []
childExercise = []
def exerciseFunction(exerciseData):
    index = 0
    while(index < len(exerciseData['data'])):
        exercise = exerciseData['data'][index]
        exerciseName = exercise["name"]
        childExerciseList = exercise["childExercises"]
        childExercise.append(childExerciseList)
        # print (childExercise)
        exerciseSlug = exercise["slug"]
        print index + 0,exerciseName,"***",exerciseSlug
        exerciseSlugList.append(exerciseSlug)
        index = index + 1
exerciseResponse = saralRequest(exerciseUrl)
exerciseData = exerciseFunction(exerciseResponse)

print "......................................................"

selectExercise = int(raw_input("Select the Exercise :-"))
selectExerciseId = exerciseSlugList[selectExercise]
print (selectExerciseId)

slugUrl = "{0}/{1}/exercise/getBySlug?slug={2}".format(coursesUrl,selectCourseId,selectExerciseId,)
def contentAndchildEx(slug):
        content = slug['content']
        return content
slugResponse = saralRequest(slugUrl)
slugData=contentAndchildEx(slugResponse)
print slugData
childSlugList = []
def childExerciseFun():
        index = 0
        while index < len(childExercise[selectExercise]):
                childExerciseIndex = childExercise[selectExercise][index]
                childName = childExerciseIndex["name"]
                childSlug = childExerciseIndex["slug"]
                childSlugList.append(childSlug)
                print index,"=", childName
                index = index + 1
        return childSlugList
childExerciseFun()

selectChildEx = int(raw_input("Selsec the ChildEx :-"))
childExSlug = childSlugList[selectChildEx]
print (childExSlug)




slugUrl = "{0}/{1}/exercise/getBySlug?slug={2}".format(coursesUrl,selectCourseId,childExSlug)
def contentChild(childSlug):
        content = childSlug["content"]
        return content
childContent = saralRequest(slugUrl)      
childExContent = contentChild(childContent)

print childExContent 
