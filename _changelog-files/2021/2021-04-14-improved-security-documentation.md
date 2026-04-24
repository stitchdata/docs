---
title: "Improved security documentation"
content-type: "changelog-entry"
date: 2021-04-14
entry-type: improvement
entry-category: "documentation, security"
pull-request: "https://github.com/stitchdata/docs/pull/626"
---

We've been working hard to improve our security documentation - here's a high-level look at the changes:

- **Added a dedicated [category page]({{ site.data.urls.security.main | prepend: site.baseurl }})**, ensuring you can easily view and navigate all things Stitch security

- **Reformatted the Security FAQ (now the [Security Overview]({{ site.data.urls.security.faq | prepend: site.baseurl }}))**, allowing you to view all content at once. You can also now use `Ctrl+F` to perform an on-page search.

- **Expanded the Security Overview** to include detailed info about:
  
  - [Stitch's environment]({{ site.data.urls.security.faq | prepend: site.baseurl | append: "#environment" }})
  - [Stitch account access]({{ site.data.urls.security.faq | prepend: site.baseurl | append: "#account-access" }}), [connectivity]({{ site.data.urls.security.faq | prepend: site.baseurl | append: "#connectivity" }}), and [connection permissions]({{ site.data.urls.security.faq | prepend: site.baseurl | append: "#permissions" }})
  - [Compliance with various privacy and security regulations]({{ site.data.urls.security.faq | prepend: site.baseurl | append: "#stitch-compliance" }})
  - [Data retention]({{ site.data.urls.security.faq | prepend: site.baseurl | append: "#data-retention" }})