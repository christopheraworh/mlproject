from setuptools import find_packages,setup
from typing import List


HYPHEN_e_DOT = '-e .'
def get_requirements(file_path:str) -> List[str]:
    '''
    This fucntion will return the list of requirments
    '''

    requirements =  []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements =  [req.replace('\n','') for req in requirements]

        if  HYPHEN_e_DOT in requirements:
            requirements.remove(HYPHEN_e_DOT)
    return requirements
setup(
    name = 'mlproject',
    version = '0.0.1',
    author = 'Christopher',
    author_email= 'chidiaworh@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')

)