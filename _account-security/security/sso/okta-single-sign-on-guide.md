---
# -------------------------- #
#      Page & Formatting     #
# -------------------------- #

title: Enabling Single Sign-On Using Okta
permalink: /account-security/single-sign-on/enabling-okta
summary: "Connect your Okta account to Stitch and enable Single Sign-On (SSO)."

input: false
layout: tutorial
feedback: true

key: "single-sign-on-okta"
type: "security"
weight: 4


# -------------------------- #
#         IdP Details        #
# -------------------------- #

idp: true
name: "okta"
display-name: "Okta"


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
      **Application Management privileges in {{ page.display-name }} that allow you to add and configure applications.** If you don't have these privileges, **contact an {{ page.display-name }} admin before continuing**.

      Refer to [{{ page.display-name }}'s documentation](https://help.okta.com/en/prod/Content/Topics/Security/administrators-admin-comparison.htm#Applicat){:target="new"} for more info.


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
          1. Sign into your {{ page.display-name }} account as a user with privileges that allow you to add and configure apps.
          2. Click **Applications > Applications**.
          3. On the **Applications** page, click **Add Application**.
          4. On the **Add Application** page, click **Create New App**.
          5. In the **Create a New Application Integration** window, fill in the fields as follows:
             - **Platform**: This should default to `Web`. Leave it as-is.
             - **Sign on method**: Select `SAML 2.0`.
          6. Click **Create**.

      - title: "Define the app's general settings"
        anchor: "define-app-general-settings"
        content: |
          A **General Settings** page will display. Fill in the fields as desired, clicking **Next** when finished.

      - title: "Configure SAML for the app"
        anchor: "configure-app-saml"
        parameters:
          - saml-name: "given_name"
            value: "user.firstName"
          - saml-name: "family_name"
            value: "user.lastName"
          - saml-name: "email"
            value: "user.email"
        content: |
          Next, you'll configure SAML for the app on the **Configure SAML** page:

          {% for sub-substep in substep.sub-substeps %}
          - [Step 1.4.{{ forloop.index }}: {{ sub-substep.title }}](#{{ sub-substep.anchor }})
          {% endfor %}

        sub-substeps:
          - title: "Define the General settings"
            anchor: "configure-app-saml--general"
            content: |
              In the **General** section, fill in the following fields:

              - **Single sign on URL**: Paste the value from the **SSO URL** field in Stitch.
              - **Audience URI (SP Entity ID)**: Paste the value from the **SP Entity ID** field in Stitch.

              This is how the section should look after the fields have been populated:

              ![General SAML attribute fields populated in Okta]({{ site.baseurl }}/images/account-security/sso/okta-app-general-saml.png)

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

              1. Scroll down to the attributes section, located after the **Show Advanced Settings** link.
              2. In the **Field name** field, enter the **SAML Attribute Name** of the parameter. For example: `given_name`
              3. In the **Value** field, select the corresponding **Value** from the dropdown. For example: `user.firstName` is the value for the **SAML Attribute** `given_name`.
              4. Click **Add Another** to add the next attribute.
              5. Repeat steps 2-4 until all attributes have been added. This is how the section should look when all the parameters have been added:

                 ![Stitch attributes fully configured for the Okta app]({{ site.baseurl }}/images/account-security/sso/okta-attributes-screen.png)
              6. When finished, click **Next**.

      - title: "Save the app configuration"
        anchor: "save-app-configuration"
        content: |
          The next page that displays is the **Feedback** page. You can fill it out, or click **Finish** if you've finished defining the app's [general settings](#configure-app-saml--general) and [configuring its SAML](#configure-app-saml--attributes). 

      - title: "Download the app's SAML metadata file"
        anchor: "download-app-saml-metadata-file"
        content: |
          Next, you'll download your app's SAML metadata file. This is required to connect your {{ page.display-name }} app with Stitch and enable SSO.

          After the app has been saved, a page for the app will display in {{ page.display-name }}.

          1. If you're not in the **Sign On** tab, click it to navigate there.
          2. In the **Settings** section, locate the **Identity Provider metadata** link and click it:

             ![Highlighted Identity Provider metadata link in the Okta web app]({{ site.baseurl }}/images/account-security/sso/okta-download-saml-link.png)

             This will open a new tab in your browser with the SAML XML metadata for the app.
          3. Download/save this page, or copy and paste the XML data from the new tab into a text editor and save it as an `.xml` file. For example: `stitch-sso-saml-metadata.xml`

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
      3. Locate and select the SAML metadata file you downloaded in [Step 1.6](#download-app-saml-metadata-file).

  - title: "Activate SSO"
    anchor: "activate-sso"
    summary: "Activating SSO for your Stitch account"
    content: |
      When finished, click the **Activate SSO** button.

next-steps: |
  After you've enabled SSO for your Stitch account, remember to grant Stitch access to users in your {{ page.display-name }} instance, if you haven't already.
---