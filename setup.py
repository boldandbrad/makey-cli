from setuptools import setup, find_packages

# parse version number from makey/__init__.py:
with open("makey/__init__.py") as f:
    info = {}
    for line in f.readlines():
        if line.startswith("version"):
            exec(line, info)
            break

setup_info = dict(
    name="makey-cli",
    version=info["version"],
    author="Bradley Wojcik",
    author_email="bradleycwojcik@gmail.com",
    license="MIT",
    description="CLI passkey maker.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://boldandbrad.github.io/makey-cli/",
    project_urls={
        "Source": "https://github.com/boldandbrad/makey-cli/",
        "Bug Tracker": "https://github.com/boldandbrad/makey-cli/issues",
    },
    packages=find_packages(),
    include_package_data=True,
    install_requires=["click>=8", "pyperclip>=1.8"],
    extras_require={
        "dev": [
            "black",
            "pytest",
            "pytest-cov",
            "pytest-mock",
            "codecov",
            "homebrew-pypi-poet",
        ]
    },
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
    ],
    entry_points="""
        [console_scripts]
        makey=makey.makey:cli
    """,
)

setup(**setup_info)
