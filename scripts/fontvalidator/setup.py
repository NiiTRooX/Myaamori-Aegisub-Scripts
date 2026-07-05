from setuptools import setup

setup(
    name='fontvalidator',
    version='0.1.0',
    py_modules=['fontvalidator'],
    install_requires=['ass', 'fonttools', 'ebmlite', "rich"],
    entry_points={
        "console_scripts": ["fontvalidator=fontvalidator:main"]
    }
)
