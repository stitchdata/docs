---
title: "Salesforce (v1) integrations: Location data types unsupported for Bulk API"
content-type: "changelog-entry"
date: 2020-03-30
entry-type: removed
entry-category: integration
connection-id: "salesforce"
connection-version: "1"
pull-request: "https://github.com/singer-io/tap-salesforce/pull/75"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've determined that the `locations` fields aren't supported by the {{ this-connection.display_name }} Bulk API. If selected, the following erorr will surface during Extraction:

```shell
[FIELD_NAME] cannot query compound address fields or geolocations with bulk API
```

Refer to the [tap repository](https://github.com/singer-io/tap-salesforce/blob/master/Blacklisting.md){:target="new"} for more info.