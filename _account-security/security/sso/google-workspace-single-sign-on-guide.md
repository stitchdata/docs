---
# -------------------------- #
#      Page & Formatting     #
# -------------------------- #

title: Enabling Single Sign-On Using Google Workspace
permalink: /account-security/single-sign-on/enabling-google-workspace-saml
summary: "Connect your Google Workspace account to Stitch and enable Single Sign-On (SSO)."

input: false
layout: tutorial
feedback: true

key: "single-sign-on-google-workspace"
type: "security"
weight: 4


# -------------------------- #
#         IdP Details        #
# -------------------------- #

idp: true
name: "google-workspace"
display-name: "Google Workspace"


# -------------------------- #
#   RELATED SIDEBAR LINKS    #
# -------------------------- #

related:
  - title: "Single Sign-On documentation"
    link: "{{ link.security.single-sign-on | prepend: site.baseurl }}"

  - title: "Stitch team roles and permissions"
    link: "{{ link.account.team-roles-permissions | prepend: site.baseurl }}"


# -------------------------- #
#        Introduction        #
# -------------------------- #

intro: |
  {% capture sso-admin %}
  Refer to the [Team member roles and permissions documentation]({{ link.account.team-roles-permissions | prepend: site.baseurl }}) for more info about privileges in Stitch.
  {% endcapture %}

  {% capture sso-admin-note %}
  Setting up or modifying an existing {{ page.display-name }} connection requires Admin privileges in Stitch. {{ sso-admin }}
  {% endcapture %}

  {% include note.html first-line="**Stitch Admin privileges required**" content=sso-admin-note %}

  {{ page.summary }}

  In this guide, we'll cover:

  {% for step in page.steps %}
  - [{{ step.summary | flatify }}](#{{ step.anchor }})
  {% endfor %}


# -------------------------- #
#        Requirements        #
# -------------------------- #

requirements:
  - item: |
      **Admin privileges in Stitch.** {{ sso-admin }}

  - item: |
      **Super Admin privileges in {{ page.display-name }} that allow you to add and configure applications.** If you don't have these privileges, **contact a {{ page.display-name }} admin before continuing**.

      Refer to [{{ page.display-name }}'s documentation](https://support.google.com/a/answer/2405986#super_admin){:target="new"} for more info.


# -------------------------- #
#           Content          #
# -------------------------- #

steps:
  - title: "Create and configure an {{ page.display-name }} app"
    anchor: "create-configure-sso-app"
    summary: "Creating and configuring an {{ page.display-name }} app"
    content: |
      {% for substep in step.substeps %}
      - [Step 1.{{ forloop.index }}: {{ substep.title | flatify }}](#{{ substep.anchor }})
      {% endfor %}

    substeps:
      - title: "Retrieve your SSO info from Stitch"
        anchor: "retrieve-sso-info-from-stitch"
        content: |
          1. Sign into your Stitch account.
          {% include shared/sso/stitch-sso-menu-path.html type="initial-setup" %}

          Leave this page open - you'll need it to complete the setup.

      - title: "Create the app in {{ page.display-name }}"
        anchor: "create-app"
        content: |
          1. Sign into your [Google Admin Console](https://admin.google.com){:target="new"}.
          2. From the Admin console home page, click **Apps > Web and mobile apps**.
          3. Click **Add App > Add custom SAML app**.
          4. On the **App Details** page, enter the name of the custom app. Optionally, upload an **app icon**.
          5. Click **Continue**.
          6. On the **Google Identity Provider** details page, get the setup information needed by the service provider (Stitch) and select the option for downloading the IDP metadata. This will be used later for the Stitch SSO configuration steps.
          7. Click **Continue**.

      - title: "Configure SAML for the app"
        anchor: "configure-app-saml"
        parameters:
          - saml-name: "given_name"
            value: "First Name"
          - saml-name: "family_name"
            value: "Last Name"
          - saml-name: "email"
            value: "Primary Email"
        content: |
          Next, you'll configure SAML for the app starting from the **Service Provider Details** window:

          {% for sub-substep in substep.sub-substeps %}
          - [Step 1.3.{{ forloop.index }}: {{ sub-substep.title }}](#{{ sub-substep.anchor }})
          {% endfor %}

        sub-substeps:
          - title: "Define the General settings"
            anchor: "configure-app-saml--general"
            content: |
              In the **Service Provider Details** window, enter an:

              - ACS URL
              - Entity ID
              - StartURL (if needed)

              The `ACS URL` and `SP Entity ID` will come from the Stitch SSO configuration screen in the Stitch App (the browser tab you should still have open). Copy those values into the corresponding fields on the Google Workspace SAML app configuration screen, and then click **Continue**.


          - title: "Define the Attribute Statements"
            anchor: "configure-app-saml--attributes"
            content: |
              Next, you'll add the required attributes for the app:

              <table>
                <tr>
                  <td>
                    <strong>#</strong>
                  </td>
                  <td>
                    <strong>SAML Attribute Name</strong>
                  </td>
                  <td>
                    <strong>Value</strong>
                  </td>
                </tr>
                {% for parameter in substep.parameters %}
                  <tr>
                    <td>
                      {{ forloop.index }}
                    </td>
                    <td>
                      {{ parameter.saml-name }}
                    </td>
                    <td>
                      {{ parameter.value }}
                    </td>
                  </tr>
                {% endfor %}
              </table>

              To add the attributes:

              1. Click **Add another mapping**.
              2. In the **Google Directory attributes** field, select the corresponding **Value** from the dropdown. For example: `First Name` is the value for the **SAML Attribute** `given_name`.
              3. In the **App attribues** field, enter the **SAML Attribute Name** of the parameter. For example: `given_name`.
              4. Click **Add another mapping** to add the next attribute.
              5. Repeat steps 2-4 until all attributes have been added. This is how the section should look when all the parameters have been added:

                 ![Stitch attributes fully configured for the Google Workspace app]({{ site.baseurl }}/images/account-security/sso/google-workspace-attributes-screen.png)
              6. When complete, click **Finish**.

      - title: "Grant users access to the app"
        anchor: "grant-user-app-access"
        content: |
          The last step to configuring the app is to grant access to users in your {{ page.display-name }} instance. This ensures that they'll be able to access Stitch via SSO.

          Using the process your organization follows, grant Stitch {{ page.display-name }} app access to your colleagues.

  - title: "Connect to Stitch"
    anchor: "connect-to-stitch"
    summary: "Connecting your {{ page.display-name }} app to Stitch"
    content: |
      Navigate back to the page where your Stitch account is open.

      1. In Stitch, scroll down to the **Connect to Stitch** section of the {{ page.display-name }} setup page.
      2. Click **Upload SAML Metadata**.
      3. Locate and select the `GoogleIDPMetadata.xml` file you downloaded in [Step 1.2](#create-app).

  - title: "Activate SSO"
    anchor: "activate-sso"
    summary: "Activating SSO for your Stitch account"
    content: |
      When finished, click the **Activate SSO** button.

next-steps: |
  After you've enabled SSO for your Stitch account, remember to grant Stitch access to users in your {{ page.display-name }} instance, if you haven't already.
---