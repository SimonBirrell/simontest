from setuptools import setup

package_name = 'test_pack'
sub_pack = 'test_pack/subfolder'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name , sub_pack ],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='yousif',
    maintainer_email='yousif@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'test_node = test_pack.test_node:main'
        ],
    },
)
