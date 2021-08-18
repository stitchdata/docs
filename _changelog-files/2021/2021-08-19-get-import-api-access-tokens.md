---
title: "Updated feature: Response for Import API access tokens"
content-type: "changelog-entry"
date: 2021-08-19
entry-type: "updated-feature"
entry-category: "connect-api"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've updated the response in the Stitch Connect API when retrieving access token IDs.

The timestamp from when the Import API access token ID was retrieved will now be included in the `GET /v4/sources/{source_id}/tokens` response. Check our docs to [learn more]({{ link.connect.guides.manage-import-api-access-tokens | prepend: site.baseurl | append: "#rotate--get-iapi-access-token-id" }}).

