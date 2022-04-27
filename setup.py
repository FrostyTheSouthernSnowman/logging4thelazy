from distutils.core import setup
import pathlib

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

VERSION = "0.0.2"

setup(
    name="logs4thelazy",
    packages=["l4l"],
    version=VERSION,
    license="MIT",
    description="A simple and easy to use library for logging in python",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Yosi Frost",
    author_email="yosi_frost@icloud.com",
    url="https://github.com/FrostyTheSouthernSnowman/logging4thelazy",
    download_url="https://github.com/FrostyTheSouthernSnowman/logging4thelazy/archive/v_0.0.2.tar.gz",  # I explain this later on
    keywords=["logging", "python3", "simple"],
    install_requires=[],
    classifiers=[
        "Development Status :: 4 - Beta",  # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        "Intended Audience :: Developers",  # Define that your audience are developers
        "Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
