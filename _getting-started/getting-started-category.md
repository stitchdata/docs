---
# -------------------------- #
#          PAGE INFO         #
# -------------------------- #

title: Getting Started
permalink: /getting-started/
keywords: getting started get started stitch onboarding new user set up stitch
summary: "Resources and guides for learning about Stitch and setting up your own data pipeline."
feedback: false

layout: page
sidebar: stitch

key: "getting-started"

level: "category"


# -------------------------- #
#       HOME PAGE DATA       #
# -------------------------- #

## Used to display info on the home page as a category tile

icon: "file"
display-title: "Getting Started"
display-summary: "Learn about Stitch and set up your own data pipeline."
weight: 1

---

{% include misc/data-files.html %}

{{ page.summary }}

---

{% assign guides = site.getting-started | where_exp:"guide","guide.title != page.title" |sort:"weight" %}

{% for guide in guides %}
<span class="h3"><a href="{{ guide.url | prepend: site.baseurl }}">{{ guide.title }}</a></span>
{{ guide.summary }}
{% endfor %}