---
# -------------------------- #
#          PAGE INFO         #
# -------------------------- #

title: Analysis Tools
permalink: /analysis-tools/
redirect_from: /analysis-integrations/
keywords: analysis, analysis integration, analytics, analyze stitch data, layer, analysis tool, visualization tool, sql, query stitch data
summary: "Stitch gives you the ability to consolidate and optimize your data, but if you want to do some exploring, you’ll need an additional visualization or middleware tool."

layout: general
toc: true

level: "category"

key: "analysis-tools"


# -------------------------- #
#       HOME PAGE DATA       #
# -------------------------- #

## Used to display info on the home page as a category tile

icon: "analytics"
display-title: "Analysis tools"
display-summary: "Interact with your Stitch-replicated data using an additional analysis tool."
weight: 7

# -------------------------- #
#        CONTENT DATA        #
# -------------------------- #

analytics:

  - name: "Metabase"
    id: "metabase"
    url: https://www.metabase.com/
    pricing: "Proprietary"
    partner: true
    tutorial: https://www.stitchdata.com/blog/tutorial-metabase-with-data-warehouse-for-analytics

  - name: "Google Data Studio"
    id: "google-data-studio"
    url: https://datastudio.google.com/
    pricing: "Proprietary"
    partner: true
    tutorial: https://www.stitchdata.com/blog/tutorial-using-google-data-studio-with-bigquery-and-stitch

  - name: "PowerBI"
    id: "powerbi"
    url: https://powerbi.microsoft.com/
    pricing: "Proprietary"
    partner: true
    tutorial: https://www.stitchdata.com/blog/tutorial-using-power-bi-with-your-data-warehouse-for-analytics-2

  - name: "Grafana"
    id: "grafana"
    url: https://grafana.com/
    pricing: "Proprietary"
    partner: true

  - name: "Tableau"
    id: "tableau"
    url: https://www.tableau.com/
    pricing: "Proprietary"
    partner: true
    tutorial: https://www.stitchdata.com/blog/tutorial-connecting-tableau-to-your-data-warehouse-for-analytics

  - name: "Chart.io"
    id: "chartio"
    url: https://chartio.com/?utm_source=stitch&utm_medium=documentation&utm_campaign=stitch+partner+referral
    pricing: "Proprietary"
    partner: true
    tutorial: https://www.stitchdata.com/blog/tutorial-using-chartio-with-a-data-warehouse-for-business-analytics

  - name: "Looker"
    id: "looker"
    url: http://www.looker.com/
    pricing: "Proprietary"
    partner: true

  - name: "Mode"
    id: "mode-analytics"
    url: https://www.modeanalytics.com/
    pricing: "Proprietary"
    partner: true

  - name: "Indicative"
    id: "indicative"
    url: https://indicative.com/
    pricing: "Proprietary"
    partner: true

  - name: "Redash"
    id: "redash"
    url: https://redash.io/
    pricing: "Free & Proprietary"
    partner: true

  - name: "Cluvio"
    id: "cluvio"
    url: https://www.cluvio.com/?utm_source=stitch&utm_medium=partner+page&utm_campaign=stitch+partner+referral
    pricing: "Proprietary"
    partner: true 

  - name: "Trifacta"
    id: "trifacta"
    url: https://www.trifacta.com/
    pricing: "Proprietary"
    partner: true

