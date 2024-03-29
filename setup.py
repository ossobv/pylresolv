# pylresolv -- DNS querying through libc libresolv.so using ctypes
# Copyright (C) 2019  Walter Doekes, OSSO B.V.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
from distutils.core import setup
from os.path import dirname, join


if __name__ == '__main__':
    long_descriptions = []
    with open(join(dirname(__file__), 'README.rst')) as file:
        long_descriptions.append(file.read())
    version = '0.2'

    setup(
        name='pylresolv',
        version=version,
        data_files=[('share/doc/pylresolv', ['README.rst'])],
        packages=['pylresolv'],
        description='DNS querying through libc libresolv.so using ctypes',
        long_description=('\n\n\n'.join(long_descriptions)),
        author='Walter Doekes, OSSO B.V.',
        author_email='wjdoekes+pylresolv@osso.nl',
        url='https://github.com/ossobv/pylresolv',
        license='GPLv3+',
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Developers',
            ('License :: OSI Approved :: GNU General Public License v3 '
             'or later (GPLv3+)'),
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 3',
            'Topic :: Internet :: Name Service (DNS)',
            'Topic :: Software Development :: Libraries',
        ],
    )

# vim: set ts=8 sw=4 sts=4 et ai tw=79:
