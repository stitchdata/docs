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

title: PostgreSQL Destination Documentation
permalink: /destinations/postgresql

keywords: postgresql, postgres, heroku-postgres destination, amazon rds postgresql destination
summary: "Documentation for Stitch's PostgreSQL destination."

destination: true
content-type: "destination-category"
key: "postgresql-category"

order: 1

layout: general


# -------------------------- #
#     Destination Details    #
# -------------------------- #

display_name: "PostgreSQL"
type: "postgres"

this-version: "1"

# -------------------------- #
#          Sections          #
# -------------------------- #

sections:
  - title: "Getting started"
    anchor: "get-started"
    content: |
      {% assign all-destination-setup-guides = site.documents | where:"content-type","destination-setup" %}
      {% assign destination-setup-guides = all-destination-setup-guides | where:"type",page.type | sort:"title" %}

      Using Stitch's {{ destination.display_name }} destination, you can connect the following versions of {{ destination.display_name }} to Stitch:

      {% for guide in destination-setup-guides %}
      - [{{ guide.title | remove: "Connecting an " | remove: "Connecting a " | remove: " Destination to Stitch" }}]({{ guide.url | prepend: site.baseurl }})
      {% endfor %}

  - title: "Using {{ page.display_name }}"
    anchor: "using-destination"
    guides:
      - key: "de-nesting-json"
    content: |
      {% for guide in section.guides %}
      {% assign this-guide = site.documents | where:"key",guide.key | first %}
      <span class="h4">
      [{{ this-guide.title }}]({{ this-guide.url | prepend: site.baseurl }})
      </span>
      {{ this-guide.summary | flatify }}
      {% endfor %}

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
      - key: "dedicated-overview"
      - key: "postgresql-loading-reference"
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
---