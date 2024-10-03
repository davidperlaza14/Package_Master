# Package Master 🚀

##  ***A Comprehensive Package Management and Automation System with JWT Authentication***


# Table of Contents

1. [Project Overview](#project-overview)
2. [Key Features](#key-features)
3. [Project Structure](#project-structure)
4. [System Requirements](#system-requirements)
5. [Getting Started](#getting-started)
   - [Clone the Repository](#clone-the-repository)
   - [Execution Example](#execution-example)
   - [Environment Setup](#environment-setup)
   - [Build the Docker Image](#build-the-docker-image)
   - [Run the Application](#run-the-application)
6. [Authentication](#authentication)
7. [Package Management](#package-management)
8. [Testing](#testing)
9. [Security](#security)
10. [Roadmap](#roadmap)
11. [Contributing](#contributing)
12. [License](#license)
13. [Contact](#contact)



## 📖 Project Overview
**Package Master** is an advanced system designed to simplify and automate the installation, upgrading, uninstallation, and listing of Python packages through a command-line interface (CLI). With robust JWT-based authentication, it ensures that only authenticated users can access or modify the packages. This project leverages Docker for containerization, making it easy to deploy, maintain, and scale across different environments.

## 💡 Key Features
1. **JWT-Based Authentication**: Secure access to the system with token-based authentication, ensuring only authorized users can perform operations.

2. **Package Management**: Perform the following actions with Python packages:

   * Install packages from PyPI.
    * Upgrade installed packages.
    * Uninstall packages.
    * List all installed packages.

3. **Database Integration**: Track package information through a connected database (configurable via environment variables).

4. **User-Friendly CLI**: A smooth and intuitive interface for managing Python packages with easy-to-follow prompts and feedback.

5. **Containerization with Docker**: Package Master is fully containerized using Docker, ensuring seamless deployment across various environments with consistent performance.

6. **Error Handling and Logging**: Robust error handling ensures all failures are logged, and users receive meaningful feedback to help them troubleshoot issues quickly.

## 📚 Project Structure
    .
    ├── docker-compose.yml       # Docker Compose for multi-container setup
    ├── Dockerfile               # Dockerfile to build the app environment
    ├── install_package.sh       # Bash script for installing packages
    ├── list_packages.sh         # Bash script for listing packages
    ├── README.md                # Project documentation
    ├── requirements.txt         # Project dependencies
    ├── setup_env.sh             # Script to setup environment variables
    ├── src
    │   ├── main.py              # Main script for package management
    └── tests
        ├── test_main.py         # Unit tests for the system


## 🛠️ System Requirements
To run Package Master, you’ll need the following:
* Python 3.8+: The project uses Python 3.8 or later.
* Docker: The app runs in a Docker container for easy setup and deployment.
* pip: To install, update, and manage Python packages.
* Git: For version control (optional).

## 🚀 Getting Started
### 1. **Clone the Repository**
    git clone https://github.com/yourusername/package-master.
    cd package-master

### Execution example:


### 2. Environment Setup
Set up your environment variables by running the setup_env.sh script. You can specify the DATABASE_URL for the system to use your preferred database.
    ``` 

    docker build -t package-master .

### 3. Build the Docker Image
Build the Docker image using the provided Dockerfile:
    ```
    
    docker build -t package-master .


    


### 4. Run the Application
Once the Docker image is built, use Docker Compose to spin up the application. 
   ```
   docker-compose up
   ```
This will start the application and expose it via the terminal where you can start managing your Python packages.


## 🔑 Authentication
The system uses JWT (JSON Web Tokens) for authentication. Each user must log in with their credentials to generate a token. The token is then used to authenticate further operations like installing or removing packages.

To log in, follow the prompt in the CLI:
```
    Username: admin
    Password: password123
```
After login, the system will return a JWT token which must be provided for any further package management operations.

## 📦 Package Management
Once authenticated, you can manage Python packages by selecting an option in the CLI interface:

* **Install Package**: Select an option to install any * **available package from PyPI.
* **Update Package**: Choose to update a specific package.
* **Uninstall Package**: Remove a specific package from the environment.
* **List Packages**: View all installed packages with version numbers.

Here’s an example of how the CLI interface looks:
```
Welcome to the Package Management System!
1. Install Package
2. Update Package
3. Uninstall Package
4. List Packages

Select an option: 1
Enter package name: requests
Paquete 'requests' instalado correctamente.
```



## 🔍 Testing
This project includes unit tests for all major functionalities. You can run tests using the following command:
```
pytest tests/test_main.py
```
Make sure to run tests regularly to ensure your system works as expected.

## 🛡️ Security

* **Token Expiration**: The JWT tokens generated have an expiration time, ensuring the security of the system. Users must re-authenticate after the token expires.
* **Error Handling**: Comprehensive error handling is implemented to provide meaningful feedback when errors occur (e.g., invalid credentials, expired tokens, etc.).


## 🗺️ Roadmap

* **Role-based Access Control (RBAC)**: Introduce roles (e.g., admin, user) to restrict specific operations to certain roles.
* **Web Interface**: Develop a web-based interface for easier management of packages via a browser.
* **Extended Package Management**: Add support for custom Python package repositories.
* **Multi-Language Support**: Extend support to package managers of other languages (e.g., npm, pipenv).

## 🤝 Contributing
Contributions are always welcome! Please follow the guidelines below to contribute:

1. Fork the repository.
2. Create a new feature branch.
3. Submit a pull request.

## 📝 License
This project is licensed under the MIT License. See the LICENSE file for details.

## 🌟 Contact
Feel free to contact me via email at davidperlaza1427@gmail.com if you have any questions or suggestions. Let’s build something amazing together!

# Sistema de Gestión de Paquetería con Autenticación JWT

Este proyecto es una CLI (Command Line Interface) que permite gestionar paquetes Python mediante comandos para instalar, actualizar, desinstalar y listar paquetes. La aplicación usa autenticación basada en tokens JWT para proteger el acceso a estas operaciones.


