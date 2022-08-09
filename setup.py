from setuptools import find_packages, setup
data_files = [('config/', ['app/config/conf.yaml'])]

setup(
    name='pysparkdemo',
    extras_require=dict(tests=['pytest']),
    packages=find_packages(where="app"),
    package_dir={"": "app"},
    data_files=data_files
)