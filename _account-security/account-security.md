---
title: Account & Security
permalink: /account-security/
keywords: billing, plan, change plan, cancel, cancel account, delete, remove
summary: "Resources for everything account-related: managing billing details, inviting team members, security info, and more."
feedback: false
---
{% include misc/data-files.html %}

{{ page.summary }}

---

## Getting Started

{% assign getting-started = site.account-security | where:"permalink","/getting-started/" %}

{% for page in getting-started %}
### [{{ page.title }}]({{ page.url | prepend: site.baseurl }})
{{ page.summary }}
{% endfor %}

---

{% assign account-docs = site.account-security | where:"type","account" | sort:"weight" %}

## Managing Your Account

{% for page in account-docs %}
### [{{ page.title }}]({{ page.url | prepend: site.baseurl }})
{{ page.summary }}
{% endfor %}

---

{% assign billing-docs = site.account-security | where:"type","billing" | sort:"weight" %}

## Stitch Billing

{% for page in billing-docs %}
### [{{ page.title }}]({{ page.url | prepend: site.baseurl }})
{{ page.summary }}
{% endfor %}

---

{% assign security-docs = site.account-security | where:"type","security" | sort:"weight" %}

## Security

{% for page in security-docs %}
### [{{ page.title }}]({{ page.url | prepend: site.baseurl }})
{{ page.summary }}
{% endfor %}