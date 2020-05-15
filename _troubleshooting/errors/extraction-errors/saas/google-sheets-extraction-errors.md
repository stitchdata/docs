---
title: Google Sheets Extraction Error Reference
keywords: troubleshooting, integration, extraction error
layout: general

permalink: /troubleshooting/integrations/google-sheets-extraction-error-reference

summary: "Extraction errors for Google Sheets integrations and how to resolve them."

level: "guide"
top-level: "replication"
# category: "extraction-errors"
type: "saas-integration, error, replication"

sections:
  - content: |
      These errors will surface in the Google Sheets integration's [Extraction Logs]({{ link.replication.extraction-logs | prepend: site.baseurl }}).

      {% assign errors = site.data.errors.extraction.saas.google-sheets.all | sort_natural:"message" %}

      {% include troubleshooting/error-messages.html display-name="Google Sheets" %}
---
{% include misc/data-files.html %}