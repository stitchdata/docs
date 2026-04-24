---
title:  "New feature: Integration changelogs"
content-type: "changelog-entry"
date: 2021-03-24
entry-type: "new-feature"
entry-category: integration, documentation
connections:
  - id: "facebook-ads"
    version: "1"
  - id: "google-analytics"
    version: "1"
  - id: "mongodb"
    version: "2"
  - id: "mysql"
    version: "1"
  - id: "postgres"
    version: "1"
  - id: "salesforce"
    version: "1"
pull-request: "https://github.com/stitchdata/docs/pull/620"
---

Introducing: Integration changelogs!

Check out the history of our integrations and stay in the loop on updates with dedicated changelogs for these integrations:

{% assign all-connection-changelogs = site.saas-integrations | concat: site.database-integrations | where:"content-type","changelog-entry-list" %}

{% for connection in page.connections %}
{% assign connection-changelog = all-connection-changelogs | find:"name",connection.id %}
- [{{ connection-changelog.display_name }}]({{ connection-changelog.url | prepend: site.baseurl }})
{% endfor %}

We'll add changelogs for other popular integrations and destinations in the weeks to come. If there's a specific integration you'd like to see us work on, let us know by creating an issue in the [Stitch Docs GitHub repo]({{ site.github_issues }}){:target="new"}.