from setuptools import setup

exec (open('react_player_dash/version.py').read())

setup(
    name='react_player_dash',
    version=__version__,
    author='freshwuzhere',
    author_email='iab@ianburns.com',
    packages=['react_player_dash'],
    include_package_data=True,
    license='MIT',
    description='componentise the react-player to work with Dash',
    long_description='Dash by Plot.ly is a python web authoring tool that allows use of Plotly.js graphics in a web interface.  This javascript component uses react-player and allows implementationand usage from Dash',
    url="https://github/freshwuzhere/react_player_dash",
    install_requires=[],
)
