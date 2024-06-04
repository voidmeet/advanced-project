from setuptools import setup, find_packages

setup(
    name='advanced_project',  # Replace with your actual package name
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'flask',  # List your dependencies here
    ],
    author='meet',
    author_email='your.email@example.com',
    description='A simple example package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/voidmeet/advanced-project.git',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
