from setuptools import setup

setup(name='SampleOO',
      version='0.12',
      description='Testing and proof of loading and reloading packages in Python',
      url='https://github.com/sada-narayanappa/sampleOO.git',
      author='Code Red',
      author_email='sada@geospaces.org',
      license='MIT',
      packages = ['SampleOO'],
      package_data={'SampleOO':['*']},
      zip_safe=False,
      zip_ok=False,
      install_requires=['Jupytils'],
      classifiers=[
          # How mature is this project? Common values are
          #   3 - Alpha
          #   4 - Beta
          #   5 - Production/Stable
          'Development Status :: 3 - Alpha',
            
          # Indicate who your project is intended for
          'Intended Audience :: Developers',
          #'Topic :: Jupyter Prettification :: Utilities ',
      
          # Pick your license as you wish (should match "license" above)
           'License :: OSI Approved :: MIT License',
      
          # Specify the Python versions you support here. In particular, ensure
          # that you indicate whether you support Python 2, Python 3 or both.
          #'Programming Language :: Python :: 2',
          #'Programming Language :: Python :: 2.6',
          #'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
      ],
)
