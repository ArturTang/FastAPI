from setuptools import setup

setup(
    name='server_app',
    version='0.0.1',
    author='Artur Tangatarov',
    author_email='arturdommer@gmail.com',
    description='FastApi app',
    install_requires=[
        'uvicorn==0.15.0',
        'fastapi==0.70.0',
        'SQLAlchemy==1.4.26',
        'pytest==6.2.5',
        'requests==2.26.0',
    ],
    scripts=[
        'app/main.py',
        'scripts/create_db.py'
    ]
)
