# AirBnB clone - The console

![](https://upload.wikimedia.org/wikipedia/commons/6/69/Airbnb_Logo_Bélo.svg)

**AirBnB clone project**  is a replica of the famous **AirBnb** solution, it doesn't include all features but only the basics one. the user can interact with this replica using only CLI instead of graphic interface.

## how to start it ?

you can start using this project by running the console.py
After changing the current directory to the folder "AirBnB_clone" , just type in your terminal :
~/AirBnb$ ./console.py\
(hbnb) help

##### Documented commands (type help <topic>):
##### ========================================
EOF  help  quit

(hbnb) \
(hbnb) help quit\
Quit command to exit the program\
\
(hbnb) \
(hbnb) \
(hbnb) quit


## how to use it ?

once the console is started, you can type one of the commands bellow to intercat with program:
- **quit** : to quit the program
- **create [class name]** : Creates a new instance of particular class, saves it (to the JSON file) and prints the id.\
  Ex: $ create BaseModel.
-  **show** : Prints the string representation of an instance based on the class name and id.\
   Ex: $ show BaseModel 1234-1234-1234.
- **destroy** : Deletes an instance based on the class name and id (save the change into the JSON file).\
   Ex: $ destroy BaseModel 1234-1234-1234.
- **all [class name]** : Prints all string representation of all instances based or not on the class name.\
   Ex: $ all BaseModel or $ all.
- **update** :  Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file).\
 Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".
- **count [class name]** : Counts instances number of the given class name.
## Examples :
~/AirBnb_clone$ ./console.py\
(hbnb) all MyModel\
** class doesn't exist **\
(hbnb) show BaseModel\
** instance id missing **\
(hbnb) show BaseModel My_First_Model\
** no instance found **\
(hbnb) create BaseModel\
49faff9a-6318-451f-87b6-910505c55907\
(hbnb) all BaseModel\
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}"]
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907\
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"\
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907\
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}
