---
# -------------------------- #
#          PAGE INFO         #
# -------------------------- #

title: Security Overview
permalink: /security/overview
redirect_from: 
  - /security/frequently-asked-questions
  - /account-security/stitch-security
  - /account-security/security-faq
summary: "Stitch gives you the power to secure, analyze, and govern your data by centralizing it into your data infrastructure. Our most important job is to keep your data safe along the way."
keywords: security, secure, data access, credentials, security protocol, breach, encryption, encrypted, store data, retain data, vpn, ssl, hipaa, pci, connectivity, retain, retention

key: "security-faq"
type: "security"
content-type: "basics"
weight: 1

display-title: "All Security basics"

layout: general
toc: true
feedback: false

enterprise-utm:
  hipaa-url: "?utm_medium=docs&utm_campaign=hipaa-compliance"
  reverse-ssh-url: "?utm_medium=docs&utm_campaign=reverse-ssh"
  soc2-url: "?utm_medium=docs&utm_campaign=soc2-compliance"

# -------------------------- #
#           INTRO            #
# -------------------------- #

intro: |
  {{ page.summary }}


# -------------------------- #
#          CONTENT           #
# -------------------------- #

sections:
  - title: "Stitch's environment"
    anchor: "environment"
    content: |
      - Stitch’s servers are hosted in Amazon Web Services (AWS), which provides assurances for their physical and virtualized computing environments including SOC 1, 2, and 3, and ISO/IEC 27001. The servers used to process replicated data for your account will be located in the AWS region associated with your [Stitch data pipeline region]({{ link.security.supported-operating-regions | prepend: site.baseurl }}).
      - Stitch operates within an Amazon Virtual Private Cloud (VPC), with subnets segregated by security level, and firewalls configured to restrict network access.
      - Stitch regularly performs automated vulnerability scans and installs security updates and patches.
      - Stitch’s application and environment are protected by dedicated firewall services to prevent unauthorized access and regularly audited by third-party security professionals conducting specialized penetration tests.

  - title: "Data access policies"
    anchor: "stitch-access"
    content: |
      - Stitch strictly controls access to data and credentials and requires them to be encrypted using industry-standard methods both at rest and in transit within our [environment](#environment).
      - Stitch's secure infrastructure is a closed network protected by multi-factor authentication and accessible only to qualified members of our engineering team. On the rare occassion that a Stitch engineer needs to read or move data to investigate an issue, your data will never leave our infrastructure.

         Additionally, all members of the Stitch team - not just engineers - have signed non-disclosure agreements.
      - Stitch's data centers are protected by electronic security, intrusion detection systems, and a 24/7/365 human staff. 
      - Stitch monitors application, system, and data access logs within its production environment for anomalous behavior.
      - Stitch will never access data in your destination without your explicit permission. We'll ask every time this is required and notify you when it's happening.

  - title: "PII stored by Stitch"
    anchor: "stitch-pii-stored"
    content: |
        Stitch stores some PII (Personal Identifiable Information) related to your account. This PII is provided during signup and includes:
          - First and last name
          - Email address
          - Company name
          - Country and state
          - Phone number
          - Billing address
        
        The only PII that goes through Stitch is the data sent from your source. This data is not stored outside of our [retention window](#data-retention).
        Additionally, Stitch collects performance metrics, but these do not include any customer-provided information. Stitch also stores table names for functional reasons.



  - title: "Access control"
    anchor: "access-control"
    content: |
      {% for subsection in section.subsections %}
      - [{{ subsection.title }}](#{{ subsection.anchor }})
      {% endfor %}
      
    subsections:
      - title: "Stitch account access"
        anchor: "account-access"
        content: |
          Stitch supports Single Sign-On (SSO), which allows you to securely grant members of your team access to Stitch by internally managing their credentials. Stitch currently supports the following Identity Providers (IdP):

          {% assign supported-identity-providers = site.account-security | where:"idp",true | sort_natural:"display-name" %}

          {% for idp in supported-identity-providers %}
          - [{{ idp.display-name }}]({{ idp.url | prepend: site.baseurl }})
          {% endfor %}

          The SSO feature is available on all Stitch plans.

      - title: "Connectivity"
        anchor: "connectivity"
        content: |
          - **All plans** include [SSH tunnels]({{ link.security.encryption | prepend: site.baseurl | append: "#ssh-tunnel-connections" }}) and [IP whitelisting]({{ link.security.ip-addresses | prepend: site.baseurl }}) for integrations and destinations that support these features.
          - **For {{ site.data.stitch.subscription-plans.premium.name }} plans**, additional [advanced connectivity options]({{ link.security.encryption | prepend: site.baseurl | append: "#advanced-connectivity" }}) - such as VPNs, reverse SSH tunneling, and Amazon Web Services Private Link - may be available.

      - title: "Permissions for integrations and destinations"
        anchor: "permissions"
        content: |
          {% for sub-subsection in subsection.sub-subsections %}
          - [{{ sub-subsection.title }}](#{{ sub-subsection.anchor }})
          {% endfor %}

        sub-subsections:
          - title: "Integration permissions"
            anchor: "permissions--integrations"
            content: |
              Stitch’s integrations use the minimum permissions that allow read access to necessary data and can be configured by users to replicate only a subset of available data.

              However, the permissions Stitch requires to successfully pull your data will depend on the database or SaaS application's permission structure. In some cases, we only need read-only permissions to pull all the data required - in others, we need what amounts to full access.

              Regardless of the level of permissions we request for an integration, **we will only ever read your data.** Any permissions beyond the scope of read-only will not be used.

              To ensure Stitch remains visible in logs and audits, we recommend creating a dedicated Stitch user as a best practice.

          - title: "Destination permissions"
            anchor: "permissions--destinations"
            content: |
              Stitch's destinations use the minimum permissions that allow Stitch to successfully load data into your destination. In most cases, Stitch requires the ability to create schemas, tables, columns, and to read and insert data.

              The specific permissions Stitch requires are different for each destination. Refer to the documentation [for your destination]({{ link.destinations.main | prepend: site.baseurl }}) for more info.

## NOTE: Data in the table in this section lives here: _data/stitch/compliance.yml
  - title: "Compliance"
    anchor: "stitch-compliance"
    content: |
      {% include misc/icons.html %}

      The following table contains info about Stitch's level of compliance or certification with various security regulations and programs:

      - {{ supported | replace:"TOOLTIP","Fully certified/compliant" | strip }} - Indicates Stitch is fully compliant/certified
      - {{ sometimes-supported | replace:"TOOLTIP","May be compliant/certified, with caveats" | strip }} - Indicates Stitch may be compliant/certified, but with caveats
      - {{ not-supported | replace:"TOOLTIP","Not currently compliant/certified" | strip }} - Indicates Stitch isn't currently compliant/certified

      <table>
        <tr>
          <td align="right" width="15%; fixed">
            <strong>Type</strong>
          </td>
          <td width="14%; fixed">
            <strong>Compliant/<br>Certified</strong>
          </td>
          <td width="20%; fixed">
            <strong>Stitch plan</strong>
          </td>
          <td>
            <strong>Notes</strong>
          </td>
        </tr>
      {% for compliance in site.data.stitch.compliance %}
        <tr>
          <td align="right">
            <strong>{{ compliance.name }}</strong>
          </td>
          <td>
            {% case compliance.level %}
              {% when 'none' %}
                {% assign full-tooltip = "Not currently " | append: compliance.name | append: " compliant/certified" %}
                {{ not-supported | replace:"TOOLTIP",full-tooltip | strip }}
              {% when 'some' %}
                {% assign full-tooltip = "May be " | append: compliance.name | append: " compliant/certified, with caveats" %}
                {{ sometimes-supported | replace:"TOOLTIP",full-tooltip | strip }}
              {% when 'full' %}
                {% assign full-tooltip = "Fully " | append: compliance.name | append: " compliant/certified" %}
                {{ supported | replace:"TOOLTIP",full-tooltip | strip }}
            {% endcase %}
          </td>
          <td>
            {% if compliance.level == "none" %}
              Not applicable
            {% else %}
              {{ compliance.tier | capitalize | append: " plans" }}
            {% endif %}
          </td>
          <td>
            {{ compliance.description | flatify | markdownify }}
          </td>
        </tr>
      {% endfor %}
      </table>

  - title: "Data encryption"
    anchor: "stitch-encryption"
    content: |
      - Stitch's web application enforces SSL to ensure communication remains secure.
      - All credentials used to access other systems (i.e., your database or a SaaS integration) are encrypted before Stitch stores them.
      - Data is always encrypted [in transit]({{ link.security.encryption | prepend: site.baseurl | append: "#in-transit-encryption" }}) and at rest within the Stitch environment. At rest, Stitch uses [AES-256](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard){:target="new"} to encrypt data.
      - Stitch offers several secure options for creating connections to integrations and destinations:

         - **All plans** include [SSL/TLS]({{ link.security.encryption | prepend: site.baseurl | append: "#ssl-connections" }}), [SSH tunnels]({{ link.security.encryption | prepend: site.baseurl | append: "#ssh-tunnel-connections" }}), and [IP whitelisting]({{ link.security.ip-addresses | prepend: site.baseurl }}) for integrations and destinations that support these features.
         - **For {{ site.data.stitch.subscription-plans.premium.name }} plans**, additional [advanced connectivity options]({{ link.security.encryption | prepend: site.baseurl | append: "#advanced-connectivity" }}) - such as VPNs, reverse SSH tunneling, and Amazon Web Services Private Link - may be available.
      
      Refer to the [Data encryption guide]({{ link.security.encryption | prepend: site.baseurl }}) for more info.

  - title: "Data processing and retention"
    anchor: "stitch-data-processing-retention"
    content: |
      {% for subsection in section.subsections %}
      - [{{ subsection.title }}](#{{ subsection.anchor }})
      {% endfor %}
    subsections:
      - title: "Data processing"
        anchor: "data-processing"
        content: |
          The **Data pipeline region** setting, defined when you create a Stitch account, controls the region where Stitch-hosted data centers process replicated data.

          **Note**: The **Data pipeline region** setting only affects the replication of data in your Stitch account, specifically extracting, preparing, and loading data into your destination. All other processes and data, such as billing, reporting, and other metadata, are not affected by your account's data pipeline region. Data and metadata related to these processes will be processed using Stitch's `north-america` region.

          Refer to the [Supported Data Pipeline Regions documentation]({{ link.security.supported-operating-regions | prepend: site.baseurl }}) for more info.

      - title: "Data retention"
        anchor: "data-retention"
        pipeline:
          - step-name: "The Pipeline"
            maximum-retention-period: "7 days"
            description: |
              Stitch uses Apache Kafka and Amazon S3 systems spanning multiple data centers to durably buffer the data received by the Import API. Data is always encrypted at rest, and automatically deleted from the buffer before the maximum retention period for this step.

          - step-name: "The Streamery"
            maximum-retention-period: "30 days"
            description: |
              The Streamery reads data from the Pipeline and separates, batches, and prepares it for loading. Prepared data is encrypted, separated by tenant (Stitch account) and data set, and written to Amazon S3 to be loaded.

                Most data is loaded within minutes, but if a destination is unavailable, it can stay in S3 for up to 30 days before being automatically deleted.
        content: |
          To ensure we meet our most important service-level target - don't lose data - replicated data may be retained in Stitch's system for a short period of time. Stitch automatically deletes data when it is no longer needed for replication. 

          During the [**Preparing** phase of the replication process]({{ link.getting-started.basic-concepts | prepend: site.baseurl | append: "#system-architecture--preparing" }}), Stitch buffers extracted data in its internal data pipeline and readies it for loading. This phase consists of the following steps:

          {% assign attributes = "step-name|maximum-retention-period|description" | split: "|" %}

          <table>
            <tr>
              {% for attribute in attributes %}
                {% if forloop.index == 1 %}
                  <td align="right" width="20%; fixed">
                {% elsif forloop.index == 2 %}
                  <td width="25%; fixed">
                {% else %}
                  <td>
                {% endif %}
                  <strong>
                    {{ attribute | replace:"-"," " | capitalize }}
                  </strong>
                </td>
              {% endfor %}
            </tr>
            {% for step in subsection.pipeline %}
              <tr>
              {% for attribute in attributes %}
                {% if forloop.first == true %}
                  <td align="right">
                    <strong>
                      {{ step[attribute] | markdownify }}
                    </strong>
                {% else %}
                  <td>
                    {{ step[attribute] | markdownify }}
                {% endif %}
                </td>
              {% endfor %}
              </tr>
            {% endfor %}
          </table>

          To summarize, all data that Stitch processes for customers will be deleted from our systems within 30 days.

  - title: "Protocols and recommendations"
    anchor: "stitch-protocols-recommendations"
    content: |
      - **Create a dedicated user for Stitch whenever possible.** This applies to any integration or destination. Refer to the [Permissions for integrations and destinations section](#permissions) for more info.
      - **For database connections**, utilize Stitch's built-in support for SSH and SSL/TLS connections to encrypt data in transit. Refer to the [Data encryption guide]({{ link.security.encryption | prepend: site.baseurl }}) for more info.
      - **For SaaS data**, keep any credentials or sensitive information such as passwords, API keys or tokens, etc. secure.
      - **If your database(s) or SaaS account(s) have been hacked**, we recommend that you:

           1. Immediately recycle any credentials used to access your system or service,
           2. Generate new credentials, and
           3. Update the credentials for the appropriate integration(s) in Stitch.

        Our team can help you remediate any data issues that might have occurred as a result of the breach.

  - title: "Issue reporting and handling"
    anchor: "security-issues"
    content: |
      If our team verifies a security vulnerability in our system, our first priority is to prevent its exploitation. After it’s contained, we do a thorough analysis to determine the scope of impact and notify affected users within 24 hours.

      If you believe you’ve found a security vulnerability in Stitch, we encourage you to let us know right away by emailing [security@stitchdata.com](mailto: security@stitchdata.com). We request that you do not publicly disclose the issue until we have a chance to address it. We won’t pursue legal action as long as you make a good-faith effort to avoid privacy violations and destructive exploitation of the vulnerability.
      
      We will respond as quickly as we can and reward the confidential and non-destructive disclosure of any design or implementation issue that could be used to compromise the confidentiality or integrity of our users' data (such as bypassing our login process, injecting code into another user's session, or acting on another user's behalf) with some swag. Other issues may be rewarded at our discretion.
---
{% include misc/data-files.html %}