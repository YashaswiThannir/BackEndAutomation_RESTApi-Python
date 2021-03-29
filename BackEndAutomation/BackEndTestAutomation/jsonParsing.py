import json

courses = '{"name": "YashaswiThannir", "languages": ["CSharp", "Python"]}'

# loads will parse json and convert it to dictionary
dictCourses = json.loads(courses)
print(dictCourses)
print(type(dictCourses))

print(dictCourses['name'])
print(dictCourses['languages'])

listLanguages = dictCourses['languages']
print(listLanguages[0])


#****** Parse content present in Json file ******

with open('C:\\course.json') as file:
    data = json.load(file) # converts json to dictionary
    print(data)
    print(type(data))
    print(data['courses'][1]['title'])  # to access value cypress
    print(data['dashboard']['website'])  # to access the value 910

    for course in data['courses']:
        if course['title'] == "RPA":
            print(course['price'])
            assert course['price'] == 45