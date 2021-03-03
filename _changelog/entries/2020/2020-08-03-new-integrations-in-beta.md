---
title: New integrations in open beta
content-type: "changelog-entry"
date: 2020-08-03
entry-type: "beta"
entry-category: integration
connections:
  - id: "adroll"
    version: 1
    copy: |
      The new {{ integration.display_name }} integration utilizes the Singer framework which affords several quality of life enhancements such as column and table selection and full Stitch Connect API support.

  - id: "intercom"
    version: 1
    copy: |
      The new Intercom integration also takes advantage of the Singer framework. Additionally, it utilizes version 2 of the {{ integration.display_name }} API to provide additional tables to be extracted and enhanced scaling functionality.

  - id: "zoom"
    version: 1
    copy: |
      The new {{ integration.display_name }} Communications integration now allows the extraction of meeting, webinar and report data.
---

Stitch is pleased to announce the release of three new integrations into open beta and available to all customers:

{% for connection in page.connections %}
{% assign integrations = site.saas-integrations | where:"name",connection.id %}
{% assign integration = integrations | where:"this-version",connection.version | first %}

- [{{ integration.display_name }}]({{ integration.url | prepend: site.baseurl | prepend: site.home }}): {{ connection.copy | flatify }}
{% endfor %}

All three of these integrations are available to all customers in open beta and can be added to your account through the integrations page. 