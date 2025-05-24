# ruamelfmt

Autoformat your YAML files like [ruamel.yaml](https://pypi.org/project/ruamel.yaml/) does.

## Why?

You want to enforce a consistent style in YAML for many YAML documents in a git
repository that *humans* write, but you also want to be able to write scripts
against your YAML for mass refactorings. This requires:

1. An autoformatter that keeps a consistent but human readable style for your YAML documents
2. A round-trip capable YAML parser that you can use to write scripts for mass automated editing
   of your YAML documents

Without (2), you are stuck manually hand-editing your YAML files. And without (1), you will never
have clean diffs, as there may be ancillary stylistic changes caused by the round trippin parser (none
are perfect) when you do automated changes.

This is particularly important if you have a lot of config files for various infrastructure bits
in YAML, and refactoring it may require you to edit many YAML files in an automated fashion. This was
the use case for 2i2c in our [infrastructure](https://github.com/2i2c-org/infrastructure) repository,
where refactoring (say) how we set up home directories required manual edits to a ton of YAML files.

[ruamel.yaml](https://pypi.org/project/ruamel.yaml/) is an excellent round trip parser in python
that satisfies (2). This project uses was built to satisfy (1).

## Using with `pre-commit`

This package is designed to work well with [pre-commit](https://pre-commit.com/). You can put the
following in your `pre-commit

```yaml
repos:
- repo: https://github.com/yuvipanda/ruamelfmt
  rev: 7b4cf00cefbdbd0d1289226b9aa04f5e94fc5409
  hooks:
  - id: ruamelfmt
    # Optionally, exclude any directories that you don't want this to touch
    # exclude: helm-charts/.*|config/clusters/templates/.*
```

Run it once so it reformats all YAML files to its structure, and then you are good to go.