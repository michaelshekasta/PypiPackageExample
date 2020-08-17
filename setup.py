import setuptools


def parse_requirements(filename):
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if not line.startswith('#')]


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pypi-package-example",  # Replace with your own username
    version="0.0.7",
    author="Michael Shekasta",
    author_email="shkasta@post.bgu.ac.il",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/michaelshekasta/PypiPackageExample",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=parse_requirements('requirements.txt'),
)
