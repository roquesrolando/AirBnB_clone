# **AirBnB clone - The console**
## Description:
The console is a command interpreter for our AirBnB clone limited to methonds we create like manage, retrieve, update and delete objects from a file, database, etc.
## Instructions:
To start your console execute the console.py file and press enter as shown:
```
$ ./console.py
(hbnb)
```
As described before once inside the console the user will be able to:

    create
    destroy (delete)
    show
    update


You can see all commands available by typing the help command as seen below:
```
$ ./console.py 
(hbnb) help
```
## Avaliable commands:
### create:
Creates a new class instance, if sucessful it prints 
the ID of the new instance.
```
$ ./console.py
(hbnb) create <classname>
```
### destroy:
Destroys and instances based on the given class and ID
```
$ ./console.py
(hbnb) destroy <classname> or <id>
```
### all:
Prints all objects of a certain type, or all objects if no Class 
was specified.
```
$ ./console.py
(hbnb) all <classname> or none
```
### update:
 Updates an instance based on the Class name and ID by adding
or updating an attribute
```
$ ./console.py
(hbnb) update <classname> <id> <attribute> <value>
```
### show
Shows the string representation of an instance based on the
given Class and ID
```
$ ./console.py
(hbnb) show <classname> <id>
```
## Unittest:
The command to run all the unitest in the /test directory is as such:
```
$ python3 -m unittest discover test
```
## JSON:
In this project we serialize and store dictionary in file.json 
using the json format. Once the program has stored it we can 
deserialize it from file.json and reloade it as a dictionary 
for our purposes

