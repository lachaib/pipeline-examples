from setuptools import setup

setup(name='myApp',
      version='0.0.1',
      description='Sample App',
      install_requires=['flask',
                        'flask-pymongo',
                        'pymongo',
                        'jinja2'],
      packages=['src']
      )
