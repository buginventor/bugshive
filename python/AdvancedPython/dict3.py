students={'name':'alex','age':'19','grade':'sixth grade','comments':'this is a comment'}
print('name is', students['name'])

students['name']='alex whitman'; #changing value

print('name: ', students['name'])

print('comments: ', students['comments'])

del students['comments'] #deleting value and key
print('comments: ', students['comments'])
students.clear() #remove everything in that object
del students #delete object
print(students)
