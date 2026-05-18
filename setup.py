from setuptools import setup,find_packages
from typing import List

hypen= '-e .'
def get_req(file_path:str)->List[str]:

    reqments=[]
    with open(file_path) as file_obj:
        reqments=file_obj.readlines()
        reqments=[req.replace("\n"," ") for req in reqments]
        
        if hypen in reqments:
         reqments.remove(hypen)

    return reqments 



setup(
name="etoe_ml",
version= '1.1',
 author= None,
 author_email = 'vanshikasharma01122004@gmail.com',
 packages=find_packages(),
 install_requires=get_req('requirement.txt')

)