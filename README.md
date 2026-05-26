# JDEV 2026 Python Workshop



# RSA Encryption & Breaking Demo (Educational)

This project is an **educational Python workshop** designed to illustrate how RSA encryption works and why **small or poorly implemented RSA keys are insecure**.

The prime numbers are extracted from https://t5k.org/lists/small/millions/

# 1st step: Create the architecture:

To create the architecture of the package, the pythonfiles are inside the folder <package_name> and the README.md file is outside of it. __init__.py file is needed to make the folder a package and to be able to import automaticaly the modules inside it.

-> Move the scripts to the folder <package_name> and add __init__.py file

# 2nd step: Create the pyproject.toml file:

To create the pyproject.toml file, we need to specify the build system and the dependencies of the package. We will use setuptools as the build system and we will specify the dependencies in the install_requires section.

-> From the model complete the pyproject.toml file, change the name of the package and add the dependencies
