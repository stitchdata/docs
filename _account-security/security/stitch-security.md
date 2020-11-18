---
# -------------------------- #
#          PAGE INFO         #
# -------------------------- #

title: Security FAQ
permalink: /security/frequently-asked-questions
redirect_from: 
  - /account-security/stitch-security
  - /account-security/security-faq
summary: "We take securing your data seriously. Here's what we do to ensure that your private data stays private and our recommended best practices for protecting your data."
keywords: security, secure, data access, credentials, security protocol, breach, encryption, encrypted, store data, retain data, vpn, ssl, hipaa, pci

key: "security-faq"
type: "security"
content-type: "basics"
weight: 1

layout: general
toc: true

enterprise: true
enterprise-cta:
  feature: "HIPAA and SOC2 compliance "
  title: "{{ site.data.strings.enterprise.title.multiple | prepend: page.enterprise-cta.feature }}"

enterprise-utm:
  hipaa-url: "?utm_medium=docs&utm_campaign=hipaa-compliance"
  reverse-ssh-url: "?utm_medium=docs&utm_campaign=reverse-ssh"
  soc2-url: "?utm_medium=docs&utm_campaign=soc2-compliance"


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
      - Stitch’s application and environment is regularly audited by third-party security professionals conducting specialized penetration tests.

  - title: "Data access policies"
    anchor: "stitch-access"
    content: |
      - Stitch strictly controls access to data and credentials and requires them to be encrypted using industry-standard methods both at rest and in transit within our [environment](#environment).
      - Stitch's secure infrastructure is a closed network protected by multi-factor authentication and accessible only to qualified members of our engineering team. On the rare occassion that a Stitch engineer needs to read or move data in our infrastrucutre to investigate an issue, your data will never leave our infrastructure.

         Additionally, all members of the Stitch team - not just engineers - have signed non-disclosure agreements.
      - Stitch monitors application, system, and data access logs within its production environment for anomalous behavior.
      - Stitch will never access data in your destination without your explicit permission. We'll ask every time this is required and notify you when it's happening.

  - title: "Permissions for integrations and destinations"
    anchor: "permissions"
    content: |
      {% for subsection in section.subsections %}
      - [{{ subsection.title }}](#{{ subsection.anchor }})
      {% endfor %}

    subsections:
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

  - title: "Data processing"
    anchor: "stitch-data-processing"
    items:
      - question: "Can Stitch process data outside of the United States?"
        anchor: "data-processing-outside-us"
        answer: |
          Yes. The **Data pipeline region** setting, defined when you create a Stitch account, controls the region where Stitch-hosted data centers process replicated data.

          Refer to the [Supported Data Pipeline Regions documentation]({{ link.security.supported-operating-regions | prepend: site.baseurl }}) for more info.

      - question: "What types of data are affected by the data pipeline region setting?"
        anchor: "data-types-data-pipeline-region"
        answer: |
          {% assign north-america-region = site.data.stitch.regions | where:"id","north-america" | first %}

          The **Data pipeline region** setting only affects the replication of data in your Stitch account, specifically extracting, preparing, and loading data into your destination.

          All other processes and data, such as billing, reporting, and other metadata, are not affected by your account's data pipeline region. Data and metadata related to these processes will be processed using Stitch's `{{ north-america-region.name }}` region.

          Refer to the [Supported Data Pipeline Regions documentation]({{ link.security.supported-operating-regions | prepend: site.baseurl }}) for more info.

  - title: "Data encryption"
    anchor: "stitch-encryption"
    items:
      - question: "How are credentials handled after they're entered into Stitch?"
        anchor: "credential-handling"
        answer: |
          All credentials used to access other systems (i.e., your database or a SaaS integration) are encrypted before we store them.

      - question: "Is my data encrypted in transit? Is it encrypted at rest?"
        anchor: "is-data-encrypted-transit"
        answer: |
          Your data is always encrypted in transit and at rest within the Stitch environment. We offer several ways to get data into Stitch using encryption. Refer to the [Data encryption guide]({{ link.security.encryption | prepend: site.baseurl }}) for more info.

      - question: "Are SSL connections supported?"
        anchor: "ssl-connection-support"
        answer: |
          SSL connections are available on all plans for the majority of integrations and destinations. Refer to the [Data encryption guide]({{ link.security.encryption | prepend: site.baseurl | append: "#ssl-connections" }}) for more info. 

      - question: "Are SSH tunnel connections supported?"
        anchor: "ssh-connection-support"
        answer: |
          SSH connections are available on all plans for the majority of database integrations and some destinations. Refer to the [Data encryption guide]({{ link.security.encryption | prepend: site.baseurl | append: "#ssh-tunnel-connections" }}) for more info.

      - question: "Are VPN or reverse SSH tunnel connections supported?"
        anchor: "vpn-connection-support"
        answer: |
          Additional connection options such as VPNs or reverse SSH tunnels may be implemented as part of an Enterprise plan. Contact [Stitch Sales]({{ site.sales | append: page.enterprise-utm.reverse-ssh-url }}) for more info.

          Refer to the [Advanced connectivity section]({{ link.security.encryption | prepend: site.baseurl | append: "#advanced-connectivity" }}) in the Data encryption guide for more info.

  - title: "Protocols and recommendations"
    anchor: "stitch-protocols-recommendations"
    items:
      - question: "What security protocols does Stitch have in place?"
        anchor: "stitch-security-protocols"
        answer: |
          - Our data centers are protected by electronic security, intrusion detection systems, and a 24/7/365 human staff. 
          - Our operating systems and other software are kept up to date with the latest security patches. 
          - Our network is protected by dedicated firewall services to prevent unauthorized access, and our systems regularly undergo automated vulnerability scans.

          Those are just our internal measures. We also take great care to ensure your data is secure as it makes its way through Stitch and into your data warehouse.

      - question: "Does Stitch undergo any security audits?"
        anchor: "stitch-security-audits"
        answer: |
          New features undergo a security review by our team before release. In addition, security professionals conduct regular audits and penetration tests on our existing systems.

      - question: "What are Stitch's recommendations for keeping my data secure?"
        anchor: "stitch-recommendations-data-secure"
        answer: |
          For your database data, we recommend using our SSH and SSL features to ensure your data stays secure and encrypted in transit. Additionally, we encourage you to require strong passwords for database users.

          For your SaaS data, we recommend that you keep your API keys private and don’t share your login credentials - for Stitch or any other service - with anyone.

  - title: "Issue reporting and handling"
    anchor: "security-issues"
    items:
      - question: "What's Stitch's policy on informing customers about security breaches?"
        anchor: "stitch-policy-inform-customers"
        answer: |
          If our team verifies a security vulnerability in our system, our first priority is to prevent its exploitation. After it’s contained, we do a thorough analysis to determine the scope of impact and notify affected users within 24 hours.

      - question: "How do I report a security issue?"
        anchor: "report-security-issue"
        answer: |
          If you believe you’ve found a security vulnerability in Stitch, we encourage you to let us know right away by emailing [security@stitchdata.com](mailto: security@stitchdata.com). We request that you do not publicly disclose the issue until we have a chance to address it. We won’t pursue legal action as long as you make a good-faith effort to avoid privacy violations and destructive exploitation of the vulnerability.

          We will respond as quickly as we can and reward the confidential and non-destructive disclosure of any design or implementation issue that could be used to compromise the confidentiality or integrity of our users' data (such as bypassing our login process, injecting code into another user's session, or acting on another user's behalf) with some swag. Other issues may be rewarded at our discretion.

      - question: "What should I do if one of my data sources is hacked?"
        anchor: "help-i-was-hacked"
        answer: |
          If your database(s) or SaaS account(s) have been hacked, we recommend that you:

            1. Immediately recycle any credentials used to access your system or service,
            2. Generate new credentials, and
            3. Update the credentials for the appropriate integration(s) in Stitch.

          Our team can help you remediate any data issues that might have occurred as a result of the breach.



frequently-asked-questions:
  
  
  
---
{% include misc/data-files.html %}

{{ page.summary }}
