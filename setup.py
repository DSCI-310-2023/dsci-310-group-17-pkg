from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / "README.md").read_text(encoding="utf-8")



setup(

    name="hyperthyroidclassifier",  
    version="0.1.0",  
    description="A package for classifying individuals based on the presence of hyperthyroid diseases based on various characteristics",
    long_description=long_description,  
    long_description_content_type="text/markdown", 
    url="https://github.com/DSCI-310/dsci-310-group-17-pkg/tree/main",  
    author="Ryan Lee, Matthew Gillies, Eric Liu, Arman Moztarzadeh", 
    author_email="author@example.com",  # Optional
    # Classifiers help users find your project by categorizing it.
    #
    # For a list of valid classifiers, see https://pypi.org/classifiers/
    #classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        #"Development Status :: 3 - Alpha",
        # Indicate who your project is intended for
        # "Intended Audience :: Developers",
        # "Topic :: Software Development :: Build Tools",
        # Pick your license as you wish
        # "License :: OSI Approved :: MIT License",
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate you support Python 3. These classifiers are *not*
        # checked by 'pip install'. See instead 'python_requires' below.
        # "Programming Language :: Python :: 3",
        # "Programming Language :: Python :: 3.7",
        # "Programming Language :: Python :: 3.8",
        # "Programming Language :: Python :: 3.9",
        # "Programming Language :: Python :: 3.10",
        # "Programming Language :: Python :: 3 :: Only",
    #],
    # This field adds keywords for your project which will appear on the
    # project page. What does your project relate to?
    #
    # Note that this is a list of additional keywords, separated
    # by commas, to be used to assist searching for the distribution in a
    # larger catalog.
    #keywords="sample, setuptools, development",  # Optional
    # When your source code is in a subdirectory under the project root, e.g.
    # `src/`, it is necessary to specify the `package_dir` argument.
    package_dir={"": "src"},  # Optional
    # You can just specify package directories manually here if your project is
    # simple. Or you can use find_packages().
    #
    # Alternatively, if you just want to distribute a single Python file, use
    # the `py_modules` argument instead as follows, which will expect a file
    # called `my_module.py` to exist:
    #
    #   py_modules=["my_module"],
    #
    #python_requires=">=3.7, <4",
    # This field lists other packages that your project depends on to run.
    # Any package you put here will be installed by pip when your project is
    # installed, so they must be valid existing projects.
  
)