---
title: Replicating Database Views
permalink: /replication/replicating-database-views
keywords: replicate, replication, replicate views, view, database view, replicate database view
tags: [replication]
layout: general

content-type: "select-data"
toc: true
weight: 3

summary: "Replicating a database view is almost the same as replicating a database table. In this guide, we'll cover the database integrations that support views and the additional steps required to replicate a database view."

sections:
  - content: |
      {{ page.summary }}

  - title: "Supported databases"
    anchor: "supported-databases"
    content: |
      Database views can be replicated from the following database integrations only:

      {% assign all-databases = site.database-integrations | where:"input",true %}
      {% assign databases-with-view-support = all-databases | where:"view-replication",true | sort:"display_name" %}

      {% for integration in databases-with-view-support %}
      - [{{ integration.display_name }}]({{ integration.url | prepend: site.baseurl }})
      {% endfor %}

  - title: "Setting a view to replicate"
    anchor: "set-view-to-replicate"
    content: |
      To replicate a database view, follow these steps:

      {% for subsection in section.subsections %}
      - [{{ subsection.title | flatify }}](#{{ subsection.anchor }})
      {% endfor %}
    subsections:
      - title: "Step {{ forloop.index }}: Verify the database user's permissions"
        anchor: "step--verify-database-user-permissions"
        content: |
          To replicate the view, the Stitch database user must have the appropriate level of permissions to access it.

          **If you don't see the view you want in the Stitch app**, it may be because the Stitch user has insufficient permissions. Verify that the Stitch user's permissions and, if necessary, grant any that are missing.

          For a refresher on the permissions Stitch needs, refer to the articles linked below:

          {% for integration in databases-with-view-support %}
          - [{{ integration.display_name }}]({{ integration.url | prepend: site.baseurl | append: "#create-stitch-db-user" }})
          {% endfor %}

      - title: "Step {{ forloop.index }}: Select the view in Stitch"
        anchor: "step--select-view-in-stitch"
        content: |
          **Note**: [Parent objects]({{ link.replication.syncing | prepend: site.baseurl | append: "#set-data-to-replicate" }}) - like the database containing the view - must also be set to replicate. If they aren't, set them to replicate before continuing.

          1. Click into the database integration from the {{ app.page-names.dashboard }} page.
          2. Navigate to the view you want to replicate.
          3. Click the icon next to the **Sync Status** column to set the view to replicate.
          3. Once a view has been set to replicate, the **View Settings** page will display.

      - title: "Step {{ forloop.index }}: Define the view's Primary Key"
        anchor: "step--define-view-primary-key"
        content: |
          Next, you'll define the Primary Key setting for the view. There are two options:

          - **No Primary Key:** The view will be replicated using [Append-Only Replication]({{ link.replication.append-only | prepend: site.baseurl }}). Existing rows will not be updated, and any new rows will be appended to the end of the table.
          - **Custom Primary Key:** If selected, the field or fields you define will be used as the view's Primary Keys. To add additional fields, click the **Add** button.

          **Note**: You can change the Primary Key setting - including adding or removing fields to the Custom Primary Key - at any time, but doing so will require a full re-replication of the view. This is to ensure that there aren't any gaps in the data.

      - title: "Step {{ forloop.index }}: Define the view's Replication Method"
        anchor: "step--define-view-replication-method"
        content: |
          The last step is to define the view's Replication Method. Replication Methods tell Stitch how to extract data from a source table, which will directly impact your overall row usage.

          The following Replication Methods are available for use with database views:

          - [**Key-based Incremental Replication**]({{ link.replication.key-based-incremental | prepend: site.baseurl }}): This method will only replicate new and updated data, based on the Replication Key column you define. **A Replication Key is required to use this method.** Refer to the [Replication Key]({{ link.replication.rep-keys | prepend: site.baseurl }}) documentation for more info.

          - [**Full Table Replication**]({{ link.replication.full-table | prepend: site.baseurl }}): This method will replicate the view in full during every replication job.

      - title: "Step {{ forloop.index }}: Save the view's settings"
        anchor: "step--save-view-settings"
        content: |
          Once you've defined the view's Primary Key(s) and Replication Method, click the **Save Settings** button.

          During the next replication job, Stitch will replicate the view according to the settings you defined.
---
{% include misc/data-files.html %}