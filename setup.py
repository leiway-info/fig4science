import setuptools


setuptools.setup(
                 name="scientific_fig_lib",
                 version="1.0",
                 author="LeiWay Info",
                 author_email="leiwayinfo@gmail.com",
                 description="Make pretty figures for scientific publication and presentation",
                 packages=setuptools.find_packages(),
                 install_requires=[
                                   "matplotlib",
                                   ],
                 )
