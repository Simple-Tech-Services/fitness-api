### Dependencies

- Flask

## Setup

###### Windows

#### Make Repo

```
git clone repo_name
```

```
cd repo_name
```

### Create a virual enviroment

```
py -3 -m venv venv
```

Activate Script

```
venv\Scripts\activate
```

deactive virtual enviroment

```
deactivate
```

#### Install required packages

```
pip install -r ./requirements.txt
```

#### Create your .env file for enviroment variables

Use the .env.example to make a .env file for the enviroment variables

## Usage

#### Run App

```
flask --app ./main.py --debug run
```
