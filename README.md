## About

*Conan recipe for [QtXlsxWriter (MIT)](https://github.com/VSRonin/QtXlsxWriter)*

QtXlsx is a library that can read and write Excel files.

The recipe works with a specific commit from the master-branch since there is no released (tagged) version with a CMake-based build and Qt5 support atm.

The recipe will install Qt5 as its dependency, so it doesn't rely on any existing Qt5 installation.

The recipe supports only Windows atm.
Tested on [Windows, Visual Studio 15]

Example:
```
conan create <path-to-recipe> qtxlsxwriter/0.0.0@<username>/<channel>
```
