---
title: "PostgreSQL (v1) destinations: SSL certificate verification support" 
content-type: "changelog-entry"
date: 2018-11-12
entry-type: new-feature
entry-category: destination
connection-id: postgres
connection-version: 1
---

{{ site.data.changelog.metadata.single-destination | flatify }}

Users can now provide a certificate for their {{ this-connection.display_name }} destination that will be used to verify the identity of their server.