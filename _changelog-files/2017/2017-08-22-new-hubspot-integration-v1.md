---
title: "HubSpot integration: New version (v1)" 
content-type: "changelog-entry"
date: 2017-08-22
entry-type: new-feature
entry-category: integration
connection-id: hubspot
connection-version: 1
---

{{ site.data.changelog.metadata.single-integration | flatify }}

A new (open-sourced!) version (v1) of our HubSpot integration is now available!

Major improvements include:

- [Table selection]({{ site.data.urls.replication.syncing | prepend: site.baseurl | prepend: site.home }})
- Improved data typing
- Improved Primary Keys
- New tables:
  - `hubspot_contacts_by_company`
  - `engagements`

Open sourcing our integrations means more transparency into and flexibility around integration features. If you'd like to contribute to the HubSpot integration, you can check out the source repository.

Learn more about the integration and these features in the HubSpot documentation for currently supported versions.

**Note**: HubSpot version v1 has been removed.
