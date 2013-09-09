#!/usr/bin/env python

import xmlrpclib
import pip
from subprocess import call
import argparse


def inform(old, new):
    doinstall = False

    if not new:
        msg = 'no releases at pypi'
    elif new[0] != old.version:
        doinstall = True
        msg = '{} available'.format(new[0])
    else:
        msg = 'up to date'

    pkg_info = '{dist.project_name} {dist.version}'.format(dist=old)
    print '{pkg_info:40} {msg}'.format(pkg_info=pkg_info, msg=msg)

    return doinstall


def install(old, new):
    doinstall = inform(old, new)
    if doinstall:
        call('pip install --upgrade {}'.format(old.project_name), shell=True)

class Check(object):
    _pypi = xmlrpclib.ServerProxy('http://pypi.python.org/pypi')

    def __init__(self, skiplist=[]):
        self.skiplist = set(skiplist)

    def __call__(self, method=inform):
        for dist in pip.get_installed_distributions():
            if dist.project_name not in self.skiplist:
                available = self._pypi.package_releases(dist.project_name)
                if not available:
                    available = self._pypi.package_releases(dist.project_name.capitalize())
            method(dist, available)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Upgrade or check for new versions of installed packages on pypi.")
    parser.add_argument('--install', action="store_true", help="Install upgradable packages")
    parser.add_argument('--skip', default=[], nargs='*', help="Skip these packages")

    args = parser.parse_args()
    c = Check(args.skip)

    try:
        if args.install:
            c(install)
        else:
            c()
    except KeyboardInterrupt:
        exit("\nAction aborted by user")
