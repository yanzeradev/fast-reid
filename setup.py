# setup.py (na raiz do seu repositório fast-reid)
import os
from setuptools import setup, find_packages

def get_version():
    return "1.0.0" # Defina a versão do seu fork

setup(
    name="fastreid",
    version=get_version(),
    author="yanzeradev",
    description="Fork do FastReID para o projeto SenseVision",
    packages=find_packages(exclude=("configs", "tests", "tools")),
    python_requires=">=3.7",
    install_requires=[
        "yacs",
        "cython",
        "gdown",
        "ninja",
        "tabulate",
        "termcolor",
        "fvcore>=0.1.1",
        "iopath>=0.1.7",
        "portalocker",
    ],
    # Isso permite que o pip encontre os arquivos de código
    include_package_data=True,
    zip_safe=False,
)
