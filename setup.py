from setuptools import setup
from setuptools import setup, find_namespace_packages

with open("README.md", "r", encoding="utf-8") as f:
    logn_desc = f.read()

setup(
    name='chandlerbot',
    version='1',
    description='You personal assistant',
    long_description=logn_desc,
    url='https://github.com/MKuzich/bot',
    author='MKuzich',
    author_email='chandlerbot@gmail.com',
    license='MIT',
    packages=find_namespace_packages(),
    install_requires=['markdown', 'prompt-toolkit', 'pycountry',
                      'Pygments', 'tabulate', 'wcwidth', 'requests'],
    entry_points={'console_scripts': ['chandler = chandlerbot.bot:main']}
)
