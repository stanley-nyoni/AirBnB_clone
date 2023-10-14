# AirBnB clone - The console

## Description

This project is an implementation of a command-line interface (CLI) for an AirBnB clone. It allows users to create, manage and interact with varoius objects.
The project is structured around classes that inherit from a BaseModel, and a FileStorage system that handles object serialization and deserialization to a JSON file.

## Command Interpreter

**Starting the command interpreter**
To start the AirBnB Clone console, you can run the console.py script. You can do this by executing the following command:

```./console.py```

**Using the Command Interpreter**
The AirBnB Clone command interpreter provides various commands for managing and interacting with objects. Some of the key commands include:

- CREATE 
Creates a new instance of a specified class, saves it, and prints its ID.

**Usage**
``` (hbnb) create BaseModel```

- SHOW
 Displays the string representation of an instance based on class name and ID.

 **Usage**
 ``` (hbnb) show BaseModel 1234-5678```

 - DESTROY
 Deletes an instance based on class name and ID.

 **Usage**
 ```(hbnb) destroy BaseModel 1234-5678```

- ALL
Lists all instances or instances of a specific class.

**Usage**
```(hbnb) all BaseModel```

- UPDATE 
Updates the attributes of an instance based on class name and ID.

```(hbnb) update BaseModel 1234-5678 email "new@email.com"```

- QUIT / EOF
 Exits the command interpreter.

 **Usage**
 ```(hbnb) quit```

- HELP
Prints the information or documentation about the available commands and their usage within the interpreter

**Usage**
```(hbnb) help```

