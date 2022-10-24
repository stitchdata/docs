---
title: "Mambu (v2) update: Time zone endpoint version downgrade"
content-type: "changelog-entry"
date: 2022-10-07
entry-type: improvement
entry-category: integration
connection-id: mambu
connection-version: 2
pull-request: "https://github.com/singer-io/tap-mambu/pull/96"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration by downgrading the version of the API endpoint used to retrieve the client time zone. This was done to remove the extra steps needed to use the more recent version.
