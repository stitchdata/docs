---
# -------------------------- #
#          PAGE INFO         #
# -------------------------- #

title: Extraction Tab Features
permalink: /replication/extractions/extraction-tab-features
keywords: extractions, extraction job, replication job, start job, force start, tab
summary: "An integration's Extractions tab provides detail about the extraction portion of the replication process for a the integration. This includes detailed logs and on-demand job controls."

key: "extractions-tab"
category: "extraction"
content-type: "basics"

layout: general
toc: true
weight: 1


# -------------------------- #
#           INTRO            #
# -------------------------- #

intro: |
  The {{ app.tabs.extractions }} tab — accessed by clicking into the integration from the {{ app.page-names.dashboard }} — provides detail about the Extraction portion of the replication process for a given integration.

  In this guide, we'll cover:

  {% for section in page.sections %}
  - [{{ section.summary }}](#{{ section.anchor }})
  {% endfor %}


# -------------------------- #
#          CONTENT           #
# -------------------------- #

sections:
  - title: "Extraction tab availability"
    anchor: "extraction-tab-availability"
    summary: "Availability of the Extraction tab"
    content: |
      The features in the {{ app.tabs.extractions }} tab may not be available for some integrations.

      Generally, these features are available for integrations powered by Singer taps. As integrations are converted to the Singer system, the features listed below will be made available.

      **Note**: Integrations that send data directly and continuously to Stitch will not have these features. This applies to Import API and webhook-based integrations.

  - title: "Extraction tab features"
    anchor: "extraction-tab-features"
    summary: "The features in the Extraction tab"
    content: |
      The {{ app.tabs.extractions }} tab contains the following features:

      {% for subsection in section.subsections %}
      - [{{ subsection.title }}](#{{ subsection.anchor }})
      {% endfor %}

    subsections:
      - title: "On-demand extraction"
        anchor: "features--starting-stopping-extractions"
        content: |
          All integrations run on a [schedule]({{ link.replication.rep-scheduling | prepend: site.baseurl }}) but you can also start and stop extractions on demand. This is useful for testing configuration changes or recovering from an error. Refer to the [Start and stop extraction jobs documentation]({{ link.replication.start-stop-extraction | prepend: site.baseurl }}) for more info.

      - title: "Extraction logs"
        anchor: "features--extraction-logs"
        content: |
          Extraction logs provide detail about the extraction portion of the replication process for an integration. Refer to the [Extraction logs documentation]({{ link.replication.extraction-logs | prepend: site.baseurl }}) for more info.
---
{% include misc/data-files.html %}