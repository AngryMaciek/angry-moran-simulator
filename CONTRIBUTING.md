# Contributing

## Reporting bugs 🐛

Before reporting a bug, try to search for a similar problem in the *Issues* section on GitHub. Clear the search bar to include closed issues in the search and type your phrase.

If you have not found a relevant issue, you can report the bug in the *Issues* section. When you click on *New issue*, two templates will be displayed — please pick *Bug Report*. Carefully fill out the template and submit the issue.

## Requesting features 💡

If you have an idea for improvement, you can submit your proposal in the *Issues* section on GitHub. When you click on *New issue*, two templates will be displayed — please pick *Feature Request*. Carefully fill out the template and submit the issue.

## Pull requests ⤴️

**Working on your first Pull Request?** You can learn how from this *free* series [How to Contribute to an Open Source Project on GitHub](https://kcd.im/pull-request)

### Local development environment setup

In order to begin working on the project, please complete these tasks:

1. Clone our repository and enter the project's root directory:

   ```
   git clone https://github.com/AngryMaciek/angry-moran-simulator.git
   cd angry-moran-simulator
   ```
2. Install Conda (package management system and environment management). You can find the installation instructions in
   [Anaconda page](https://www.anaconda.com/) or in [Miniconda page](https://docs.conda.io/en/latest/miniconda.html).
3. Install Mamba package manager on top, according to [these instructions](https://mamba.readthedocs.io/en/latest/installation.html#existing-conda-install).
4. (Optional) This tools is (also) packaged as a _conda_ package. If you plan to build it during development please install [conda-build](https://docs.conda.io/projects/conda-build/en/latest/install-conda-build.html) or [boa](https://boa-build.readthedocs.io/en/latest/getting_started.html#installation) together with [conda-verify](https://anaconda.org/anaconda/conda-verify). These should be installed in `base` environment too, otherwise [bad things will happen](https://github.com/conda/conda-build/issues/3813).
5. Setup a Conda environment to install all needed dependencies:

   ```bash
   mamba env create
   ```
6. In order to activate new created Conda environment type:

   ```bash
   conda activate moranpycess-dev
   ```

   If you have no experience with Conda environments, read about them
   [under this address](https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html).
7. Install our [pre-commit](https://pre-commit.com/) hooks into your local version of the repository:

   ```bash
   pre-commit install
   ```
8.  To install moranpycess in your development environment please run:

   ```bash
   make install # Linux, macOS
   pip install . # Windows
   ```

   If you want to uninstall it use:

   ```bash
   make uninstall # Linux, macOS
   pip uninstall moranpycess --yes # Windows
   ```

### Ephemeral development environment

(╯°□°)╯︵ ┻━┻  
If that above is you, feeling like flipping a table just by the sheer looks of all the instructions above, do not despair! You still can contribute to our codebase from the cloud! We set up an ephemeral [Gitpod](https://www.gitpod.io) environment for all the developers who prefer coding from a remote server.

Just click on this cool button below:  
[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/AngryMaciek/angry-moran-simulator)

See more information on how to start up a _Gitpod_ environment dedicated to a specific remote branch [here](https://www.gitpod.io/docs/introduction/learn-gitpod/context-url#branch-and-commit-contexts), specific issue [here](https://www.gitpod.io/docs/introduction/learn-gitpod/context-url#issue-context) and a specific pull request [here](https://www.gitpod.io/docs/introduction/learn-gitpod/context-url#pullmerge-request-context).

However, please remember that such luxury is limitted:

> Gitpod offers a free plan for new users which includes 50 hours of standard workspace usage.
> If you need more hours, you can upgrade to one of the paid plans in your personal settings.

### Branch naming convention

You can read about git branching [under this address](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging). The branch names should follow the convention specified below:

```
<type>/<issue id>/<short description>
```

where

- **type** is one of the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)' types, i.e. `feat`, `ci`, `docs`, `fix`, `refactor`, `test`, `chore`, etc.
- **issue id** is the id of the issue which will be fixed by this PR.
- **short description** is ~25 characters long at max and is hyphenated.

Examples:

```
chore/6/gitignore
ci/20/testing-and-code-coverage
ci/21/flake8-action
ci/46/docstring-linting
docs/22/contributing-instructions
feat/3/license
feat/4/github-templates
feat/40/version-flag
feat/7/code-of-conduct
refactor/8/initial-project-structure
```

### Performing checks before submitting the pull request

Make sure the following checks pass with no errors:
* `make format`
* `make lint`
* `make test`
* `make install`
* `make build`

### Merging the pull request

A pull request can only be merged after it completed all of the checks performed by CI. After a manual review by one of the maintainers, it can be merged into `master`. The merge commit should follow the rules outlined in [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/).
