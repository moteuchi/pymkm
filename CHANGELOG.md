# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Added
- Lightweight usage reporting

## [1.0.4]
### Added
- Configurable rounding limits for prices.
### Changed
- Broke out the console menu to a separate class.
### Removed
- Cached price changes. It was not very useful. This also fixed one bug.

## [1.0.2] - 2019-07-08
### Fixed
- Fixed a bug with comparing prices for cards not found in stock.

## [1.0.1] - 2019-06-24
### Fixed
- Fixed a bug where the cached price changes file was not present.

## [1.0.0] - 2019-06-18
### Added
- More tests, making it easier to spot bugs and errors.
- This changelog.

### Changed
- Refactored the menu printing function and added version number.