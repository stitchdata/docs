---
title: Amazon Aurora integrations
keywords: amazon, amazon rds, rds, relational database services, database integration, etl rds, rds etl, aurora, amazon aurora, aurora rds
permalink: /integrations/databases/amazon-aurora
summary: "Connect and replicate data from your Amazon Aurora RDS databases using Stitch's database integrations."
layout: general
input: false

key: "amazon-aurora-integration"

toc: false
feedback: false

sections:
  - content: |
      {% assign all-databases = site.database-integrations | where_exp:"integration","integration.name contains 'aurora'" %}

      Stitch supports connecting to both MySQL and PostgreSQL-backed Amazon Aurora databases as data sources:

      <ul class="tiles">
          {% for integration in all-databases %}
              {% if integration.show-in-menus == true %}
              <li>
                  <a href="{{ integration.url | prepend: site.baseurl }}">
                      <img src="{{ site.baseurl }}/images/integrations/icons/{{ integration.name }}.svg" alt="{{ integration.display_name }}">
                  </a>
                  <strong>{{ integration.display_name| remove:"(latest)" | prepend: "Amazon "}}</strong><br>

                  {% if integration.has-versions %}
                      {% include shared/versioning/version-menu.html connection-type="integration" menu-type="category-page" item-name="integration" %}

                  {% else %}
                      <a href="{{ integration.url | prepend: site.baseurl | append: "#setup" }}">Setup</a> 
                      | <a href="{{ integration.url | prepend: site.baseurl | append: "#replication" }}">Replication</a>
                  {% endif %}
              </li>
              {% endif %}
          {% endfor %}
      </ul>

      For the full list of RDS databases Stitch supports, [click here]({{ site.baseurl }}/integrations/databases/amazon-rds).
---
{% assign integration = page %}
{% include misc/data-files.html %}