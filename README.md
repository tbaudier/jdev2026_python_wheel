# JDEV 2026 Python Workshop



# RSA Encryption & Breaking Demo (Educational)

This project is an **educational Python workshop** designed to illustrate how RSA encryption works and why **small or poorly implemented RSA keys are insecure**.

The prime numbers are extracted from https://t5k.org/lists/small/millions/

-> Fork and clone the repository. Create a new virtual environment and install the package to test it.

```bash
python -m venv rsa_demo_env
source rsa_demo_env/bin/activate  # On Windows: rsa_demo_env\Scripts\activate
pip install numpy
decrypt_rsa.py
```

# 1st step: Create the architecture:

To create the architecture of the package, the pythonfiles are inside the folder <package_name> and the README.md file is outside of it. __init__.py file is needed to make the folder a package and to be able to import automaticaly the modules inside it.

-> Move the scripts to the folder <package_name> with your name, add and complete __init__.py file and change the path of the data to be able to load it from the package.

# 2nd step: Create the pyproject.toml file:

To create the pyproject.toml file, we need to specify the build system and the dependencies of the package. We will use setuptools as the build system and we will specify the dependencies in the install_requires section.

-> From the model complete the pyproject.toml file, change the name of the package and add the dependencies

-> Fist try to build the package (see step 5 and 6).

# 3rd step: Add the data files to the package:

To add the data files to the package, we need to specify the data files in the MANIFEST.in (for the archive) and pyproject.toml (for the wheel) files. 

-> Create a MANIFEST.in file, complete it to include the data files in the archive. Modify also the pyproject.toml.

# 4th step: Add the entry point to the package:

To add the entry point to the package, we need to specify the entry point in the pyproject.toml file. We will use the entry_points section to specify the entry point of the package.

-> Complete the pyproject.toml file to add the entry point of the package.

# 5th step: Build the package locally:

To build the package locally, we need to run the following command in the terminal:

```bash
pip install build
python -m build
ls dist
```

This will create a dist folder with the built package. We can then install the package locally using pip:

```bash
pip install dist/<package_name>-<version>.whl
```

It's better to have a recent version of pip and setuptools to avoid any issues when building the package. You can upgrade them using the following command:

```bash
pip install --upgrade pip setuptools
```

# 6th step: Test the package:

To test the package, it's better to create a new virtual environment and install the package in it. Then we can run the entry point of the package to see if it works correctly.

```bash
python -m venv test_env
source test_env/bin/activate  # On Windows: test_env\Scripts\activate
pip install dist/<package_name>-<version>.whl
<entry_point_command>
```

# 7th step: .gitignore file:

There is a lot of files that are generated when we build the package, we don't want to commit them to the repository. We can create a .gitignore file to ignore these files.

-> Create a .gitignore file and add the files and folders that you want to ignore. Do not forget to ignore .gitignore file itself.

# 8th step: Publish the package on PyPI:

To publish the package on PyPI (test), you need to create an account on test PyPI (https://test.pypi.org/). In "Account Settings", you can find your API token. Then tag the version of your package and then run the following command:

```bash
git tag -a 0.1.0 -m "tag 0.1.0"
git push --tags
pip install twine
twine upload --repository testpypi dist/*
```

# 9th step: Automatization with Github Actions:

To automatize the build and publish process, we can use Github Actions. We can create a workflow that will be triggered when we push a new commit or a new tag to the repository. The workflow will build the package and publish it on test PyPI. You will need to create a secret in the Github repository settings (settings/secrets/actions) to store your API token for test PyPI.

-> Copy the file .github/workflows/publish.yml from the model and modify it to fit your package. You will need to add your API token as a secret in the Github repository settings called TEST_PYPI_API_TOKEN. Push everything on Github and check if the workflow is triggered and if the package is published on test PyPI.
