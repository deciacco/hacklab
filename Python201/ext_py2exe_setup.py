from distutils.core import setup
import py2exe

setup(
    options = {'py2exe': {'bundle_files': 1, 'compressed' : True}},
    console = [{'script':'ext_py2exe.py'}],
    zipfile = None
)

# need to run this script as
# python ext_py2exe_setup.py py2exe

# further studying as distutils has been deprecated, setuptools going forward
