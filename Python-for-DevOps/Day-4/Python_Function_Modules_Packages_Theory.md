

*** Python Functions, Modules, and Packages:-

1. Differences Between Functions, Modules and Packages......

*** Function:- A function in python is a block of code that performs a specific task.
               Functions are defined using the "def" keyword and can take inputs,
               called arguments. They are a way to encapsulate and reuse code.

*** Modules:-  A module is a Python script containing Python code. It can define 
               functions, classes, and variables that can be used in other Python scripts. Modules help organize and modularize your code, making it more maintainable.

*** Packages:- A package is a collection of modules organized in directories. Packages 
               help you organize related modules into a hierarchy. They contain a special
               file named "__init__.py", which indicates that the directory should
               be treated as a package.


2. How to Import a Package.....

==>> Importing a package or module in python is done using the "import" statement.
     You cam import the entire package, specific modules, or individual functions/variables
     from a module.


3. Python Workspaces.....

==>> Python workspaces refer to the environment in which you develop and run your Python 
     code. They include the Python interpreter, installed libraries, and the current working directory. Understanding workspaces is essential for managing dependencies and code organization.

==>> Python workspaces can be local or virtual environments. A local environment is the 
     system-wide Python installation, while a virtual environment is an isolated environment for a specific project. You can create virtual environments using tools like "virtualenv" or "venv".

# Example:-
      
       # Create a virtual environment
           ==>> python -m venv myenv

       # Activate the virtual environment (on windows)
           ==>> myenv\Scripts\activate

       # Activate the virtual environment (on macOS/Linux)
          ==>> source myenv/bin/activate

           
