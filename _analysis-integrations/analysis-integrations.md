---
title: Analysis Integrations
permalink: /analysis-integrations/
keywords: analysis, analysis integration, analytics, analyze stitch data, layer, analysis tool, visualization tool, sql, query stitch data
tags: [analysis_integrations]
summary: "Stitch gives you the ability to consolidate and optimize your data, but if you want to do some exploring, you’ll need an additional visualization or middleware tool. Whether you want to create visual analyses or run SQL queries, Stitch is compatible with a broad range of tools - from business intelligence platforms to SQL editors to data science tools."
toc: true

analytics:
  - name: "Chart.io"
    url: https://chartio.com/?utm_source=stitch&utm_medium=documentation&utm_campaign=stitch+partner+referral
    icon: /images/analysis-integrations/chartio.svg
    price: "Proprietary"
    partner: true

  - name: "Looker"
    url: http://www.looker.com/
    icon: /images/analysis-integrations/looker.svg
    price: "Proprietary"
    partner: true

  - name: "Mode"
    url: https://www.modeanalytics.com/
    icon: /images/analysis-integrations/mode_analytics.svg
    price: "Proprietary"
    partner: true

  - name: "Indicative"
    url: https://indicative.com/
    icon: /images/analysis-integrations/indicative.svg
    price: "Proprietary"
    partner: true

  - name: "Redash"
    url: https://redash.io/
    price: "Free & Proprietary"
    icon: /images/analysis-integrations/redash.svg
    partner: true

  - name: "Cluvio"
    url: https://www.cluvio.com/?utm_source=stitch&utm_medium=partner+page&utm_campaign=stitch+partner+referral
    price: "Proprietary"
    icon: /images/analysis-integrations/cluvio.svg
    partner: true 

  - name: "Trifacta"
    url: https://www.trifacta.com/
    price: "Proprietary"
    icon: /images/analysis-integrations/trifacta.svg
    partner: true

sql:
  - name: "SQL Workbench"
    url: http://www.sql-workbench.net/
    price: "Free"
    os: "Windows, OS X"

  - name: "Postico"
    url: https://eggerapps.at/postico/
    price: "Free & Proprietary"
    os: "OS X"

  - name: "SQuirreL"
    url: http://squirrel-sql.sourceforge.net/
    price: "Open Source"
    os: "Windows, OS X"

  - name: "DBeaver"
    url: http://dbeaver.jkiss.org/
    price: "Open Source"
    os: "Windows, OS X"

  - name: "PG Commander"
    url: https://eggerapps.at/pgcommander/
    price: "Proprietary"
    os: "OS X"

  - name: "Aginity Workbench for Redshift"
    url: http://www.aginity.com/workbench/redshift/
    price: "Free & Proprietary"
    os: "Windows"

  - name: "Navicat"
    url: http://navicat.com/products/navicat-for-postgresql
    price: "Proprietary"
    os: "Windows, OS X"

  - name: "RazorSQL"
    url: http://razorsql.com/features/redshift_database_query_tool.html
    price: "Proprietary"
    os: "Windows, OS X"

  - name: "JackDB"
    url: https://www.jackdb.com/
    price: "Proprietary"
    os: "Windows, OS X"

  - name: "0xDBE"
    url: https://www.jetbrains.com/dbe/
    price: "Proprietary"
    os: "Windows, OS X"

  - name: "Aqua Data Studio"
    url: http://www.aquafold.com/dbspecific/amazon_redshift_client.html
    price: "Proprietary"
    os: "Windows, OS X"

data-science:
  - name: "Amazon Machine Learning"
    url: https://aws.amazon.com/machine-learning/
    price: "Proprietary"
    webapp: true
    os: "Windows, OS X"

  - name: "Dato"
    url: https://dato.com/
    price: "Free & Proprietary"
    webapp: false
    os: "Windows, OS X"

  - name: "Julia"
    url: http://julialang.org/
    price: "Open Source"
    webapp: false
    os: "Windows, OS X"

  - name: "Jupyter"
    url: https://jupyter.org/
    price: "Open Source"
    webapp: true
    os: "Windows, OS X"

  - name: "MATLAB"
    url: http://www.mathworks.com/products/matlab/
    price: "Proprietary"
    webapp: false
    os: "Windows, OS X"

  - name: "R"
    url: https://www.r-project.org/
    price: "Open Source"
    webapp: false
    os: "Windows, OS X"

  - name: "Scala"
    url: https://eggerapps.at/pgcommander/
    price: "Open Source"
    webapp: false
    os: "Windows, OS X"

display-table: |
  <table id="[LIST]" width="80%; fixed">
  <thead>
  <tr>
  <th width="38%; fixed">Integration</th>
  <th>Pricing</th>
  <th>OS</th>
  </tr>
  </thead>
  <tbody>
  {% assign [LIST] = page.[LIST] | sort:"name" %}
  {% for integration in [LIST] %}
  <tr>
  <td valign="top" markdown="span">[{{ integration.name }}]({{ integration.url }})</td>
  <td valign="top">{{ integration.price }}</td>
  <td valign="top">{{ integration.os }}</td>
  </tr>
  {% endfor %}
  </tbody>
  </table>

---
Stitch gives you the ability to consolidate and optimize your data, but if you want to do some exploring, you'll need an additional visualization or middle ware tool. 

Whether you want to create visual analyses or run SQL queries, Stitch is compatible with a broad range of tools - from business intelligence platforms to SQL editors to data science tools.

---

## Analytics Integrations

We've partnered with some of the best-in-class tools for business intelligence and visualization. These tools will enable you to take a deep-dive into your data and visualize the results.

As a bonus, some tools - like Mode - also include a built-in SQL querying tool.

<ul class="tiles">
{% assign analytics = page.analytics | sort:"name" %}
{% for integration in analytics %}
    <li>
        <a href="{{ integration.url }}" target="new">
            <img src="{{ integration.icon | prepend: site.baseurl }}" alt="{{ integration.name }}">
        </a>
        <strong>{{ integration.name }}</strong><br>
        {{ integration.price }}
    </li>
{% endfor %}
</ul>

---

## SQL Editors

If you want to directly query your data, you'll need a SQL editor to connect to your data warehouse.

In addition to allowing you to use SQL to analyze your data, a SQL editor is an incredibly valuable asset when diagnosing a data discrepancy. As we'll ask you to submit the results of several SQL queries to us to help troubleshoot the discrepancy, we recommend finding one you like. We happen to like Postico here at Stitch.

{{ page.display-table | replace:"[LIST]","sql" | flatify }}

---

## Data Science

Want to use your data for something other than creating charts or queries? From machine learning to statistical modeling, this list of data science clients will get you started.

{{ page.display-table | replace:"[LIST]","data-science" | flatify }}