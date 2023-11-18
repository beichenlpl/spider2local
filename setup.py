from setuptools import setup, find_packages

setup(
    name='spider2local',
    author_email='beichenlpl@foxmail.com',
    version='0.1.1',
    packages=find_packages(),
    url='https://github.com/beichenlpl/spider2local',
    install_requires=[
        'requests',
        'bs4',
    ]
)
