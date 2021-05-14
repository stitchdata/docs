---
title: Intercom Extraction Error Reference
keywords: troubleshooting, integration, extraction error
layout: general

permalink: /troubleshooting/integrations/intercom-extraction-error-reference

summary: "Extraction errors for Intercom integrations and how to resolve them."

key: "intercom-extraction-error-reference"

level: "guide"
top-level: "replication"
category: "extraction-errors"
integration-type: "saas"

type: "saas-integration, error, replication"

sections:
  - content: |
      The errors in this guide are specific to Intercom integrations. Refer to the [Common SaaS extraction error reference]({{ link.troubleshooting.saas-extraction-errors | prepend: site.baseurl }}) for errors common to all SaaS integrations.

      These errors will surface in the integration's [Extraction Logs]({{ link.replication.extraction-logs | prepend: site.baseurl }}).

      {% assign errors = site.data.errors.extraction.saas.intercom.all | sort_natural:"message" %}

      {% include troubleshooting/error-messages.html display-name="Intercom" %}
---
{% include misc/data-files.html %}