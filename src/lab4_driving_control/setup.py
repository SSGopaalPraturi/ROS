from setuptools import find_packages, setup

package_name = 'lab4_driving_control'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='me',
    maintainer_email='ryanmin77@icloud.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'open_loop = lab4_driving_control.open_loop_drive:main',
            'closed_loop = lab4_driving_control.closed_loop_drive:main',
            'return_to_start = lab4_driving_control.return_to_start:main',
        ],
    },
)
