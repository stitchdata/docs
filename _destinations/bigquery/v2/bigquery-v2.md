---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/destination-templates/destination-setup/
## FOR INSTRUCTIONS & REFERENCE INFO


# -------------------------- #
#        Page Controls       #
# -------------------------- #

title: Google BigQuery (v2) Destination Documentation
keywords: bigquery, google bigquery data warehouse, bigquery data warehouse, bigquery etl, etl to bigquery, bigquery destination
summary: "Documentation for version 2 of Stitch's Google BigQuery destination."

permalink:  /destinations/google-bigquery/v2

destination: true
content-type: "destination-category"
key: "bigquery-version-category"

order: 1

layout: general


# -------------------------- #
#     Destination Details    #
# -------------------------- #

display_name: "Google BigQuery"
type: "bigquery"

this-version: "2"


# -------------------------- #
#          Sections          #
# -------------------------- #

sections:
  - title: "Getting started"
    anchor: "get-started"
    guides:
      - key: "bigquery-setup"
        version: "2"
      - key: "bigquery-v1-migration"
    content: |
      {% include layout/category-sections.html %}

  - title: "Using {{ page.display_name }}"
    anchor: "using-destination"
    guides:
      - key: "bigquery-pricing"
      - key: "bigquery-partitioning"
      - key: "bigquery-nested-data"
      - key: "append-only-querying"
    content: |
      {% include layout/category-sections.html %}

  - title: "Troubleshooting"
    anchor: "troubleshooting-destination"
    guides:
      - key: "destination-loading-errors"
      - key: "destination-connection-errors"
    content: |
      {% for guide in section.guides %}
      {% assign this-guide = site.documents | where:"key",guide.key | first %}
      <span class="h4">
      [{{ this-guide.title }}]({{ this-guide.url | prepend: site.baseurl }})
      </span>
      {{ this-guide.summary | flatify }}
      {% endfor %}

  - title: "Reference"
    anchor: "reference-guides"
    guides:
      - key: "bigquery-reference"
        version: "2"
      - key: "bigquery-loading-reference"
        version: "2"
      - key: "source-destination-compatibility"
      - key: "system-tables-and-columns"
      - key: "reserved-keywords"
      - key: "primary-key-system-table"
#   - loading-errors
#   - connection-errors
    content: |
      {% include layout/category-sections.html %}
---