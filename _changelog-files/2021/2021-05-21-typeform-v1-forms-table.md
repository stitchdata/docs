---
title: "Typeform (v1) update: New forms table!"
content-type: "changelog-entry"
date: 2021-05-21
entry-type: improvement
entry-category: integration
connection-id: typeform
connection-version: 1
pull-request: "https://github.com/singer-io/tap-typeform/pull/29"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've added a new table to our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration!

The new `forms` table contains info about the forms accesible to the user who authorized the {{ this-connection.display_name }} integration in Stitch.

Learn more in [our documentation]({{ this-connection.url | prepend: site.baseurl | prepend: site.home | append: "#forms" }}).