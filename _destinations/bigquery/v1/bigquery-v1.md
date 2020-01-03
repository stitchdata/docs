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

title: Google BigQuery (v1) Destination Documentation
keywords: bigquery, google bigquery data warehouse, bigquery data warehouse, bigquery etl, etl to bigquery, bigquery destination
summary: "Documentation for version 1 of Stitch's Google BigQuery destination."

permalink:  /destinations/google-bigquery/v1

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

this-version: "1"


# -------------------------- #
#          Sections          #
# -------------------------- #

sections:
  - title: "Getting started"
    anchor: "get-started"
    guides:
      - key: "bigquery-setup"
        version: "1"
      - key: "bigquery-v1-migration"
    content: |
      {% include layout/category-sections.html %}

  - title: "Using {{ page.display_name }}"
    anchor: "using-destination"
    guides:
      - key: "bigquery-pricing"
      - key: "bigquery-partitioning"
      - key: "switch-bigquery-location"
      - key: "append-only-querying"
    content: |
      {% include layout/category-sections.html %}

  - title: "Reference"
    anchor: "reference-guides"
    guides:
      - key: "bigquery-reference"
        version: "1"
      - key: "source-destination-compatibility"
      - key: "system-tables-and-columns"
      - key: "reserved-keywords"
#   - loading-errors
#   - connection-errors
    content: |
      {% include layout/category-sections.html %}
# Loading:
#   - sdc-rejected
#   - column-splits
---