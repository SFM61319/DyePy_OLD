import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='dyepy',
    version='0.0.4',
    author='SFM61319',
    author_email='svasssakavi@gmail.com',
    description='A styling and color conversion module as a mini CLI',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/SFM61319/DyePy',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.0',
)
