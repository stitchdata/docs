---
title: Inviting & Deactivating Team Members
permalink: /account-security/managing-team-members
keywords: security, secure, data access, credentials, security protocol, breach, encryption, encrypted, store data, retain data
tags: [getting_started, account, security]

summary: "Invite your team members to collaborate in Stitch. When someone leaves your company, learn how to remove them from your account."
type: "account"
toc: true
weight: 2
---
{% include misc/data-files.html %}

{% capture invoice %}
Only the user who initially adds the payment information to the account will receive a copy of the monthly invoice in their email.

Everyone can view the Past Payment details in the {{ app.page-names.billing }} page, however.
{% endcapture %}

{% include note.html first-line="**Who receives invoices?**" content=invoice %}

## Invite a Team Member

1. To add a new user, click the {{ app.menu-paths.account-settings }}.
2. {{ app.menu-paths.add-user }}
3. Enter the user’s email address.
4. Click **Send Invitation**.

Shortly after this process is completed, an email invite will be sent to the email address you entered.

**Note**: The invitation link in the invite email is only good for one attempt. If the login should fail, try re-sending the invite.

---

## Add Team Members to Multiple Accounts

A few of our customers have two Stitch accounts: one for staging and one for production usage. If you want the same email address to be used for both accounts, you can use the '`+`' feature if your email provider supports it.

If this email address is used to create the first Stitch account, which is used for staging:

`stitch@stitchdata.com`

You can use '`+`' to add this team member to the second Stitch account, which is used for production:

`stitch+prod@stitchdata.com`

---

## Deactivate a Team Member {#deactivate-team-member}

If a team member no longer requires access to Stitch, you can deactivate them.

**This process is reversible** - if you deactivate a user by accident, you can simply re-add them.

1. Click the {{ app.menu-paths.account-settings }}.
2. In the Team Members section, find the user you want to deactivate.
3. Click the **Deactivate** button next to the user's name.