Nested Lists

Given the names and grades for each student in a Physics class of students, store them in a nested list
and print the name(s) of any student(s) having the second lowest grade.
Note: If there are multiple students with the same grade, order their names alphabetically and print each
name on a new line.
Input Format
The first line contains an integer, , the number of students.
The subsequent lines describe each student over lines; the first line contains a student's name, and
the second line contains their grade.
Constraints
There will always be one or more students having the second lowest grade.


Output Format
Print the name(s) of any student(s) having the second lowest grade in Physics; if there are multiple
students, order their names alphabetically and print each one on a new line.


Sample Input 0
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39


Sample Output 0
Berry
Harry


Explanation 0
There are students in this class whose names and grades are assembled to build the following list:
python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
The lowest grade of belongs to Tina. The second lowest grade of belongs to both Harry and
Berry, so we order their names alphabetically and print each name on a new line.






def check(l):
    x=[]
    for i in range(len(l)):
        x.append(l[i][1]) 
    x=list(set(x))
    x.sort()  
    return(x[1])

if __name__ == '__main__':
    list_students=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list_student=[]
        list_student.append(name)
        list_student.append(score)
        list_students.append(list_student)
    m=check(list_students)
    list_students.sort()  
    for i in range(len(list_students)):
        if m==list_students[i][1]:
            print(list_students[i][0])
            
            
            
----------------------------------------------------------------

n=int(input())
arr=[[input(),float(input())] for _ in range(0,n)]
arr.sort(key=lambda x: (x[1],x[0]))
names = [i[0] for i in arr]
marks = [i[1] for i in arr]
min_val=min(marks)
while marks[0]==min_val:
    marks.remove(marks[0])
    names.remove(names[0])    
for x in range(0,len(marks)):
    if marks[x]==min(marks):
        print(names[x])
