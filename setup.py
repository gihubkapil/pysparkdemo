from setuptools import find_packages, setup
data_files = [('config', ['app/config/conf.yaml'])]

setup(
    name='pysparkdemo',
    extras_require=dict(tests=['pytest']),
    packages=['app', 'app.config', 'app.utils'],
    #packages=find_packages('app'),
    #package_dir={"": "app"},
    data_files=data_files
)