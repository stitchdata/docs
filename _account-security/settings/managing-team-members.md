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
      {% assign user-management = site.data.stitch.user-management %}

      {% assign permissions = user-management.permissions %}
      {% assign permission-groups = permissions.group-types %}

      {% assign user-roles = user-management.roles %}
      {% assign role-types = user-roles.role-types %}

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
          Only the team member who initially adds the payment information to the account will receive a copy of the monthly invoice in their email. This team member is also known as the **{{ user-roles.invoice-admin.name }}**. Refer to the [Team member roles and permissions](#team-member-roles-permissions) section for more info.

      - title: "What can team members do in the account?"
        anchor: "what-can-team-members-do"
        content: |
          The actions team members can perform depends on their user role. Refer to the [Team member roles and permissions](#team-member-roles-permissions) section for more info.

  - title: "Team member roles and permissions"
    anchor: "team-member-roles-permissions"
    summary: "What users can and can't do in your Stitch account"
    content: |
      {% for subsection in section.subsections %}
      - [{{ subsection.title | flatify }}](#{{ subsection.anchor }})
      {% endfor %}
    subsections:
      - title: "Team member user roles"
        anchor: "team-member-user-roles"
        content: |
          {% for sub-subsection in subsection.sub-subsections %}
          - [{{ sub-subsection.title | flatify }}](#{{ sub-subsection.anchor }})
          {% endfor %}

        sub-subsections:
          - title: "User role assignment"
            anchor: "team-member-user-role--assignment"
            content: |
              Currently, Stitch automatically assigns user roles to team members. Defining user roles for individual team members isn't currently supported.

              When inviting and managing team members, keep the following in mind:

              - New team members invited to the account are automatically assigned the **{{ user-roles.general-user.name }}** user role.
              - Every account has an **{{ user-roles.invoice-admin.name }}**. This is the team member who initially enters payment info for the account.
              - If [Single sign-on (SSO)]({{ link.security.single-sign-on | prepend: site.baseurl }}) is enabled, every account will have an **{{ user-roles.sso-admin.name }}**. This is the team member who initially enables SSO for the account. Additional {{ user-roles.sso-admin.name | append: "s" }} can be added by contacting support.
              - It's possible for a team member to be both an {{ user-roles.invoice-admin.name }} and an {{ user-roles.sso-admin.name }}.

          - title: "User role types"
            anchor: "team-member-user-role--types"
            content: |
              Team members can have have one or more of the following roles:

              <table>
                <tr>
                  <td width="25%; fixed">
                    <strong>User role</strong>
                  </td>
                  <td>
                    <strong>Description</strong>
                  </td>
                </tr>
                {% for role in role-types %}
                  <tr>
                    <td>
                      <strong>{{ user-roles[role]name }}</strong>
                    </td>
                    <td>
                      {{ user-roles[role]description | flatify | markdownify }}
                    </td>
                  </tr>
                {% endfor %}
              </table>

      - title: "Team member permissions"
        anchor: "team-member-permissions"
        content: |
          {% include misc/icons.html %}

          Refer to the following sections for info about the permissions each [user role](#team-member-user-roles) has. In the permission tables, you'll see the following icons:

          - {{ supported | replace:"TOOLTIP","[USER ROLE] users can perform this action" }} indicates that the user role has the permission to perform the described action

          - {{ support-exception | replace:"TOOLTIP","[USER ROLE] users can perform this action, but there may be exceptions" }} indicates that the user role has the permission to perform the described action, but there may be exceptions. For example: All users can reset their own passwords, but if SSO is enabled for the account, only the SSO Admin can reset their own password.

          - {{ not-supported | replace:"TOOLTIP","[USER ROLE] users can't perform this action" }} indicates that the user role doesn't have the permission to perform the described action

        sub-subsections:
          - title: "Permission groups"
            anchor: "team-member-permissions--groups"
            content: |
              {% for permission-group in permission-groups %}
              - [{{ permissions[permission-group]name | append: " permissions" }}](#{{ permission-group | append: "-permissions" }})
              {% endfor %}

              {% for permission-group in permission-groups %}
              ##### {{ permissions[permission-group]name | append: " permissions" }} {#{{ permission-group | append: "-permissions" }}}

                <table>
                  <tr>
                    <td width="55%; fixed">
                      <strong>Permission</strong>
                    </td>
                    {% for role in role-types %}
                      <td>
                        <strong>{{ user-roles[role]name }}</strong>
                      </td>
                    {% endfor %}
                  </tr>

                  {% for permission in permissions[permission-group]all %}
                    <tr>
                      <td>
                        <strong>{{ permission.name | flatify }}</strong>
                        <br>
                        {{ permission.description | flatify | markdownify }}
                      </td>

                      {% for role in role-types %}
                        <td align="center">
                          {% assign permission-check = user-roles[role][permission-group] | where:"id",permission.id | first %}

                          {% if permission-check != null %}
                            {% if permission-check.use-exception == true %}
                              {% capture tooltip %}
                              {{ user-roles[role]name | append:"s" }} can perform this action unless {{ permissions[permission-group][permission.id]exception }}.
                              {% endcapture %}

                              {{ support-exception | replace:"TOOLTIP",tooltip }}

                            {% else %}
                              {% capture tooltip %}
                              {{ user-roles[role]name | append:"s" }} can perform this action: {{ permission.name }}
                              {% endcapture %}

                              {{ supported | replace:"TOOLTIP",tooltip }}
                            {% endif %}
                          {% else %}
                            {% capture tooltip %}
                            {{ user-roles[role]name | append:"s" }} can't perform this action: {{ permission.name }}
                            {% endcapture %}

                            {{ not-supported | replace:"TOOLTIP",tooltip }}
                          {% endif %}
                        </td>
                    {% endfor %}
                    </tr>
                  {% endfor %}
                </table>
                [Back to Team member permissions](#team-member-permissions)
              {% endfor %}

  - title: "Invite a team member"
    anchor: "invite-team-member"
    summary: "How to invite a team member"
    content: |
      {% include note.html type="" content="" %}
      
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