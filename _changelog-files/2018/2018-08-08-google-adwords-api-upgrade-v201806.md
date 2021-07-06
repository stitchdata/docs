---
title: "Google AdWords (v1) integrations: API upgrade to v201806"
content-type: "changelog-entry"
date: 2018-08-08
entry-type: updated-feature
entry-category: integration
connection-id: google-ads
connection-version: 1
---

{{ site.data.changelog.metadata.single-integration | flatify }}

The Google AdWords integration has been updated to use v201806 of the AdWords API, from v201802.

Notable changes include:

- **Ad Groups**: The `AdGroupType` enum value `SHOPPING_UNIVERSAL_ADS` was renamed to `SHOPPING_GOAL_OPTIMIZED_ADS`.

- **Ad Group Performance Report**: The `AdGroupType` field will now return a value of `“Shopping - Goal-optimized”` where it previously returned `“Shopping - Universal”`, and the corresponding enum value changed from `SHOPPING_UNIVERSAL_ADS` to `SHOPPING_GOAL_OPTIMIZED_ADS`.