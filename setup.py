from setuptools import setup, find_packages # type: ignore[import-untyped]


HYPEN_DASH = '-e .'
def read_requirements(file_path:str) -> list[str]:
    '''Reads the requirements from a file and returns them as a list of strings.'''

    requirements = []
    with open(file_path, 'r') as file:
        requirements = file.readlines()
        requirements = [req.replace("\n", " ") for req in requirements]

        if HYPEN_DASH in requirements:
            requirements.remove(HYPEN_DASH)

    return requirements



setup(
    name='general-ml-project',
    version='0.0.1',
    author='Javidan Akbarov',
    author_email='iamjavidanakbarov@gmail.com',
    packages=find_packages(),
    install_requires=read_requirements('requirements.txt')
)