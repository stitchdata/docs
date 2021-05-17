---
title: "New feature: Passwordless authentication with Magic Link"
content-type: "changelog-entry"
date: 2021-05-19
entry-type: new-feature
entry-category: "security, documentation"
# pull-request: ""
---

If you've signed into Stitch today, you might notice that the sign in page looks a little different:

[TODO- image]

You can now log into your Stitch account using a "magic" link, or passwordless authentication. When you request a magic link, Stitch will send you an email containing a link that directs you to Stitch and immediately logs you into your account.

This feature is available on all plans, but there are some important things to note if your account has Single Sign-On (SSO) enabled. Refer to the [SSO documentation]({{ site.home | append: site.baseurl | append: link.security.single-sign-on | append: "#basics--magic-link" }}) for more info.