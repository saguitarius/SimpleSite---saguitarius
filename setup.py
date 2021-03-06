try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='SimpleSite',
    version='0.3.0',
    description='',
    author='saguitarius',
    author_email='saguitarius@gmail.com',
    url='',
    install_requires=[
        "Pylons>=1.0",
        "SQLAlchemy>=0.5,<=0.5.99",
        "Mako>=0.2.2,<=0.2.99",
        "FormBuild>=2.0,<2.99",
        "AuthKit>=0.4.3,<=0.4.99",
    ],
    setup_requires=["PasteScript>=1.6.3"],
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    test_suite='nose.collector',
    package_data={'simplesite': ['i18n/*/LC_MESSAGES/*.mo']},
    #message_extractors={'simplesite': [
    #        ('**.py', 'python', None),
    #        ('templates/**.mako', 'mako', {'input_encoding': 'utf-8'}),
    #        ('public/**', 'ignore', None)]},
    zip_safe=False,
    paster_plugins=['PasteScript', 'Pylons'],
    entry_points="""
    [paste.app_factory]
    main = simplesite.config.middleware:make_app

    [paste.app_install]
    main = pylons.util:PylonsInstaller
    """,
)
