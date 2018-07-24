---
title: Connecting an Existing Panoply Data Warehouse to Stitch
permalink: /destinations/panoply/connecting-an-existing-panoply-data-warehouse-to-stitch
tags: [panoply_destination]
keywords: panoply, panoply.io, panoply data warehouse, panoply.io data warehouse etl to redshift, redshift etl, panoply etl
summary: "Connect your existing Panoply destination to Stitch."
toc: true
layout: destination-setup-guide
display_name: "Panoply"
type: "panoply"


# -------------------------- #
#      Setup Requirements    #
# -------------------------- #

requirements-list:
  - item: "**Admin permissions in Panoply.**"

# -------------------------- #
#     Setup Instructions     #
# -------------------------- #

setup-steps:
  - title: "Locate the Connection Details in Panoply"
    anchor: "locate-connection-info"
    content: |
      1. Sign into your Panoply account.
      2. In the left panel menu, click **Connect**.
      3. The database connection info - the **host, port, database name**, and **username** - will display.

      Leave this page open - you’ll need it in the next step.

  - title: "connect stitch"

---
{% include misc/data-files.html %}
{% assign destination = site.destinations | where:"type",page.type | first %}

{{ destination.description }}

{% capture account-management %}
Stitch is in no way involved with the management of Panoply data warehouses. If you have billing questions or need help regarding your Panoply data warehouse, [reach out to Panoply]({{ destination.main-site }}){:target="new"}.
{% endcapture %}

{% include note.html first-line="**Panoply account management**" content=account-management %}