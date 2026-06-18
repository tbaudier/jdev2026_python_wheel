# JDEV 2026 Python Workshop

This project is a **Python workshop** designed to teach students how to create and publish a Python package on PyPI. The package is an educational demo of RSA encryption and breaking.

# RSA Encryption & Breaking Demo (Educational)

RSA encryption is a widely used public-key cryptographic system that allows secure communication over the internet. It is based on the mathematical properties of prime numbers and modular arithmetic. The security of RSA relies on the difficulty of factoring large composite numbers, which are the product of two large prime numbers.  
In this demo, we use a simple RSA encryption and breaking algorithm using Python, a list of prime numbers to generate the keys and encrypt a message and a simple algorithm to break the encryption by factoring the composite number and finding the private key.  
The prime numbers are extracted from https://t5k.org/lists/small/millions/

-> In Github, fork the repository. Do not forget to unselect "Copy the master branch only" to be able to access all branches.  

-> Clone the forked repository. Create a new virtual environment and install the package to test it.

```bash
deactivate
rm -rf rsa_demo_env
python -m venv rsa_demo_env
source rsa_demo_env/bin/activate  # On Windows: rsa_demo_env\Scripts\activate
pip install --upgrade pip setuptools
pip install numpy
cd jdev2026_python_wheel
python decrypt_rsa.py
```

We will repeat the creation of a new virtual environment and the installation of the package several times during the workshop to test the package at different stages of its development. It's a good practice to create a new virtual environment for each test to avoid any issues with dependencies and to have a clean environment. Create the virtual environment in another folder to avoid any issues with relative paths.  
The line pip install --upgrade pip setuptools is also important to avoid any issues when building the package with an old version of pip or setuptools.

The code "decrypt_rsa.py" starts to encrypt the message "Hello" with your public key (n and e in the code). You can see in the next window, the encrypted message as you receive from the internet. As you have the private key (d in the code), you can decrypt the message and see the original message.  
But, as a hacker you do not have access to the private key, so you want to try to break the encryption and find the private key. The function "break_rsa_with_primes" try to break the encryption by factoring the composite number n using a list of available prime numbers, and finding the private key d.  
When d is found, the script decrypt the encrypted message and display it in the last window.

# 1st step: Create the architecture:

To create the architecture of the package, the python files are inside the folder <package_name> and the README.md file is outside of it. `__init__.py` file is needed to make the folder a package and to be able to import automaticaly the modules inside it.  

-> From the branch workshop_starting_point, move the scripts to the folder <package_name> with your name, add `__init__.py` files.  

-> For the data "primes.npz", move them to the folder <package_name>/data and change the path in decrypt_rsa.py. Do not forget the `__init__.py` file. You can use the following code to load the data from the package:

```python
from importlib.resources import files
data_path = files("jdev2026_python_wheel_XXXXXX.data") / "primes.npz"
primes = np.load(data_path).tolist()
```

# 2nd step: Create the pyproject.toml file:

pyproject.toml is a configuration file used to create wheels. It is used to specify the build system and the dependencies of the package. It is a standard file that is used by all Python packages. It is also used to specify the metadata of the package, such as the name, version, description, etc.  

-> From the model, complete the pyproject.toml file, change the name of the package (be aware of `_` and `-`) and add the dependencies (here numpy). For information, the line in `decrypt_rsa.py`: `from helpers import` became `from .helpers import` to be able to import the module from the package.  

-> First try to build the package (see step 5).

# 3rd step: Add the entry point to the package:

For the moment, we can only run the scripts by importing them in a python file as a librairy or in the terminal. We cannot run them directly from the terminal.  
To be able to run the scripts directly from the terminal, we need to add an entry point to the package. An entry point is a command that is executed when we run a specific command in the terminal. For example, if we want to run the script `decrypt_rsa.py` by running the command `decrypt_rsa` in the terminal, we need to add an entry point for this command.  
To add the entry point to the package, we need to specify the entry point in the `pyproject.toml` file. We will use the scripts section to specify the entry point of the package.  

-> Uncomment and complete the lines in the pyproject.toml related to scripts. Here the entry point is `decrypt-tool`

# 4th step: Add the data files to the package:

