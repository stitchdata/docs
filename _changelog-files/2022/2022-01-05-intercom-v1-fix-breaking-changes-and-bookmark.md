---
title: "Intercom (v1) bug fixes: Fixed breaking changes"
content-type: "changelog-entry"
date: 2022-01-05
entry-type: bug-fix
entry-category: integration
connection-id: intercom
connection-version: 1
pull-request: "https://github.com/singer-io/tap-intercom/pull/45"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've fixed the following issues in our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration:
- The `epoch_milliseconds_to_dt_str()` function was updated to convert epoch to UTC time.
- The `time_extracted` element was added back to the `write_record` function.
- The bookmark for the `conversation_parts` stream will be updated with the parent `conversation`'s replication key after the collection of child records.