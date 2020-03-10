---
title: NetSuite Extraction Error Reference
keywords: troubleshooting, integration, extraction error
layout: general

permalink: /troubleshooting/integrations/netsuite-suitetalk-extraction-error-reference

summary: "Extraction errors for NetSuite integrations and how to resolve them."

level: "guide"
top-level: "replication"
# category: "extraction-errors"
type: "saas-integration, error, replication"

sections:
  - content: |
      These errors will surface in the NetSuite integration's [Extraction Logs]({{ link.replication.extraction-logs | prepend: site.baseurl }}).

      {% assign errors = site.data.errors.extraction.saas.netsuite.all | sort_natural:"message" %}

      {% include troubleshooting/error-messages.html display-name="NetSuite" %}
---
{% include misc/data-files.html %}