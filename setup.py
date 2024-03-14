from setuptools import setup , find_packages

setup(
    name='mouse_movement_tracker',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'pyautogui>=0.9.53' 
    ],
    description='A package for tracking mouse movement',
    author='Jatin',
    
#     classifiers=[
#         'Programming Language :: Python :: 3',
#         'License :: OSI Approved :: MIT License',
#         'Operating System :: OS Independent',
#     ],
)