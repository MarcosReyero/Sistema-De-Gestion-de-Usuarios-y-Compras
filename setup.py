from setuptools import setup, find_packages

setup(
    name="gestor_usuarios_compras",
    version="0.1.1",
    author="Marcos Reyero",
    author_email="reyeromateo@gmail.com",
    description="Sistema de Gestión de Usuarios y Compras en Línea",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'gestor-usuarios-compras=gestor_de_usuarios.main:main',
        ],
    },
    include_package_data=True,
    package_data={
        '': ['*.txt', '*.rst'],
        'gestor_de_usuarios': ['*.py'],
    },
)
