This script checks if a new version is available on pypi and installs if asked to.

Adapted from this recipe:
http://code.activestate.com/recipes/577708-check-for-package-updates-on-pypi-works-best-in-pi/

```
usage: pipupgrade.py [-h] [--install] [--skip [SKIP [SKIP ...]]]

Upgrade or check for new versions of installed packages on pypi.

optional arguments:
  -h, --help            show this help message and exit
  --install             Install upgradable packages
  --skip [SKIP [SKIP ...]]
                        Skip these packages
```

You can pass a skip list as a file, where each package name is on a separate line by prefixing the file name with '@' symbol, for example:

```
python pipupgrade.py --skip @skip.txt
```
