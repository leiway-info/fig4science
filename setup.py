import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fig4science",
    version="1.0",
    author="LeiWuInfo",
    author_email="leiwuinfo@gmail.com",
    description="Make pretty figures for scientific publication and presentation",
    long_description=long_description,
    url="https://github.com/leiwuinfo/fig4science",
    packages=setuptools.find_packages(),
    classifiers=[
       "Programming Language :: Python :: 3",
       "License :: OSI Approved :: MIT License",
       "Operating System :: OS Independent",
    ],
)
