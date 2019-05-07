---
title: Extractions
permalink: /replication/extractions
keywords: extractions, extraction job, replication job, start job, force start, tab
summary: "An integration's Extractions tab provides detail about the extraction portion of the replication process for a the integration. This includes detailed logs and on-demand job controls."

layout: general

content-type: ""
toc: true
weight: 1

sections:
  - content: |
      The first phase of every Stitch replication job is called **Extraction**. During Extraction, Stitch completes the following: 

      1. Check for changes to the structure of your data, including the addition of new tables and columns.
      2. Query for data according to the integration's replication settings. This includes the [tables and fields you set to replicate]({{ link.replication.syncing | prepend: site.baseurl }}) and the [Replication Methods]({{ link.replication.rep-methods | prepend: site.baseurl }}) used by those tables.
      3. Extract the appropriate data, if any.

      The {{ app.tabs.extractions }} tab — accessed by clicking into the integration from the {{ app.page-names.dashboard }} — provides detail about the extraction portion of the replication process for a given integration.

  - title: "Extraction tab availability"
    anchor: "extraction-tab-availability"
    content: |
      The features in the {{ app.tabs.extractions }} tab may not be available for some integrations.

      Generally, these features are available for integrations powered by Singer taps. As integrations are converted to the Singer system, the features listed below will be made available.

      **Note**: Integrations that send data directly and continuously to Stitch will not have these features. This applies to Import API and webhook-based integrations.

  - title: "Extraction tab features"
    anchor: "extraction-tab-features"
    content: |
      The {{ app.tabs.extractions }} tab contains the following features:

      - **Start/stop an extraction** - All integrations run on a [schedule]({{ link.replication.rep-scheduling | prepend: site.baseurl }}) but you can also start and stop extractions on demand. This is useful for testing configuration changes or recovering from an error. Refer to the [Start and stop extraction jobs documentation]({{ link.replication.start-stop-extraction | prepend: site.baseurl }}) for more info.

      - **Extraction logs** - Extraction logs provide detail about the extraction portion of the replication process for an integration. Refer to the [Extraction logs documentation]({{ link.replication.extraction-logs | prepend: site.baseurl }}) for more info.
---
{% include misc/data-files.html %}