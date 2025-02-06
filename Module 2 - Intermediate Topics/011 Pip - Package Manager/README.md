![Cover image](https://media.licdn.com/dms/image/v2/D5612AQHAUKwDFm3oxg/article-cover_image-shrink_720_1280/article-cover_image-shrink_720_1280/0/1695482293859?e=2147483647&v=beta&t=D2MqjYLj9jOAcOrXCXVRlzKVvRF16HE0hgg4yy3p678)

# Lecture 11: Package Managers

## Packages, Libraries, Modules, and Frameworks: The Differences
First, understand some core differences.

- **Module**:  
  A module is a single Python file containing functions, classes, or variables. It is the smallest unit of code reuse.  
  *Example*: A file named `math_utils.py` that contains a function to calculate the factorial.

- **Package**:  
  A package is a collection of related modules organized in a directory with an `__init__.py` file. This structure helps in organizing code into a hierarchical namespace.  
  *Example*: A package named `data_processing` that contains modules like `cleaning.py`, `transform.py`, and `visualize.py`.

- **Library**:  
  A library is a collection of packages and modules that provides a wide range of functionalities. Libraries are created to be reused in various projects.  
  *Example*: NumPy is a library that provides numerical computing functions, and it contains several packages and modules.

- **Framework**:  
  A framework is a collection of libraries and tools that provides a specific structure and guidelines to build applications. Frameworks often dictate the architecture of the application.  
  *Example*: Django is a web framework that includes many built-in libraries and modules to help build web applications.

---

### 1. What are Packages?
A Python package is a way of organizing related modules into a single directory hierarchy. It allows for a hierarchical file structure that is easy to navigate and manage. A package contains all the files you need for a module. 
*Example:*

my_package/
|-- __init__.py  
|-- module1.py  
|-- module2.py  
|-- subpackage/  
|----- __init__.py  
|----- module3.py


### 2. What Are Package Managers?

Package managers are tools that automate the process of installing, upgrading, configuring, and removing software packages. They are essential in managing dependencies for your projects and ensuring that you have the correct versions of libraries installed.

**Examples of Package Managers**:
- **pip**: The most widely used package manager for Python.
- **conda**: An open-source package management system and environment management system that runs on Windows, macOS, and Linux.
- **npm**: Used for JavaScript, though mentioned here for context as a package manager in other ecosystems.
- **UV**: `uv` is a fastest Python package and project manager, written in Rust.
- **poetry**: Poetry comes with an exhaustive dependency resolver, which will always find a solution if it exists.

---

**NOTE:**  
You can search for Python packages on the Python Package Index (PyPI), which is a repository of software packages developed and maintained by the Python community. https://pypi.org/



### 3. Detailed Look at pip

**pip** is the de facto package manager for Python. PIP is Python’s default package manager. This comes pre-installed after Python 3.4

Here are the key details and common commands:

#### a. Checking if pip Is Installed

Open your terminal or command prompt and type:
```bash
pip --version
```
If pip is installed, it will display the version number. If not, you may need to install it or ensure that Python is correctly installed.

#### b. Installing a Package Using pip

To install a package, use the command:
```bash
pip install package_name
```
*Example*: Installing the `requests` library:
```bash
pip install requests
```

You have to enter this command in your terminal or CMD and press Enter. This command tells the Python Package Installer (pip) to download and install the MyPackage package from the Python Package Index (PyPI).

#### c. Uninstalling a Package Using pip

To uninstall a package, use:
```bash
pip uninstall package_name
```
*Example*: Uninstalling the `requests` library:
```bash
pip uninstall requests
```

#### d. Listing Installed pip Packages

To see all packages installed in your current environment:
```bash
pip list
```
This command displays a list of packages along with their versions.

#### e. Creating and Sharing Your Own Packages

You can create your own package by organizing your modules in a directory with an `__init__.py` file. Once your package is ready:
- **Create a setup.py File**: This file includes metadata about your package.
  ```python
  # setup.py
  from setuptools import setup, find_packages

  setup(
      name="your_package_name",
      version="0.1",
      packages=find_packages(),
      install_requires=[],  # List dependencies here
      author="Your Name",
      author_email="your.email@example.com",
      description="A short description of your package",
  )
  ```
- **Build and Distribute**: Use tools like `setuptools` to build your package, and then publish it on PyPI (Python Package Index) so others can install it using pip.

For now this is beyond the scope. [Find details here.](https://packaging.python.org/en/latest/tutorials/packaging-projects/)

---

### 4. Virtual Environments with venv

Virtual environments are isolated Python environments that allow you to manage project-specific dependencies without interfering with the system-wide packages.

#### Creating a Virtual Environment

In your project directory, run:
```bash
python -m venv venv
```
This command creates a new directory named `venv` that contains the virtual environment.

#### Activating the Virtual Environment

- **Windows**:
  ```bash
  venv\Scripts\activate
  ```
- **macOS/Linux**:
  ```bash
  source venv/bin/activate
  ```

Once activated, your terminal prompt will change, indicating that you are now working within the virtual environment.

#### Deactivating the Virtual Environment

To deactivate, simply run:
```bash
deactivate
```

---



### Exercises

1. **pip Practice**:  
   - Verify your pip installation and install the `numpy` package. Then, list all installed packages to confirm the installation.

2. **Create Your Package**:  
   - Create a simple package named `greetings` with a module that defines two functions: `hello()` and `goodbye()`. Write a `setup.py` file and simulate installing it in a virtual environment.

3. **Virtual Environment Setup**:  
   - Create a new virtual environment for a project, activate it, and install the `requests` package inside that environment. Then, list the installed packages and deactivate the environment.

---

### Conclusion

Package managers like pip, along with virtual environments (via venv), play a critical role in modern Python development. They enable you to manage dependencies, share your own code as packages, and maintain clean, isolated project environments. Understanding these tools and the differences between modules, packages, libraries, and frameworks is essential for writing scalable and maintainable Python applications. Practice the exercises to become proficient with these concepts, and you’ll be well-prepared for managing larger projects and collaborative development. Happy coding!


[![Prev Lecture](../../Previous.png)](https://github.com/wasiqs-classics/Python-Lectures-Github/tree/master/Module%202%20-%20Intermediate%20Topics/010%20Modules)       [![Next Lecture](../../Next.png)](https://github.com/wasiqs-classics/Python-Lectures-Github/tree/master/Module%202%20-%20Intermediate%20Topics/012%20Some%20Important%20Packages)
