# MySite
MySite is a blog and review web application built with Django, containerized using Docker, and documented with Sphinx. Users can browse blogs and reviews, and registered users can log in to contribute their reviews. This platform ensures secure user authentication for content contribution.

## Table of Contents
- [Description](#description)
- [Features](#features)
- [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
    - [Running the Project](#running-the-project)
        - [Running Locally](#running-locally)
        - [Using Docker](#using-docker)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [License](#license)

## Description

MySite is a dynamic web application that serves as a blog and review platform.

- Users can browse public blogs and reviews without logging in.
- Registered users can log in to contribute by writing reviews or engaging with the content.
- Authentication ensures secure access to content contribution features.

## Features

- Browse blogs and reviews.
- User login is required to submit reviews.
- Secure user authentication and authorization.
- Deployment using Docker containers.
- Comprehensive Sphinx documentation.

## Getting Started

### Prerequisites

- **Python**: Version 3.8 or above.
- **pip**: Python package manager.
- **Docker**: Installed and running.
- **Git**: To clone the repository.

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/mysite.git
    cd mysite
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

### Running the Project

#### Running Locally

1. Apply migrations:
    ```sh
    python manage.py migrate
    ```

2. Create a superuser:
    ```sh
    python manage.py createsuperuser
    ```

3. Run the development server:
    ```sh
    python manage.py runserver
    ```

4. Open your browser and navigate to `http://127.0.0.1:8000/`.

#### Using Docker

1. Build the Docker image:
    ```sh
    docker build -t mysite .
    ```

2. Run the Docker container:
    ```sh
    docker run -d -p 8000:8000 mysite
    ```

3. Open your browser and navigate to `http://localhost:8000/`.

## Documentation

Documentation is generated using Sphinx. To build the documentation, navigate to the `docs` directory and run:
```sh
make html
```

## License

None
<hr>
*Note: This documentation is AI-assisted.*
