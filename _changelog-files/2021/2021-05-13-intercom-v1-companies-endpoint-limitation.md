---
title: "Intercom (v1): Identified issue with companies endpoint"
content-type: "changelog-entry"
date: 2021-05-13
entry-type: bug-fix
entry-category: "integration, documentation"
connection-id: "intercom"
connection-version: "1"
pull-request: ""
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've identified an issue replicating data for the `companies` table in {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integrations due to a limit in {{ this-connection.display_name }}'s API.

Currently, [{{ this-connection.display_name }}'s API allows an {{ this-connection.display_name }} app to make one request to the **Scroll over all companies** endpoint](https://developers.intercom.com/intercom-api-reference/v2.0/reference#iterating-over-all-companies){:target="new"} at a time. Stitch uses this endpoint to replicate the `companies` table. 

If multiple connections exist and they attempt to use this endpoint at the same time, only the connection who made the request first will succeed.

This means that if Stitch attempts to extract data when another connection is using the endpoint, Extraction will fail and an error will surface in the Extraction Logs.

{% assign intercom-extraction-errors = site.troubleshooting | find:"key","intercom-extraction-error-reference" %}

We've updated the [{{ this-connection.display_name }} documentation]({{ site.home | append: site.baseurl | append: this-connection.url }}) to include this info and how to mitigate it. Additionally, we've created a new [resource for troubleshooting {{ this-connection.display_name }} Extraction errors]({{ site.home | append: site.baseurl | append: intercom-extraction-errors.url }}).