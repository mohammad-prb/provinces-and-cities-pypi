import setuptools

setuptools.setup(
    name="provinces-and-cities",
    version="1.0.4",
    description="Package of countries provinces and cities.",
    url="https://github.com/mohammad-prb/provinces-and-cities-pypi",
    project_urls={
        "Source Code": "https://github.com/mohammad-prb/provinces-and-cities-pypi",
    },
    author="Mohammad Pourbehzad",
    author_email="pspipm27@gmail.com",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.6",
    install_requires=[],
    packages=["provinces_and_cities"],
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
)
