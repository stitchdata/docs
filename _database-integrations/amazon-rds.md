---
title: Amazon RDS
keywords: amazon, amazon rds, rds, relational database services, database integration, etl rds, rds etl
tags: [database_integrations]
permalink: /integrations/databases/amazon-rds
summary: "Connect and replicate data from your Amazon RDS database using Stitch's RDS integration."
layout: page-no-edit
input: false
---
{% assign integration = page %}
{% include misc/data-files.html %}

{% assign all-databases = site.database-integrations | where:"input",true %}

Stitch supports connecting to the following Amazon Relational Database System (RDS) databases:

<ul class="tiles">
    {% for database in all-databases %}
        {% if database.name contains "rds" %}
            <li>
                <a href="{{ database.url | prepend: site.baseurl }}">
                    <img src="{{ database.icon | prepend: site.baseurl }}" alt="{{ database.display_name }}">
                </a>
                <strong>{{ database.display_name| remove:"(latest)" | prepend: "Amazon "}}</strong><br>

                {% if database.this-version %}
                    {% include integrations/templates/versioning/integration-version-menu.html menu-type="category-page" %}
                {% else %}
                    <a href="{{ database.url | prepend: site.baseurl | append: "#setup" }}">Setup</a> 
                    | <a href="{{ database.url | prepend: site.baseurl | append: "#replication" }}">Replication</a>
                {% endif %}
            </li>
        {% endif %}
    {% endfor %}
</ul>