from setuptools import setup, find_packages

requires = [
    'Flask==1.0.2',
    'Werkzeug==0.14.1',
    'Click==7.0',
    'itsdangerous==1.1.0',
    'Jinja2==2.10',
    'MarkupSafe==1.0',
    'colander==1.5.1 ',
    'Flask-Cors==3.0.9',
    'Flask-SQLAlchemy==2.3.2',
    'Flask-Migrate == 2.3.0',
    'psycopg2 == 2.7.6.1',
    'passlib == 1.7.1',
    'Flask-Login == 0.4.1',
    'SQLAlchemy==1.3.1',
    'marshmallow==2.13.5',
]

setup(
    name='d-growth',
    version='1.0',
    description='d-growth',
    author='Unkown',
    author_email='unknown@jameswatson.tkneih',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    tests_require=requires,
)
