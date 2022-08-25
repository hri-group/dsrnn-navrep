from setuptools import setup


setup(
    name='soadrl-crowdnav',
    version='0.0.3',
    packages=[
        'crowd_nav',
        'crowd_nav.policy',
        'crowd_nav.utils',
        'crowd_nav.cadrl_utils',
        'crowd_sim',
        'crowd_sim.envs',
        'crowd_sim.envs.policy',
        'crowd_sim.envs.utils',
    ],
    install_requires=[
        'gitpython',
        'gym',
        'matplotlib',
        'numpy',
        'scipy',
        'torch',
        'torchvision',
    ],
    extras_require={
        'test': [
            'pylint',
            'pytest',
        ],
    },
    package_data={'crowd_nav': ['config/test_soadrl_static.config']},
)
