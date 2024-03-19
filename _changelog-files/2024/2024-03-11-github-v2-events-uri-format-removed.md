---
title: "GitHub (v2) fix: remove uri format from the events url field"
content-type: "changelog-entry"
date: 2024-03-11
entry-type: bug-fix
entry-category: integration
connection-id: github
connection-version: 2
pull-request: "https://github.com/singer-io/tap-github/pull/205"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've updated our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to fix the following error:

```
INFO Exit status is: Discovery succeeded. Tap failed with code -15. Target failed with code 1 and error message: "Error persisting data to Stitch: 400: {'error': 'Record 0 for table events did not conform to schema:\n#: #: no subschema matched out of the total 2 subschemas\n#/payload}".
```

The URI format restriction for the `events` field has been removed.