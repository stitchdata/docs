---
title: Stitch SaaS Integrations
keywords: saas integration, etl saas integration, saas integration etl, app etl, cloud app etl
layout: general
summary: "Resources & guides for connecting your SaaS apps and services to Stitch. Setup instructions, replication info, and schema details for each of Stitch's SaaS integrations."
permalink: /integrations/saas/

toc: false
input: false
feedback: false

sections:
  - content: |
      With Stitch, you can consolidate data from a variety of SaaS apps and services into a [single destination]({{ site.baseurl }}/destinations).
  - title: "Destination and integration compatibility"
    anchor: "destination-integration-compatibility"
    content: |
      Some integrations may be partially or fully incompatible with some of the destinations offered by Stitch. For example: some destinations don’t support storing multiple data types in the same column. If a SaaS integration sends over a column with mixed data types, [some destinations may reject the data]({{ link.destinations.storage.rejected-records | prepend: site.baseurl }}).

      To see if the integrations you're using are compatible with your destination, check out the [Destination and Integration Compatibility Guide]({{ link.destinations.overviews.compatibility | prepend: site.baseurl }}).

  - title: "All SaaS integrations"
    anchor: "all-saas-integrations"
    content: |
      Stitch classifies integrations as either **Certified** or **Community**:

      - [**Certified Integrations**](#certified-saas-integrations) - {{ site.data.tooltips.certified-integration }}
      - [**Community Integrations**](#community-saas-integrations) - {{ site.data.tooltips.community-integration }}

      If you don't see what you're looking for in the list below, check out the Singer project. A simple, composable, open-source ETL standard, Singer allows you to extract data from any source. Check out the [Roadmap]({{ site.singer-roadmap }}){:target} or [GitHub repo]({{ site.singer-github }}){:target="new"} to see what's currently being worked on.

      Additionally, Stitch's Import API or Incoming Webhooks integrations can be used to extract data from sources that don't currently have a native integration.

      {% include integrations/templates/integration-category-tiles.html type="where-is-integration" which-integrations="all" %}
    subsections:
      - title: "Certified integrations"
        anchor: "certified-saas-integrations"
        content: |
          The following integrations are **Stitch Certified** and officially supported by the Stitch team. {{ site.data.tooltips.certified-integration }}

          {% include integrations/templates/integration-category-tiles.html type="saas" which-integrations="certified" %}

          ---

      - title: "Community integrations"
        anchor: "community-saas-integrations"
        content: |
          The following integrations are **Community Supported** and are maintained by the [Singer community]({{ site.singer }}){:target="new"}. {{ site.data.tooltips.community-integration }}

          For support, visit the integration's GitHub repo (linked below) or [join the Singer Slack]({{ site.singer-slack }}){:target="new"}.

          **Note**: Commercial Stitch support contracts are available for all Community integrations. For more info, contact the [Stitch Sales team]({{ site.sales }}){:target="new"}.

          {% include integrations/templates/integration-category-tiles.html type="saas" which-integrations="community" %}

  - title: "Suggest an integration"
    anchor: "suggest-an-integration"
    content: |
      Don’t see your integration of choice listed here? We’d love to hear from you! [Reach out to us](mailto:{{ site.support }}) with your suggestion.

---
{% include misc/data-files.html %}
