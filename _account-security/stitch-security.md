---
title: Security FAQ
permalink: /account-security/stitch-security
keywords: security, secure, data access, credentials, security protocol, breach, encryption, encrypted, store data, retain data, vpn, ssl
tags: [getting_started, account, security]

summary: "We take securing your data seriously. Here's what we do to ensure that your private data stays private and our recommended best practices for protecting your data."
type: "security"
toc: true
layout: faq
weight: 5

frequently-asked-questions:
  - topic: "Compliance"
    anchor: "stitch-compliance"
    items:
      - question: "Is Stitch PCI or HIPAA compliant?"
        anchor: "pci-hipaa-compliant"
        answer: |
          All payment information submitted through Stitch's billing interface to pay for your subscription is handled in a PCI-compliant manner.
          
          If you'd like to know how Stitch can replicate data that is subject to compliance requirements like HIPAA or PCI, reach out to our [support team](mailto: {{ site.support }}) and tell us more about your needs.

      - question: "Does Stitch comply with any EU privacy laws?"
        anchor: "eu-privacy-compliance"
        answer: |
          Stitch is certified under the [US-EU and US-SWISS Privacy Shield Programs](https://www.privacyshield.gov/participant?id=a2zt0000000GnxUAAS&status=Active){:target="new"}, meaning any EU or Swiss data transfer will be handled in accordance with the principles laid out in the Privacy Shield Framework.

          For more information on Privacy Shield, check out the link above or [this FAQ on the program](https://www.privacyshield.gov/Program-Overview){:target="new"}.
  
  - topic: "Encryption"
    anchor: "stitch-encryption"
    items:
      - question: "How are credentials handled after they're entered into Stitch?"
        anchor: "credential-handling"
        answer: |
          All credentials used to access other systems (i.e., your database or a SaaS integration) are encrypted before we store them.

      - question: "Is my data encrypted in transit?"
        anchor: "is-data-encrypted-transit"
        answer: |
          We offer several ways to get data into Stitch using encryption:

          - **For data pulled from an API or submitted directly to Stitch's Import API,** we'll use SSL-based encryption.
          
          - **For data replicated from a database**, we can use the encryption functionality built into the database. 

          - **For databases that don't support encryption**, or if encryption isn't activated, we can transport the data through an SSH tunnel. After we receive your data, it won't leave our network without being encrypted.

      - question: "Are SSL connections supported?"
        anchor: "ssl-connection-support"
        answer: |
          {% assign ssl-databases = site.database-integrations | where: "ssl",true | sort:"display_name" %}

          Yes. SSL connections are currently supported for:

          - **Database (input) integrations**
            {% for database in ssl-databases %}
             - [{{ database.display_name }}]({{ database.url | prepend: site.baseurl }})
            {% endfor %}
          - **Destinations (data warehouses)**
            - Heroku-Postgres

          Any database connected to Stitch using SSL must have SSL support turned on. To use SSL, just click the **Connect using SSL checkbox** underneath the **Encryption Type** menu in any of the credential pages of the databases listed above.

          For Heroku-specific instructions regarding SSL, we recommend [checking out their documentation](https://devcenter.heroku.com/articles/connecting-to-relational-databases-on-heroku-with-java#connecting-to-a-database-remotely"){:target="new"}.

          You can also dive into the [PostgreSQL SSL docs](https://jdbc.postgresql.org/documentation/head/ssl.html){:target="new"} to learn more.

      - question: "Are VPN connections supported?"
        anchor: "vpn-connection-support"
        answer: |
          Not currently. If you're interested in adding support for VPN connections, [contact our support team](mailto: {{ site.support }}) with your use case. We're always interested in exploring the possibility of the features our customers want, so don't hesitate.

  - topic: "Data Access"
    anchor: "stitch-access"
    items:
      - question: "What are Stitch's policies regarding access to my data?"
        anchor: "stitch-policies-data-access"
        answer: |
          Before your data is loaded into your data warehouse, it passes through Stitch's secure infrastructure. This is a closed network protected by multi-factor authentication and accessible only to qualified members of our engineering team. On rare occasions, our engineers may need to read or move the data while it is in our infrastructure to debug or resolve an operational issue.

          When this happens, your data will never leave our infrastructure. All members of our team - not just our engineers - have signed non-disclosure agreements. We're committed to ensuring your data remains private.

          **As for your data warehouse, we will never access it without your explicit permission.** We’ll ask every time it’s required to troubleshoot an issue and we’ll be sure to notify you when we’re doing it. No one likes surprises, least of all when it comes to their private data.

      - question: "Why is full access required for some SaaS integrations?"
        anchor: "full-access-saas-integrations"
        answer: |
          The access we need to successfully pull your data from a SaaS integration depends entirely on the vendor's API and permission structure. In some cases, we only need read-only access to pull all the data required - in others, we need what amounts to full access.

          Regardless of the level of permissions we need for an integration, we will only ever read your data.

  - topic: "Protocols & Recommendations"
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
          New features undergo a security review by our team before release. In additiona, security professionals conduct regular audits and penetration tests on our existing systems.

      - question: "What are Stitch's recommendations for keeping my data secure?"
        anchor: "stitch-recommendations-data-secure"
        answer: |
          For your database data, we recommend using our SSH and SSL features to ensure your data stays secure and encrypted in transit. Additionally, we encourage you to require strong passwords for database users.

          For your SaaS data, we recommend that you keep your API keys private and don’t share your login credentials - for Stitch or any other service - with anyone.
  - topic: "Security Issues"
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
---
{% include misc/data-files.html %}

{{ page.summary }}
