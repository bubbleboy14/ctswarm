from setuptools import setup

setup(
    name='ctswarm',
    version="0.1",
    author='Mario Balibrera',
    author_email='mario.balibrera@gmail.com',
    license='MIT License',
    description='Cloudish plugin for cantools (ct)',
    long_description='The aim of this plugin is to simplify the deployment of cloud based web services.',
    packages=[
        'ctswarm'
    ],
    zip_safe = False,
    install_requires = [
        "ct >= 0.9.14.5"
    ],
    entry_points = '''''',
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
