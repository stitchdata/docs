---
title: "Salesforce (v15-10-2015) integrations: Field selection support"
content-type: "changelog-entry"
date: 2016-10-07
entry-type: new-feature
entry-category: replication
connection-id: salesforce
connection-version: "15-10-2015"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

Do objects in your {{ this-connection.display_name }} have a lot of fields? Do you only care about a few of them? Don't you wish you could only track what you want?

Well, now you can! Starting today, you can select which fields to replicate from your {{ this-connection.display_name }} objects, giving you more control to keep your destination clean and simple. Learn more in the [docs]({{ site.data.urls.replication.syncing | prepend: site.baseurl | prepend: site.home }}).