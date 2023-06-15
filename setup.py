from setuptools import setup,find_packages

setup(
    name='django_project_creator',
    version='1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts':['django-admin=django_project_creator.__init__:create_django_project']
    },
)