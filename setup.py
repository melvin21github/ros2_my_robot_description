from setuptools import setup
import os
from glob import glob

package_name = 'my_robot_description'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        # register package
        ('share/ament_index/resource_index/packages',
         ['resource/' + package_name]),

        # install launch, urdf and rviz directories
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
        (os.path.join('share', package_name, 'urdf'), glob('urdf/*')),
        (os.path.join('share', package_name, 'rviz'), glob('rviz/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='melvin',
    maintainer_email='melvin@example.com',
    description='Simple robot description package',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [],
    },
)
