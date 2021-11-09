---
# -------------------------- #
#      Page & Formatting     #
# -------------------------- #

title: Stitch Features for Unlimited Plans
permalink: /account-security/stitch-unlimited-features
redirect_from: /account-security/stitch-enterprise-features
keywords: enterprise stitch enterprise mission-critical ent unlimited unlimited plus
summary: "Guides for the features included in Unlimited and Unlimited Plus plans."

layout: general
toc: true
weight: 1

key: "enterprise-features"

type: "enterprise"


# -------------------------- #
#  Stitch Plan Requirements  #
# -------------------------- #

minimum-plan: "unlimited"

minimum-plan-cta:
  title: "Stitch {{ site.data.stitch.subscription-plans.unlimited.name }} features"
  copy: "The features listed in this guide are available during the free trial or for customers on an {{ site.data.stitch.subscription-plans.unlimited.name }} or {{ site.data.stitch.subscription-plans.unlimited-plus.name }} plan."


# -------------------------- #
#        Introduction        #
# -------------------------- #

intro: |
  {% include misc/data-files.html %}

  For mission-critical applications, Stitch offers {{ site.data.stitch.subscription-plans.unlimited.name }} and {{ site.data.stitch.subscription-plans.unlimited-plus.name }} plans. These plans can include the features listed below, along with custom integrations and row volumes, priority support, and more.


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
  - title: "Unlimited plan features"
    anchor: "unlimited-plan-feature-list"
    plan: "unlimited"
    content: |
      {% assign stitch-unlimited = site.data.stitch.subscription-plans.unlimited %}

      The features listed below are available during the free trial or to accounts on an {{ stitch-unlimited.name }} plan. Unless noted, all features are available during the free trial.

      **Note**: After the free trial ends, access to these features will be revoked.

      {{ page.feature-table | flatify }}

  - title: "Unlimited Plus plan features"
    anchor: "unlimitedl-plus-plan-feature-list"
    plan: "unlimited-plus"
    content: |
      {% assign stitch-unlimited-plus = site.data.stitch.subscription-plans.unlimited-plus %}

      In addition to the [{{ stitch-unlimited.name }} plan features](#unlimited-plan-feature-list), accounts on an {{ stitch-unlimited-plus.name }} plan will also have access to the features listed below.

      {{ page.feature-table | flatify }}

  - title: "Compare all plans"
    anchor: "compare-all-plans"
    content: |
      To compare all of Stitch's plans, refer to our [pricing page]({{ site.pricing }}){:target="new"}.
---