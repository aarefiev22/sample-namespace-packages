from setuptools import setup


setup(
    name='all packages',

    license='Apache Software License',

    packages=['example_pkg.a', 'example_pkg.b'],
    namespace_packages=['example_pkg'],
    zip_safe=False,
)
