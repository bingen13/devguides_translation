# Add on Store Proposal

The intention of this proposal is to improve the end to end process and supporting infrastructure for hosting Addons.
This is the current plan from NV Access.
However, before starting this work we would like feedback from the add-ons community, particularly addon authors and addon reviewers since this will affect them the most.

The main goal of this is to enable an "NVDA addon store" accessible from within NVDA itself.
In this proposal the word "store" is used to refer to the system allowing users to acquire addons, there is no intention of supporting paid addons.
This "store" system includes any website, API, process, or infrastructure to support users to browse, search, install and update Addons for NVDA.

Many considerations in this proposal have been given to creating a more secure and robust NVDA Addon store.
While there is little that can be done to guarantee an addon is safe to run, we can ensure that all versions are viewed, and that users are running the addon they think they are.
The process is intended to be as transparent as possible to make it simple (for developers) to understand the current state of the store or the state of a submission of a new / updated addon pending review.
The process should enable authors and reviewers to learn about and improve the addon-review process.

Much of the recent [conversation on the addons mailing list](https://nvda-addons.groups.io/g/nvda-addons/topic/69393202#10878) has been about reviewing Addons.
While NV Access has some opinions on this, I think it will be more productive to first focus on the steps around this.
For now, this step will just be referred to as 'review performed'.
Later, I suggest a new thread to agree on a "addon review check list".
With the right infrastructure, we can automate many checks and reduce the burden on reviewers.

This proposal does not intend to restrict Addon authors from developing, publishing, and distributing Addons outside of this store.
NVDA will still allow local installation from a `*.nvda-addon` file.

## Too Long; Didn't Read for Addon authors
With this proposal if an addon author wishes to submit their addon to be visible in this addon store they will need to:
- Store their addon on Github in an open (not private) repository.
- Create an issue on the `addon-store-submission` repository for each addon version they want to make available.
- Paste into the issue description a link to the commit or github release.
- Wait for it to be reviewed and accepted or participate in review actions and resubmit the new version.

## Too Long; Didn't Read for Addon reviewers
As an Addon reviewer you will:
- Look at pending PR's on the `addon-store-submission` repository.
- These will include a link to the addon version being reviewed.
- Follow the review process (yet to be documented here).
- Either 'approve' the PR, or 'request changes' while providing feedback and close the PR.
- When approving the PR, press the merge button to finalise the submision.

## Considerations

- Submissions and reviews should be easy to find and get the status of.
- Make it possible to automate many steps in the process, saving reviewers time.
- Once submitted an addon version should be immutable. No changing the addon on an external server, it must be updated in the store via the submission process.
- Allow addon authors to easily revoke a version if it is buggy / no longer supported. It should no longer be presented in the store, halting installation by new users.
- Enable support in the store for multiple versions of an Addon, based on NVDA version.
  - EG addon version 1.2.5 for NVDA 2019.3 and addon version 1.3.2 for NVDA 2020.1
- Enable support in the store for 'pre-release' Addons, for instance:
  - Addons being developed against alpha / beta NVDA.
  - Addons that want early feedback from end users.
  - End users can choose "show me pre-release addons"

## Overview

Use GitHub reviews for store submissions.
Use GitHub for storage of meta-data for addons available from the store.
Use GitHub actions (or other integrations) to automate construction of the data store, and as many of the review checks as possible. This will all be open source and extensible by the community.

### Why GitHub reviews?
- GitHub is where much of the NVDA development ecosystem is already based.
- Handles all the of the CRUD ([create, read, update, delete](https://en.wikipedia.org/wiki/CRUD)) for users, authentication is handled, and we can determine how a user relates to an addon repository and what their permissions are for that repository. Are they actually an owner / maintainer?
- GitHub has a review system that allows for proposing changes and discussing these changes. We can leverage this for a store submission and review process.
- GitHub PR's provided a atomic view of a store submission.
- Interested parties can 'watch' PR's they care about without being subjected to the noise from PR's they don't care about.
- The result (open / merged / closed) of the PR is clear.
- GitHub allows us to manage permissions for accepting reviews more easily.

## Infrastructure

- `NVDA-Addon-submission` GitHub Repository
  - For Addon authors / reviewers.
  - Where new Addon versions are submitted
  - Where reviews of Addon submissions happen
- `NVDA-Addon-store-data` GitHub Repository
  - For storage of meta-data about addons "in the store"
  - This repository acts as a back-end database, but is more transparent.
  - Since our needs are simple, preconfigured "views" of the data will suffice.
- NV Access server - To provide the endpoint for "available Addons" meta-data
  - While this is technically not necessary, it provides a good separation from implementation.
    If we wished to change our storage mechanism, we would not be breaking old versions of NVDA.

## `NVDA-Addon-submission` GitHub Repository

Essentially this repository holds references to all the accepted versions of Addons which are included in the store. A reference to an old version of an addon remains until it is explicitly removed or becomes invalid, allowing delivery to older versions of NVDA, or as a fall back in case the newer version is revoked after a critical bug is found.
Addons versions are submitted by submitting a pull request, adding the commit for that version to a file that describes the GitHub repository for the addon.

### Layout

Root directory of repository:
 - `readme.md` - A guide for submission
 - `addons/owner1/repo1.commits`
 - `addons/owner1/repo2.commits`
 - `addons/owner2/repo3.commits`

Example for the NV Access addon, 'NVDA - OCR': `addons/nvaccess/nvda-ocr.commits`

Contents of a `*.commits` file, is a (newline separated) list of git SHAs, one for each commit which could be available in the store.
This is intentionally a very simple format to maximise the ease of editing, and minimise the risk of format corruption.
Commits are used rather than tags because tags can be changed after creation, a SHA collision should be quite difficult to achieve.
This is important to stop the possibility of a malicious author changing an addon post review, bypassing the review process.

### Submitting an Addon version

Pre-requisites:
- An addon must be stored on GitHub in a public repository
- The commit which will be submitted must be a valid NVDA `*.nvda-addon` file if zipped and renamed.

Process:
1. A PR is created on the `NVDA-Addon-submission` repository
   - It adds/removes the SHA of the commit (for the submitted version) to the appropriate `addons/owner/repo.commits` file.
   - Refer to 'Creating the submission PR' below
1. A bot adds a comment in the PR with links to the addon versions that are added or removed
   - NOTE: the URL for this link can be is built from 'owner', 'repo', 'commit' of the lines added / removed. 
   - This allows the reviewer to browse the source online or download the addon with, see (in suffix) heading "Example of bot message for `NVDA-Addon-submission` PR" for an example message.
1. A review is performed (resulting in: request changes, merge, close)
   - A bot may perform some automated checks or provide helpful information, refer to 'automated review ideas' below
   - Manual review is done according to some published review check list (so that everyone knows what to expect)
   - Automated and human process can be decided later, we can address these details as they come up and improve upon the process
1. When the PR is merged, the Addon becomes available in the store.

### Creating the submission PR
To simplify the initial implementation of this process the PR will need to be created manually, later we can streamline this, and automate only requiring the addon author to paste a link in a new issue.

A new Pull Request (PR) is created on the `NVDA-Addon-submission` repository.
   1. Find or create a file: `addons/owner/repo.commits`
      - Example: `addons/nvaccess/nvda-ocr.commits`
      - Where 'owner' is the username or organisation that owns the addon GitHub repository. E.G. for `nvda-ocr` it is `nvaccess`
      - Where 'repo' is the name of the repository. E.G. `nvda-ocr`
      - NOTE: creating the file means this is an entirely new submission
   1. To submit a new version, add the SHA of the commit to the file
   1. For no longer supported addon versions, remove the SHA of the commit.
This could be done with the web editor, though screen reader users may be more comfortable making the changes locally with their chosen editor.

Because this requires addon authors to fork the `NVDA-Addon-submission` repository, this is a little cumbersome.
To streamline this process, we could use GitHub issues.
- The addon author would pick from two issue templates:
  - "Add addon version"
  - "Remove addon version"
- In the template they would paste a link to the commit or tag that should be added or removed.
- Automation creates the PR automatically from this and closes the issue.
- NOTE: In this approach it is safe to use a git tag, because the commit ID can be determined from the tag. The commit is then used in the PR and the rest of the process is the same.

### Automated review ideas
Several suggestions for automated review ideas to streamline the process.
- Check manifest validity
- Provide links to relevant diffs
- Check to see if the GitHub user submitting the PR is a maintainer of the Addon version being submitted.
- Consider using CI (Appveyor) to check the addon installs cleanly:
  - Install NVDA (the most recent version supported by the addon)
  - Install the addon
  - Restart NVDA and check for errors

### Concerns
This approach requires that an addon repository is already a valid (and installable) addon once it is zipped. Most addons require build steps.
 - Can github actions be used to run these steps and produce a certifiable build artifact?
   - If we can certify the source for a commit, and the source for the github actions that produces the artifact, then the artifact itself is certified?
   - If this is true we can provide this action along with the addon-template.

### Other notes
- By using a git repository and and PR process, `git blame` and `git log` can be used to get more context about addons listed in the store. For instance:
  - When was the addon accepted
  - What did the review look like
  - How often does this addon have updates accepted
- GitHub allows assigning reviews to reviewers

## `NVDA-Addon-store-data` GitHub Repository

Holds meta-data about addons accepted to the store.

Using a separate repository for this data store separates concerns, gives greater flexibility for managing permissions, makes it easier to verify changes (eg in a PR, or via automation), and simplifies the commit history (no automation commits "updating data store")

The exact implementation details for this repository are not exposed to users, because on one side the `NVDA-Addon-submission` repository feeds data in and the NV Access server is on the other side fetching and providing data to NVDA or a web based store.
This means that changing the layout or implementation of this repository does not cause wide breaking changes to the process and it can be updated independently.
Since the details of this repository don't really matter too much they don't need to be concrete at this point, however I'll give a brief overview of the current plan.

### Overview

For each version of NVDA, the meta-data of the most recent (highest version number) of each Addon is automatically added, based on the data in 'NVDA-Addon-submission'.

### Layout

Root directory of repository:
- `/NVDA API Version/addon-1-ID/release.json`
- `/NVDA API Version/addon-1-ID/pre-rel.json`
- `/NVDA API Version/addon-2-ID/release.json`
- `/NVDA API Version/all.json`

Notes:
- 'NVDA API Version' will be something like '2019.3', there will be one folder for each NVDA API Version.
- The `pre-rel.json` and `release.json` contain the information necessary for a store entry.
  This is essentially the URL to download the addon (a zip of the commit), and the rest of the contents of the addon manifest. Of course, by including translated descriptions in the manifest a multilingual addon store can be created, though possible not the core goal of this proposal.
- The contents of `all.data` is all (pre-release and release) data for this NVDA API version together.

The simplicity of this is that the NV Access server can just forward these files on directly when asked "what are the latest Addons for NVDA API Version X" or "What is the latest version of Addon-ID for NVDA API Version X". Using the NV Access server as the endpoint for this is important in case the implementation has to change or be migrated away from GitHub for some reason.

### How does data arrive
For the sake of a simple explanation, optimisations and minor details will be omitted from this description.

A GitHub Action is created to respond to a new commit on the `NVDA-Addon-submission` repository. For each commit in each `*.commits` file in the `NVDA-Addon-submission` repository, the manifest for the addon is fetched.

Addons manifests that support each NVDA API version are found.
For each NVDA API version the most recent (based on version number) release and pre-release addon manifest is kept.

These remaining manifest files are used to reconstruct the data in the repository and commit it.

## Suffix

### Example of bot message for `NVDA-Addon-submission` PR.

```
Added Version.
- [Browse source](https://github.com/nvaccess/nvda-ocr/tree/632d037dae906cd582ff4995628aa3fbaacd84e9)
- [Download zip](https://github.com/nvaccess/nvda-ocr/archive/632d037dae906cd582ff4995628aa3fbaacd84e9.zip)
```

### Pre-release addon version support

This will require an update to the addon-manifest. While this proposal plans for it, it will not be in the initial scope of work.

### Invalid Addon references

When building the data-store, any references to commits that no longer exist (repo deleted, history rewritten etc) will obviously be excluded since the manifest can not be fetched. Although not high priority, a mechanism may need to be developed to update the 'NVDA-Addon-submission' repository so that these invalid references can be removed.

### Terminology: Addon version vs Addon release

Since this proposal supports pre-release addons, I have tried to avoid using the term "addon release", instead favouring "addon version".
