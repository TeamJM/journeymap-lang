JourneyMap Language Files
=========================

[![Website](https://img.shields.io/badge/Website-journeymap.info-FF7139?logo=Mozilla%20Firefox)](https://journeymap.info) [![Discord](https://img.shields.io/discord/239040424214396929?color=7289DA&label=Discord&logo=Discord)](https://discord.gg/eP8gE69)

This repository contains the latest version of the language files that are used by the mod. We're making these public
in order to allow for additions to be made by the community. If you'd like to add translations for your language
(or correct the translations already preset), please see below for information on contributing.

[![Creative Commons BY-NC-ND 4.0](https://licensebuttons.net/l/by-nc-nd/4.0/88x31.png)](http://creativecommons.org/licenses/by-nc-nd/4.0/)
This work is licensed under a 
[Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License](http://creativecommons.org/licenses/by-nc-nd/4.0/).

**Please note**: _This is a development repository. If you're a JourneyMap user, you do not need anything in this
repo - everything you need will be included with the JourneyMap mod itself._

Contributing
============

We're huge fans of the open source community, and we're happy to accept pull requests. If you'd like to chat with us
before making a contribution, we suggest you join [join the discord server](https://discord.gg/eP8gE69). Please also 
take a look at the [Code of Conduct](CONDUCT.md) before posting an issue, PR or comment.

How to translate JourneyMap
===========================

Before getting started, please take the following steps:

1. [Sign up](https://github.com/join) for a free account on GitHub if you don't have one already
1. Review [the current issues](https://github.com/TeamJM/language-files/issues) for a list of known translation needs
1. Read the [How to translate JourneyMap](https://journeymap.info/Translate_JourneyMap_For_Your_Language) wiki page 
   for detailed instructions on doing a translation correctly

   _**Note**: Changes to `en_us` files are generally not accepted unless they address typos_

If you have questions or need help, feel free to [join the discord server](https://discord.gg/eP8gE69). Please be
patient and hang around; it may be minutes or hours before someone sees your question.

---

You can either use your web browser to suggest changes to our translations, or you can use Git directly if you're
already comfortable with it.

Using your browser
------------------

If you're new to working with GitHub or aren't a programmer, the easiest way to contribute a translation is using the
GitHub website directly in your browser.

1. First of all, open the file you need for editing.

   **If a file doesn't already exist for your language**: Navigate to the `lang` folder, and click **Create new file** at 
   the top of the file list. Make sure to enter a name for your file in the box provided above the editor - for example,
   `es_es.json` would be the correct name for a Spanish language file. Your file should contain 
    
   **If a file exists for your language**: Simply navigate to it and click on the pencil icon at the top right to begin 
   editing.
1. Make your edits to the file, and **provide some additional context for your edits** by writing a summary in the boxes 
   provided.
1. Click **Propose file change** to open a pull request. This will be used to keep track of the changes you've made, and
   will allow us to merge them into our copies of the files.

   * If you have further changes to make, feel free to keep editing. You'll find that a copy of this repository has
     been created under your own account when you opened your pull request - continue to edit the files in your copy
     and the changes will be added to your pull request.
1. Wait. We'll review your pull request and provide you with feedback; the pull request will be merged when we're
   happy with your changes. At this point, **your job is done** - your translations will show up in a future version of
   JourneyMap!

Using Git
---------

If you're already familiar with Git, feel free to make use of it in the usual way. If you're using Git then we assume
that you're used to working collaboratively in this way, but here's what you need to do:

1. Click the **Fork** button at the top of the page and, if prompted, select your GitHub account as the target for the
   fork.
1. On your own computer, clone the repository to a local directory. You can find a command to copy-and-paste by clicking
   on the **Clone or Download** button just above the list of files in your fork.
1. Create a new branch for your changes. **This is important!** You can use `git checkout -b branchname` to create
   a new branch - we suggest naming your branch after the language you're working with, but anything other than
   `master` is fine for a branch name.
1. Make your changes. Remember that all new language files must be of the form `LOCALE.json`, where `LOCALE` is the
   locale code for the language you're working with - for example, `es_es` for Spanish.
1. Use `git commit -a -m "summary"` to create a commit with your changes. Remember to make sure your summary is
   descriptive!
1. Use `git push` to push your changes to GitHub.
1. Navigate to your fork on GitHub, and you'll see a prompt to create a new pull request with your changes. Click on
   the button and follow the instructions to create your pull request.
1. If you have further changes to make, feel free to keep editing, committing, and pushing. All new changes made to
   your fork will automatically appear in the pull request.
1. Wait. We'll review your pull request and provide you with feedback - the pull request will be merged when we're
   happy with your changes. At this point, your job is done; your translations will show up in a future version of
   JourneyMap!

Dealing with problems
---------------------

**If you notice a translation error, an issue with phrasing or other similar issue**: Please follow the instructions
above to contribute a fixed translation.

**For all other issues** (for example, display issues in the mod):

1. Locate the problematic message key in the language files
1. Check that the issue hasn't already been reported on the issues page
1. Click the **New issue** button and provide a title, making sure to reference the message key and locale name
   
   For example: `Problem displaying jm.advanced.announcemod.tooltip in es_es`
1. Provide a detailed description of the problem you see as part of the issue comment
1. Take screenshots and attach them to your issue before submission
