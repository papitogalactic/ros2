from setuptools import find_packages, setup

package_name = 'my_py_pkg'

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
    maintainer='jr',
    maintainer_email='juanrapf00@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "cmd_vel_publisher=my_py_pkg.controlador_robot:main",
            "mostrar_puntos=my_py_pkg.mostrar_puntos:main",
            "pure_pursuit=my_py_pkg.pure_pursuit:main"
        ],
    },
)
