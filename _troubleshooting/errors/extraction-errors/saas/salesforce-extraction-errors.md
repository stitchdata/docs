---
title: Salesforce Extraction Error Reference
keywords: troubleshooting, integration, extraction error
layout: general

permalink: /troubleshooting/integrations/salesforce-extraction-error-reference

summary: "Extraction errors for Salesforce integrations and how to resolve them."

key: "salesforce-extraction-error-reference"

level: "guide"
top-level: "replication"
category: "extraction-errors"
integration-type: "saas"

type: "saas-integration, error, replication"

sections:
  - content: |
      The errors in this guide are specific to Salesforce integrations. Refer to the [Common SaaS extraction error reference]({{ link.troubleshooting.saas-extraction-errors | prepend: site.baseurl }}) for errors common to all SaaS integrations.

      These errors will surface in the integration's [Extraction Logs]({{ link.replication.extraction-logs | prepend: site.baseurl }}).

      {% assign errors = site.data.errors.extraction.saas.salesforce.all | sort_natural:"message" %}

      {% include troubleshooting/error-messages.html display-name="Salesforce" %}
---
{% include misc/data-files.html %}