sql:
  - name: "SQL Workbench"
    url: http://www.sql-workbench.net/
    pricing: "Free"
    supports: |
      [Most JDBC-compliant databases](http://www.sql-workbench.eu/databases.html){:target="new"}
    webapp: false
    operating-system: "Windows, OS X"

  - name: "Postico"
    url: https://eggerapps.at/postico/
    pricing: "Free & Proprietary"
    supports: "PostgreSQL-based databases"
    webapp: false
    operating-system: "OS X"

  - name: "SQuirreL"
    url: http://squirrel-sql.sourceforge.net/
    pricing: "Open Source"
    supports: "Any JDBC-compliant database"
    webapp: false
    operating-system: "Windows, OS X"

  - name: "DBeaver"
    url: http://dbeaver.jkiss.org/
    pricing: "Open Source"
    supports: |
      [Many popular databases](https://dbeaver.io/docs/features/#Supported_databases_and_platforms){:target="new"}
    webapp: false
    operating-system: "Windows, OS X"

  - name: "Aginity Workbench for Redshift"
    url: http://www.aginity.com/workbench/redshift/
    pricing: "Free & Proprietary"
    supports: "Amazon Redshift"
    webapp: false
    operating-system: "Windows"

  - name: "Navicat"
    url: http://navicat.com/products/navicat-for-postgresql
    pricing: "Proprietary"
    supports: "PostgreSQL databases"
    webapp: false
    operating-system: "Windows, OS X"

  - name: "RazorSQL"
    url: http://razorsql.com/features/redshift_database_query_tool.html
    pricing: "Proprietary"
    supports: "Amazon Redshift"
    webapp: false
    operating-system: "Windows, OS X"

  - name: "JackDB"
    url: https://www.jackdb.com/
    pricing: "Proprietary"
    supports: |
      [Many popular databases](https://www.jackdb.com/data-sources){:target="new"}
    webapp: true
    operating-system: "Windows, OS X"

  - name: "DataGrip"
    url: https://www.jetbrains.com/dbe/
    pricing: "Proprietary"
    supports: |
      [Many popular databases](https://www.jetbrains.com/datagrip/features/){:target="new"}
    webapp: false
    operating-system: "Windows, OS X"

  - name: "Aqua Data Studio"
    url: http://www.aquafold.com/dbspecific/amazon_redshift_client.html
    pricing: "Proprietary"
    supports: "Amazon Redshift"
    webapp: false
    operating-system: "Windows, OS X"
    
  - name: "SeekWell"
    url: https://www.seekwell.io/
    pricing: "Free & Proprietary"
    supports: "Many popular databases"
    webapp: true
    operating-system: "Windows, OS X"

data-science:
  - name: "Amazon Machine Learning"
    url: https://aws.amazon.com/machine-learning/
    pricing: "Proprietary"
    webapp: true
    operating-system: "Windows, OS X"

  - name: "Dato"
    url: https://dato.com/
    pricing: "Free & Proprietary"
    webapp: false
    operating-system: "Windows, OS X"

  - name: "Julia"
    url: http://julialang.org/
    pricing: "Open Source"
    webapp: false
    operating-system: "Windows, OS X"

  - name: "Jupyter"
    url: https://jupyter.org/
    pricing: "Open Source"
    webapp: true
    operating-system: "Windows, OS X"

  - name: "MATLAB"
    url: http://www.mathworks.com/products/matlab/
    pricing: "Proprietary"
    webapp: false
    operating-system: "Windows, OS X"

  - name: "R"
    url: https://www.r-project.org/
    pricing: "Open Source"
    webapp: false
    operating-system: "Windows, OS X"

  - name: "Scala"
    url: https://eggerapps.at/pgcommander/
    pricing: "Open Source"
    webapp: false
    operating-system: "Windows, OS X"

display-table: |
  {% assign attributes = "Name|Pricing|Web app|OS" | split:"|" %}

  <table id="[LIST]" class="attribute-list">
  <tr>
  {% for attribute in attributes %}
  {% if forloop.first == true %}
  <td class="attribute-name">
  {% else %}
  <td>
  {% endif %}

  <strong>{{ attribute }}</strong>
  </td>
  {% endfor %}
  </tr>

  {% assign [LIST] = page.[LIST] | sort:"name" %}
  {% for tool in [LIST] %}
  <tr>

  <td class="attribute-name" markdown="span">
  [{{ tool.name }}]({{ tool.url }})
  </td>
  
  <td valign="top">
  {{ tool.pricing }}
  </td>
  
  <td valign="top">
  {% case tool.webapp %}
  {% when true %}
  {{ supported }}
  {% when false %}
  {{ not-supported }}
  {% endcase %}
  </td>
  
  <td valign="top">
  {{ tool.operating-system }}
  </td>
  </tr>
  
  {% endfor %}

  </table>


# -------------------------- #
#      CONTENT SECTIONS      #
# -------------------------- #

intro: |
  {% include misc/data-files.html %}
  {% include misc/icons.html %}

  Stitch gives you the ability to consolidate and optimize your data, but if you want to do some exploring, you'll need an additional visualization or middle ware tool. 

  Whether you want to create visual analyses or run SQL queries, Stitch is compatible with a broad range of tools - from business intelligence platforms to SQL editors to data science tools.

sections:
  - title: "Analytics tools"
    anchor: "analytics-tools"
    content: |
      Stitch can consolidate your data for use in some of the best-in-class tools for business intelligence and visualization. These tools will enable you to take a deep-dive into your data and visualize the results.

      <ul class="tiles three-columns">
      {% assign analytics = page.analytics | sort:"name" %}
      {% for tool in analytics %}
          <li>
              <a href="{{ tool.url }}" target="new">
                  <img src="{{ site.baseurl }}/images/analysis-tools/{{ tool.id }}.svg" alt="{{ tool.name }}">
              </a>
              <strong>{{ tool.name }}</strong><br>
              {% if tool.tutorial %}<a href="{{tool.tutorial}}" target="_blank">Tutorial: using Stitch <br/>and {{tool.name}} →</a>{% endif %}
          </li>
      {% endfor %}
      </ul>

  - title: "SQL editors"
    anchor: "sql-editors"
    content: |
      If you want to directly query your data, you'll need a SQL editor to connect to your data warehouse.

      In addition to allowing you to use SQL to analyze your data, a SQL editor is an incredibly valuable asset when diagnosing a data discrepancy. As we'll ask you to submit the results of several SQL queries to us to help troubleshoot the discrepancy, we recommend finding one you like. We happen to like Postico here at Stitch.

      {{ page.display-table | replace:"[LIST]","sql" | flatify }}

  - title: "Data science"
    anchor: "data-science"
    content: |
      Want to use your data for something other than creating charts or queries? From machine learning to statistical modeling, this list of data science clients will get you started.

      {{ page.display-table | replace:"[LIST]","data-science" | flatify }}
---