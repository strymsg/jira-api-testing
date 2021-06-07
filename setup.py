from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    readme = f.read()

if __name__ == '__main__':
    setup(
        name='jira-api-testing',
        description='Task Manager',
        # install_requires='requirements',
        python_requires='>=3.5',
        # version="0.1.0",
        # long_description='\n\n'.join([readme, changes]),
        # license='MIT license',
        url='https://gitlab.com/atbootcamppython/teamprojects/',
        # version=version,
        author='Rodrigo Garcia',
        author_email='',
        maintainer='Rodrigo Garcia',
        maintainer_email='',
        keywords=['jira-api-testing'],
        # package_dir={'': 'src'},
        packages=find_packages(include=['api', 'common', 'utils', 'tests']),
        zip_safe=False,
        classifiers=['Development Status :: 3 - Alpha',
                     'Intended Audience :: Developers',
                     'Programming Language :: Python :: 3.9']
    )
