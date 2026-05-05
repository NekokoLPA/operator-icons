# OperatorIcons

Offline operator icon catalog for NekokoLPA.

## Layout

- `catalog/<mcc>.toml` contains operator metadata grouped by MCC.
- `icons/<mcc>/<name>.png` contains single-country icons.
- `icons/worldwide/<name>.png` contains icon files reused by operators in multiple MCCs.

Catalog entries reference icons by `icon` name plus `icon_scope`. A consumer can resolve
`icon_scope = "202"` as `icons/202/<icon>.png`, and `icon_scope = "worldwide"` as
`icons/worldwide/<icon>.png`.
