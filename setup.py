from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = '-e .'


def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements.
    input: file path of requirements.txt file
    output: List of libraries mentioned in the file
    '''

    requirements = []

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)

    return requirements


setup(
    name="ml_project",
    version="0.0.1",
    author="Aastha Tanwar",
    author_email="_____@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)