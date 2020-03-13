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
feedback: false

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
#       ANALYTICS TOOLS      #
# -------------------------- #

## Properties for analytics tools:
  ## name: "Display name for the tool"
  ## url: "URL for the tool's marketing site"
  ## tutorial: "URL for tutorial on the Stitch blog - if included, it will display in the "Tutorials" section. Don't include if the tool doesn't have a tutorial."

analytics:
  - name: "Alteryx"
    url: https://www.alteryx.com/
    tutorial: https://www.stitchdata.com/blog/tutorial-alteryx-designer-with-stitch

  - name: "Amazon Quicksight"
    url: https://aws.amazon.com/quicksight/
    tutorial: https://www.stitchdata.com/blog/tutorial-using-redshift-and-amazon-quicksight-to-deliver-business-analytics

  - name: "Chart.io"
    url: https://chartio.com/?utm_source=stitch&utm_medium=documentation&utm_campaign=stitch+partner+referral
    tutorial: https://www.stitchdata.com/blog/tutorial-using-chartio-with-a-data-warehouse-for-business-analytics

  - name: "Cluvio"
    url: https://www.cluvio.com/?utm_source=stitch&utm_medium=partner+page&utm_campaign=stitch+partner+referral

  - name: "Domo"
    url: https://www.domo.com/

  - name: "Google Data Studio"
    url: https://datastudio.google.com/
    tutorial: https://www.stitchdata.com/blog/tutorial-using-google-data-studio-with-bigquery-and-stitch

  - name: "Grafana"
    url: https://grafana.com/

  - name: "Highcharts"
    url: https://www.highcharts.com/

  - name: "Indicative"
    url: https://indicative.com/

  - name: "Knime"
    url: https://www.knime.com/

  - name: "Looker"
    url: http://www.looker.com/

  - name: "Metabase"
    url: https://www.metabase.com/
    tutorial: https://www.stitchdata.com/blog/tutorial-metabase-with-data-warehouse-for-analytics

  - name: "Mode"
    url: https://www.modeanalytics.com/
    tutorial: https://www.stitchdata.com/blog/tutorial-how-to-use-mode-with-a-data-warehouse-for-analytics

  - name: "Qlik"
    url: https://www.qlik.com/us

  - name: "Plotly"
    url: https://plot.ly/

  - name: "PowerBI"
    url: https://powerbi.microsoft.com/
    tutorial: https://www.stitchdata.com/blog/tutorial-using-power-bi-with-your-data-warehouse-for-analytics-2

  - name: "Redash"
    url: https://redash.io/

  - name: "Shiny"
    url: https://shiny.rstudio.com/

  - name: "Sisense"
    url: https://www.sisense.com/

  - name: "Superset"
    url: https://superset.incubator.apache.org/

  - name: "Tableau"
    url: https://www.tableau.com/
    tutorial: https://www.stitchdata.com/blog/tutorial-connecting-tableau-to-your-data-warehouse-for-analytics

  - name: "Trifacta"
    url: https://www.trifacta.com/


# --------------------------------- #
#  ANALYTICS TOOLS & COMAPTIBILITY  #
# --------------------------------- #

## Destinations the analytics tool may be compatible with. Adding a tool to this list will display it in the "Destination compatibility" section.

## Properties for this list:
  ## name: "Display name for the tool"
  ## [destination]: The slugified name of the destination. Lowercase, spaces are dashes. Ex: amazon-redshift. This can be commented out if the combo isn't compatible.

    ## link-copy: "Add only if the tool+destination combo is compatible. This will be the copy that displays for the link in the table."
    ## link-url: "URL for documentation/guide/etc about the tool+destination combo."

compatibility-list:
  - name: "Amazon Quicksight"
    amazon-redshift:
      link-copy: "Supported"
      link-url: "https://docs.aws.amazon.com/quicksight/latest/user/supported-data-sources.html"
    amazon-s3:
      link-copy: "Supported"
      link-url: https://www.tableau.com/about/blog/2017/5/connect-your-s3-data-amazon-athena-connector-tableau-103-71105)
    # google-bigquery:
    # microsoft-azure:
    # postgresql:
    snowflake:
      link-copy: "Supported"
      link-url: "https://docs.aws.amazon.com/quicksight/latest/user/supported-data-sources.html"

  - name: "Google Data Studio"
    # amazon-redshift:
    # amazon-s3:
    google-bigquery:
      link-copy: "Supported"
      link-url: "https://support.google.com/datastudio/answer/6370296"
    # microsoft-azure:
    postgresql:
      link-copy: "Supported"
      link-url: "https://support.google.com/datastudio/answer/7288010"
    # snowflake:

  - name: "Grafana"
    # amazon-redshift:
    # amazon-s3:
    google-bigquery:
      link-copy: "Via plugin"
      link-url: "https://grafana.com/grafana/plugins/doitintl-bigquery-datasource"
    # microsoft-azure:
    postgresql:
      link-copy: "Supported"
      link-url: "https://grafana.com/docs/grafana/latest/features/datasources/postgres/"
    # snowflake:

  - name: "Looker"
    amazon-redshift:
      link-copy: "Supported"
      link-url: "https://docs.looker.com/setup-and-management/database-config/amazon-redshift"
    # amazon-s3:
    google-bigquery:
      link-copy: "Supported"
      link-url: "https://docs.looker.com/setup-and-management/database-config/google-bigquery"
    microsoft-azure:
      link-copy: "Supported"
      link-url: "https://docs.looker.com/setup-and-management/database-config/ms-azure-sql-dw"
    postgresql:
      link-copy: "Supported"
      link-url: "https://docs.looker.com/setup-and-management/database-config/postgresql"
    snowflake:
      link-copy: "Supported"
      link-url: "https://docs.looker.com/setup-and-management/database-config/snowflake"

  - name: "Metabase"
    amazon-redshift:
      link-copy: "Supported"
      link-url: "https://www.metabase.com/docs/latest/administration-guide/01-managing-databases.html"
    # amazon-s3:
    google-bigquery:
      link-copy: "Supported"
      link-url: "https://www.metabase.com/docs/latest/administration-guide/databases/bigquery.html"
    # microsoft-azure:
    postgresql:
      link-copy: "Supported"
      link-url: "https://www.metabase.com/docs/latest/administration-guide/01-managing-databases.html"
    snowflake:
      link-copy: "Supported"
      link-url: "https://www.metabase.com/docs/latest/administration-guide/01-managing-databases.html"

  - name: "PowerBI"
    amazon-redshift:
      link-copy: "Supported"
      link-url: "https://docs.microsoft.com/en-us/power-bi/desktop-connect-redshift"
    amazon-s3:
      link-copy: "Via REST API"
      link-url: "https://community.powerbi.com/t5/Power-Query/Can-I-connect-to-a-Amazon-S3-bucket-using-Power-Query/td-p/111919"
    google-bigquery: 
      link-copy: "Supported"
      link-url: "https://docs.microsoft.com/en-us/power-bi/desktop-connect-bigquery"
    microsoft-azure:
      link-copy: "Supported"
      link-url: "https://docs.microsoft.com/en-us/azure/sql-data-warehouse/sql-data-warehouse-get-started-visualize-with-power-bi"
    postgresql:
      link-copy: "Supported"
      link-url: "https://docs.microsoft.com/en-us/power-bi/desktop-data-sources"
    snowflake:
      link-copy: "Supported"
      link-url: "https://docs.microsoft.com/en-us/power-bi/desktop-connect-snowflake"

  - name: "Qlik"
    url: https://www.qlik.com/us
    amazon-redshift:
      link-copy: "Supported"
      link-url: "https://help.qlik.com/en-US/connectors/Subsystems/ODBC_connector_help/Content/Connectors_ODBC/Redshift/Redshift-connector.htm"
    # amazon-s3:
    google-bigquery:
      link-copy: "Supported"
      link-url: "https://help.qlik.com/en-US/connectors/Subsystems/ODBC_connector_help/Content/Connectors_ODBC/GoogleBigQuery/Google-BigQuery-Connector.htm"
    # microsoft-azure:
    # postgresql:
    snowflake:
      link-copy: "Supported"
      link-url: "https://help.qlik.com/en-US/connectors/Subsystems/ODBC_connector_help/Content/Connectors_ODBC/Snowflake/Snowflake-connector.htm"

  - name: "Sisense"
    amazon-redshift:
      link-copy: "Supported"
      link-url: "https://documentation.sisense.com/latest/managing-data/connectors/redshift-live.htm"
    amazon-s3:
      link-copy: "Via Amazon Athena"
      link-url: "https://documentation.sisense.com/latest/managing-data/connectors/athena.htm"
    google-bigquery:
      link-copy: "Supported"
      link-url: "https://documentation.sisense.com/latest/managing-data/connectors/bigquerylive.htm"
    postgresql:
      link-copy: "Supported"
      link-url: "https://documentation.sisense.com/latest/managing-data/connectors/postgresql-live.htm"
    snowflake:
      link-copy: "Supported"
      link-url: "https://documentation.sisense.com/latest/managing-data/connectors/snowflake-live.htm"

  - name: "Tableau"
    amazon-redshift:
      link-copy: "Supported"
      link-url: "https://help.tableau.com/current/pro/desktop/en-us/examples_amazonredshift.htm"
    amazon-s3:
      link-copy: "Via Amazon Athena"
      link-url: "https://www.tableau.com/about/blog/2017/5/connect-your-s3-data-amazon-athena-connector-tableau-103-71105"
    google-bigquery:
      link-copy: "Supported"
      link-url: "https://help.tableau.com/current/pro/desktop/en-us/examples_googlebigquery.htm"
    microsoft-azure:
      link-copy: "Supported"
      link-url: "https://help.tableau.com/current/pro/desktop/en-us/examples_azure_sql_dw.htm"
    postgresql:
      link-copy: "Supported"
      link-url: "https://help.tableau.com/current/pro/desktop/en-us/examples_postgresql.htm"
    snowflake:
      link-copy: "Supported"
      link-url: "https://help.tableau.com/current/pro/desktop/en-us/examples_snowflake.htm"


