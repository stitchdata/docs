---
## FOR DESTINATIONS THAT HAVE MORE THAN 1 VERSION.

# -------------------------- #
#        Page Controls       #
# -------------------------- #

title: "MySQL Destination Documentation"
permalink: /destinations/mysql

keywords: mysql, mysql data warehouse, mysql data warehouse, mysql etl, etl to mysql, mysql destination
summary: "Documentation for Stitch's MySQL destination."

destination: true
content-type: "destination-category"
key: "mysql-category"

order: 1

layout: general


# -------------------------- #
#     Destination Details    #
# -------------------------- #

display_name: "MySQL"
type: "mysql"

this-version: "1"

sections:
  - title: "Select version"
    anchor: "select-version"
    content: |
      For a side-by-side comparison of each version of the {{ destination.display_name }} destination, refer to the [Version comparison section](#version-comparison).

      {% assign destinations = site.destinations | where:"key","mysql-version-category" | sort:"this-version" | reverse %}

      <ul class="tiles three-columns">
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

  - title: "Version history"
    anchor: "version-history-comparison"
    content: |
      {% include shared/versioning/version-history.html %}

  - title: "Version comparison"
    anchor: "version-comparison"
    content: |
      {% include shared/versioning/destination-supported-features.html %}
---