---
## FOR DESTINATIONS THAT HAVE MORE THAN 1 VERSION.

# -------------------------- #
#        Page Controls       #
# -------------------------- #

title: Microsoft SQL Server Destination Documentation
permalink: /destinations/microsoft-sql-server

keywords: microsoft sql server, microsoft sql server data warehouse, microsoft sql server data warehouse, microsoft sql server etl, etl to microsoft sql server, microsoft sql server destination
summary: "Documentation for Stitch's Microsoft SQL Server destination."

destination: true
content-type: "destination-category"
key: "microsoft-sql-server-category"


order: 1

layout: general


# -------------------------- #
#     Destination Details    #
# -------------------------- #

display_name: "Microsoft SQL Server"
type: "microsoft-sql-server"

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
      - key: "microsoft-sql-server-loading-reference"
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