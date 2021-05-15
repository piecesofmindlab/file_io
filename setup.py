from setuptools import setup, find_packages

# with open('requirements.txt') as fid:
# 	requirements = fid.readlines()
# 	requirements = [x.strip() for x in requirements]

setup(
    name='file_io',
    version='0.1.0',
    packages=find_packages(),
    long_description=open('README.md').read(),
    #install_requires=requirements,
    #include_package_data=True,
)
