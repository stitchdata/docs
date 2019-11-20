---
## FOR DESTINATIONS THAT HAVE MORE THAN 1 VERSION.

# -------------------------- #
#        Page Controls       #
# -------------------------- #

title: DESTINATION-NAME Destination Documentation
permalink: /destinations/destination-type

keywords: destination-type, destination-type data warehouse, destination-type data warehouse, destination-type etl, etl to destination-type, destination-type destination
summary: "Documentation for Stitch's DESTINATION-NAME destination."

content-type: "destination-category"
key: "destination-type-category"

order: 1

toc: true
layout: general


# -------------------------- #
#     Destination Details    #
# -------------------------- #

display_name: "DESTINATION-NAME"
type: "destination-type"

sections:
  - title: "Select version"
    anchor: "select-version"
    content: |
      For a side-by-side comparison of each version of the {{ destination.display_name }} destination, refer to the [Version comparison section](#version-comparison).

      {% assign destinations = site.destinations | where:"key","bigquery-version-category" | sort:"this-version" | reverse %}

      <ul class="tiles">
      {% for destination in destinations %}
        <li style="width: 45%">
          <a href="{{ site.baseurl | append: destination.url }}">
            <img src="{{ site.baseurl }}/images/destinations/icons/{{ destination.type }}.svg" style="max-height: 60px;" alt="{{ destination.display_name }} v{{ destination.this-version }} logo">
          </a>
          <strong>{{ destination.display_name }} (v{{ destination.this-version }})</strong><br>
          <a href="{{ site.baseurl | append: destination.url }}">All {{ destination.display_name }} (v{{ destination.this-version }}) documentation</a>
        </li>
      {% endfor %}
      </ul>

  - title: "Version history and changelog"
    anchor: "version-history-comparison"
    content: |
      {% include shared/versioning/history-and-changelog.html connection-type="destination" %}

  - title: "Version comparison"
    anchor: "version-comparison"
    content: |
      {% include shared/versioning/destination-supported-features.html %}
---