---
# -------------------------- #
#      Page & Formatting     #
# -------------------------- #

title: Enabling Single Sign-On Using Microsoft Azure Active Directory
permalink: /account-security/single-sign-on/enabling-azure-active-directory-saml
summary: "Connect your Microsoft Azure Active Directory account to Stitch and enable Single Sign-On (SSO)."

input: false
layout: tutorial
feedback: true

key: "single-sign-on-azure-ad"
type: "security"
weight: 4


# -------------------------- #
#         IdP Details        #
# -------------------------- #

idp: true
name: "azure-ad"
display-name: "Azure AD"

setup-name: "Azure Active Directory SAML"

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
  If this is the first time SSO is enabled, the Stitch user who configures the connection will become an SSO Admin. Additional SSO Admins may be added by contacting support.

  Refer to the [Team member roles and permissions documentation]({{ link.account.team-roles-permissions | prepend: site.baseurl }}) for more info about privileges in Stitch.
  {% endcapture %}

  {% capture sso-admin-note %}
  Setting up or modifying an existing {{ page.display-name }} connection requires SSO Admin privileges in Stitch. {{ sso-admin }}
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
      **[TODO] privileges in {{ page.display-name }} that allow you to add and configure applications.** If you don't have these privileges, **contact an {{ page.display-name }} admin before continuing**.

      Refer to [{{ page.display-name }}'s documentation](TODO){:target="new"} for more info.


# -------------------------- #
#           Content          #
# -------------------------- #

steps:
  - title: "Create and configure an {{ page.display-name }} SAML app"
    anchor: "create-configure-sso-app"
    summary: "Creating and configuring an {{ page.display-name }} SAML app"
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
          1. Sign into your Microsoft Azure account.
          2. In the search bar, enter `azure active directory` and click the **Azure Active Directory** result:

             ![The Azure Active Directory search result on the Azure dashboard]({{ site.baseurl }}/images/account-security/sso/azure-ad-search-result.png)

          3. On the page that displays, **verify you're in the correct tenant before proceeding**. Otherwise, click **Switch tenant** and navigate to the correct tenant.
          4. In the left sidenav, click **Manage > Enterprise applications**.
          5. On the page that displays, click **+ New application**. This will open the **{{ page.display-name }} Gallery** page.
          6. Click **+ Create your own application**.
          7. In the window that displays, fill in the fields as follows:

             - Enter a name for the app. For example: `Stitch Data Loader`
             - Check **Integrate any other application you don't find in the gallery (Non-gallery)**

                ![Populated fields in the Create your own application page in the Azure AD Gallery]({{ site.baseurl }}/images/account-security/sso/azure-ad-create-application-window.png)
          8. When finished, click **Create**.

          It may take a few minutes for the app to be created. When it's finished, you'll be redirected to the app's **Overview** page.

      - title: "Configure the app's Single Sign-on method using SAML"
        anchor: "define-app-sso-saml-method"
        content: |
          {% for sub-substep in substep.sub-substeps %}
          - [Step 1.3.{{ forloop.index }}: {{ sub-substep.title }}](#{{ sub-substep.anchor }})
          {% endfor %}

        sub-substeps:
          - title: "Define the basic SAML configuration"
            anchor: "define-basic-saml"
            content: |
              1. On the app's **Overview** page, click **Manage Single-sign on** in the left sidenav.
              2. On the **Select a single sign-on method** page, click **SAML**.
              3. On the page that displays, click **Basic SAML Configuration > Edit**:

                 ![The Edit link in the Basic SAML Configuration section, highlighted]({{ site.baseurl }}/images/account-security/sso/azure-ad-basic-saml-edit-link.png)

              4. In the window that displays, fill in the fields as follows:
                 - **Identifier (Entity ID)**: Copy and paste the **Identifier (Entity ID) value from Stitch** into this field and check the **Default** checkbox.
                 - **Reply URL**: Copy and paste the **Reply URL value from Stitch** into this field and check the **Default** checkbox.

                 The page should look similar to the following:

                 ![Populated Identifier and Reply URL fields in the Basic SAML Configuration page in Azure]({{ site.baseurl }}/images/account-security/sso/azure-ad-saml-configuration.png)
              5. When finished, click **Save**. You'll be redirected back to the app's **Set up Single Sign-On with SAML** page.

          - title: "Define the user attributes and claims"
            anchor: "define-user-attributes-claims"
            parameters:
              - saml-name: "given_name"
                value: "user.firstName"
              - saml-name: "family_name"
                value: "user.lastName"
              - saml-name: "email"
                value: "user.email"
            content: |
              Next, you'll define the user attributes for the app.

              1. On the app's **Set up Single Sign-On with SAML** page, click **User Attributes & Claims > Edit**.
              2. 

              TODO: The defaults for this part seem to match with what I'm seeing in other test apps in our account, meaning the user may not need to change anything?

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

          - title: "Download the app's federation metadata XML file"
            anchor: "download-app-saml-metadata-file"
            content: |
              The last step to configuing the app's SAML is to download its SAML metadata file, or the Federation Metdata XML file. This is required to connect your {{ page.display-name }} app with Stitch and enable SSO.

              1. In the **Set up Single Sign-On with SAML** page, scroll to the **SAML Signing Certificate** section.
              2. Next to the **Federation Metdata XML** field, click the **Download** link.
              3. Save the file somewhere handy - you'll need it to complete the setup in Stitch.

      - title: "Configure the app's permissions"
        anchor: "configure-app-permissions"
        content: |
          The last step to complete the app setup is to configure its permissions.

          1. Navigate back to your **Azure tenant's Overview page**. This will typically be the first link after **Home** in the breadcrumbs near the top of the page.
          2. In the left sidenav, click **Manage > App registrations**.
          3. In the **All applications** tab, click the app you created in [Step 1.2](#create-app).
          4. In the left sidenav, click **Manage > API permissions**.
          5. On the **API permissions** page, click **+ Add a permission.**
          6. Click **Microsoft Graph**, then **Delegated permissions**.
          {% include layout/inline_image.html type="right" file="account-security/sso/azure-ad-add-api-permissions.png" alt="The Request API permissions page in Azure with the Directory.Read.All permission displayed and checked" max-width="450px" %}
          {:start="7"}
          7. In the **Select permissions** section, add the following permissions:

             - `Directory.Read.All`
             - `User.Read`

             To add the permissions:

             1. Enter the permission name into the **Search** box.
             2. Locate the permission in the results and check the box next to its name.
             3. Repeat steps 1-2 for both permissions.
             4. When finished, click **Add permissions.**

             When the changes have been saved, you'll be redirected back to the **API permissions** page.
          8. On the **API permissions** page, click **Grant admin consent for [YOUR_APP_NAME]**.
          9. When prompted, click **Yes** to grant consent for the app's permissions.

  - title: "Connect to Stitch"
    anchor: "connect-to-stitch"
    summary: "Connecting your {{ page.display-name }} app to Stitch"
    content: |
      Navigate back to the page where your Stitch account is open.

      1. In Stitch, scroll down to the **Connect to Stitch** section of the {{ page.display-name }} setup page.
      2. Click **Upload SAML Metadata**.
      3. Locate and select the SAML metadata (Federation Metadata XML) file you downloaded in [Step 1.3.3](#download-app-saml-metadata-file).

  - title: "Activate SSO"
    anchor: "activate-sso"
    summary: "Activating SSO for your Stitch account"
    content: |
      When finished, click the **Activate SSO** button.

next-steps: |
  After you've enabled SSO for your Stitch account, remember to grant Stitch access to users in your {{ page.display-name }} instance.
---