---
# -------------------------- #
#          PAGE INFO         #
# -------------------------- #

title: Account Management
permalink: /account-security/
keywords: billing, plan, change plan, cancel, cancel account, delete, remove
summary: "Resources for everything account-related: Managing billing details, inviting team members, and more."
feedback: false

key: "account-security"

level: "category"


# -------------------------- #
#       HOME PAGE DATA       #
# -------------------------- #

## Used to display info on the home page as a category tile

icon: "user-profile"
display-title: "Your Stitch account"
display-summary: "Manage your account and learn about Stitch's security practices."
weight: 2

---
{% include misc/data-files.html %}

{{ page.summary }}

{% assign sections = "account-settings|team-members|notifications|billing|security" | split:"|" %}

{% for section in sections %}
- [{{ section | capitalize | replace:"-"," " }}](#{{ section | slugify | append: "-category" }})
{% endfor %}

---

{% for section in sections %}

## {{ section | capitalize | replace:"-"," " }} {#{{ section | slugify | append: "-category" }}}

{% assign pages = site.account-security | where_exp:"page","page.type contains section" | sort:"weight" %}

{% for page in pages %}
<span class="h3"><a href="{{ page.url | prepend: site.baseurl }}">{{ page.title | replace:"stitch","Stitch" | replace:"faq","FAQ" | replace:"api","API" }}</a></span>
{{ page.summary }}
{% endfor %}

{% unless forloop.last == true %}
---
{% endunless %}
{% endfor %}