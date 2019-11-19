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

title: data.world Destination Documentation
permalink: /destinations/data-world

keywords: data.world, data world, data.world destination
summary: "Documentation for Stitch's data.world destination."

content-type: "destination-category"
key: "data-world-category"

order: 1

layout: general


# -------------------------- #
#     Destination Details    #
# -------------------------- #

display_name: "data.world"
type: "data-world"


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
---