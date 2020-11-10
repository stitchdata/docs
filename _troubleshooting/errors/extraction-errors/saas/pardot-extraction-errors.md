---
# -------------------------- #
#      Page & Formatting     #
# -------------------------- #

title: Pardot Extraction Error Reference
keywords: troubleshooting, integration, extraction error
layout: general

permalink: /troubleshooting/integrations/pardot-extraction-error-reference

summary: "Extraction errors for Pardot integrations and how to resolve them."

level: "guide"
top-level: "replication"
category: "extraction-errors"
integration-type: "saas"

type: "saas-integration, error, replication"


# -------------------------- #
#           Content          #
# -------------------------- #

sections:
  - content: |
      The errors in this guide are specific to Pardot integrations. Refer to the [Common SaaS extraction error reference]({{ link.troubleshooting.saas-extraction-errors | prepend: site.baseurl }}) for errors common to all SaaS integrations.

      These errors will surface in the integration's [Extraction Logs]({{ link.replication.extraction-logs | prepend: site.baseurl }}).

      {% assign errors = site.data.errors.extraction.saas.pardot.all | sort_natural:"message" %}

      {% include troubleshooting/error-messages.html display-name="Pardot" %}
---
{% include misc/data-files.html %}