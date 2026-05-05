# Operator Icons

Offline mobile operator icon catalog for NekokoLPA.

## Layout

- `catalog/<mcc>.toml` contains operator metadata grouped by MCC.
- `icons/<mcc>/<name>.png` contains single-country icons.
- `icons/worldwide/<name>.png` contains icon files reused by operators in multiple MCCs.

Catalog entries reference icons by `icon` name plus `icon_scope`. A consumer can resolve
`icon_scope = "202"` as `icons/202/<icon>.png`, and `icon_scope = "worldwide"` as
`icons/worldwide/<icon>.png`.

## Catalog Format

Each catalog file starts with country-level metadata, followed by one or more
`[[operators]]` entries. Operators can also contain nested `[[operators.gids]]`
entries when a profile is identified by GID1/GID2.

```toml
mcc = "202"
country = "Greece"
iso = "GR"
region = "Europe"

[[operators]]
mnc = "05"
plmn = "20205"
operator = "Vodafone Greece"
brand = "Vodafone"
icon = "vodafone"
icon_scope = "worldwide"

[[operators.gids]]
gid1 = ""
gid2 = ""
profile_provider_names = ["Vodafone GR"]
profile_names = ["Vodafone GR"]
```

Icon references are filename stems, not paths. For example, the entry above
resolves to `icons/worldwide/vodafone.png`.

## Icon Rules

Pull requests validate the icon set with GitHub Actions. Every file under
`icons/` must be:

- PNG format
- square
- at least `256x256`
- no larger than `1024x1024`

The same check also parses every TOML catalog and verifies that each
`icon`/`icon_scope` pair points to an existing PNG file.

## Branch

The default branch is `master`.
