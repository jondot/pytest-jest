from setuptools import setup

setup(
    name='pytest-jest',
    description='A custom jest-pytest oriented Pytest reporter',
    packages=['pytest_jest'],
    author='numirias, jondot',
    author_email='jondotan@gmail.com',
    version='0.2.0',
    url='https://github.com/jondot/pytest-jest',
    license='MIT',
    install_requires=[
        'pytest>=3.3.2',
        'pytest-metadata',
    ],
    entry_points={'pytest11': [
        'pytest_jest = pytest_jest.plugin',
    ]},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Framework :: Pytest',
    ],
)
