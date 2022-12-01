## Introduction

Fitness API built with Flask and MySQL

## Setup

#### Clone repository

###### Windows - Mac - Linux

```
git clone repo_name
```

```
cd repo_name
```

#### Create virtual environment

###### Windows

Generate virtual environment

```
py -3 -m venv venv
```

Activate virtual environment

```
venv\Scripts\activate
```

Deactivate virtual environment

```
deactivate
```

###### Mac - Linux

Generate virtual environment

```
python3 -m venv venv
```

Activate virtual environment

```
. venv/bin/activate
```

Deactivate virtual environment

```
deactivate
```

#### Install required packages

###### Windows - Mac - Linux

```
pip install -r ./requirements.txt
```

#### Create your .env file for environment variables

Use the .env.example to make a .env file for the environment variables. Populate the variables with your local database information.

## Usage

###### Windows - Mac - Linux

#### Run App

```
flask --app ./main.py --debug run
```
