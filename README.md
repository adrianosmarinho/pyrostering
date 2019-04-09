# PyRostering

A simple rostering application written in Python and Django.

## Installation

To run PyRostering locally, you will need:

- Python 3.6 or greater;
- Django 2.1 or greater;

Then, using a command-line prompt, clone the repository and navigate to root folder and run:

```console
> python manager.py runserver
```

Note that you might need to run python manager.py migrate before. The server should warn you about that.

Once the server is running, type http://127.0.0.1:8000/rostering/ (or whatever local ip adress your server gives to you) to go to the PyRostering webpage.

## Usage

Currently PyRostering is very simple. The home page will allow you to create new employees and also to see a list of employees.
For each employee you can create a new shift. You can access the shifts of the employees by clicking on "view details" in the list of employees.

## ER Diagram for the PyRostering Database

The ER Diagram for the PyRostering database can be found in:
https://github.com/adrianosmarinho/pyrostering/blob/master/docs/images/erdiagram.png

## Where to from here

There are a few things to improve that I am currently work on.

### Backend

- Shift validation: the specification required some minimal rules like no more than 5 consecutives shifts in a week or at least 10 hours of rest over night. That is my priority for the next iterations.
- Shift validation includes form validation and proper display of custom error messages.
- Support for an external mathematical module: I want to build a prototype of that by calling a module that reads the example data spreadsheets and automatic populate the database of PyRostering. Then, the same architecture can be used to call an external mathematical module.

### Frontend

- Using css and bootstrap to improve the look and feel of PyRostering.

### Deployment

- I am currently checking how to deploy properly using Heroku.
