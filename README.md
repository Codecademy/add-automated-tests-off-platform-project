# BankAccount
This is an educational public repository to illustrate the power of automated testing through Github Actions.

## Run locally
1. Set up Python virtual environment.
```
python -m venv venv
```
2. Install required dependencies.
```
pip install -r requirements.txt
```
3. Run unit tests.
```
python -m pytest
```
4. Run the app.
```
python app.py
```

## Code Description

1. app.py: A flask application that exposes the following API endpoints: 
  - index at / : Retun a JSON data structure indicating the current balance. 
  - deposit at /deposit : Take the deposit amount as a URL parameter and return the new balance after adding the amount. 
  - withdraw at /withdraw : Take the withdrawal amount as a URL parameter and return the new balance after subtracting the amount. 
App relies on a global in-memory variable (`balance`) to store the balance of the account.

2. requirements.txt: A text file including all the Python libraries and packages needed to run the app. 

3. .gitignore: Refer to the gitignore article for more details. In short, this file makes it possible that local configuration or binary files are not pushed to the repository. 

4. tests: It's a directory that includes several unit tests for the APIs. The tests utilize the PyTest library.