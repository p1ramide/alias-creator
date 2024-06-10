from setuptools import setup, find_packages

setup(
    name='alias_creator',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'alias_creator=alias_creator.main:main',  
        ],
    },
    url='https://github.com/p1ramide/alias-creator.git',  
    author='p1ramide',
    description='A simple tool to create aliases in the shell and reload .bashrc',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
