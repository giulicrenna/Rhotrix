from setuptools import setup, find_packages

setup(
    name='rhotrix',
    version='0.1.0',
    description='A Python library to implement and manipulate Rhotrix matrices.',
    author='Giuliano Crenna',
    author_email='giulicrenna@gmail.com',
    url='https://github.com/giulicrenna/rhotrix',  # Replace with the actual URL of your repository
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
)