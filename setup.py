from setuptools import setup, find_packages

setup(
    name='SuspiciousMoneyFlow',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'networkx',
        'scikit-learn',
        'flask',
        'joblib'
    ]
)
