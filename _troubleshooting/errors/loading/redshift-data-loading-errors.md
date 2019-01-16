---
title: Redshift Data Loading Errors
keywords: troubleshooting, destination, trouble, issue, help, error, errors, redshift, panoply
permalink: /troubleshooting/errors/data-loading/redshift-panoply
redirect_from: /troubleshooting/destinations/redshift-data-loading-errors
layout: general
tags: [troubleshooting_destinations, troubleshooting_errors]

summary: "Received an error about Stitch loading data into your Redshift data warehouse? Check out these common errors and how to resolve them."
type: "redshift-destination, error, replication"


sections:
  - content: |
      blah

  - title: "Using this guide"
    anchor: "using-this-guide"
    content: |
      In the next section is a list of the connection errors that might arise for destinations in Stitch. Every error in this list will have the following info:

      {% include troubleshooting/error-messages.html content-type="error-fields" %}

  - title: "Error list"
    anchor: "error-list"
    content: |
      {% assign destination-type = "redshift" %}
      {% assign destination-name = "Redshift and Panoply" %}

      {% assign common-errors = site.data.errors.data-loading.common.all %}
      {% assign errors = site.data.errors.data-loading.redshift.all | sort: "message" %}

      {% include troubleshooting/error-messages.html content-type="error-list" %}

  - title: "Contacting support"
    anchor: "contact-support"
    content: |
      To help us troubleshoot the problem quickly, we ask that you provide us with the following:

      1. **The exact error you received.** The full text or a screenshot is ideal.
      2. **The type of destination experiencing the issue.** For example: Redshift, PostgreSQL-RDS.
      3. **The type of integration associated with the loading error,** if applicable.

    subsections:
      - title: "Don't see the error here?"
        anchor: "missing-error"
        content: |
          If the error you received isn't listed here, contact support and then [let us know through a GitHub issue]({{ site.github_issue }}{:target="new"}.
---
{% include misc/data-files.html %}

{% assign destination-type = "redshift" %}
{% assign destination-name = "Redshift and Panoply" %}






## Contacting Support

If you still encounter trouble after following the troubleshooting steps above, please reach out to support for assistance.