from setuptools import setup, find_packages

setup(
    name='research_project_template',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy', 'torch', 'pyyaml',  # etc.
    ],
)
