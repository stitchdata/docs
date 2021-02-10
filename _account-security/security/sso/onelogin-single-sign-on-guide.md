---
# -------------------------- #
#      Page & Formatting     #
# -------------------------- #

title: Enabling Single Sign-On Using OneLogin
permalink: /account-security/single-sign-on/enabling-onelogin
summary: "Connect your OneLogin account to Stitch and enable Single Sign-On (SSO)."

input: false
layout: tutorial
feedback: true

key: "single-sign-on-onelogin"
type: "security"
weight: 4


# -------------------------- #
#         IdP Details        #
# -------------------------- #

idp: true
name: "onelogin"
display-name: "OneLogin"


# -------------------------- #
#        Introduction        #
# -------------------------- #

intro: |
  {% capture sso-admin %}
  If this is the first time SSO is enabled, the Stitch user who configures the connection will become an SSO Admin. Additional SSO Admins may be added by contacting support.

  Refer to the [Team member roles and permissions documentation]({{ link.account.team-roles-permissions | prepend: site.baseurl }}) for more info about privileges in Stitch.
  {% endcapture %}

  {% capture sso-admin-note %}
  Setting up or modifying an existing {{ page.display-summary }} connection requires SSO Admin privileges in Stitch. {{ sso-admin }}
  {% endcapture %}

  {% include note.html first-line="**Stitch SSO Admin privileges required**" content=sso-admin-note %}

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
      **SSO Admin privileges in Stitch.** {{ sso-admin }}

  - item: |
      **Privileges in {{ page.display-name }} that allow you to add and configure applications.** If you don't have this privilege, **contact a {{ page.display-name }} admin before continuing**.

      Refer to [{{ page.display-name }}'s documentation](https://onelogin.service-now.com/support/?id=kb_article&sys_id=12d1703fdb4c2050ca1c400e0b9619c1&kb_category=fdf52dfcdbd45340d5505eea4b96192b){:target="new"} for more info.


# -------------------------- #
#           Content          #
# -------------------------- #

steps:
  - title: "Create and configure a {{ page.display-name }} app"
    anchor: "create-configure-sso-app"
    summary: "Creating and configuring a {{ page.display-name }} app"
    content: |
      {% for substep in step.substeps %}
      - [Step 1.{{ forloop.index }}: {{ substep.title | flatify }}](#{{ substep.anchor }})
      {% endfor %}

    substeps:
      - title: "Retrieve your SSO info from Stitch"
        anchor: "retrieve-sso-info-from-stitch"
        content: |
          1. Sign into your Stitch account.
          2. TODO

      - title: "Create the app in {{ page.display-name }}"
        anchor: "create-app-in-onelogin"
        content: |
          1. Sign into your {{ page.display-name }} account.
          2. Click **Applications** in the top navigation.
          3. On the **Applications** page, click **Add App**.
          4. In the search box, enter `saml test`.
          5. In the results, click **SAML Test Connector (Advanced)**:

             ![Highlighted SAML Test Connector (Advanced) app in OneLogin application search results]({{ site.baseurl }}/images/account-security/sso/onelogin-app-selection.png)

          6. On the app configuration page, enter a **Display Name** for the app. This is the name that will also display on the app's tile for users in your {{ page.display-name }} instance.
          7. Click **Save**.

      - title: "Define the app's configuration settings"
        anchor: "define-app-configuration-settings"
        content: |
          1. After the app successfully saves, click **Configuration** on the left side of the page.
          2. In the **Application details** section, fill in the following fields:
             - **Audience**: Paste the value from the **Audience** field in Stitch.
             - **Recipient**: Paste the value from the **Recipient** field in Stitch.
             - **ACS (Consumer) URL**: Paste the value from the **ACS (Consumer) URL** field in Stitch.
             - **ACS (Consumer) URL Validator**: Paste the value from the **ACS (Consumer) URL Validator** field in Stitch.

             This is how the page should look when you're finished:

             ![TODO]()

      - title: "Define the app's parameters"
        anchor: "define-app-parameters"
        parameters:
          - saml-name: "given_name"
            value: "First Name"
          - saml-name: "family_name"
            value: "Last Name"
          - saml-name: "email"
            value: "Email"
        content: |
          Next, you'll add the following parameters to the app:

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

          1. Click **Parameters** on the left side of the page.
          2. Click the **plus button** to add a parameter.
          3. In the **New Field** window that displays:
             1. In the **Field name** field, enter the **SAML Attribute Name** of the parameter. For example: `given_name`
             2. In the **Flags** section, check the **Include in SAML assertion** box.
             3. Click **Save**.
          4. In the **Edit Field** window that displays, select the corresponding **Value** from the dropdown. For example: `First Name` is the value for the **SAML Attribute** `given_name`.
          5. Click **Save**.
          6. Repeat steps 2-5 for the remaining parameters.

          This is how the page should look when all the parameters have been added:

          ![Stitch parameters fully configured for the OneLogin app]({{ site.baseurl }}/images/account-security/sso/onelogin-parameters.png)

      - title: "Save the app configuration"
        anchor: "save-app-configuration"
        content: |
          After you've finished defining the app's [configuration settings](#define-app-configuration-settings) and [parameters](#define-app-parameters), click the **Save** button in the upper right section of the page.

      - title: "Download the app's SAML metadata file"
        anchor: "download-app-saml-metadata-file"
        content: |
          The last step is to download your app's SAML metadata file. This is required to connect your {{ page.display-name }} app with Stitch and enable SSO.

          1. Click the **More Actions** menu in the upper right section of the page.
          2. Click **SAML Metadata**.
          3. Download the file somewhere convenient.

  - title: "Connect to Stitch"
    anchor: "connect-to-stitch"
    summary: "Connecting your {{ page.display-name }} app to Stitch"
    content: |
      Navigate back to the page where your Stitch account is open. If you closed this page, navigate to [TODO]

      1. In Stitch, scroll down to the **Connect to Stitch** section of the {{ page.display-name }} setup page.
      2. Click **Upload SAML Metadata**.
      3. Locate and select the SAML metadata file you downloaded in [Step 1.6](#download-app-saml-metadata-file).

  - title: "Activate SSO"
    anchor: "activate-sso"
    summary: "Activating SSO for your Stitch account"
    content: |
      When finished, click the **Activate SSO** button.

next-steps: |
  TODO
---