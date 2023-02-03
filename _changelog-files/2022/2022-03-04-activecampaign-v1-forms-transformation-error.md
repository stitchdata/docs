---
title: "Activecampaign (v1) bug fix: Fixed teh forms stream array error"
content-type: "changelog-entry"
date: 2022-03-04
entry-type: updated-feature
entry-category: integration
connection-id: activecampaign
connection-version: 1
pull-request: "https://github.com/singer-io/tap-activecampaign/pull/22"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've added the `string` type to the `recent` field in the `forms` stream to stop a recurring error.