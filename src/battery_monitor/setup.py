from setuptools import find_packages, setup

package_name = 'battery_monitor'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools', 'battery_msg'],
    zip_safe=True,
    maintainer='jr',
    maintainer_email='jr@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        "battery_publisher = battery_monitor.battery_publisher:main",
        "battery_subscriber = battery_monitor.battery_subscriber:main"
        ],
    },
)
