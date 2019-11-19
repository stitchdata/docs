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

title: Amazon S3 Destination Documentation
permalink:  /destinations/amazon-s3

keywords: 
summary: "Documentation for Stitch's Amazon S3 destination."

destination: true
content-type: "destination-category"
key: "amazon-s3-category"

order: 1

layout: general


# -------------------------- #
#     Destination Details    #
# -------------------------- #

display_name: "Amazon S3"
type: "amazon-s3"

this-version: "1"

# -------------------------- #
#          Sections          #
# -------------------------- #

sections:
  - title: "Getting started"
    anchor: "getting-started"
    content: |
      {% assign all-destination-setup-guides = site.documents | where:"content-type","destination-setup" %}
      {% assign destination-setup-guides = all-destination-setup-guides | where:"type",page.type | sort:"title" %}

      {% for guide in destination-setup-guides %}
      <span class="h4">
      [{{ guide.title }}]({{ guide.url | prepend: site.baseurl }})
      </span>
      {{ guide.summary | markdownify }}
      {% endfor %}

  - title: "Using {{ page.display_name }}"
    anchor: "using-destination"
    guides:
      - key: "de-nesting-json"
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
#   - append-only-queries

# References:
#   - dedicated
#   - system-columns
#   - sdc-rejected
#   - reserved-keywords
#   - compatibility

# Loading:
#   - json-denesting (CSV only)
#   - data-structure (content is in dedicated-reference)
---