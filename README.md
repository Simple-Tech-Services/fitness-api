## Introduction

Fitness API built with Flask and MySQL

## Setup

### 1. Clone repository

Windows - Mac - Linux

```
git clone https://github.com/Simple-Tech-Services/fitness-api.git
```

```
cd https://github.com/Simple-Tech-Services/fitness-api.git
```

### 2. Create a virtual environment with venv

Generate virtual environment Windows

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

Generate virtual environment on Mac or Linux

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

### 3. Install required packages

```
pip install -r ./requirements.txt
```

#### Create your .env file for environment variables

Use the .env.example to make a .env file for the environment variables. Populate the variables with your local database credential.

## Usage

On Windows

```
py -3 run.py
```

On Mac or Linux

```
python3 run.py
```
