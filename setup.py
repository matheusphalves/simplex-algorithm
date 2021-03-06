from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    readme = fh.read()

setup(name='simplex-algorithm',
    version='1.0.0',
    url='https://github.com/matheusphalves/simplex-algorithm',
    license='MIT License',
    author= ['Matheus Phelipe'],
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='matheusphalves@gmail.com',
    keywords=['Optimization', 'PPL', 'Simplex-Algorithm'],
    description=u'Basic implementation of Simplex Algorithm for maximization problems',
    packages=find_packages(),
    install_requires=['numpy'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ])