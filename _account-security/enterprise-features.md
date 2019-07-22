---
title: Stitch Enterprise Features
permalink: /account-security/stitch-enterprise-features
keywords: enterprise stitch enterprise mission-critical ent
layout: general

summary: "Guides for all of the features included in Stitch's Enterprise plan."
toc: true

type: "enterprise"
weight: 1

enterprise: true
enterprise-cta:
  title: "Stitch Enterprise features"
  copy: "The features listed in this guide are available during the free trial or for customers on an Enterprise plan."

intro: |
  {% include misc/data-files.html %}

  For mission-critical applications, Stitch offers the Enterprise plan. Stitch Enterprise plans can include the features listed below, along with custom integrations, row volumes, priority support, and more.

sections:
  - title: "Feature list"
    anchor: "feature-list"
    content: |
      The features listed below are available during the free trial or for customers on an Enterprise plan.

      {% assign enterprise-features = site.data.stitch.subscription-plans.enterprise.features %}
      {% assign enterprise-docs = site.documents | where:"enterprise",true %}

      {% for feature in enterprise-features %}
      ### {{ feature.category }} {#{{ feature.category | slugify }}}

      {% for guide in feature.guides %}
      {% for enterprise-doc in enterprise-docs %}
      {% if enterprise-doc.key == guide.key %}
      - [**{% if guide.title %}{{ guide.title }}{% else %}{{ enterprise-doc.title }}{% endif %}**]({{ enterprise-doc.url | prepend: site.baseurl }}):
      {% if guide.summary %}{{ guide.summary }}{% else %}{{ enterprise-doc.summary }}{% endif %}
      {% endif %}
      {% endfor %}
      {% endfor %}

      {% endfor %}

  - title: "Compare all plans"
    anchor: "compare-all-plans"
    content: |
      To compare all of Stitch's plans, refer to our [pricing page]({{ site.pricing }}){:target="new"}.
---