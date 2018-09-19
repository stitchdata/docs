---
title: Connecting an Amazon Redshift Data Warehouse to Stitch
permalink: /destinations/redshift/connecting-redshift-data-warehouse-to-stitch
tags: [redshift_destination]
keywords: redshift, amazon redshift, redshift data warehouse, etl to redshift, redshift etl, create redshift user, stitch redshift user, stitch user

summary: "Ready to spin up a Redshift data warehouse and connect it to Stitch? This step-by-step tutorial will walk you through every part of the process."
toc: true
layout: destination-setup-guide
type: "redshift"

# -------------------------- #
#      Setup Requirements    #
# -------------------------- #

requirements-list:
  - item: |
      **An Amazon Web Services (AWS) account.** Signing up is free - [click here](https://aws.amazon.com){:target="new"} or go to `https://aws.amazon.com` to create an account if you don't have one already.
  - item: "**Some technical know-how and familiarity with AWS.**"
  - item: |
      **Optional: Create a non-default VPC**. {% include destinations/redshift/create-a-vpc.html %}

# -------------------------- #
#     Setup Instructions     #
# -------------------------- #

setup-steps:
  - title: "Create Cluster Login Credentials"
    anchor: "create-cluster-login-credentials"
    content: |
      {% include destinations/redshift/create-cluster-login-credentials.html %}

  - title: "Select Nodes & Cluster Types"
    anchor: "select-nodes--cluster-types"
    content: |
      {% include destinations/redshift/select-nodes-cluster-types.html %} 

  - title: "Configure & Launch the {{ destination.display_name }} Cluster"
    anchor: "configure-launch-cluster"
    content: |
      Next, you'll define the additional configuration settings for the Redshift cluster. For our purposes, we're going to leave most of the settings as-is and focus on the **Configure Networking Options** and **Security Groups** sections.
    substeps:
      - title: "Configure Networking Options"
        anchor: "configure-cluster-networking-options"
        content: |
          {% include destinations/redshift/configure-cluster--networking-options.html %}

      - title: "Define a Security Group"
        anchor: "define-cluster-security-group"
        content: |
          {% include destinations/redshift/configure-cluster--define-security-group.html %}

      - title: "Review & Launch the Redshift Cluster"
        anchor: "review-launch-cluster"
        content: |
          {% include destinations/redshift/configure-cluster--review-launch.html %}


  - title: "Configure Security & Access Settings"
    anchor: "configure-security-access-settings"
    content: |
      When the cluster creation process is complete, you can move onto editing the cluster security group's access rules.

      To ensure that Stitch can access your Redshift instance and load data into your data warehouse, you'll create a Security Group Connection Rule for the security group associated with the cluster. This will whitelist the IP addresses Stitch uses and ensure we can access your Redshift.

      1. On the **Redshift Dashboard page**, click the **Clusters** option in the left nav bar.
      2. In the Clusters page, locate and click on the cluster you just created. This will display the **Cluster Details** page.
      3. Locate the **Cluster Properties** section.
      4. Click the name of the security group in the **VPC Security Groups** field.
      5. This will open the **Security Groups** page.
      {% include shared/aws-whitelisting.html %}

  - title: "create db user"
    content: |
      {% include destinations/setup/postgresql-create-user-intro.html %}

      {% include destinations/setup/redshift-postgres-permissions.html %}

      ### Create the Database User {#create-the-user}

      {% include destinations/setup/redshift-postgres-database-users.html %}

  - title: "connect stitch"
    content: |
      To complete the setup, you need to enter your {{ destination.display_name }} connection details into the {{ app.page-names.dw-settings }} page in Stitch.

    substeps:
      - title: "Locate the {{ destination.display_name }} Connection Details"
        anchor: "locate-connection-details-aws"
        content: |
          {% include shared/aws-connection-details.html %}

---
{% include misc/data-files.html %}
{% assign destination = site.destinations | where:"type",page.type | first %}

{% capture setup-notice %}
This tutorial describes how to spin up a Redshift cluster and connect it to Stitch via a **direct connection**.

By default, Stitch will attempt to connect to Redshift using SSL, but SSH connections are also supported. Refer to the [Connecting a Redshift Data Warehouse via SSH Tunnel]({{ link.destinations.setup.redshift-ssh | prepend: site.baseurl }}) guide.
{% endcapture %}

{% include note.html first-line="**This tutorial is for Redshift direct connections**" content=setup-notice %}
