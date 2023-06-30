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
      **Privileges in {{ page.display-name }} that allow you to add, configure, and register applications.** If you don't have these privileges, **contact an {{ page.display-name }} admin before continuing**.


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

                    **Note**: You can leave or remove the initial default `adapplicationregistry` Entity ID. If you leave it, verify that the **Default** box is checked next to the value from Stitch.
                 - **Reply URL**: Copy and paste the **Reply URL value from Stitch** into this field and check the **Default** checkbox.

                 The page should look similar to the following:

                 ![Populated Identifier and Reply URL fields in the Basic SAML Configuration page in Azure]({{ site.baseurl }}/images/account-security/sso/azure-ad-saml-configuration.png)
              5. When finished, click **Save**. You'll be redirected back to the app's **Set up Single Sign-On with SAML** page.

          - title: "Define the user attributes and claims"
            anchor: "define-user-attributes-claims"
            parameters:
              - saml-name: "given_name"
                value: "user.givenname"
              - saml-name: "family_name"
                value: "user.surname"
              - saml-name: "email"
                value: "user.mail"
            content: |
              Next, you'll define the user attributes for the app:

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
                {% for parameter in sub-substep.parameters %}
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

              By default, {{ page.display-name }} applications are created with user attributes. To make {{ page.display-name }} work with Stitch, you'll need to modify the default attributes so they map to the correct attributes in Stitch. **Note**: If preferred, you can delete the default attributes and re-create them, as long as the claim names and values match the table above.

              To modify the default attributes:

              1. On the app's **Set up Single Sign-On with SAML** page, click **User Attributes & Claims > Edit**. This opens the **User Attributes & Claims** page.
              2. For each of the attributes in the table above, perform the following:
                 1. In the **Additional claims** section, click a claim. For example: `user.mail`
                 2. On the **Manage claim** page, edit the **Name** field to match the corresponding **SAML Attribute Name** value in the table above. For example: For `user.mail`, the **Name** value should be `email`:

                    ![The Manage Claim page in Azure for the user.mail user attribute]({{ site.baseurl }}/images/account-security/sso/azure-ad-manage-claim.png)
                 3. When finished, click **Save**.

              When all the user attributes have been modified, the **Addtional claims** section should look like the following:

              ![The completed Additional claims section in Azure]({{ site.baseurl }}/images/account-security/sso/azure-ad-additional-claims.png)

          - title: "Download the app's federation metadata XML file"
            anchor: "download-app-saml-metadata-file"
            content: |
              The last step to configuring the app's SAML is to download its SAML metadata file, or the Federation Metadata XML file. This is required to connect your {{ page.display-name }} app with Stitch and enable SSO.

              **Note**: Downloading this file before completing the previous steps will result in errors in Stitch.

              1. In the **Set up Single Sign-On with SAML** page, scroll to the **SAML Signing Certificate** section.
              2. Next to the **Federation Metdata XML** field, click the **Download** link.
              3. Save the file somewhere handy - you'll need it to complete the setup in Stitch.

      - title: "Configure the app's permissions"
        anchor: "configure-app-permissions"
        content: |
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
      3. Locate and select the SAML metadata (Federation Metadata XML) file you downloaded in [Step 1.3.3](#download-app-saml-metadata-file).

  - title: "Activate SSO"
    anchor: "activate-sso"
    summary: "Activating SSO for your Stitch account"
    content: |
      When finished, click the **Activate SSO** button.

next-steps: |
  After you've enabled SSO for your Stitch account, remember to grant Stitch access to users in your {{ page.display-name }} instance, if you haven't already.
---