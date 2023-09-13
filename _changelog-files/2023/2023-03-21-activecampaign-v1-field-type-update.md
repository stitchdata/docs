---
title: "ActiveCampaign (v1): Field type update"
content-type: "changelog-entry"
date: 2023-03-21
entry-type: updated-feature
entry-category: integration
connection-id: activecampaign
connection-version: 1
pull-request: "https://github.com/singer-io/tap-activecampaign/pull/28"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've updated our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to support the `string` type for the `style.button.padding` field in the `forms` stream.