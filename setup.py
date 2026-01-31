# setup.py na raiz do repositório yanzeradev/fast-reid
import os
from setuptools import setup, find_packages

setup(
    name="fastreid",
    version="1.0.0",
    author="yanzeradev",
    description="Fork do FastReID para o projeto SenseVision - Otimizado para TCC",
    packages=find_packages(exclude=("configs", "tests", "tools")),
    python_requires=">=3.8",
    install_requires=[
        "yacs",           # Gestão de ficheiros de configuração
        "cython",         # Necessário para compilação de métricas
        "gdown",          # Download de modelos pré-treinados
        "ninja",          # Aceleração de compilação
        "tabulate",       # Formatação de tabelas de resultados
        "termcolor",      # Logs coloridos no terminal
        "fvcore>=0.1.1",  # Biblioteca core do Facebook AI Research
        "iopath>=0.1.7",  # Abstração de I/O
        "portalocker",    # Bloqueio de ficheiros para segurança
        "faiss-cpu",      # Biblioteca de busca rápida (essencial para ReID)
        "opencv-python",  # Processamento de imagem
        "pandas",         # Manipulação de dados para relatórios
    ],
    include_package_data=True,
    zip_safe=False,
)
