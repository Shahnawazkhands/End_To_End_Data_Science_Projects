from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .' ### If we want to run and make packages by using requirements.txt file

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of all requirements
    '''
    requirements=[]

    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[i.replace('\n',"") for i in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
name='End To End Data Science Projects',
version='0.0.3',
author='Shahnawaz',
author_email='4ushahnawazkhan@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)