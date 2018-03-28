from setuptools import setup

setup(name='pythercis',
      version='0.1.0',
      description='Python bindings for EtherCIS',
      url='https://github.com/Epidurio/pythercis',
      author='Dr Marcus Baw',
      author_email='marcusbaw@gmail.com',
      license='MIT',
      packages=['pythercis'],
      install_requires=[
          'requests',
      ],
      zip_safe=False)
