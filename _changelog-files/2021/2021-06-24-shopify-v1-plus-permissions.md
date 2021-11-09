---
title: "Shopify (v1) update: Updated setup requirements for Shopify Plus plans"
content-type: "changelog-entry"
date: 2021-06-24
entry-type: updated-feature
entry-category: "integration, documentation"
connection-id: "shopify"
connection-version: "1"
pull-request: "https://github.com/stitchdata/docs/pull/644"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've updated our [{{ this-connection.display_name }} documentation]({{ this-connection.url | prepend: site.baseurl | prepend: site.home }}#setup-requirements) to include info about the required permissions for users on {{ this-connection.display_name }} Plus plans.

In general, **view-level** permissions should be sufficient to allow Stitch to replciate data. We recommend checking out [{{ this-connection.display_name }}'s Staff Permissions documentation](https://help.shopify.com/en/manual/your-account/staff-accounts/staff-permissions#store-owner-permissions){:target="new"} for details on the permissions available in{{ this-connection.display_name }}.