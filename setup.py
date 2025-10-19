from setuptools import setup, find_packages

setup(
    name="tail-cli",
    version="1.0.1",
    packages=find_packages(),  # автоматично знайде папку tail_cli
    include_package_data=True,
    install_requires=[
        "click",
        "colorama"
    ],
    entry_points={
        "console_scripts": [
            "tail-cli = tail_cli.tail:tail"  # команда tail-cli викликає функцію tail() у tail.py
        ]
    },
    python_requires=">=3.7",
    description="Tail CLI — програма tail на Python з підтримкою Click і кольорового виводу.",
    author="Anastasia Pelyno",
    license="MIT",
)
