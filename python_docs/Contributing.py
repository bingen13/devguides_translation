# -*- coding: utf-8 -*-
documentation = [
_(u"""# Contributing to NVDA"""),
_(u"""If you would like to contribute code or documentation to NVDA, please follow these guidelines."""),
"",_(u"""## Testing"""),
"",_(u"""Testing alpha / beta / and release candidates help to ensure the quality of the NVDA."""),
_(u"""User / community testing is particularly important for languages other than English."""),
_(u"""There are several approaches you may take for this:"""),
_(u"""- Unfocused usage: Just use NVDA as you normally would, and try to complete everyday tasks."""),
_(u"""- Recent change focused testing: By following the changes that are being made to NVDA and purposefully testing these changes and looking for edge-cases."""),
_(u"""- Regression testing: Testing older features and behavior to look for unintended regressions in behavior that don't seem related to recent changes."""),
"",_(u"""Forming a group can help you to get good coverage, brainstorm on what should be tested, and perhaps learn new ways to use NVDA."""),
"",_(u"""## Issue triage and investigation:"""),
_(u"""You can also make non-code contributions by helping process incoming Github issues. For information on this please see the [triage process](https://github.com/nvaccess/nvda/wiki/Triage-process) and [issue triage help](https://github.com/nvaccess/nvda/wiki/Issue-triage-help) on the wiki."""),
"",_(u"""## Submitting Changes"""),
"",_(u"""For anything other than minor bug fixes, please comment on an existing issue or create a new issue providing details about your proposed change."""),
_(u"""Unrelated changes should be addressed in separate issues."""),
_(u"""Include information about use cases, design, user experience, etc."""),
_(u"""This allows us to discuss these aspects and any other concerns that might arise, thus potentially avoiding a great deal of wasted time."""),
_(u"""You should generally wait for acceptance of your proposal before you start coding. Please understand that we very likely will not accept changes that are not discussed first."""),
"",_(u"""If this is a minor/trivial change which definitely wouldn't require design, user experience or implementation discussion (e.g. a fix for a typo/obvious coding error or a simple synthesizer/braille display driver), you can just create a pull request rather than using an issue first. However, this should be fairly rare. If in doubt, use an issue first. Use this issue to discuss the alternatives you have considered in regards to implementation, design, and user experience. Then give people time to offer feedback."""),
"","",_(u"""If this is your first contribution, you will first need to \"fork\" the NVDA repository on GitHub."""),
"",_(u"""When you fork the repository, GitHub will create a copy of the master branch. However, this branch will not be updated when the official master branch is updated. To ensure your work is always based on the latest commit in the official master branch, it is recommended that your master branch be linked to the official master branch, rather than the master branch in your GitHub fork. If you have cloned your GitHub fork, you can do this from the command line as follows:"""),
"",_(u"""```"""),
_(u"""# Add a remote for the NV Access repository."""),
_(u"""git remote add nvaccess https://github.com/nvaccess/nvda.git"""),
_(u"""# Fetch the nvaccess branches."""),
_(u"""git fetch nvaccess"""),
_(u"""# Switch to the local master branch."""),
_(u"""git checkout master"""),
_(u"""# Set the local master to use the nvaccess master as its upstream."""),
_(u"""git branch -u nvaccess/master"""),
_(u"""# Update the local master."""),
_(u"""git pull"""),
_(u"""```"""),
"",_(u"""You should use a separate \"topic\" branch for each issue."""),
_(u"""All code should usually be based on the latest commit in the official master branch at the time you start the work unless the code is entirely dependent on the code for another issue."""),
_(u"""Branches should *never* be based on the \"next\" branch."""),
"",_(u"""If you are adding a feature or changing something that will be noticeable to the user, you should update the User Guide accordingly."""),
"",_(u"""For anything touching code, please run `scons tests` before you open your Pull Request, and make sure all the unit tests pass. If possible for your PR, please consider creating a set of unit tests to test your changes. Please also run our linter, see [`tests/lint/readme.md`](https://github.com/nvaccess/nvda/tree/master/tests/lint) for more information."""),
"",_(u"""### Create a Pull Request (PR)"""),
"",_(u"""When it is time to submit your code, you should open a pull request referring to the original issue."""),
_(u"""Code review will then be done on this pull request."""),
_(u"""Pull requests that fix bugs will be reviewed before PR's that add features / enhancements."""),
"",_(u"""## Code Style"""),
"",_(u"""Code style is enforced with the flake8 linter, see [`tests/lint/readme.md`](https://github.com/nvaccess/nvda/tree/master/tests/lint) for more information."""),
"",_(u"""### Encoding"""),
_(u"""* Where Python files contain non-ASCII characters, they should be encoded in UTF-8."""),
_(u"""    * There should be no Unicode BOM at the start of the file, as this unfortunately breaks one of the translation tools we use (xgettext). Instead, include this as the first line of the file (only if the file contains non-ASCII characters):"""),
_(u"""        ```"""),
_(u"""        # -*- coding: UTF-8 -*-"""),
_(u"""        ```"""),
_(u"""    * This coding comment must also be included if strings in the code (even strings that aren't translatable) contain escape sequences that produce non-ASCII characters; e.g. `\"\\xff\"`. This is particularly relevant for braille display drivers. This is due to a gettext bug; see https://github.com/nvaccess/nvda/issues/2592#issuecomment-155299911."""),
_(u"""* Most files should contain CRLF line endings, as this is a Windows project and can't be used on Unix-like operating systems."""),
"",_(u"""### Indentation"""),
_(u"""* Indentation must be done with tabs (one per level), not spaces."""),
_(u"""* When splitting a single statement over multiple lines, just indent one or more additional levels. Don't use vertical alignment; e.g. lining up with the bracket on the previous line."""),
_(u"""  - Be aware that this requires a new-line after an opening parenthesis/bracket/brace if you intend to split the statement over multiple lines."""),
_(u"""  - For the parameter list of function definitions, double indent, this differentiates the parameters and the body of the function."""),
"",_(u"""### Identifier Names"""),
_(u"""* Use descriptive names"""),
_(u"""  - name constants to avoid \"magic numbers\" and hint at intent or origin of the value. Consider, what does this represent?"""),
_(u"""* Functions, variables, properties, etc. should use mixed case to separate words, starting with a lower case letter; e.g. `speakText`."""),
_(u"""* Boolean functions or variables"""),
_(u"""  - should try to use the positive form of the language (to avoid double negatives like `shouldNotDoSomething = False`)"""),
_(u"""  - start with a \"question word\" to hint at their boolean nature. EG `shouldX`, `isX`, `hasX`"""),
_(u"""* Classes should use mixed case to separate words, starting with an upper case letter; e.g. `BrailleHandler`."""),
_(u"""* Constants should be all upper case, separating words with underscores; e.g. `LANGS_WITH_CONJUNCT_CHARS`."""),
_(u"""* Event handlers are prefixed with \"event_\", and are often in the form \"event_ACTION\" or \"event_OBJECT_ACTION\". Where OBJECT refers to the class type that the ACTION refers to."""),
_(u"""* Extension points:"""),
_(u"""  * `Action`: Prefixed with `pre_` or `post_` to specify that handlers are being notified before / after the action has taken place."""),
_(u"""  * `Decider`: Prefixed with `should_` to turn them into a question eg `should_doSomething`"""),
_(u"""  * `Filter`: TBD. Ideally follows a similar style the others, and communicates if the filtering happens before or after some action. It would also be nice to have a naming scheme that differentiates it from the others."""),
"",_(u"""### Translatable Strings"""),
_(u"""* All strings that could be presented to the user should be marked as translatable using the `_()` function; e.g. `_(\"Text review\")`."""),
_(u"""* All translatable strings should have a preceding translators comment describing the purpose of the string for translators. For example:"""),
_(u"""```"""),
_(u"""# Translators: The name of a category of NVDA commands."""),
_(u"""SCRCAT_TEXTREVIEW = _(\"Text review\")"""),
_(u"""```"""),
]