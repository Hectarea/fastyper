from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="Fastyper-Hectarea",
    version="0.0.1",
    author="Hectarea",
    author_email="gonzalez.craqnell@gmail.com",
    description="A fast typing tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Hectarea/fastyper.git",
    packages=['random_words', 'names','pynput'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]

)