---
title: Role-Based Access Control (RBAC)
permalink: /account-security/role-based-access-control
keywords: role based, access control
summary: "Control user's access to application functionality based on the user role."

layout: general
toc: true

key: "role-based-access-control"

type: "invite-your-team"

intro: |
  You can now control what users have access to within the Stitch app based on an assigned role! In this guide, you will learn everything you need to know on how to fully utilize this feature.
  {% capture notice %}
  **Note**: If you are not on an SSO enabled account, every user will have an Administrator role by default, and then you can downgrade roles to General User. If you are on an SSO enabled account, SSO Admins will become the Administrators by default and all other users will become General Users. Refer to the [SSO Doccumentation]({{ link.security.single-sign-on | prepend: site.baseurl }}) for more information.
  {% endcapture %}

  {% include note.html type="single-line" content=notice %}

  In this guide, we'll cover:

  {% for section in page.sections %}
  - [{{ section.summary }}](#{{ section.anchor }})
  {% endfor %}
  
sections:
  - title: "Roles within the Stitch app"
    anchor: "stitch-roles"
    summary: "The roles that currently exist within Stitch"
    content: |
      There are currently two manually assignable roles that a user can have: **Administrator** and **General User**.

      **Administrator**: An Administrator is a person responsible for ensuring the Stitch account is set up as needed and is therefore the ultimate owner of the Stitch account. They have total control over every possible action a user can take on Stitch. They also have some exclusive privileges that no other role has. Keep in mind all [{{ user-roles.sso-admin.name | append: "s" }}]({{ link.security.single-sign-on | prepend: site.baseurl }}) are also {{ user-roles.administrator.name | append: "s" }}.

      **General User**: A General User is responsible for ensuring data is correctly ingested and available for consumers. Their primary responsibility within Stitch is to create and manage the necessary connections and configurations to ingest data. They have the ability to take any action except the ones exclusive to the Administrator.

      For a list of all existing roles and permissions, visit our [team member permissions]({{ link.account.team-members#team-member-roles-permissions | prepend: site.baseurl }}) documentation.

  - title: "Role-Based Access Control FAQ"
    anchor: "faq"
    summary: "Some frequently asked questions around Role-Based Access Control"
    content: |
      {% for subsection in section.subsections %}
      - [{{ subsection.title }}](#{{ subsection.anchor }})
      {% endfor %}

    subsections:  
      - title: "What role will I have?"
        anchor: "faq-user-roles"
        content: |
          A user must be one of the following roles: Administrator or General User. A user can only have one role at a time, and their must be at least one Administrator on your account at all times. The user who created the account will be an Administrator by default.

      - title: "What can an Administrator do?"
        anchor: "faq-administrator"
        content: |
          An Administrator can take any action possible through the Stitch web app or Connect API.

      - title: "What can a General User do?"
        anchor: "faq-general-user"
        content: |
          A General User can take any action possible throught the Stitch app or Connect API **EXCEPT**:
            1. Change company name
            2. Manage SSO settings 
            3. Invite, disinvite, or deactivate a user  
            4. Select/Change billing plan  
            5. Edit billing details
            6. Manage user roles  
            7. Disable or delete Partner Keys  
            8. Configure plain-text notification settings  

      #- title: "What happens if my role is changed?"
      #  anchor: "faq-role-changes"
      #  content: |
      #    You will receive an in-app notification if there are any changes to your role in your account.
---