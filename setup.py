from setuptools import find_packages, setup


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='waitgroup',
    version='0.0.1',
    description='waitgroup like Go sync.WaitGroup',
    long_description=readme,
    license=license,
    author='Shun Fukusumi',
    author_email='shun.fukusumi@gmail.com',
    url='https://github.com/juv-shun/py-waitgroup',
    packages=find_packages(exclude=('tests')),
    test_suite='tests',
)
