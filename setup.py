from setuptools import setup, find_packages

import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

def read(filename):
    with open(os.path.join(BASE_DIR, filename)) as file:
        return file.read()


setup(name='livescore_client',
      version='0.1',
      description='Client-Server SDK for LiveScore',
      long_description= read('README.rst'),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6.1',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content,
      ],
      keywords='livescore api',
      url='https://github.com/Livescore-api/sdk-python',
      author='SuperMario',
      author_email='will_add_something__here@gmail.com',
      license='MIT',
      packages=find_packages(),
      install_requires=[
          'markdown',
      ],
      include_package_data=True,
      zip_safe=False)
