---
title: Common SaaS Integration Extraction Error Reference
keywords: troubleshooting, integration, saas integration, extraction error, common errors, 6 hour limit, table limit
layout: general

permalink: /troubleshooting/integrations/common-saas-extraction-error-reference

summary: "Extraction errors applicable to all SaaS integrations and how to resolve them."

level: "guide"
top-level: "replication"
category: "extraction-errors"
integration-type: "saas"

type: "saas-integration, error, replication"
popular: true

intro: |
  When Stitch replicates data from a SaaS integration, it will check for the required user permissions and account configuration. If permisisons are insufficient or the source isn't configured correctly, you may receive an error during the Extraction phase of the replication process. These errors will surface in the integration's [Extraction Logs]({{ link.replication.extraction-logs | prepend: site.baseurl }}).

  **Note**: The errors in this reference are applicable to all SaaS integrations that support Extraction Logs. For integration-specific errors, refer to the [reference for that integration](#integration-specific-error-references).

  {% for section in page.sections %}
  - [{{ section.title | flatify }}](#{{ section.anchor }})
  {% endfor %}

sections:
  - title: "Common extraction errors"
    anchor: "common-extraction-errors"
    content: |
      {% assign errors = site.data.errors.extraction.common.saas | sort_natural:"message" %}

      {% include troubleshooting/error-messages.html %}

  - title: "Integration-specific error references"
    anchor: "integration-specific-error-references"
    content: |
      {% capture notice %}
      **Looking for database integrations?** Refer to the [Database Extraction Error Reference]({{ link.troubleshooting.database-extraction-errors | prepend: site.baseurl }}).
      {% endcapture %}

      {% include note.html type="single-line" content=notice %}

      {% assign all-extraction-errors = site.troubleshooting | where:"category","extraction-errors" %}
      {% assign saas-extraction-error-references = all-extraction-errors | where:"integration-type","saas" | sort_natural:"title" %}

      {% for reference in saas-extraction-error-references %}
      {% if reference.title != page.title %}
      - [{{ reference.title | remove: " Extraction Error Reference" }}]({{ reference.url | prepend: site.baseurl }})
      {% endif %}
      {% endfor %}
---
{% include misc/data-files.html %}