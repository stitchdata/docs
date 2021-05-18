---
# -------------------------- #
#          PAGE INFO         #
# -------------------------- #

title: "Connecting [TODO: a/an] [display-name] (v[version]) database integration to Stitch"
permalink: /integrations/databases/[db-type]/v[version]/connecting-[db-flavor]

keywords: "[db-type], database integration, etl [db-type], [db-type] etl, etl"
summary: "Connect and replicate data from your [display-name] database using Stitch's [display-name] (v[version]) integration."

layout: tutorial
content-type: "integration-setup"
key: "[db-type]-integration-setup"


# -------------------------- #
#     Integration Details    #
# -------------------------- #

this-version: ""

name: "[db-flavor]"
display_name: "[display-name]"
db-type: "[db-type]"


# -------------------------- #
#           Intro            #
# -------------------------- #

# REMOVE IF NOT USED.
# `intro` displays a single paragraph. Use `intro-sections` if you need headings.

# intro:
# intro-sections: 


# -------------------------- #
#      Setup Requirements    #
# -------------------------- #

requirements:
  - item: ""


# -------------------------- #
#     Setup Instructions     #
# -------------------------- #

## REMOVE ANY STEPS IF THEY'RE NOT NEEDED.

steps:
  - title: "Configure database connection settings"
    anchor: "connect-settings"
    content: |
      {% include integrations/templates/configure-connection-settings.html %}

  - title: "Create a Stitch database user"
    anchor: "create-a-database-user"
    content: |
      Next, you'll create a dedicated database user for Stitch. This will ensure Stitch is visible in any logs or audits, and allow you to maintain your privilege hierarchy.

      {% include integrations/templates/create-database-user-tabs.html %}

  - title: "Configure Log-based Incremental Replication"
    anchor: "configure-log-based-incremental-replication"
    content: |
      {% include note.html type="single-line" content="**Note**: Skip this step if you're not planning to use Log-based Incremental Replication. [Click to skip ahead](#connect-stitch)." %}

      {% include integrations/databases/setup/binlog/configure-server-settings-intro.html %}

      In this section:

      {% for substep in step.substeps %}
      - [Step 3.{{ forloop.index }}: {{ substep.title | flatify }}](#{{ substep.anchor }})
      {% endfor %}
    substeps:

  - title: "Connect Stitch"
    anchor: "connect-stitch"
    content: |
      In this step, you'll complete the setup by entering the database's connection details and defining replication settings in Stitch.

      {% for substep in step.substeps %}
      - [Step 4.{{ forloop.index }}: {{ substep.title | flatify }}](#{{ substep.anchor }})
      {% endfor %}

    substeps:
      - title: "Define the database connection details"
        anchor: "define-connection-details"
        content: |
          {% include shared/database-connection-settings.html type="general" %}

      - title: "Define the SSH connection details"
        anchor: "ssh-connection-details"
        content: |
          {% include shared/database-connection-settings.html type="ssh" %}

      - title: "Define the SSL connection details"
        anchor: "ssl-connection-details"
        content: |
          {% include shared/database-connection-settings.html type="ssl" %}

      - title: "Define the Log-based Replication setting"
        anchor: "define-log-based-replication-setting"
        content: |
          {% include note.html type="single-line" content="**Note**: Skip this step if you're not planning to use Log-based Incremental Replication. [Click to skip ahead](#create-replication-schedule)." %}

          {% include integrations/databases/setup/binlog/log-based-replication-default-setting.html %}

      - title: "Create a replication schedule"
        anchor: "create-replication-schedule"
        content: |
          {% include integrations/shared-setup/replication-frequency.html %}

      - title: "Save the integration"
        anchor: "save-integration"
        content: |
          {% include shared/database-connection-settings.html type="finish-up" %}

  - title: "Select data to replicate"
    anchor: "sync-data"
    content: |
      {% include integrations/shared-setup/data-selection/object-selection.html %}
---
{% assign integration = page %}
{% include misc/data-files.html %}