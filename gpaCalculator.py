# A program to calculate the Degree GPA of a UWI Cavehill student (after 2014)

print('Welcome the the UWI Degree GPA Calculator.')
print('Please enter your letter grades, one per line.')
print('Enter a blank space to finish data entry.')

#Grade point mapping

points = { 'A+':4.3, 'A':4.0, 'A-':3.7, 'B+':3.3, 'B':3.0, 'B-':2.7, 'C+':2.3, 'C':2.0, 'F1':1.7, 'F2':1.3, 'F3':0.0 }

num_courses = 0
total_points = 0
done = False

while not done:                             #Run until empty space
    grade = input()
    if grade == '':
        done = True
    elif grade not in points:               #Invalid input
        print("Unknown grade '{0}' being ignored".format(grade))
    else:
        num_courses += 1
        total_points += points[grade]

if num_courses > 0:                     #Block Division by zero
        print('Your GPA is {0:.3}'.format(total_points / num_courses))
