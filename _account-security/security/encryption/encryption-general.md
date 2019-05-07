---
# -------------------------- #
#      Page & Formatting     #
# -------------------------- #

title: Data Encryption
permalink: /account-security/data-encryption
summary: "Stitch offers secure options for making connections to all data sources and destinations, giving you the power to secure your data as you see fit."

input: false
layout: general
feedback: false

# -------------------------- #
#        Introduction        #
# -------------------------- #

intro: |
  {% capture security-faq %}
  **Looking for general security info?** Check out the [Security FAQ]({{ link.security.faq | prepend: site.baseurl }}).
  {% endcapture %}

  {% include note.html type="single-line" content=security-faq %}

  Our most important job here at Stitch is to keep your data safe. To do that, Stitch always encrypts data in transit and at rest within the Stitch environment.

  {{ page.summary }}

  In this guide, we'll cover Stitch's supported connection options and provide links to additional resources.

# -------------------------- #
#           Content          #
# -------------------------- #


ssh-tunnels:
  - name: "Self-hosted"
    guide: "ssh-generic"
    description: "If your database is hosted on your server and not in the cloud, it's considered a 'self-hosted' database. This is applicable to both integrations and destinations."

  - name: "Amazon"
    guide: "ssh-amazon"
    description: "Stitch currently supports connecting Amazon RDS and Amazon Redshift (destination only) databases."

  - name: "Microsoft Azure"
    guide: "ssh-microsoft-azure"
    description: "Stitch currently supports connecting Microsoft Azure SQL Server (as an integration) and Azure SQL Data Warehouse (as a destination). Other Microsoft Azure offerings aren't currently supported."

sections:
  - title: "SSL connections"
    anchor: "ssl-connections"
    content: |
      [SSL/TLS](https://www.verisign.com/en_US/website-presence/online/ssl-certificates/index.xhtml){:target="new"} is a standard security technology used to establish encrypted communication between a web server and a browser. SSL/TLS ensures that communication to and from Stitch remains private and secure.

    subsections:
      - title: "Stitch application access"
        anchor: "stitch-application"
        content: |
          The Stitch application enforces SSL to ensure all communication with Stitch remains secure.

      - title: "Connections that use verified SSL by default"
        anchor: "connections-ssl-default"
        content: |
          For any connection using an HTTP API - for example, integrations like [Salesforce]({{ site.baseurl }}/integrations/saas/salesforce) or [Facebook Ads]({{ site.baseurl }}/integrations/saas/facebook-ads) - or Stitch's [Import API]({{ link.integrations.import-api | prepend: site.baseurl }}), Stitch will use [SSL/TLS-based encryption](https://www.verisign.com/en_US/website-presence/online/ssl-certificates/index.xhtml){:target="new"} by default.

          This is also applicable to Stitch's [Amazon Redshift]({{ link.destinations.overviews.redshift | prepend: site.baseurl }}), [Google BigQuery]({{ link.destinations.overviews.bigquery | prepend: site.baseurl }}), [Microsoft Azure SQL Data Warehouse]({{ link.destinations.overviews.azure | prepend: site.baseurl }}), and [Snowflake]({{ link.destinations.overviews.snowflake | prepend: site.baseurl }}) destination offerings.

          Connections to these integrations and destinations will attempt to use verified SSL with no action required on your part.

      - title: "Connections with configurable SSL options"
        anchor: "connections-configurable-ssl"
        content: |
          For some integrations - for example, a database hosted on your server - Stitch may support configurable SSL. To use SSL with a database Stitch supports, the database must be configured to support and allow SSL connections.

          **Note**: SSL connections are not supported for all databases. Refer to the [documentation for the database]({{ site.baseurl }}/integrations/databases) for SSL support details.

  - title: "SSH tunnels"
    anchor: "ssh-tunnel-connections"
    content: |
      If a database you want to connect to Stitch doesn't support [SSL connections](#ssl-connections) or isn't publicly accessible, you can use an SSH tunnel.

      The steps for setting up an SSH connection vary depending on where your database is hosted.

      <table class="attribute-list">
      {% for item in page.ssh-tunnels %}
      <tr>
      <td class="attribute-name">
      <strong>{{ item.name | append: " databases" }}</strong>
      </td>
      <td>
      {{ item.description | markdownify }}

      <p>Refer to the <a href="{{ link.security[item.guide] | prepend: site.baseurl }}">SSH tunnels for {{ item.name | append: " databases"}}</a> guide.</p>
      </td>
      </tr>
      {% endfor %}
      </table> 

  - title: "Advanced connectivity"
    anchor: "advanced-connectivity"
    content: |
      Additional connection options are available as part of a Stitch Enterprise plan. This includes:

      - Virtual Private Network (VPN)
      - Reverse SSH tunneling
      - [Amazon Web Services (AWS) Private Link](https://aws.amazon.com/privatelink/){:target="new"}

      Reach out to [Stitch Sales]({{ site.sales }}){:target="new"} for more info.
---