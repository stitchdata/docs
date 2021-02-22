---
title: "Google AdWords (v1) integrations: API upgrade to v2.11"
content-type: "changelog-entry"
date: 2018-03-14
entry-type: updated-feature
entry-category: integration
connection-id: google-adwords
connection-version: 1
---

{{ site.data.changelog.metadata.single-integration | flatify }}

We’ve updated our Google AdWords integration to use the newest Adwords API - [version v201802](https://developers.google.com/adwords/api/docs/reference/release-notes/v201802){:target="new"}.

Additionally, we've made the following chanegs:

- In the `ads` table, the `policyTopicEvidences` object in the `policySummary.policyTopicEntries` field contains an `evidenceText` field.  This field (`evidenceText`) has been renamed to `evidenceTextList` and is now a list.

- In the `ad_performance_report` table, the `ImageAdUrl` field now returns the entire URL string

- In various reports:
	- The `BidType` field has been removed
  - The `EnhancedCpvEnabled` field has been removed from all reports. This field was used for experiments that are no longer active.

See the [AdWords API release notes](https://developers.google.com/adwords/api/docs/reference/release-notes/v201802){:target="new"} for additional details.