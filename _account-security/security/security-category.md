---
# -------------------------- #
#          PAGE INFO         #
# -------------------------- #

title: Security
permalink: /security
keywords: billing, plan, change plan, cancel, cancel account, delete, remove
summary: "Stitch gives you the power to secure, analyze, and govern your data by centralizing it into your data infrastructure. Use these resources to learn how we keep your data safe along the way."
feedback: false

key: "security"
content-type: "category-page"

layout: general
feedback: false
toc: false


# -------------------------- #
#       HOME PAGE DATA       #
# -------------------------- #

## Used to display info on the home page as a category tile

level: "category"

icon: "lock"
display-title: "Security"
display-summary: "Learn about Stitch's security practices and how to keep your account secure."
weight: 3


# -------------------------- #
#           INTRO            #
# -------------------------- #

intro: |
  {% assign this-collection = site.account-security | where:"type","security" %}

  {{ page.summary }}

  {% for section in page.sections %}
  - [{{ section.title }}](#{{ section.anchor }})
  {% endfor %}

sections:
  - title: "Security basics"
    anchor: "security-basics-category"
    type: "basics"
    additional-guides:
      - title: "All Security basics"
        url: "{{ link.security.faq }}"
    content: |
      Familiarize yourself with Stitch's security practices and features with these resources.

      {% assign parent-category = this-collection | where:"key","security-faq" | first %}
      {% assign guides = parent-category.sections %}

      {% include layout/category-section-tiles.html subsection=true %}

  - title: "Data processing"
    anchor: "data-processing-category"
    type: "data-processing"
    additional-guides:
      - title: "Regional data processing with data pipeline regions"
        url: "{{ link.security.supported-operating-regions }}"

      - title: "Compliance and certifications"
        url: "{{ link.security.faq }}#stitch-compliance"

      - title: "Data retention periods"
        url: "{{ link.security.faq }}#data-retention"   
    content: |
      Subject to specific data regulations? Concerned about data security? Use these resources to learn about Stitch's compliance and certification with various data processing regulations and security programs.

      {% assign guides = section.additional-guides %}

      {% include layout/category-section-tiles.html %}

  - title: "Access control"
    anchor: "access-control-category"
    type: ""
    additional-guides:
      - title: "Configuring SSH tunnels"
        url: "{{ page.url }}#data-encryption--ssh"

      - title: "Advanced connectivity"
        url: "{{ link.security.encryption }}#advanced-connectivity"

      - title: "IP whitelisting"
        url: "{{ link.security.ip-addresses }}"
    content: |
      Learn about the options Stitch provides for securing access to your integrations and destinations with these guides.

      {% assign guides = section.additional-guides  %}

      {% include layout/category-section-tiles.html %}

  - title: "Data encryption"
    anchor: "data-encryption-category"
    type: "encryption"
    content: |
      Along with securing access to your connections, Stitch supports several options for encrypting your data. Check out these guides to learn more about ensuring your data pipeline is secure from source to destination.

      {% for subsection in section.subsections %}
      - [{{ subsection.title }}](#{{ subsection.anchor }})
      {% endfor %}
    subsections:
      - title: "General"
        anchor: "data-encryption--general"
        additional-guides:
          - title: "SSL connections"
            url: "{{ link.security.encryption }}#ssl-connections"

          - title: "SSH tunnels"
            url: "{{ link.security.encryption }}#ssh-tunnel-connections"

          - title: "Advanced connectivity"
            url: "{{ link.security.encryption }}#advanced-connectivity"

          - title: "Encryption at rest"
            url: "{{ link.security.encryption }}#data-at-rest"
        content: |
          {% assign guides = subsection.additional-guides %}

          {% include layout/category-section-tiles.html %}

      - title: "Configuring SSH tunnels"
        anchor: "data-encryption--ssh"
        type: "ssh"
        content: |
          {% assign guides = this-collection | where_exp:"guide","guide.key contains subsection.type" | sort:"title" %}

          {% include layout/category-section-tiles.html %}


---