from setuptools import find_packages , setup
from typing import List


def get_requirements(file_path:str)-> list[str]:
    '''
    This function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if "-e ." in requirements:
            requirements.remove("-e .")

    return requirements

    '''
    This function will return the list of requirements
    '''

setup(
    name = 'End_to_End_machine_learning_project',
    version = '0.1.0',
    author = 'Om',
    author_email='omkalore11@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')

)