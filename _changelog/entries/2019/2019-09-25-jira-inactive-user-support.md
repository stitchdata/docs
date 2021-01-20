---
title: "JIRA (v1) improvement: Added support for inactive users"
content-type: "changelog-entry"
date: 2019-09-25
entry-type: improvement
entry-category: integration
connection-id: jira
connection-version: 1 
---
{{ site.data.changelog.metadata.single-integration | flatify }}

The {{ this-connection.display_name }} integration can now replicate inactive users into the [users]({{ this-connection.url | prepend: site.baseurl | append: "#users" }}) table.

To determine the status of a user, use the `active` field. For example: The following query will only return active users:

{% capture code %}
SELECT *
  FROM jira.users
 WHERE active = TRUE
{% endcapture %}

{% include layout/code-snippet.html code=code language="sql" %}