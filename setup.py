from setuptools import setup, find_packages

setup(
    name='camomilla',
    version='4.0.0',
    url='https://gitlab.com/lotrekdevteam/camomilla/camomilla',
    install_requires=[
        'django-hvad @ https://github.com/lotrekagency/django-hvad/archive/master.zip',
        'djangorestframework==3.10.0',
        'Pillow==5.0.0',
        'sqlparse==0.3.0'
    ],
    dependency_links=[
        # Make sure to include the `#egg` portion so the `install_requires` recognizes the package
        'git+ssh://git@github.com/lotrekagency/django-hvad.git@master#egg=django-hvad-lotrek-1.8.0'
    ],
    description="Our internal CMS",
    long_description=open('README.md', 'r').read(),
    license="Private",
    author="Lotrèk",
    author_email="dimmitutto@lotrek.it",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3'
    ]
)
