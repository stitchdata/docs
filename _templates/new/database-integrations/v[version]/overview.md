---
# -------------------------- #
#          PAGE INFO         #
# -------------------------- #

title: "[DB-TYPE] (v[VERSION]) Overview"
keywords: "[db-type], database integration, etl [db-type], [db-type] etl, elt [db-type]"
permalink: /integrations/databases/[db-type]/v[version]
summary: "Details about version [VERSION] of Stitch's [DB-TYPE] integration, including supported features, data types, setup guides, and replication info."
layout: general

content-type: "database-version-overview"
key: "[db-type]-version-overview"


# -------------------------- #
#    INTEGRATION DETAILS     #
# -------------------------- #

this-version: "[VERSION]"

db-type: "[db-type]"
display_name: "[DB-TYPE]"


# -------------------------- #
#         CONTENT            #
# -------------------------- #

## TODO:
## - version data - release date, status, etc
## - feature summary
## - changelog
## - links to flavored guides for this version
## - supported features, across all flavors
## - replication info
## - data types

sections:
  - title: ""
    anchor: ""
    content: ""


# -------------------------- #
#      Replication Info      #
# -------------------------- #

  - title: "Replication"
    anchor: "replication"
    content: |
      In this section:

      {% for section in page.sections %}
      {% if section.title %}
      - [{{ section.summary | flatify }}](#{{ section.anchor }})
      {% endif %}
      {% endfor %}
    subsections:
      - title: "Extraction"
        anchor: "extraction-details"
        summary: "Details about Extraction, including object and data type discovery and selecting data for replication"
        content: |
          For every table set to replicate, Stitch will perform the following during Extraction:

          {% for subsection in section.subsections %}
          - [{{ subsection.summary | flatify }}](#{{ subsection.anchor }})
          {% endfor %}

        subsections:
          - title: "Discovery"
            anchor: "extraction--discovery"
            summary: "Discover table schemas and type discovered columns"
            content: |
              During Discovery, Stitch will:

              {% for sub-subsection in subsection.sub-subsections %}
              - [{{ sub-subsection.summary | flatify }}](#{{ sub-subsection.anchor }})
              {% endfor %}
            sub-subsections:
              - title: "Determining table schemas"
                anchor: "discovery--objects"
                summary: "Determine table schemas"
                content: |
                  During this phase of Discovery, Stitch queries system tables to retrieve metadata about the objects the Stitch database user has access to. This metadata is used to determine which databases, tables, and columns to display in Stitch for replication.

                  [TODO: EXTRACTION QUERIES]

              - title: "Data typing"
                anchor: "discovery--data-types"
                summary: "Type the data in discovered columns"
                content: ""

          - title: "Data replication"
            anchor: "extraction--data-replication"
            summary: "Select records for replication"
            content: |
              During data replication, Stitch will:

              {% for sub-subsection in subsection.sub-subsections %}
              - [{{ sub-subsection.summary | flatify }}](#{{ sub-subsection.anchor }})
              {% endfor %}

            sub-subsections:
              - title: ""
                anchor: ""
                content: ""
---
{% include misc/data-files.html %}