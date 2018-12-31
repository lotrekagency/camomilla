from setuptools import setup, find_packages

setup(
    name='camomilla',
    version='4.0.0',
    url='https://gitlab.com/lotrekdevteam/camomilla/camomilla',
    install_requires=[
        'django-hvad==1.8.0',
        'djangorestframework==3.5.2',
        'Pillow==3.4.2',
        'django-wysiwyg-redactor==0.5.0'
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
