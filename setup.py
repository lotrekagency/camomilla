from setuptools import setup, find_packages

setup(
    name='camomilla',
    version='4.0.1',
    url='https://gitlab.com/lotrekdevteam/camomilla/camomilla',
    install_requires=[
        'django-hvad @ https://github.com/kristianoellegaard/django-hvad/tarball/releases/2.0.x',
        'djangorestframework==3.9.2',
        'Pillow==6.0.0',
        'django-redactor-2.0==0.3'
    ],
    description="Our internal CMS",
    long_description=open('README.md', 'r').read(),
    license="Private",
    author="Lotrek",
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
