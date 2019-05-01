# coding=utf-8
"""
Setup for scikit-surgerybard
"""

from setuptools import setup, find_packages
import versioneer

# Get the long description
with open('README.rst') as f:
    long_description = f.read()

setup(
    name='scikit-surgerybard',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description='scikit-surgerybard is a Basic Augmented Reality Demo (BARD)'
                'based on scikit-surgery (SNAPPY)',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    url='https://weisslab.cs.ucl.ac.uk/WEISS/SoftwareRepositories/SNAPPY/'
        'scikit-surgerybard',
    author='Mian Asbat Ahmad',
    author_email='rmapaah@ucl.ac.uk',
    license='BSD-3 license',
    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Intended Audience :: Healthcare Industry',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',


        'License :: OSI Approved :: BSD License',


        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',

        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Medical Science Apps.',
    ],

    keywords='medical imaging',

    packages=find_packages(
        exclude=[
            'doc',
            'tests',
        ]
    ),

    install_requires=[
        'six>=1.10',
        'numpy>=1.11',
        'glob2',
        'opencv-contrib-python',
        'sksurgerycore',
    ],

    entry_points={
        'console_scripts': [
            'bardCameraCalibration=sksurgerybard.ui.bard_camera_'
            'calibration_command_line:main',
            'bardPivotCalibration=sksurgerybard.ui.bard_pivot_'
            'calibration_command_line:main',
            'bardGrabVideoImages=sksurgerybard.ui.bard_grab_'
            'video_images_command_line:main',
        ],
    },
)
