from setuptools import setup, find_packages


setup(
    name='tortoise-shell',
    version='0.1.0', 
    packages=find_packages(),
    include_package_data=True,
    description='A shell_plus like tool for Tortoise ORM.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown', 
    author='Michael Pearce',
    author_email='firstflush@protonmail.com', 
    url='https://github.com/firstflush/tortoise-shell',
    keywords='tortoise, tortoise-orm, shell, cli, command' 'command-line',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    python_requires='>=3.10',
    entry_points={
        'console_scripts': [
            'tortoise-shell=tortoise_shell.tortoise_shell:main',
        ],
    },
    license='MIT',
    install_requires=[
        "tortoise-orm",
        "ipython",
        "toml",
        "traitlets",
    ],
)



# from setuptools import setup, find_packages

# setup(
#     name="tortoise-shell",
#     version="0.1.0",
#     packages=find_packages(),
#     install_requires=[
#         "tortoise-orm",
#         "ipython",
#         "toml",
#         "traitlets",
#     ],
#     entry_points={
#         'console_scripts': [
#             'tortoise-shell=tortoise_shell.tortoise_shell:main',
#         ],
#     },
#     description="A shell_plus like tool for Tortoise ORM.",
#     long_description=open('README.md').read(),
#     long_description_content_type='text/markdown',
#     author="Michael Pearce",
#     author_email="firstflush@protonmail.com",
#     url="https://github.com/firstflush/tortoise-shell",
#     license="MIT",
# )