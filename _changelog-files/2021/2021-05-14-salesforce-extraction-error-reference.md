---
title: "New extraction error reference for Salesforce"
content-type: "changelog-entry"
date: 2021-05-14
entry-type: new-feature
entry-category: "integration, documentation"
connection-id: "salesforce"
connection-version: "1"
pull-request: "https://github.com/stitchdata/docs/pull/642"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

{% assign sf-extraction-error-reference = site.troubleshooting | find:"key","salesforce-extraction-error-reference" %}

We've added [a new resource for troubleshooting Extraction errors]({{ site.home | append: site.baseurl | append: sf-extraction-error-reference.url }}) in {{ this-connection.display_name }} integrations. If Stitch receives an error during Extraction, you can use this reference to locate the error, pinpoint the cause, and identify next steps for resolution.