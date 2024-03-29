## Table of Contents
1. [General Info](#general-info)
2. [Installation and run](#installation)

### General Info
***
This application was created to help players of a chess club to manage their tournaments and their results.

### Installation and run
***
Please follow the instructions below to use and run the application :

1. Clone the repository :
```
$ git clone https://github.com/antoinekk/chess-tournament-python.git <your path>
```

2. Go into the folder of the repository :
```
$ cd ../path/to/the/folder
```

3. Create a virtual environment :
```
$ python -m venv env
```

4. Activate your environment :
```
$ source env/bin/activate
```

5. Install python modules:
```
$ pip install -r requirements.txt
```

6. Run the "main.py" file:
```
$ python3 main.py
```

7. Follow instructions :
```
Here the menu of the application is displayed in your terminal.
You just have to follow the instructions to create tournament/players, run a tournament or generate a report.
```

8. Run a flake8 report:
```
$ flake8 --max-line-length=119 --format=html --htmldir=flake-report
```
