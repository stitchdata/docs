---
title: Connecting a DESTINATION-NAME Data Warehouse to Stitch
permalink: /destinations/destination-type/connecting-destination-type-to-stitch
tags: [destination-type_destination]
keywords: destination-type, destination-type data warehouse, destination-type data warehouse, destination-type etl, etl to destination-type, destination-type destination
summary: "Connect a DESTINATION-NAME destination to your Stitch account."
toc: true
type: "destination-type"
---
{% include misc/data-files.html %}
{% assign destination = site.destinations | where:"type","destination-type" | first %}

{{ destination.description }}



---

## Prerequisites

--- 

## Step X: Connect Stitch

{% include destinations/setup/destination-settings.html heading="[ENTER IF NEEDED]" ssh=true %}

- Include `ssh=true` in the include if the instructions are for connecting via SSH tunnel. Otherwise, remove