# Contributing

Thank you for contributing to Cortex AI Skills.

For improvements to instructions or technical examples, follow the [detailed policy](source/CONTRIBUTING.md) and [architecture](source/ARCHITECTURE.md). Include the product, version, specific official source, and validation scope.

## Documentation

The README and `docs/` contain the current usage documentation. Preserve historical reports and distinguish verified facts, documentation changes, and tests that have not been performed.

## Packages

Preserve the versioned archives, manifest, and checksums under `packages/0.1.0/`; do not silently replace them. The human-readable package index may be translated without changing those artifacts. Runtime changes require appropriate versioning, hashes, and validation. Do not distribute tests or answer keys inside runtime packages.

## Checks before submitting a change

Run the build and validation commands in the [README](README.md). Do not publish credentials, raw customer data, dumps, or private identifiers. Use synthetic or anonymized examples.

This project does not install integrations, execute queries, or apply changes to your tenant as part of its publication tests.
