# Guidelines for contributing

## Issue tracker

Please use each project's GitHub [issue tracker][res-issue-tracker] to:

- find issues to work on
- report bugs
- propose features
- discuss future directions

## Submitting issues

Please choose a template when submitting an issue: choose the [Bug report
template][res-bug-report] only when reporting bugs; for all other issues,
choose the [Feature request template][res-feature-request]. Please follow the
instructions in the template.

You do not need to worry about adding labels or milestones for an issue, the
project maintainers will do that for you. However, it is important that all
issues are written concisely, yet with enough detail and with proper
references (links, screenshots, etc.) to allow other contributors to start
working on them. For bug reports, it is essential that they include
reproducible examples.

Please **do not** use the issue tracker to ask usage questions, installation
problems etc., unless they appear to be bugs.

## Code style & testing

To make it easier for everyone to maintain, read and contribute to the code,
as well as to ensure that the code base is robust and of high quality, we
would kindly ask you to stick to the following guidelines for code style and
testing.

- Please use a recent version of [Python 3][res-py] (3.7.4+)
- Please try to conform to the used code, docstring and commenting style within
  a project to maintain consistency
- Please use type hints for all function/method signatures
  (exception: tests)
- Please use the following linters (use default settings unless otherwise
  stated):
  - [`flake8`][res-py-flake8]
- Please use the following test suites:
  - [`pytest`][res-py-pytest]
  - [`coverage`][res-py-coverage]

## Merging your code

Here is a check list that you can follow to make sure that code merges
happen smoothly:

1. [Open an issue](#submitting-issues) _first_ to give other contributors a
   chance to discuss the proposed changes (alternatively: assign yourself
   to one of the existing issues)
2. Clone the repository, create a feature branch off of the default branch
   (never commit changes to protected branches directly) and implement your
   code changes
3. If applicable, update relevant sections of the [documentation][res-documentation]
4. Add or update tests; untested code will not be merged; refer to the
   [guidelines](#code-style--testing) above for details
5. Ensure that your coding style is in line with the
   [guidelines](#code-style--testing) described above
6. Ensure that all tests and linter checks configured in the [Travis
   CI][res-travis-docs] [continuous integration][res-ci-cd] (CI) pipeline pass without
   issues
7. If necessary, clean up excessive commits with `git rebase`; cherry-pick and
   merge commits as you see fit; use concise and descriptive commit messages
8. Push your clean, tested and documented feature branch to the remote; make
   sure the Travis CI pipeline passes
9. Issue a pull request against the default branch; follow the instructions in
   the [template][res-pull-request]; importantly, describe your changes in
   detail, yet with concise language, and do not forget to indicate which
   issue(s) the code changes resolve or refer to; assign a project maintainer
   to review your changes


[res-issue-tracker]: <https://github.com/zavolanlab/binding-scanner/issues>
[res-bug-report]: .github/ISSUE_TEMPLATE/bug_report.md
[res-feature-request]: .github/ISSUE_TEMPLATE/feature_request.md
[res-py]: <https://www.python.org/>
[res-sh-shellcheck]: <https://github.com/koalaman/shellcheck>
[res-py-flake8]: <https://gitlab.com/pycqa/flake8>
[res-py-pytest]: <https://docs.pytest.org/en/latest/>
[res-py-coverage]: <https://pypi.org/project/coverage/>
[res-conv-commits]: <https://www.conventionalcommits.org/en/v1.0.0-beta.2/#specification>
[res-conv-commits-lint]: <https://github.com/conventional-changelog/commitlint>
[res-conv-commits-blog]: <https://nitayneeman.com/posts/understanding-semantic-commit-messages-using-git-and-angular/>
[res-docs]: README.md
[res-documentation]: workflow/documentation.md
[res-ci-cd]: <https://en.wikipedia.org/wiki/Continuous_integration>
[res-travis-docs]: <https://docs.travis-ci.com/>
[res-pull-request]: PULL_REQUEST_TEMPLATE.md
