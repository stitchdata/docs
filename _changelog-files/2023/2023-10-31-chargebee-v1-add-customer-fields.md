---
title: "Chargebee (v1) update: Add missing customer details"
content-type: "changelog-entry"
date: 2023-10-31
entry-type: improvement
entry-category: integration
connection-id: chargebee
connection-version: 1
pull-request: "https://github.com/singer-io/tap-chargebee/pull/100"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've updated our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to add the `business_entity_id`, `cf_people_id`, and `tax_providers_fields` fields to the `customers` stream.