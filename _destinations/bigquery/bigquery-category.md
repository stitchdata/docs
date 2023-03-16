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

title: Google BigQuery Destination Documentation
permalink: /destinations/google-bigquery

keywords: bigquery, google bigquery data warehouse, bigquery data warehouse, bigquery etl, etl to bigquery, bigquery destination
summary: "Documentation for Stitch's Google BigQuery destination."

content-type: "destination-category"
key: "bigquery-category"

order: 1

toc: true
layout: general


# -------------------------- #
#     Destination Details    #
# -------------------------- #

connection-type: "destination"

display_name: "Google BigQuery"
type: "bigquery"

sections:
  - title: "Select version"
    anchor: "select-version"
    content: |
      For a side-by-side comparison of each version of the {{ destination.display_name }} destination, refer to the [Version comparison section](#version-comparison).

      {% assign destinations = site.destinations | where:"key","bigquery-version-category" | sort:"this-version" | reverse %}

      <ul class="tiles two-columns">
      {% for destination in destinations %}
        <li>
          <a href="{{ site.baseurl | append: destination.url }}">
            <img src="{{ site.baseurl }}/images/destinations/icons/{{ destination.type }}.svg" style="max-height: 60px;" alt="{{ destination.display_name }} v{{ destination.this-version }} logo">
          </a>
          <strong>{{ destination.display_name }} (v{{ destination.this-version }})</strong><br>
          <a href="{{ site.baseurl | append: destination.url }}">All {{ destination.display_name }} (v{{ destination.this-version }}) documentation</a>
        </li>
      {% endfor %}
      </ul>

      **Interested in migrating from v1 to v2?** [Here's how]({{ link.destinations.setup.bigquery-v1-migration | prepend: site.baseurl }}). 

  - title: "Version history"
    anchor: "version-history-comparison"
    content: |
      {% include shared/versioning/version-history.html %}

  - title: "Version comparison"
    anchor: "version-comparison"
    content: |
      {% include shared/versioning/destination-supported-features.html %}
---