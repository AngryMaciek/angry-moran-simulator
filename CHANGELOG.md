# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

- Added: makefile for development
- Changed: CI builds for linux/mac a pip/conda pkg separately, installs it and tests import; unit tests run on **not**-installed pkg.
- Fixed: Circular import errors

## [1.0.29] - 2020-12-28

### Added

- PiPI package
- _conda_ package
- new installation notes
- GitHub Action: workflow to automatically publish tagged commits
- interactive usecase notebook inspection via _binder_



[unreleased]: https://github.com/AngryMaciek/angry-moran-simulator/compare/1.0.29...HEAD
[1.0.29]: https://github.com/AngryMaciek/angry-moran-simulator/releases/tag/1.0.29
