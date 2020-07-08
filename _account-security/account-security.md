---
# -------------------------- #
#          PAGE INFO         #
# -------------------------- #

title: Account & Security
permalink: /account-security/
keywords: billing, plan, change plan, cancel, cancel account, delete, remove
summary: "Resources for everything account-related: Managing billing details, inviting team members, security info, and more."

key: "account-security"

layout: general
feedback: false


# -------------------------- #
#       HOME PAGE DATA       #
# -------------------------- #

## Used to display info on the home page as a category tile

level: "category"

icon: "user-profile"
display-title: "Your Stitch account"
display-summary: "Manage your account and learn about Stitch's security practices."
weight: 2


# -------------------------- #
#           INTRO            #
# -------------------------- #

intro: |
  {{ page.summary }}

  {% assign sections = "manage-your-account|invite-your-team|notifications|billing|security" | split:"|" %}

  {% for section in sections %}
  - [{{ section | capitalize | replace:"-"," " }}](#{{ section | slugify | append: "-category" }})
  {% endfor %}

sections:
  - title: "Manage your account"
    anchor: "manage-your-account-category"
    type: "manage-your-account"
    append-to-pages:
    content: |
      {% assign pages = site.account-security | where_exp:"page","page.type contains section.type" | sort:"weight" %}

      <ul class="tiles two-columns">
          {% for page in pages %}
              <li align="left">
                  <a href="{{ page.url | prepend: site.baseurl | flatify }}">
                      {{ page.title | flatify }}
                  </a>
              </li>
          {% endfor %}
      </ul>
---
{% include misc/data-files.html %}