# -*- coding: utf-8 -*-
documentation = [
_(u"""# Making an Official Release"""),
"",_(u"""The following instructions are for the release manager and detail how to make an official release."""),
"",_(u"""## Starting the beta"""),
_(u"""* Decide which commit to start the beta from."""),
_(u"""  - Generally master should be healthy (all checks passing and no known regressions)."""),
_(u"""  - The most recent (significant) change should have had at least one week of alpha testing."""),
_(u"""* Merge this commit into beta"""),
_(u"""* Create a new pre-release with the [Github new release page](https://github.com/nvaccess/nvda/releases/new)"""),
_(u"""  - Tag Version example: `release-2019.2beta3`"""),
_(u"""  - Target: `beta`"""),
_(u"""  - Release Title example: `Release 2019.2beta3`"""),
_(u"""  - No description necessary for first beta, subsequent betas can describe important additions / removals."""),
_(u"""  - Ensure option \"This is a pre-release\" is checked."""),
_(u"""  - The tag must have a `release-` prefix."""),
_(u"""  - This creates a new annotated tag. E.g. release-2019.2beta3"""),
_(u"""  - beta will now show up on the snapshots page"""),
_(u"""  - Auto update system will start offering it to those checking for betas"""),
_(u"""* Do a review of the `user_docs/en/changes.t2t` file."""),
_(u"""  - Ask for a second review."""),
"",_(u"""## During the Beta period"""),
_(u"""* Periodically look at recent issues filed, specifically looking for those with `p1`, `crash` or `appcrash` labels."""),
_(u"""* Periodically look for PRs based on beta and ensure they are reviewed then merged or rejected."""),
_(u"""  - As PRs based on the beta branch are merged, periodically tag further betas."""),
"",_(u"""## End of Beta period"""),
_(u"""* After the final beta, [call a translation freeze](https://github.com/nvaccess/nvda/wiki/StartingTranslationFreeze) for 2 weeks. No more commits should be made to the beta branch at this time."""),
"",_(u"""## Second translation freeze"""),
_(u"""Normally not required, however, if it is discovered that translations need to be updated after the translation freeze has started/completed then:"""),
"",_(u"""* Ensure `beta` has the changes requiring re-translation."""),
_(u"""* Re complete the steps in calling a translation freeze."""),
_(u"""* Send an email to the translation mailing list describing the need for new changes and deadline."""),
_(u"""* After translation freeze, """),
"",_(u"""## Release candidates"""),
_(u"""* Ensure it is safe to release an RC."""),
_(u"""  - Looking at recent issues filed, specifically looking for those with `P1`, `crash` or `appcrash` labels."""),
_(u"""* If this is `RC1`, update translations:"""),
_(u"""    1. Log into exbi and su to nvdal10n."""),
_(u"""    2. `cd ~/mr/mainNVDACode`"""),
_(u"""    3. `mr up`"""),
_(u"""    4. `cd ../srt`"""),
_(u"""    5. `mr up`"""),
_(u"""    6. `mr svn2nvda`"""),
_(u"""  - Note, this updates `beta` with the new translations."""),
_(u"""* Update the `rc` branch"""),
_(u"""  - For RC1, reset the `rc` branch to `beta`"""),
_(u"""  - For RC1+, merge `beta` to `rc`"""),
_(u"""* Check for PRs against `rc`"""),
_(u"""  - look for any PRs based on `rc`, and review and approve/merge or reject them."""),
_(u"""* Create a new pre-release with the [Github new release page](https://github.com/nvaccess/nvda/releases/new)"""),
_(u"""  - Tag Version example: `release-2019.2rc1`"""),
_(u"""  - Target: `rc`"""),
_(u"""  - Release Title example: `Release 2019.2rc1`"""),
_(u"""  - No description necessary for first RC, subsequent RCs can describe important additions / removals."""),
_(u"""  - Ensure option \"This is a pre-release\" is checked."""),
_(u"""  - The tag must have a `release-` prefix."""),
_(u"""  - This creates a new annotated tag. E.g. release-2019.2rc1"""),
_(u"""* Wait for the appVeyor build to complete."""),
_(u"""  - Tagging the release triggers this automatically."""),
_(u"""  - As part of this, the release will be staged."""),
_(u"""* Publish the staged release."""),
_(u"""  - On exbi: `su` to the `nvaccess` user and run `nvdaRelease`"""),
_(u"""* Publicise the release."""),
_(u"""  - Add a blog post on  www.nvaccess.org"""),
_(u"""    - Put post in the `Development` category. It should never be placed in the `News` category."""),
_(u"""    - Use a previous blog post as a base."""),
_(u"""    - If this is not the first pre-release, include a list of changes since the last pre-release."""),
_(u"""  - Email nvda-devel list"""),
_(u"""  - Email nvda-translations list"""),
_(u"""  - Post to Twitter"""),
_(u"""* Scan the launcher executable"""),
_(u"""  - Use [VirusTotal](http://www.virustotal.com/). Just submit the direct download URL."""),
"",_(u"""## Final release"""),
_(u"""* Create a new release with the [Github new release page](https://github.com/nvaccess/nvda/releases/new)"""),
_(u"""  - Tag Version example: `release-2019.2`"""),
_(u"""  - Target: `rc`"""),
_(u"""  - Release Title example: `Release 2019.2`"""),
_(u"""  - No description necessary for final release"""),
_(u"""  - Ensure option \"This is a pre-release\" is **not** checked."""),
_(u"""  - The tag must have a `release-` prefix."""),
_(u"""  - This creates a new annotated tag. E.g. release-2019.2"""),
_(u"""* Wait for the appVeyor build to complete."""),
_(u"""  - Tagging the release triggers this automatically."""),
_(u"""  - As part of this, the release will be staged."""),
_(u"""* Publish the staged release."""),
_(u"""  - On exbi: `su` to the `nvaccess` user and run `nvdaRelease`"""),
_(u"""* Close the release [milestone](https://github.com/nvaccess/nvda/milestones)."""),
_(u"""* Ensure the subsequent milestone is set on issues and pull requests now closed by GitHub automatically."""),
_(u"""  1. Get the milestone id for the new release."""),
_(u"""     - Go to https://github.com/nvaccess/nvda/milestones"""),
_(u"""     - Look at the link URL for the relevant milestone."""),
_(u"""     - The number at the end is the id."""),
_(u"""  2. On exbi, edit `~nvaccess/data/nvaServer.conf`"""),
_(u"""  3. In the `[nvdaGithub]` section, change the value of `autoCloseMilestone` to the milestone id obtained in step 1."""),
_(u"""  4. Reload `uwsgi` so the change takes effect: `sudo systemctl reload uwsgi`"""),
_(u"""* Publicise the release."""),
_(u"""  - Add a blog post on  www.nvaccess.org"""),
_(u"""    - Put post in the `Releases` category."""),
_(u"""    - Use a previous blog post as a base."""),
_(u"""  - Email nvda-devel list"""),
_(u"""  - Email nvda-translations list"""),
_(u"""  - Post to Twitter"""),
_(u"""  - Post on Facebook."""),
_(u"""  - Post to the NV Access News email list."""),
_(u"""* Ensure `master` version number and changes file are correct"""),
_(u"""    1. In `source/buildVersion.py`, update the `version_year` and/or `version_major` variables for the next version."""),
_(u"""       - If the next version is the first version for that year (e.g. 2018.1), also update `copyrightYears`."""),
_(u"""    2. Add a heading for the next version in `user_docs/en/changes.t2t`."""),
_(u"""* Scan the launcher executable"""),
_(u"""  - Use [VirusTotal](http://www.virustotal.com/). Just submit the direct download URL."""),
]