---
# -------------------------- #
#          PAGE INFO         #
# -------------------------- #

title: Troubleshooting
keywords: troubleshooting, integration, trouble, issue, help, error, errors
permalink: /troubleshooting/

layout: general
toc: false
feedback: false

key: "troubleshooting"

level: "category"


# -------------------------- #
#       HOME PAGE DATA       #
# -------------------------- #

## Used to display info on the home page as a category tile

icon: "support"
display-title: "Troubleshooting"
display-summary: "Resolve issues and get your data flowing again."
weight: 7


# -------------------------- #
#         CATEGORIES         #
# -------------------------- #

categories:
  - title: "Stitch Status"
    url: "{{ site.status }}"
    description: "Whenever the Stitch app encounters an issue, we'll post an update about it on our Status Page. We recommend checking our status first if you encounter problems in the app."

  - title: "Known issues"
    url: "{{ link.troubleshooting.known-issues | prepend: site.baseurl }}"
    description: "Occasionally, some integrations used by Stitch may encounter bugs or other issues. Whenever we've identified a third-party issue - meaning on the integration provider's end - we'll post an update here. Additionally, we'll also update any issues that have been resolved."

  - title: "Account and billing"
    url: "{{ site.baseurl }}/troubleshooting/account"
    description: "Having trouble logging into your account? Running into payment processing issues? Resources for all things account and billing related can be found here."

  - title: "Destinations"
    url: "{{ site.baseurl }}/troubleshooting/destinations"
    description: "Here you'll find help for all things destinations, including troublesome connection issues with destinations and fixes for data loading errors."

  - title: "Integrations"
    url: "{{ site.baseurl }}/troubleshooting/integrations"
    description: "Having trouble connecting your database or SaaS integration? Investigating a data discrepancy? Here you'll find resources for some of the most common causes of connection troubles and data discrepancies related to integrations."

  - title: "Replication"
    url: "{{ site.baseurl }}/troubleshooting/replication"
    description: "If you're having trouble getting Stitch to replicate or load some of your data, this is where you'll find the resources to pinpoint and resolve the issue."

  - title: "Data discrepancies"
    url: "{{ site.baseurl }}/troubleshooting/data-discrepancies"
    description: "Data discrepancies can surface as missing records, incorrect values, or fields not being correctly typed. If something in your data warehouse doesn't look quite right, these resources will help you get to the root of the problem."

  - title: "Error notifications"
    url: "{{ link.troubleshooting.errors | prepend: site.baseurl }}"
    description: "If you've received an in-app or email error notification, here's where you'll find the resources you need to get things back on track."


sections:
  - content: |
      {% for category in page.categories %}
      <span class="h3">
      <a href="{{ category.url | flatify }}">{{ category.title }}</a>
      </span>
      {{ category.description }}
      {% endfor %}
---
{% include misc/data-files.html %}