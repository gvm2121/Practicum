# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 14:47:48 2023

@author: gonzalo
"""
#Modulo 1 Crear una Cadena de Bloques.
# Test Task for Tutor Python

### **Python**

#- What are the key differences between Python2 and Python3?.
#Python2 is deprecated it was used preferent on servers, Python 3 has growing suppport, package and wonderful packages
#- What happens if you import the same library into the code twice?
#no error is raised. Nothing happend
#- What is circular (cyclic) import and how can you avoid it?
#circular (cyclic) import is when a library needs a library who is called itself. You can avoid it making conditionals imports, changing names if it is possible or import the module only when it s needed.
#- What is a context manager?
# Context manager is a bunch of code (piece of code) who starts with the "with" reserved word,
# allows, in case of fail, no process the code inside the with statement, is commontly used when you work with files (open, close, etc). 
#- Describe how a `list` data structure works.
# list is a structure that can contains any kind of objects, primitive type of objects,tuples, udf objects, etc.
# the objects has a index that you can call each one, you can make a for loop over it (iterator), add, replace, delete objects, etc...

### **Algorithms**

#Which data type in Python should I choose for the `items` container so that the operation of searching for an item is asymptotically the most efficient?

#- A set
#- A list
#- Sorted list
#- A single-linked list
#- It doesn't matter, since we'll write `for item in items:` -> correct, beacouse if you have to do a for loop it has o(n) time complexity. 
#And asymptotically search could be a binary search but ti is not object related, it s related to the algorithm that you write.
#- tuple

#Estimate the difficulty of quick sorting in the worst-case scenario.

#- O(N^2) worst escenario
#- O(N logN) best scenario
#- O(log(logN) best sceneario also.

#Estimate the complexity of the operation of searching for an element in the search tree in the worst-case scenario.

#- O(logN)
#- O(N logN)
#- O(N^2)
#- There are no correct answers

#What is a “heap data structure”?. It is a memory data structure used for complete binary tree

#What features should a binary tree have in order to be a search tree?

### **Django**

#How can I get the value of the `username` variable in the controller if it is passed from the page by the POST method?


#- request.POST.get('username')
#- request.POST['username']-> right answer
#- request.POST.username
#- request.POST('username')

#Which command runs the development web server in Django?

#- python manage.py runserver -> right answer
#- python manage.py devserver
#- python run server
#- python devserver run

#What arguments in this code are passed to the view function?

#"path('/example/<int:id>/', example_view)"

#- Named `int` argument that has an `id` type
#- Named id argument that has an `int` type 
#- Positioned `int` argument that has an `id` type
#- Positioned `id` argument that has an `int` type -> right answer

#You need to write a controller that returns data from the database in the form of an object. On the basis of which class would you create it?

#- ListView
#- DetailView -> right answer
#- RetrieveView
#- GetView

#You have changed the models in a project. What commands do you need to run to commit changes and start migrations? python3 manage.py makemigrations and python3 manage.py migrate

#What is middleware? there are functions executed between views. Ex:: Login functions are used by middleware

### **SQL**

#What types of JOIN queries in SQL do you know? Describe them and specify the differences between them.
#postgresql have RIGHT INNER JOIN,OUTER JOIN,LEFT OUTER JOIN,RIGHT OUTER JOIN,FULL OUTER JOIN,CROSS JOIN.inner joins is like an intersection between two tables, inner join (or right inner join) is tarting form the right table on FROM clause,
#outer joins is not intesection between tables(less used and sometimes it gives complex results).Left is starting from left table on the FROM clause. CROSS JOIN is a cartesian product between 2 tables.


#There are two tables: A and B. The first table has 4 columns and 10 records, and the second one has 5 columns and 8 records. How many rows and columns will be output with the `select * from A,B` query, and why?

#Indicate the main differences between SQL and NoSQL databases. Give examples of how both of them can be used and explain your choice.
#SQL is a relational database engine where the tables have o may not have a relation between them, NoSQl can be no related between them, more flexible and scalable, preferebly used on datascience and API interfaces.

### **General questions**

#1. You need to write Python code that will send users' comments to a certain forum. Which request method would you choose for this — GET, POST, or PUT? Explain your choice. POST, post is the method used to send data, by convention. Get is for retrieve data and put is to update data.
#2. Explain which is better: inheritance or composition. Why? it depens what you want, inheritance get the attributes and methods from a father class and you can add some new method if you like, composition you can reuse some implementatios of anothed class
#3. Explain how authentication differs from authorization. Auth is for be sure that the user is who is. authorizations is what kind of things the user can do (level of access).
#4. What is versioning used for when creating REST API services? MAJOR.MINOR.PATCH
#5. What HTTP methods do you know? GET,POST,PUT,DELETE,PATCH among others
#6. Suggest several options for scaling your service.
#7. What ways do you know for changing file access rights in Linux? chmod +777 -r
#8. List the key differences between processes and threads.threads run on the same memory space and processes runs in a separete memory space.
#9. What ways of interaction between processes do you know?
#10. You typed a 6-character command in the terminal and received the name of the current directory in response. Is this possible?. Yes "pwd" on linux.
#11. What types of DNS records do you know?. Three types, primera server, secondary and caching servers.
#12. 0 STDIN, 1 STDOUT, 2 STDERR — what does it mean? they are the linux output STIN, that you write.STDOUT is the output, STDERR and the errors outputs.
#13. What is the name of the DNS record for IPv6?. IP Address??

### **Writing code**

#Task 1.
#
#There are two lists: you need to return the elements that are in the first list but are missing in the second. Describe the complexity of your solution using Big O Notation.

list_1 = [1,3,4,5,7,9]
list_2 = [1,3,5,7,9]
def ver_faltantes(list_1,list_2):
    set_list_1 = set(list_1)
    set_list_2 = set(list_2)
    result = set_list_1 - set_list_2
    return result

#Task 2.

#There is an array of integers. You need to remove the zeros from it. Only O(1) of additional memory can be used. Example**:**
array = [0,1,0,0,4,5,6,7,0,8,-4,0]
output = [1,4,5,6,7,8,-4]

def remove_zeros(arr):
    set_array = set(arr)
    salida =list(set_array)
    salida.remove(0)
    return salida

assert remove_zeros(array)==output

#![Снимок экрана 2022-10-22 в 18.47.09.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/716cdd57-2cf8-4519-914c-900fe4fcb145/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2022-10-22_%D0%B2_18.47.09.png)

#You can leave your answer as a link to your repository in GitHub.

#---

#Why do you want to become a Tutor in Practicum?. Beacouse i like to teach and a need a job

#What competencies do you think a good tutor in your profession should have? Explain your opinion. Give examples from your own experience. Continium study and always improve your skills

#Where did you study back-end development and how did you get into this profession?. selftaught.