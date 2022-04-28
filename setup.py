import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="IQA",
    version="1.0.9",
    author="gonarahmaniani",
    author_email="",
    description="Evaluation metrics to assess the similarity between two images.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gonarahmaniani/IQA",
    packages=setuptools.find_packages(),
    license="License",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: License",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "Development Status :: 5 - Production/Stable",
    ],
    extras_require={
        "rasterio": ["rasterio"],
        "speedups": ["pyfftw"],
    },
    install_requires=["numpy", "scikit-image", "opencv-python", "phasepack"],
    python_requires=">=3.6, <3.10",
    entry_points={
        "console_scripts": [
            "IQA=IQA.evaluate:main"
        ],
    },
)