For the moment, the data files are not included in the package, we need to add them to the package to be able to load them from the package.  
To add the data files to the package, we need to specify the data files in the `MANIFEST.in` (for the archive) and `pyproject.toml` (for the wheel) files.  

-> Create a `MANIFEST.in` file, complete it to include the data files in the archive. You can use the following lines:

```
include LICENSE
include README.md
include jdev2026_python_wheel_XXXXXXXX/data/*.npz
```

-> Uncomment and complete the lines in the `pyproject.toml` related to package-data. This is important to include the data files in the wheel.

# 5th step: Build the package locally:

In a new virtual envienvironment, we can try to build the package locally with the following commands:

```bash
pip install build
python -m build
ls dist
```

This will create a dist folder with the built package. We can then install the package locally using pip:

```bash
pip install dist/<package_name>-<version>.whl
```

# 6th step: Test the package:

To test the package, it's better to create a new virtual environment and install the package in it. Then we can run the entry point (here `decrypt-tool`) of the package to see if it works correctly.

```bash
pip install dist/<package_name>-<version>.whl
<entry_point_command>
```

# 7th step: .gitignore file:

No, we are able to build the wheel locally and, we can commit and push the code to the Github repository.  
There is a lot of files that are generated when we build the package, we don't want to commit them to the repository. We can create a .gitignore file to ignore these files.  

-> Create a .gitignore file and add the files and folders that you want to ignore. Do not forget to ignore .gitignore file itself.

-> Commit and push everything to the forked Github repository

# 8th step: Publish the package on PyPI:

To publish the package on PyPI (test), you need to create an account on test PyPI (https://test.pypi.org/). First we can try to upload the wheel manually on test PyPI. Start to create your API token: in "Account Settings", you can find the API token section. Create a new API token with a name and for the moment a scope for the entire account. Copy it in a safe place, we will use it later.

-> Then tag the version of your package in the pyproject.toml (0.2.0 because 0.1.0 already exists) and with git:

```bash
git commit -a -m "update version to 0.2.0"
git tag -a 0.2.0 -m "tag 0.2.0"
git push
git push --tags
python -m build
```

Finally run the following commands to upload the wheel on pypi:

```bash
pip install twine
twine upload --repository testpypi dist/* # paste your API token if needed
```

# 9th step: Automatization with Github Actions:

To automatize the build and publish process, we can use Github Actions. We can create a workflow that will be triggered when we push a new commit or a new tag to the repository. The workflow will build the package and publish it on test PyPI. You will need to create a secret in the Github repository settings (settings/secrets/actions) to store your API token for test PyPI. Click on "New repository secret" and add a name (TEST_PYPI_API_TOKEN) and the value (your API token).

-> From the model, complete the file .github/workflows/create_wheel.yml and modify it to fit your package and branch name. You will need to add your API token as a secret in the Github repository settings called TEST_PYPI_API_TOKEN.   Commit, and push everything on Github and check if the workflow is triggered and if the package is published on test PyPI. Maybe tag a new version of your package to trigger the workflow.  
Maybe you need to change the default branch in the settings of the repository to the branch where you are working (workshop_starting_point) to be able to trigger the workflow when you push a new tag (Github security).

# Last step: Test everything:

To test the automatization, you can create a new tag and push it to the repository (see step 8). This will trigger the workflow and publish the package on test PyPI. Then you can create a new virtual environment and install the package from test PyPI to see if it works correctly.

```bash
python -m venv test_env
source test_env/bin/activate  # On Windows: test_env\Scripts\activate
pip install --upgrade pip setuptools
pip install --index-url https://test.pypi.org/simple/ <package_name>
<entry_point_command>
```

# Appendix:

The automatization can also be done with Gitlab with Build/Pipelines section. You have an example in `.gitlab-ci.yml`. You can copy paste your PyPI API token in Settings/CI/CD/Variables/Add Variable.

A usefull tool I like is cibuildwheel (https://github.com/pypa/cibuildwheel). It allows to build wheels for multiple platforms (Windows, MacOS, Linux) and multiple Python versions. It can be used in Github Actions or Gitlab CI/CD. It's also very usefull when you need to compile C++ code in your package: the librairies are automatically "delocated".
