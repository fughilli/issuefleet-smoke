# issuefleet-smoke

Smoke test for issuefleet — a simple hello-world Python app built with a
hermetic [Bazel](https://bazel.build/) (bzlmod) configuration.

## Hermetic setup

- Bazel version is pinned in `.bazelversion` (managed by `bazelisk`).
- `MODULE.bazel` registers `rules_python` and a pinned CPython 3.12 toolchain,
  so builds use a downloaded interpreter rather than the system Python.
- `MODULE.bazel.lock` pins the resolved dependency graph for reproducibility.

## Build & run

```sh
bazel run //src:hello           # -> Hello, world!
bazel run //src:hello -- Fleet  # -> Hello, Fleet!
```

## Test

```sh
bazel test //src:hello_test
```
