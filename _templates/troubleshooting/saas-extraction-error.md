---
title: [INTEGRATION-NAME] Extraction Error Reference
keywords: troubleshooting, integration, extraction error
layout: general

permalink: /troubleshooting/integrations/[integration-name]-extraction-error-reference

summary: "Extraction errors for [INTEGRATION-NAME] integrations and how to resolve them."

level: "guide"
top-level: "replication"
# category: "extraction-errors"
type: "saas-integration, error, replication"

intro: |
  These errors will surface in the [INTEGRATION-NAME] integration's [Extraction Logs]({{ link.replication.extraction-logs | prepend: site.baseurl }}).

sections:
  - content: |
      {% assign errors = site.data.errors.extraction.saas.[integration-name] | sort_natural:"message" %}

      {% include troubleshooting/error-messages.html display-name="INTEGRATION-NAME" %}
---
{% include misc/data-files.html %}