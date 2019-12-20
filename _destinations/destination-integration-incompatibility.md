---
title: Destination & Integration Compatibility
keywords: destinations, integrations, incompatible, mixed data types, multiple data types, compatibility, compatible
permalink: /destinations/destination-integration-compatibility
summary: "Verify your integrations' compatibility with your data warehouse."

destination: false
content-type: "destination-general"
type: "all"
key: "source-destination-compatibility"

toc: true
layout: general


intro: |
  When selecting a destination, it's important to first verify that all the data sources you want to connect to Stitch will be compatible. 

  **As Stitch currently allows only one destination per account,** we recommend verifying your integrations' compatibility before connecting a destination. This will ensure that you can successfully connect and replicate data from all your sources.

sections:
  - title: "Degrees of incompatibility"
    anchor: "degrees-of-incompatibility"
    content: |
      {% include misc/icons.html %}
      The compatibility of any integration/destination combination falls into one of three categories: **always** compatible, **sometimes** compatible, and **never** compatible.

      The matrices below use the following icons to indicate the degree of incompatibility for an integration/destination combo:

      - {{ sometimes-supported | replace:"TOOLTIP","" }} indicates that this combo is **sometimes** compatible - there may be compatibility issues, but they're infrequent or parts of the integration may still be usable.
      - {{ not-supported | replace:"TOOLTIP","" }} indicates that this combo is **never** compatible. It's unlikely that Stitch will be able to load data from this integration into the given destination.

  - title: "Incompatible integrations by destination type"
    anchor: "incompatible-integrations-by-destination-type"
    content: |
      Below you'll find a list of integrations that may have full or partial incompatibility with any of Stitch's destination offerings.

      Refer to the [Destination data loading guides]({{ link.destinations.storage.loading-data | prepend: site.baseurl }}) for a comprehensive look at how destinations will load data, including what may cause data to be rejected.

      {% include shared/incompatibilities/all-destination-incompatibility.html %}
---
{% include misc/data-files.html %}