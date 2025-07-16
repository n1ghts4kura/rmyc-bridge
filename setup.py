from setuptools import setup, find_packages

setup(
    name="rmyc_bridge",
    version="0.1",
    author="n1ghts4kura",
    author_email="1825259836@qq.com",
    description="A bridge for RMYC to connect with other systems",
    packages=find_packages(),
    install_requires=[
        "pyserial",
    ],
)