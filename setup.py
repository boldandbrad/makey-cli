from setuptools import setup, find_packages

# parse version number from makeycli/__init__.py:
with open('makeycli/__init__.py') as f:
    info = {}
    for line in f.readlines():
        if line.startswith('version'):
            exec(line, info)
            break

setup_info = dict(
    name='makey-cli',
    version=info['version'],
    author='Bradley Wojcik',
    author_email='bradleycwojcik@gmail.com',
    license='MIT',
    description='CLI passkey maker.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://bradleycwojcik.github.io/makey-cli/',
    project_urls={
        'Source': 'https://github.com/bradleycwojcik/makey-cli/',
        'Bug Tracker': 'https://github.com/bradleycwojcik/makey-cli/issues'
    },
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click>=7',
        'pyperclip>=1.8',
        'pytest',
        'pytest-cov',
        'pytest-mock',
        'codecov'
    ],
    python_requires='>=3.6',
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License'
    ],
    entry_points='''
        [console_scripts]
        makey=makeycli.makey:cli
    '''
)

setup(**setup_info)
