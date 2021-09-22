---
# -------------------------- #
#      Page & Formatting     #
# -------------------------- #

title: Stitch Features for Pro Plans
permalink: /account-security/stitch-pro-features
redirect_from: /account-security/stitch-enterprise-features
keywords: enterprise stitch enterprise mission-critical ent pro pro plus
summary: "Guides for the features included in Pro and Pro Plus plans."

layout: general
toc: true
weight: 1

key: "enterprise-features"

type: "enterprise"


# -------------------------- #
#  Stitch Plan Requirements  #
# -------------------------- #

minimum-plan: "pro"

minimum-plan-cta:
  title: "Stitch {{ site.data.stitch.subscription-plans.pro.name }} features"
  copy: "The features listed in this guide are available during the free trial or for customers on a {{ site.data.stitch.subscription-plans.pro.name }} or {{ site.data.stitch.subscription-plans.pro-plus.name }} plan."


# -------------------------- #
#        Introduction        #
# -------------------------- #

intro: |
  {% include misc/data-files.html %}

  For mission-critical applications, Stitch offers {{ site.data.stitch.subscription-plans.pro.name }} and {{ site.data.stitch.subscription-plans.pro-plus.name }} plans. These plans can include the features listed below, along with custom integrations and row volumes, priority support, and more.


# -------------------------- #
#           Content          #
# -------------------------- #

feature-table: |
  {% assign plan-features = site.data.stitch.subscription-plans.[section.plan].features %}

  <table class="attribute-list">

  {% for feature in plan-features %}
  <tr>
  <td class="table-subheading" colspan="2">
  <strong>{{ feature.category | upcase }}</strong>
  </td>
  </tr>

  {% for guide in feature.guides %}
  <tr>
  <td class="attribute-name">
  {% if guide.key %}
  {% assign doc = site.documents | find:"key",guide.key %}
  <a href="{{ doc.url | prepend: site.baseurl }}">
  <strong>
  {% if guide.title %}{{ guide.title }}{% else %}{{ doc.title }}{% endif %}
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
  {{ doc.summary | flatify | markdownify }}
  {% endif %}
  {% if guide.free-trial-available == false %}
  <strong>Note</strong>: This feature isn't available during the free trial.
  {% endif %}
  </td>
  </tr>
  {% endfor %}
  {% endfor %}
  </table>

sections:
  - title: "Pro plan features"
    anchor: "pro-plan-feature-list"
    plan: "pro"
    content: |
      {% assign stitch-pro = site.data.stitch.subscription-plans.pro %}

      The features listed below are available during the free trial or to accounts on a {{ stitch-pro.name }} plan. Unless noted, all features are available during the free trial.

      **Note**: After the free trial ends, access to these features will be revoked.

      {{ page.feature-table | flatify }}

  - title: "Pro Plus plan features"
    anchor: "pro-plus-plan-feature-list"
    plan: "pro-plus"
    content: |
      {% assign stitch-pro-plus = site.data.stitch.subscription-plans.pro-plus %}

      In addition to the [{{ stitch-pro.name }} plan features](#pro-plan-feature-list), accounts on a {{ stitch-pro-plus.name }} plan will also have access to the features listed below.

      {{ page.feature-table | flatify }}

  - title: "Compare all plans"
    anchor: "compare-all-plans"
    content: |
      To compare all of Stitch's plans, refer to our [pricing page]({{ site.pricing }}){:target="new"}.
---