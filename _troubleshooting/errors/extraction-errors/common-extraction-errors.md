---
title: Common Extraction Error Reference
keywords: troubleshooting, integration, database integration, extraction error, common errors, 6 hour limit, table limit
tags: [database_integrations, saas_integrations, troubleshooting_integrations, troubleshooting_errors]
layout: general

permalink: /troubleshooting/integrations/common-extraction-errors

summary: "Extraction errors common to all integrations, and how to resolve them."

level: "guide"
top-level: "replication"
# category: "extraction-errors"
type: "integration, error"
popular: true

intro: |
 During extraction, errors may be surfaced in the integration's [Extraction Logs]({{ link.replication.extraction-logs | prepend: site.baseurl }}) when Stitch encounters an issue.

 **Note**: All errors listed in this guide are `CRITICAL`-level errors. This means that {{ stitch.notifications.common.levels.critical.description | flatify | replace: "Data","data" }} 

sections:
  - title: "Applicable integrations"
    anchor: "applicable-integrations"
    content: |
      The errors listed below apply to any integration that supports Extraction Logs.

      Refer to the [Integration-specific error references section](#integration-specific-references) for a list of integration-specifc extraction error references.

  - title: "Common error reference"
    anchor: "error-reference"
    content: |
      {% assign errors = site.data.errors.extraction.common.all %}

      Below are the errors you might see if Stitch encounters an issue during Extraction:

      {% include troubleshooting/error-messages.html %}

  - title: "Integration-specific error references"
    anchor: "integration-specific-references"
    content: |
      Refer to the reference for your integration for extraction errors specific to the integration:

      {% assign extraction-error-references = site.troubleshooting | where:"category","extraction-errors" | sort: integration-display-name %}

      {% for reference in extraction-error-references %}
      {% if reference.url != page.url %}
      - [{{ reference.integration-display-name }}]({{ reference.url | prepend: site.baseurl }})
      {% endif %}
      {% endfor %}
---
{% include misc/data-files.html %}