# -------------------------- #
#          SQL TOOLS         #
# -------------------------- #

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


# -------------------------- #
#     DATA SCIENCE TOOLS     #
# -------------------------- #

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
  {{ supported | replace: "TOOLTIP", "This tool has a web app." }}
  {% when false %}
  {{ not-supported | replace: "TOOLTIP", "This tool doesn't have a web app."}}
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

  <img src="{{ site.baseurl }}/images/analysis-tools/analysis-tools-diagram.svg" alt="Using Stitch with analysis tools">

  Whether you want to create visual analyses or run SQL queries, Stitch is compatible with a broad range of tools - from business intelligence platforms to SQL editors to data science tools.

sections:
  - title: "Analytics tools"
    anchor: "analytics-tools"
    content: |
      Stitch consolidates your data for use in the best-in-class tools for business intelligence and visualization. These tools will enable you to take a deep-dive into your data and visualize the results.

      {% for subsection in section.subsections %}
      - [{{ subsection.summary }}](#{{ subsection.summary }})
      {% endfor %}

    subsections:
  ## If a tool has a `tutorial` property, it'll show in the list in this section.

      - title: "Tutorials"
        anchor: "tutorials"
        summary: "Stitch tutorials for setting up some popular tools"
        content: |
          On the Stitch blog, we walk you through how to use your Stitch data with each of the following tools:

          <ul class="tiles two-columns">
          {% assign tutorials = page.analytics | sort_natural:"name" %}
          {% for tool in tutorials %}
            {% if tool.tutorial %}
              <li>
                  <a href="{{ tool.url }}" target="new">
                      <img src="{{ site.baseurl }}/images/analysis-tools/{{ tool.name | slugify }}.svg" alt="{{ tool.name }}" style="height: 50px">
                  </a>
                  <strong>{{ tool.name }}</strong><br>
                  {% if tool.tutorial %}<a class="btn-primary" style="padding: 3px 10px; white-space: normal;" href="{{tool.tutorial}}" target="_blank" title="Using Stitch and {{tool.name}}">Using Stitch with {{tool.name}} →</a>{% endif %}
              </li>
            {% endif %}
          {% endfor %}
          </ul>

## If a tool doesn't have a `tutorial` property, it'll show in the list in this section.
      - title: "Additional analytics tools"
        anchor: "additional-analytics-tools"
        summary: "Additional analytics tools"
        content: |
          Stitch customers also enjoy these options:

          <ul class="tiles three-columns link-tiles">
          {% assign analytics = page.analytics | sort_natural:"name" %}

            {% for tool in analytics %}
              {% if tool.tutorial == nil %}
                <li>
                    <a href="{{ tool.url }}" target="new" style="padding: 0 20px 10px 20px;">
                        <img src="{{ site.baseurl }}/images/analysis-tools/{{ tool.name | slugify }}.svg" alt="{{ tool.name }}" style="height: 50px">
                        <strong>{{ tool.name }}</strong>
                    </a>
                </li>
              {% endif %}
            {% endfor %}
          </ul>

## If a tool is in the `compatibility-list` list, it'll show in the list in this section.
      - title: "Destination compatibility"
        anchor: "destination-compatibility"
        summary: "Compatibility with Stitch destinations"
        content: |
          When picking an analysis tool, you may want to investigate whether the tool supports a native connection to your Stitch destination. We've investigated some popular options for you:

          {% include analysis-tools/destination-compatibility.html %}

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