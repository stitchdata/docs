---
title: "HubSpot integration: New version (v2)"
content-type: "changelog-entry"
date: 2018-05-30
entry-type: new-feature
entry-category: integration
connection-id: hubspot
connection-version: 2
---

{{ site.data.changelog.metadata.single-integration | flatify }}

A new version (v2) of our HubSpot integration is now available! Major changes include:

- Column-level selection 
- More comprehensive data typing on custom properties
- **Inclusion of all form submissions for `contacts`** – Older versions only replicated the newest form submissions. Now you can extract a complete picture of your contact form submissions.
- Improved updates of the `list_memberships` table
- Several schema changes:
	- `hubspot_contacts_by_company` has been renamed to `contacts_by_company`
	- The `isDeleted` fields have been removed from the `deals` and `companies` tables. The HubSpot  API does not provide accurate values for this data, so we've removed it to prevent confusion and potential discrepancies.
	- The `keywords` table has been removed. HubSpot has deprecated the keywords feature of their product and API. Note: [HubSpot has deprecated their Keywords tool](https://www.hubspot.com/product-updates/sunsetting-keywords-in-2018) as of June 1.
	- New counters added to `campaigns`, including: `deferred`, `unsubscribed`, `statuschange`, `bounce`, `mta_dropped`, `suppressed`

Learn more about the integration and these features in the HubSpot documentation for currently supported versions.

**Note**: HubSpot version v2 has been removed.
