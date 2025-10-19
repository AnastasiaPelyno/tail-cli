from setuptools import setup, find_packages

setup(
    name="tail-cli",
    version="1.0.5",
    packages=find_packages(),  
    include_package_data=True,
    install_requires=[
        "click",
        "colorama"
    ],
    entry_points={
        "console_scripts": [
            "tail-cli = tail_cli.tail:tail"  
        ]
    },
    python_requires=">=3.7",
    description="Tail CLI — програма tail на Python з підтримкою Click і кольорового виводу.",
    author="Anastasia Pelyno",
    license="MIT",
)
