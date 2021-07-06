---
title: "[INTEGRATION] (v) deprecation"
#content-type: "changelog-entry"
date: 2016-01-01
entry-type: deprecation
entry-category: "integration"
connection-id: ""
connection-version: ""
# pull-request: "" UNCOMMENT IF THERE'S A PR
---

{{ site.data.changelog.metadata.single-integration | flatify }}

The v{{ this-connection.this-version }} version of our {{ this-connection.display_name }} integration has been deprecated. As of today, this version of the {{ this-connection.display_name }} integration is no longer formally supported.

While connections using v{{ this-connection.this-version }} will continue to run, this version will be sunset in the future. Migrate to the latest version of {{ this-connection.display_name }} (v) today to prevent possible disruptions.