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
    anchor: "getting-started"
    content: |
      {% assign all-destination-setup-guides = site.documents | where:"content-type","destination-setup" %}
      {% assign versioned-setup-guides = all-destination-setup-guides | where:"this-version",page.this-version %}
      {% assign destination-setup-guides = versioned-setup-guides | where:"type",page.type | sort:"title" %}

      {% for guide in destination-setup-guides %}
      <span class="h4">
      [{{ guide.title }}]({{ guide.url | prepend: site.baseurl }})
      </span>
      {{ guide.summary | markdownify }}
      {% endfor %}

  - title: "Using {{ page.display_name }}"
    anchor: "using-destination"
    guides:
      - key: "bigquery-pricing"
      - key: "bigquery-partitioning"
      - key: "switch-bigquery-location"
      - key: "append-only-querying"
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
      - key: "dedicated-overview"
      - key: "source-destination-compatibility"
      - key: "system-tables-and-columns"
      - key: "reserved-keywords"
#   - loading-errors
#   - connection-errors
    content: |
      {% for guide in section.guides %}
      {% if guide.key == "dedicated-overview" %}
        {% assign all-destination-overviews = site.documents | where:"content-type","destination-overview" %}

          {% assign all-this-destinations-overviews = all-destination-overviews | where:"type",page.type %}
            {% if page.this-version %}
              {% assign this-guide = all-this-destinations-overviews | where:"this-version",page.this-version | first %}
            {% else %}
              {% assign this-guide = all-this-destinations-overviews | first %}
            {% endif %}

      {% else %}
        {% assign this-guide = site.documents | where:"key",guide.key | first %}
      {% endif %}

      <span class="h4">
      [{{ this-guide.title }}]({{ this-guide.url | prepend: site.baseurl }})
      </span>
      {{ this-guide.summary | flatify }}
      {% endfor %}

# Guides:
#   - bq-pricing
#   - bq-partitioning
#   - append-only-queries

# References:
#   - system-columns
#   - reserved-keywords
#   - compatibility

# Loading:
#   - sdc-rejected
#   - column-splits
---