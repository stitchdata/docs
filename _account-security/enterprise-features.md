---
# -------------------------- #
#      Page & Formatting     #
# -------------------------- #

title: Stitch Enterprise Features
permalink: /account-security/stitch-enterprise-features
keywords: enterprise stitch enterprise mission-critical ent
summary: "Guides for the features included in Stitch's Enterprise plan."

layout: general
toc: true
weight: 1

key: "enterprise-features"

type: "enterprise"
enterprise: true
enterprise-cta:
  title: "Stitch Enterprise features"
  copy: "The features listed in this guide are available during the free trial or for customers on an Enterprise plan."


# -------------------------- #
#        Introduction        #
# -------------------------- #

intro: |
  {% include misc/data-files.html %}

  For mission-critical applications, Stitch offers the Enterprise plan. Stitch Enterprise plans can include the features listed below, along with custom integrations and row volumes, priority support, and more.


# -------------------------- #
#           Content          #
# -------------------------- #

sections:
  - title: "Feature list"
    anchor: "feature-list"
    content: |
      The features listed below are available during the free trial or for customers on an Enterprise plan. Unless noted, all features are available during the free trial.

      **Note**: After the free trial ends, access to these features will be revoked. 

      {% assign enterprise-features = site.data.stitch.subscription-plans.enterprise.features %}
      {% assign enterprise-docs = site.documents | where:"enterprise",true %}

      <table class="attribute-list">

      {% for feature in enterprise-features %}
      <tr>
      <td class="table-subheading" colspan="2">
      <strong>{{ feature.category | upcase }}</strong>
      </td>
      </tr>

      {% for guide in feature.guides %}
      <tr>

      <td class="attribute-name">
      {% if guide.key %}
      {% assign enterprise-doc = enterprise-docs | where:"key",guide.key | first %}
      <a href="{{ enterprise-doc.url | prepend: site.baseurl }}">
      <strong>
      {% if guide.title %}{{ guide.title }}{% else %}{{ enterprise-doc.title }}{% endif %}
      </strong>
      </a>
      {% else %}
      <strong>{{ guide.title }}</strong>
      {% endif %}
      </td>

      <td>
      {% if guide.summary %}
      {{ guide.summary | flatify | markdownify }}
      {% else %}
      {{ enterprise-doc.summary | flatify | markdownify }}
      {% endif %}
      {% if guide.free-trial-available == false %}
      <strong>Note</strong>: This feature isn't available during the free trial.
      {% endif %}
      </td>
      </tr>
      {% endfor %}
      {% endfor %}
      </table>

  - title: "Compare all plans"
    anchor: "compare-all-plans"
    content: |
      To compare all of Stitch's plans, refer to our [pricing page]({{ site.pricing }}){:target="new"}.
---