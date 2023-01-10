# dover

Take-Home test for Systech Unitrace Applicants:

“Create an Address Book CRUD application utilizing Django and Python. You are free to use any Python or Django library as well as any JavaScript UI framework. Application should:

•	Have Authentication. All functionality should be username and password protected.

•	Error handling. 

•	Log all SQL statements. Do not use the logger

•	Add functionality that will show your abilities in Django and/or Python

•	Make the project reproducible to another developer or server deployable. Provide instructions on how one would start using your application.

Note: do not spend too much time on CSS. We are looking for functionality.”


# Dover App

## Python setup

Install or update [Python](https://www.python.org/downloads/) version >=3.6

*`Pip` is also needed (comes with Python installation)*

### Run the server

1. open a terminal
2. go to the Python exercise directory
3. run `[pip][pip3] install virtualenv` to install it. It is used to create isolated Python environments
4. run `virtualenv venv` to create the venv environment
5. Activate virtual environment:
   - On **Windows** run `venv\Scripts\activate.bat`  (*`deactivate.bat` to deactivate the environment*).
   - On **Linux** run `source env/bin/activate`      (*`deactivate` to deactivate the environment*)
6. run `[pip][pip3] install -r requirements.txt` to install the needes packages if you didn't before
7. run `python .\manage.py migrate`
7. run `python .\manage.py makemigrations`
8. run `python .\manage.py runserver` to start the Application
10. Open your browser and type [http://localhost:8000/](http://localhost:8000/) to see and use the Application
