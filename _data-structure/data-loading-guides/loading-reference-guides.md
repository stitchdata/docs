---
title: Destination Data Loading Reference Guides
permalink: /replication/reference
redirect_from: /data-structure/loading-stitch-data-into-destinations

layout: general
toc: false
feedback: false

keywords: loading behavior, loading, how data is loaded, data structure
summary: "Every destination handles data differently. Learn about what your destination supports, what it doesn't, and how Stitch will load your data as a result."

key: "loading-reference"

intro: |
  {% include misc/data-files.html %}

  {{ page.summary }}

  Each guide covers scenarios involving Primary Keys, data types, object names, schema changes, and destination changes.

sections:
  - title: "Select your destination"
    anchor: "select-destination"
    content: |
      {% assign data-loading-guides = site.data-structure | where:"content-type","loading-reference" | sort: "display_name" %}

      <ul class="tiles">
      {% for guide in data-loading-guides %}

      {% if guide.branded == true %}
        {% assign connection-type = guide.display_name | slugify %}
      {% else %}
        {% assign connection-type = guide.type %}
      {% endif %}
        <li>
          <a href="{{ guide.url | prepend: site.baseurl }}">
            <img src="{{ site.baseurl }}/images/destinations/icons/{{ connection-type }}.svg" alt="{{ guide.display_name }}">
          </a>
          <strong>{{ guide.display_name }}</strong><br>

          {% if guide.has-versions == true %}
            {% include shared/versioning/version-menu.html connection-type="destination" menu-type="category-page" item-name="guide" %}
          {% else %}
            <a href="{{ guide.url | prepend: site.baseurl }}">Loading Reference</a>      
          {% endif %}
        </li>
      {% endfor %}
      </ul>
---