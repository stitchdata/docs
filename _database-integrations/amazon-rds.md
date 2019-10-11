---
title: Amazon Relational Database System (RDS) integrations
keywords: amazon, amazon rds, rds, relational database services, database integration, etl rds, rds etl
permalink: /integrations/databases/amazon-rds
summary: "Connect and replicate data from your Amazon RDS databases using Stitch's database integrations."
layout: general
input: false

toc: false
feedback: false

sections:
    - content: |
        {% assign all-databases = site.database-integrations | where_exp:"integration","integration.name contains 'rds'" %}

        Stitch supports connecting to the following Amazon Relational Database System (RDS) databases as data sources:

        <ul class="tiles">
            {% for integration in all-databases %}
                {% if integration.show-in-menus == true %}
                <li>
                    <a href="{{ integration.url | prepend: site.baseurl }}">
                        <img src="{{ site.baseurl }}/images/integrations/icons/{{ integration.name }}.svg" alt="{{ integration.display_name }}">
                    </a>
                    <strong>{{ integration.display_name| remove:"(latest)" | prepend: "Amazon "}}</strong><br>

                    {% if integration.has-versions %}
                        {% include integrations/templates/versioning/integration-version-menu.html menu-type="category-page" %}

                    {% else %}
                        <a href="{{ integration.url | prepend: site.baseurl | append: "#setup" }}">Setup</a> 
                        | <a href="{{ integration.url | prepend: site.baseurl | append: "#replication" }}">Replication</a>
                    {% endif %}
                </li>
                {% endif %}
            {% endfor %}
        </ul>
---
{% assign integration = page %}
{% include misc/data-files.html %}