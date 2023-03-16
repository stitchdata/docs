---
title: "Pipedrive (v1) integration: Removed goals table "
content-type: "changelog-entry"
date: 2018-11-09
entry-type: removed
entry-category: integration
connection-id: pipedrive
connection-version: 1
---
{{ site.data.changelog.metadata.single-integration | flatify }}

As per an update to the [{{ this-connection.display_name }} API](https://developers.pipedrive.com/docs/api/v1/#/){:target="new"}, the `goals` table has been removed from the Stitch integration. See more about the available {{ this-connection.display_name }} data in [our documentation]({{ this-connection.url | prepend: site.baseurl | prepend: site.home }}).