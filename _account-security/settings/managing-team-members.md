---
title: Managing Team Members
permalink: /account-security/managing-team-members
keywords: add user, remove user, delete, invite, invitation, invite team
summary: "Invite your team members to collaborate in Stitch. When someone leaves your company, learn how to remove them from your account."

layout: general
toc: true

type: "team-members"
weight: 1

intro: |
  In the **Team Members** section of the {{ app.menu-paths.account-settings }}, you can view and manage the team members associated with your Stitch account.

  In this guide, we'll cover:

  {% for section in page.sections %}
  - [{{ section.summary }}](#{{ section.anchor }})
  {% endfor %}

sections:
  - title: "Team member basics"
    anchor: "team-member-basics"
    summary: "Some team member basics"
    content: |
      {% for subsection in section.subsections %}
      - [{{ subsection.title }}](#{{ subsection.anchor }})
      {% endfor %}
    subsections:
      - title: "How many team members can be in an account?"
        anchor: "how-many-team-members"
        content: |
          {% assign all-plans = site.data.stitch.subscription-plans.all-plans %}

          The number of team members that can be added to your account depends on the [Stitch plan]({{ site.pricing }}){:target="new"} you're using:

          {% for plan in all-plans %}
          {% unless plan.name == "free-trial" %}
          {% assign this-plan = site.data.stitch.subscription-plans[plan.name] %}

          - **{{ this-plan.name }}**: {{ this-plan.users | append: " users" }}
          {% endunless %}
          {% endfor %}

      - title: "Who will receive notifications?"
        anchor: "who-will-receive-notifications"
        content: |
          All team members in the account will receive email notifications.

      - title: "Who will receive invoices?"
        anchor: "who-will-receive-invoices"
        content: |
          Only the team member who initially adds the payment information to the account will receive a copy of the monthly invoice in their email.

          Everyone can view the Past Payment details in the **{{ app.page-names.billing }}** page, however.

      - title: "What can team members do in the account?"
        anchor: "what-can-team-members-do"
        content: |
          All team members in the account have the same permissions. This includes:

          - Updating [account settings]({{ link.account.account-settings | prepend: site.baseurl }}), including modyfing company details and notification settings
          - Inviting and deactivating team members
          - Viewing and modifying [billing details]({{ link.billing.billing-faq | prepend: site.baseurl }}), including the account's plan, payment method, and past payments
          - [Canceling the account]({{ link.account.cancel-account | prepend: site.baseurl }})
          - Creating, deleting, and disabling [Stitch API access keys]({{ link.account.manage-api-keys | prepend: site.baseurl }}) (Enterprise plans only)
          - Disabling [partner access keys]({{ link.account.manage-partner-access | prepend: site.baseurl }})
          - Adding, modifying, and deleting [destinations]({{ link.destinations.main | prepend: site.baseurl }})
          - Adding, modifying, pausing, and deleting [integrations]({{ link.integrations.main | prepend: site.baseurl }})
          - [Select and de-select tables and columns]({{ link.replication.syncing | prepend: site.baseurl }}) (when available) for replication
          - Configuring table and database view replication settings, including [Replication Methods]({{ link.replication.rep-methods | prepend: site.baseurl }}) and [Primary Keys (views only)]({{ link.replication.db-views | prepend: site.baseurl }})
          - [Resetting replication]({{ link.replication.reset-rep-keys | prepend: site.baseurl }}) for integrations and tables (when available)
          - [Starting and stopping extraction jobs]({{ link.replication.start-stop-extraction | prepend: site.baseurl }})
          - Viewing [extraction logs]({{ link.replication.extraction-logs | prepend: site.baseurl }}) and [loading reports]({{ link.replication.loading-reports | prepend: site.baseurl }})

  - title: "Invite a team member"
    anchor: "invite-team-member"
    summary: "How to invite a team member"
    content: |
      When inviting a team member to your account, keep the following in mind:

      - **An email address can only be associated with a single Stitch account**. [Try this workaround](#add-to-multiple-accounts) to use the same email address for multiple accounts.
      - **Invitation links in invitation emails are good for one attempt only.** If the login fails, try re-sending the invite.

      To invite a team member:

      1. Click the {{ app.menu-paths.account-settings }}.
      2. {{ app.menu-paths.add-user }}
      3. Enter the team member's email address. **Note**: This email address must be unique, meaning it can't be associated with an existing Stitch account.
      4. Click **Send Invitation**.

      Shortly after this process is completed, an email invite will be sent to the email address you entered.

      If you run into issues, refer to the [Troubleshooting team member invites guide]({{ link.troubleshooting.team-member-invites | prepend: site.baseurl }}).

  - title: "Add a team member to multiple accounts"
    anchor: "add-to-multiple-accounts"
    summary: "How to add a team member to multiple accounts"
    content: |
      Currently, Stitch allows an email address to be associated with only a single Stitch account. If you're one of our customers with two accounts and you want to use the same email address for both accounts, you may be able to use an email alias - also known as the `+` feature - to do so.

      **Note**: Your email provider must support the use of aliases to use this workaround.

      For example: This email address is used to create the first Stitch account, which is used for staging:

      `stitch@stitchdata.com`

      Using `+`, we can use the same email address to add the team member to the second Stitch account, which is used for production:

      `stitch+prod@stitchdata.com`

      If you prefer to use an un-aliased email address for a specific account and the email is already associated with a Stitch account, use the process outlined below to modify the account using the un-aliased email. This will then allow an invitation to be sent to the un-aliased email.

      In this example, we'll use the `stitch@stitchdata.com` email address.

      1. Sign into the Stitch account using the un-aliased email. In this example, we'd sign into the account associated with the `stitch@stitchdata.com` email address.
      2. Click {{ app.menu-paths.account-settings }}.
      3. Click the **Your Profile** tab.
      4. Update the email address to something along the lines of `name+deactivated@domain.com`. In this example, we'll update the email address to `stitch+deactivated@stitchdata.com`.
      5. Click {{ app.buttons.update-profile }}.

      Additionally, if the account is no longer needed, [you can cancel it]({{ link.account.cancel-account | prepend: site.baseurl }}).

  - title: "Deactivate a team member"
    anchor: "deactivate-team-member"
    summary: "How to deactivate a team member"
    content: |
      If a team member no longer requires access to Stitch, you can deactivate them.

      **This process is reversible** - if you deactivate a user by accident, you can simply re-add them.

      1. Click the {{ app.menu-paths.account-settings }}.
      2. In the Team Members section, find the user you want to deactivate.
      3. Click the **Deactivate** button next to the user's name.
---
{% include misc/data-files.html %}