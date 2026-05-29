

contacts = {
    'number' : 4,
    'students' :
    [
        {'name' : 'sainath', 'email' : 'sainath@gmail.com'},
        {'name' : 'sainath', 'email' : 'sainath@gmail.com'},
        {'name' : 'sainath', 'email' : 'sainath@gmail.com'}
    ]
}

for student in contacts['students']:
    print(student['email'])