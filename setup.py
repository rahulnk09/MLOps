from setuptools import find_packages,setup
from typing import List


def get_requirements(file_path:str)->List[str]:
    req=[]

    with open(file_path) as f:
        req=f.readlines()
        req=[r.replace('\n',"") for r in req]
    
    if "-e ." in req:
        req.remove("-e .")
    
    return req

setup(
    name='mlProject',
    version='0.0.1',
    author='RahulN',
    author_email='rahulnakkazz@gmail.com',
    packages=find_packages(),
    requires=get_requirements('requirements.txt')

)