from setuptools import setup, find_packages
import os

os.environ['PYTHONDONTWRITEBYTECODE'] = '1'

requires = ["Jinja2>=3.1.2","mitmproxy>=10.0.0","mitmproxy_rs>=0.2.2","regex>=2023.10.3"]

setup(
    name                = "CLay",
    version				= "1.0.0",
    description         = "Concealment Layer - Reverse Proxy for Concealing Website Informations",
    url='https://github.com/kisanakkkkk/CLay/',
    python_requires     = '>=3.11',
    include_package_data=True,
    packages            = find_packages(),
    package_data        ={'CLay': ['config/*', 'static/**/*']},
    classifiers         =[
        'Development Status :: 1 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.11',
    ],
    install_requires    = requires,
    entry_points        = {
        'console_scripts': [
            'CLay = CLay.main:main',
        ],
    },
)

# del os.environ['PYTHONDONTWRITEBYTECODE']