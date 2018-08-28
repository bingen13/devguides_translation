# -*- coding: utf-8 -*-
documentation = [
_(u"""This document outlines rationale and steps for moving NVDA from Python 2.7 to 3.x."""),
"",_(u"""IMPORTANT: this document is a draft document that can change periodically."""),
"",_(u"""## Background"""),
"",_(u"""Python is one of the popular programming languages for various projects. Its ease of learning, extensive standard library modules and third-party extensions, as well as extensive documentation and clear syntax makes it an ideal choice for scripting."""),
"",_(u"""Currently there are two major branches of Python: 2.x, released in early 2000's, and 3.x, first released in 2008. At first glance, Python 3 may seem similar to Python 2, but there are numerous deeper differences, including extensive Unicode support in Python 3, module renames and so on."""),
"",_(u"""## Rationale"""),
"",_(u"""When NVDA began in 2006, it used python 2.4. Over the years, NvDA and its add-ons were written in Python 2.7. By moving to Python 3, NVDA project seeks to provide improvements in Unicode support, improved performance in various operations and other benefits, which goes beyond just the screen reader."""),
"",_(u"""## Advantages of moving to Python 3"""),
"",_(u"""* Better Unicode support, thus leading to improved internationalization efforts."""),
_(u"""* Using newer techniques for screen reading purposes."""),
_(u"""* Major overhaul of NVDA's code base."""),
"",_(u"""## Drawbacks of moving to Python 3"""),
"",_(u"""* Many add-ons not updated will no longer work."""),
_(u"""* Renamed modules."""),
_(u"""* Being careful about syntax differences."""),
"",_(u"""## Transition workflow"""),
"",_(u"""The following is a roughh overview of Python 2 to 3 transition for NVDA screen reader. As this is in draft stage, this is subject to change."""),
"",_(u"""### Notable issues and solutions:"""),
"",_(u"""* Renamed modules in Python 3 such as _winreg -> winreg, SocketServer -> socketserver, Queue -> queue and so forth."""),
_(u"""	* Try using Python 3 version before falling back to Python 2 names."""),
_(u"""	* For certain modules (especially those written in C), make sure new modules won't break functionality."""),
_(u"""* Reorganized modules in Python 3, including urllib and io."""),
_(u"""	* Try loading specific attributes from reorganized modules."""),
_(u"""* Absolute versus relative imports, especially when aliasing is involved (imports of the form 'from mod import *\", observed mostly in app modules)."""),
_(u"""	* Use relative imports of the form \"from .mod import attr\"."""),
_(u"""* Replacement of some private attributes of logging module."""),
_(u"""	* These should be changed on a case-by-case basis."""),
_(u"""* Inability to print a meaningful log text to log file."""),
_(u"""	* Investigate streaming/file handler/redirection issue."""),
_(u"""* Use of \"async\" in Python 3, which affects nvwave.playWaveFile(async=True) as this raises syntax error."""),
_(u"""	* Rename the keyword to \"asynchronous\"."""),
_(u"""* Division differences (/ versus //), most notably in nvwave.WavePlayer."""),
_(u"""	* Standardize around floor division (//) for integer values, regular division (/) for floats."""),
_(u"""* Bytes versus strings caused by encoding."""),
_(u"""	* Try unifying under Unicode."""),
_(u"""	* This is pronounced when working with C functions (Espeak DLL, for example) where ANSI strings are expected by C functions but Python prefers Unicode."""),
_(u"""* Removed modules, including new.instancemethod."""),
_(u"""	* Either find a Python 3 equivalent, or use built-in Python features."""),
"",_(u"""### Needed dependencies:"""),
"",_(u"""* Python 3.7.0 32-bit"""),
_(u"""* Visual Studio 2017 (Community, Professional, Enterprise)"""),
_(u"""* Windows 10 SDK (build 17134)"""),
_(u"""* wxPython 4.0.3 for Python 3.x"""),
_(u"""* Six 1.11.0"""),
_(u"""* SCons 3.0.1"""),
_(u"""* comtypes 1.1.7"""),
_(u"""* Pywin32 extensions build 223 for Python 3.x"""),
_(u"""* pyserial for Python 3.x"""),
_(u"""* Configobj 5.1.0"""),
_(u"""* Any other dependencies advertising support for Python 2.x in one package or a separate release for Python 3.x"""),
_(u"""* A replacement for py2exe for binary distribution"""),
"",_(u"""### Before the transition:"""),
"",_(u"""1. An NVDA version with wxPython 4 must be released. This is needed, as wxPython 4 supports Python 3, which is a stepping stone for Python 3 transition."""),
_(u"""2. Source code level dependencies must be satisfied. This includes not only wxPython 4, but also ConfigObj, Comtypes, Pyserial, Pywin32 and others."""),
_(u"""3. Transition issues must be researched and documented (see above for known issues and proposed workarounds)."""),
_(u"""4. If needed, create pull requests dealing with pre-transition workflow such as making NVDA source code Python 2 and 3 aware (imports, for instance)."""),
"",_(u"""Ideal completion: between NVDA 2018.4 and 2019.1 releases."""),
"",_(u"""### Transition:"""),
"",_(u"""1. A group of developers (code contributors, add-on developers, Python programmers outside of NVDA project and others) should work on transforming NVDA's source code to Python 3."""),
_(u"""	* Do not run 2to3 and tell the script to replace files, as further tweaking will be required."""),
_(u"""	* For each transformation iteration, test the source code to make sure functionality are identical (or almost identical) with older NVDA releases."""),
_(u"""2. Issues related to transition must be documented."""),
_(u"""	* Issues must be labeled as \"Python 3\" in GitHub."""),
_(u"""	* If needed, proposed solutions and workarounds should be documented in the issue tracker."""),
_(u"""3. Source code developers must test NVDA and add-ons to make sure no major issues are encountered while working on python 3 transition. During this phase, binary builds will not be released until the below condition is met."""),
_(u"""	* Gather dependencies and make sure they are compatible with Python 3."""),
_(u"""	* Try running SCons under Python 3 to make sure source code is prepared."""),
_(u"""	* If features are working, compare it against latest stable NVDA release in hopes of catching regressions."""),
_(u"""4. A suitable binary distribution packager must be found, tested, and documented. A series of binary builds must be created to make sure the combination of NVDA's own python 3 code, dependencies, binary packagers, and others work seamlessly."""),
_(u"""	* Py2exe was considered, but it does not support Python 3.7."""),
_(u"""	* A promising alternative is cx_freeze."""),
_(u"""5. Members of the public should be invited to test a series of try builds meant to test transition work, test add-ons, documentation purposes, community outreach and other steps."""),
"",_(u"""Estimated completion: four to six months after pre-transition steps are completed."""),
"",_(u"""### After transition:"""),
"",_(u"""1. A beta of NVDA powered by python 3 must be released."""),
_(u"""2. Members of the public should provide beta-level feedback."""),
_(u"""3. Add-on developers are asked to start porting their add-ons to Python 3."""),
_(u"""4. A stable version of NVDA powered by Python 3 is released."""),
_(u"""5. Post-transition evaluation should take place, including documenting issues found during field testing, more community outreach and other activities."""),
"",_(u"""Estimated completion date: no later than twelve to fifteen months after pre-transition activities are completed."""),
"",_(u"""## Transition progress"""),
"",_(u"""1. Before transition (in progress):"""),
_(u"""	1. July 17, 2018: NVDA alpha snapshot powered by wxPython 4.0.3 was released."""),
_(u"""	2. August 17, 2018: NVDA 2018.3 beta 3, the first beta release powered by wxPython 4.0.3, was released."""),
_(u"""	3. August 21, 2018: alpha snapshots include Python 3 import edits. Source code changed to use Python 3 module names in most cases."""),
_(u"""2. Transition: Not yet begun."""),
_(u"""3. After transition: not yet begun."""),
"",_(u"""## Notes for various audiences"""),
"",_(u"""### For code contributors:"""),
"",_(u"""* Document potential and actual issues when working with Python 3, including changed modules, attribute name chnages, internal changes and so on."""),
_(u"""* When importing a built-in Python module, use try/except when importing modules."""),
_(u"""	* Try importing Python 2 names as Python 3 name, switching to Python 3 version when Python 2 module is not found or renamed."""),
_(u"""	* See NVDA source code for implementation steps."""),
_(u"""* Pull requests should be based on master branch unless specified by lead developers."""),
_(u"""* Try using branch name of the form \"py3*\" where \"*\" denotes Python 3 feature e.g. py3socketserver for changes to socket server module."""),
_(u"""* If working with built-in Python modules, be sure to test your code via Python 2.7 and 3.7 interpreter before making changes to NVDA source code."""),
_(u"""	* Create a standalone script that'll use features from Python 2 and/or 3."""),
_(u"""	* After testing this script and if it works in Python 3, make changes to NVDA source code and add comments regarding differences between Python 2 and 3."""),
_(u"""	* Source code should target both Python 2 and 3 unless the pull request is submitted during active transition period."""),
_(u"""* Edit this page whenever major changes are committed to master branch or pull request is merged, including import changes and such."""),
"",_(u"""### For add-on developers:"""),
"",_(u"""* Try using Python modules that are known to be compatible with both Python 2 and 3."""),
"",_(u"""### For testers:"""),
"",_(u"""Nothing yet, as transitoin hasn hasn't begun."""),
"",_(u"""### For translators:"""),
"",_(u"""Nothing yet."""),
"",_(u"""### For users:"""),
"",_(u"""### For organizations:"""),
"",_(u"""* Stay informed on Python 3 transition workflow."""),
"",_(u"""### For Python community:"""),
"",_(u"""* During pre-transition period, please help NVDA project spot potential issues with Python 3 transition so they can be noted."""),
_(u"""* During transition, please help write and test Python 3 code and provide additional comments."""),
]