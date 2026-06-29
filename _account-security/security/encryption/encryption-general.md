---
# -------------------------- #
#      Page & Formatting     #
# -------------------------- #

title: Data Encryption
permalink: /security/data-encryption
redirect_from: /account-security/data-encryption
summary: "Stitch offers secure options for making connections to all data sources and destinations, giving you the power to secure your data as you see fit."

key: "data-encryption-overview"
type: "security"
content-type: "encryption"
weight: 2

input: false
layout: general
feedback: false


# -------------------------- #
#  Stitch Plan Requirements  #
# -------------------------- #

minimum-plan: "premium"
minimum-plan-cta:
  title: "Advanced connectivity for {{ site.data.stitch.subscription-plans.premium.name }} plans"
  copy: |
    [Additional connection options](#advanced-connectivity) are available as part of an {{ site.data.stitch.subscription-plans.advanced.name }} or {{ site.data.stitch.subscription-plans.premium.name }} plan.


# -------------------------- #
#        Introduction        #
# -------------------------- #

intro: |
  {% capture security-faq %}
  **Looking for general security info?** Check out the [Security overview]({{ link.security.faq | prepend: site.baseurl }}).
  {% endcapture %}

  {% include note.html type="single-line" content=security-faq %}

  Our most important job here at Stitch is to keep your data safe. To do that, Stitch always encrypts data in transit and at rest within the Stitch environment.

  {{ page.summary }}

  In this guide, we'll cover Stitch's supported connection options and provide links to additional resources:

  {% for section in page.sections %}
  - [{{ section.title }}](#{{ section.anchor }})
  {% endfor %}


# -------------------------- #
#           Content          #
# -------------------------- #

ssh-tunnels:
  - name: "Self-hosted"
    guide: "ssh-generic"
    description: "If your database is hosted on your server and not in the cloud, it's considered a 'self-hosted' database. This is applicable to both integrations and destinations."

  - name: "Amazon"
    guide: "ssh-amazon"
    description: "Stitch currently supports connecting Amazon RDS (including Aurora) and Amazon Redshift (destination only) databases."

  - name: "Microsoft Azure"
    guide: "ssh-microsoft-azure"
    description: "Stitch currently supports connecting Microsoft Azure SQL Server and MySQL databases (as integrations) and Azure Synapse Analytics (as a destination). Other Microsoft Azure offerings aren't currently supported."

sections:
  - title: "Encryption in transit"
    anchor: "in-transit-encryption"
    content: |
      {% for subsection in section.subsections %}
      - [{{ subsection.title }}](#{{ subsection.anchor }})
      {% endfor %}
    subsections:
      - title: "SSL connections"
        anchor: "ssl-connections"
        content: |
          [SSL/TLS](https://www.verisign.com/en_US/website-presence/online/ssl-certificates/index.xhtml){:target="new"} is a standard security technology used to establish encrypted communication between a web server and a browser. SSL/TLS ensures that communication to and from Stitch remains private and secure.

          {% for sub-subsection in subsection.sub-subsections %}
          - [{{ sub-subsection.title }}](#{{ sub-subsection.anchor }})
          {% endfor %}

        sub-subsections:
          - title: "Stitch application access"
            anchor: "stitch-application"
            content: |
              The Stitch application enforces SSL to ensure all communication with Stitch remains secure.

          - title: "Connections that use verified SSL by default"
            anchor: "connections-ssl-default"
            content: |
              For any connection using an HTTP API - for example, integrations like [Salesforce]({{ site.baseurl }}/integrations/saas/salesforce) or [Facebook Ads]({{ site.baseurl }}/integrations/saas/facebook-ads) - or Stitch's [Import API]({{ link.integrations.import-api | prepend: site.baseurl }}), Stitch will use [SSL/TLS-based encryption](https://www.verisign.com/en_US/website-presence/online/ssl-certificates/index.xhtml){:target="new"} by default.

              This is also applicable to Stitch's [Amazon Redshift]({{ link.destinations.overviews.redshift | prepend: site.baseurl }}), [Google BigQuery]({{ link.destinations.overviews.bigquery | prepend: site.baseurl }}), [Microsoft Azure Synapse Analytics]({{ link.destinations.overviews.azure | prepend: site.baseurl }}), and [Snowflake]({{ link.destinations.overviews.snowflake | prepend: site.baseurl }}) destination offerings.

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

          **Note**: [Reverse SSH tunnels]({{ link.security.reverse-ssh | prepend: site.baseurl }}) are also available for {{ site.data.stitch.subscription-plans.premium.name }} customers.

      - title: "Advanced connectivity"
        anchor: "advanced-connectivity"
        content: |
          {{ site.data.stitch.subscription-plans.premium.name }} plans include additional connection options to help you securely connect Stitch to your data sources or destinations. These options are useful when your infrastructure uses network isolation, IP restrictions, or other security controls that prevent direct connections.

          **Limitation:** Advanced connectivity options are not available for Snowflake and BigQuery destinations.

          #### General requirements

          To set up any advanced connectivity option, you will need to provide:

          - Client ID and company name
          - Region of your Stitch account AND the region where your database or warehouse resides
          - [Stitch SSH key]({{ link.security.encryption | prepend: site.baseurl | append: "#stitch-application" }})

          #### Reverse SSH tunneling

          [Reverse SSH tunneling]({{ link.security.reverse-ssh | prepend: site.baseurl }}) secures connections by allowing your server to initiate a connection to Stitch, rather than Stitch connecting directly to your server. Use this option when your infrastructure does not allow inbound connections or when you prefer to control the direction of connection initiation.

          **Requirements:**
          - CIDR (IP address range) of the public IP address(es) that your server will connect from
          - SSH public key that your server will use to establish the connection
          - (Optional) SSH login name in lowercase

          #### VPC Peering

          VPC Peering creates a direct, private connection between your Amazon Virtual Private Cloud (VPC) and Stitch's VPC. Use this option when your data sources or destinations are deployed in AWS and you want to avoid routing traffic over the public internet.

          **Requirements:**
          - Your AWS VPC ID (example: vpc-0441e28e3b5461e62)
          - CIDR blocks on your network (example: 10.1.2.0/28, 10.2.2.0/28)
          - Your AWS account ID (example: 253441582756)
          - The AWS region where your VPC resides

          **Note:** Peering can be established to any AWS Region or Availability Zone, but data will flow through Stitch's network in the region associated with your Stitch account (either us-east-1 or eu-central-1).

          #### Site-to-site VPN

          Site-to-site VPN creates a secure, encrypted connection between your network and Stitch's network using industry-standard VPN protocols. Use this option when you want to establish a VPN tunnel between your on-premises or cloud-hosted infrastructure and Stitch.

          **Requirements:**
          - CIDR blocks on your network (example: 10.1.2.0/28, 10.2.2.0/28)
          - VPN IP address to connect to
          - BGP ASN number (defaults to 65400 if not specified)
          - (Optional) Pre-shared key to establish the VPN connection (if not provided, one can be generated)
          - (Optional) Custom tunnel options for IKE version, encryption algorithms, integrity algorithms, and tunnel CIDR. Refer to the [AWS VPN documentation](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_VpnTunnelOptionsSpecification.html){:target="new"} for supported options.

          #### Amazon Web Services (AWS) PrivateLink

          [AWS PrivateLink](https://aws.amazon.com/privatelink/){:target="new"} enables secure, private connections between Stitch and your AWS infrastructure without traversing the public internet. Use this option when your data sources or destinations are deployed in AWS VPCs in the same region as your Stitch account.

          **Requirements:**
          - You must first set up the VPC endpoint on your AWS account following the [AWS PrivateLink setup guide](https://docs.aws.amazon.com/vpc/latest/privatelink/privatelink-share-your-services.html){:target="new"}
          - CIDR block(s) on your network (example: 10.1.2.0/28, 10.2.2.0/28)
          - Service name for the VPC endpoint (example: com.amazonaws.vpce.us-east-1.vpce-svc-0626d1982ea6ca5a7)

          **Important:** PrivateLink connections are only available within the AWS regions where Stitch operates (us-east-1 and eu-central-1). Cross-region connections are not currently supported.

          #### Next steps
          If you need help with setup, reach out to [the Support]({{ site.support }}){:target="new"}.

          Reach out to [Stitch Sales]({{ site.sales }}){:target="new"} to discuss which advanced connectivity option best fits your security and infrastructure requirements. Be prepared to provide the requirements listed above for your chosen option.

  - title: "Encryption at rest"
    anchor: "data-at-rest"
    content: |
      For data at rest, Stitch uses [AES-256](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard){:target="new"} to encrypt data.
---