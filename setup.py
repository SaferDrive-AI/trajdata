from setuptools import setup, find_packages

setup(
    name="trajdata",
    version="1.4.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "numpy>=1.19",
        "tqdm>=4.62",
        "matplotlib>=3.5",
        "dill>=0.3.4",
        "pandas>=1.4.1",
        "pyarrow>=7.0.0",
        "zarr>=2.11.0",
        "kornia>=0.6.4",
        "seaborn>=0.12",
        "bokeh>=3.0.3",
        "geopandas>=0.13.2",
        "protobuf==3.19.4",
        "scipy>=1.9.0",
        "opencv-python>=4.5.0",
        "shapely>=2.0.0",
    ],
)
