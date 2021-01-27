from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
   name='fastapi-example',
   version='0.1',
   description='A simple fastapi application',
   license="MIT",
   long_description=long_description,
   author='Kais Bettaieb',
   author_email='kaisbettaieb@gmail.com',
   url="https://kaisbettaieb.me/",
   packages=['fastapi_example'],
   install_requires=['fastapi[all]'],

)