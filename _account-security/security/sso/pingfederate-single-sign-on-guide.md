---
# -------------------------- #
#      Page & Formatting     #
# -------------------------- #

title: Enabling Single Sign-On Using PingFederate
permalink: /account-security/single-sign-on/enabling-pingfederate-saml
summary: "Connect your PingFederate account to Stitch and enable Single Sign-On (SSO)."

input: false
layout: tutorial
feedback: true

key: "single-sign-on-pingfederate"
type: "security"
weight: 4


# -------------------------- #
#         IdP Details        #
# -------------------------- #

idp: true
name: "pingfederate"
display-name: "PingFederate"

setup-name: "PingFederate SAML"

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
      **Administrator privileges in {{ page.display-name }}.** If you don't have these privileges, **contact a {{ page.display-name }} admin before continuing**.

  - item: |
      **Familiarity with {{ page.display-name }} and an existing {{ page.display-name }} adapter instance and signing certificate.** Instructions for configuring {{ page.display-name }} assets are outside the scope of this tutorial; these instructions assume you're familiar with {{ page.display-name }} and have your instance set up already. If you're not sure how to use {{ page.display-name }}, **contact a {{ page.display-name }} admin before continuing.**


# -------------------------- #
#           Content          #
# -------------------------- #

steps:
  - title: "Create and configure an SP connection in {{ page.display-name }}"
    anchor: "create-the-sp-connection"
    summary: "Creating and configuring an SP connection in {{ page.display-name }}"
    content: |
      {% include note.html type="single-line" content="**Note**: This guide was written for PingFederate v10.0.1.5. As a result, the location or names of some pages and fields may be different for you depending on your version." %}

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

      - title: "Define the SP connection's general settings"
        anchor: "define-sp-connection-general-settings"
        content: |
          1. Sign into your {{ page.display-name }} account as an administrator.
          2. Under **SP Connections**, click **Create New**:
             
             ![Create New button, highlighted, in the Identity Provider page of PingFederate]({{ site.baseurl }}/images/account-security/sso/pingfederate-create-new-sp-connection.png)
          
          3. In the **Connection Template** tab, select **Do not use a template ...** and then click **Next**.
          4. In the **Connection Type** tab, check **Browser SSO Profiles** and then click **Next**.
          5. In the **Connection Options** tab, check **Browser SSO** and then click **Next**.
          6. In the **Import Metadata** tab, select **None** and then click **Next**.
          7. In the **General Info** tab, fill in the following:
             - **Partner's Entity ID (Connection ID)**: Paste the **Entity ID** value from Stitch into this field.
             - **Connection Name**: Enter a name for the connection. For example: `Stitch`
             - **Base URL**: Paste the **Base URL** value from Stitch into this field.

             The page should look similar to the following:
             
             ![General Info tab of the SP Connection setup flow in PingFederate]({{ site.baseurl }}/images/account-security/sso/pingfederate-connection-general-info-tab.png)

          8. When finished, click **Next**.

      - title: "Define the SP connection's browser SSO configuration"
        anchor: "define-browser-sso-configuration"
        content: |
          {% for substep in substep.sub-substeps %}
          - [Step 1.3.{{ forloop.index }}: {{ substep.title | flatify }}](#{{ substep.anchor }})
          {% endfor %}

        sub-substeps:
          - title: "Define the SP connection's attribute contract"
            anchor: "define-app-attribute-contract"
            content: |
              Next, you'll define the user attributes for the app:

              <table>
                <tr>
                  <td>
                    <strong>#</strong>
                  </td>
                  <td>
                    <strong>SAML attribute name</strong>
                  </td>
                  <td>
                    <strong>Attribute name format</strong>
                  </td>
                </tr>
                {% for parameter in page.saml-parameters %}
                  <tr>
                    <td>
                      {{ forloop.index }}
                    </td>
                    <td>
                      {{ parameter.saml-name }}
                    </td>
                    <td>
                      {{ parameter.attribute-name-format }}
                    </td>
                  </tr>
                {% endfor %}
              </table>

              1. On the **Browser SSO** page, click the **Configure Browser SSO** button.
              2. On the **SAML Profiles** page:
                 1. Check **IDP-Initiated SSO** and **SP-Initiated SSO**.
                 2. Click **Next**.
              3. In the **Assertion Lifetime** tab, click **Next**.
              4. In the **Assertion Creation** tab:
                 1. Click **Configure Assertion Creation**.
                 2. In the **Identity Mapping** tab, select **Standard** and then click **Next**.
                 3. In the **Attribute Contract** tab:
                    1. In the **SAML_SUBJECT > Subject Name Format** field, select `urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress`.
                    2. In **Extend the Contract** section:
                       1. In the blank field, enter the **SAML attribute name** of an attribute in the table above. For example: `email`
                       2. In the **Attribute Name Format** field, select `urn:oasis:names:tc:SAML:2.0:attrname-format:basic`.
                       3. Repeat these steps until all attributes in the table have been added. The page should look similar to the following:

                          ![Identity Mapping tab in the SP Connection > Browser SSO setup flow]({{ site.baseurl }}/images/account-security/sso/pingfederate-attribute-contract-tab.png)

                    3. When finished, click **Next**.

          - title: "Define the SP connection's authentication source map"
            anchor: "define-sp-connection-authentication-source-map"
            content: |
              {% include note.html type="single-line" content="**Note**: These instructions assume you already have an adapter instance set up in your PingFederate account. If you don't, you'll need to create one first and then follow these steps." %}

              1. In the **Authentication Source Mapping** tab, click **Map New Adapter Instance**.
              2. In the **Adapter Instance** tab, select the instance you want to use and click **Next**.
              3. In the **Mapping Method** tab, select **Use only the adapter contract values in the SAML assertion** and click **Next**.
              4. In the **Attribute Contract Fulfillment** tab, populate each of the **Attribute Contract** values according to your Adapter Instance.
              5. When finished, click **Next**.

          - title: "Complete the SP connection's assertion creation"
            anchor: "complete-assertion-creation"
            content: |
              1. In the **Issuance Criteria** tab, click **Next**.
              2. In the **Summary** tab, click **Done**. 
              3. You'll be redirected back to the **Authentication Source Mapping** tab. Click **Next**.
              4. On the **Summary** tab, click **Done**.
              5. You'll be redirected back to the **Assertion Creation** tab. Click **Next**.

          - title: "Define the SP connection's protocol settings"
            anchor: "define-sp-connection-protocol-settings"
            content: |
              1. In the **Protocol Settings** tab, click **Configure Protocol Settings**.
              2. In the **Assertion Consumer Service URL** tab, fill in the following:
                 1. Check the **Default** box.
                 2. **Binding**: Select **POST**.
                 3. **Endpoint URL**: Paste the **Endpoint URL** value from Stitch.
                 4. Click **Add**. The page should look similar to the following:

                    ![Assertion Consumer Service URL tab in the SP Connection > Browser SSO configuration flow]({{ site.baseurl }}/images/account-security/sso/pingfederate-consumer-service-url-tab.png)
                 5. Click **Next**.
              3. In the **Allowable SAML Bindings** tab:
                 1. Check **POST** and **REDIRECT**.
                 2. Click **Next**.
              4. Accept the defaults for the **Signature Policy** and **Encryption Policy** tabs by clicking **Next**.
              5. In the **Summary** tab, review the configuration and click **Done** when finished.
              6. You'll be redirected back to the **Protocol Settings** tab. Click **Next**.
              7. In the **Summary** tab, click **Done** to complete the app's browser SSO configuration.

      - title: "Configure the SP connection's credentials"
        anchor: "configure-sp-connection-credentials"
        content: |
          {% include note.html type="single-line" content="**Note**: These instructions assume you already have a signing certificate set up in your PingFederate account. If you don't, you'll need to create one first and then follow these steps." %}

          1. After clicking **Done**, you'll be redirected back to the **Browser SSO** tab. Click **Next**.
          2. In the **Credentials** tab, click **Configure Credentials**.
          3. In the **Digital Signature Settings** tab, select a **Signing Certificate**.
          4. Check these boxes:
             - **Include the certificate in the signature [KEYINFO] element**
             - **Include the raw key in the signature [KEYVALUE] element**

             The page should look similar to the following:

             ![Digital Signature Settings tab in the SP Connection > Credentials setup flow]({{ site.baseurl }}/images/account-security/sso/pingfederate-configure-digital-signature-settings.png)
          5. When finished, click **Next**.
          6. On the **Summary** tab, click **Done**.

      - title: "Grant users access"
        anchor: "grant-user-access"
        content: |
          The last step to configuring the connection is to grant access to users in your {{ page.display-name }} instance. This ensures that they'll be able to access Stitch via SSO.

          Using the process your organization follows, grant Stitch {{ page.display-name }} access to your colleagues.

  - title: "Download the SP connection's SAML metadata file"
    anchor: "download-sp-connection-saml-metadata-file"
    summary: "Downloading the SP connection's SAML metadata file"
    content: |
      1. In the left sidenav, click **Settings > System**.
      2. On the **System** page, click **SAML Metadata > Metadata Export**.
      3. In the **Metadata Role** tab, select **I am the Identity Provider (IDP)** and  click **Next**.
      4. In the **Metadata Mode** tab, select **Use a connection for metadata generation** and click **Next**.
      5. In the **Connection Metadata** tab, select the SP connection you created in [Step 1](#create-the-sp-connection) and click **Next**.
      6. In the **Metadata Signing** tab:
         1. Select your **Signing Certificate**.
         2. Check these boxes:
            - **Include the certificate in the signature [KEYINFO] element**
            - **Include the raw key in the signature [KEYVALUE] element**
         3. Click **Next**.
      7. In the **Export & Summary** tab, click **Export**. Save the file somewhere convenient - you'll need it to complete the setup in Stitch.

  - title: "Connect to Stitch"
    anchor: "connect-to-stitch"
    summary: "Connecting your {{ page.display-name }} SP connection to Stitch"
    content: |
      Navigate back to the page where your Stitch account is open.

      1. In Stitch, scroll down to the **Connect to Stitch** section of the {{ page.display-name }} setup page.
      2. Click **Upload SAML Metadata**.
      3. Locate and select the SAML metadata file you downloaded in [Step 2](#download-sp-connection-saml-metadata-file).

  - title: "Activate SSO"
    anchor: "activate-sso"
    summary: "Activating SSO for your Stitch account"
    content: |
      When finished, click the **Activate SSO** button.

next-steps: |
  After you've enabled SSO for your Stitch account, remember to grant Stitch access to users in your {{ page.display-name }} instance, if you haven't already.


# -------------------------- #
#          Metadata          #
# -------------------------- #

saml-parameters:
  - saml-name: "given_name"
    attribute-name-format: &attribute-name-format "urn:oasis:names:tc:SAML:2.0:attrname-format:basic"
  - saml-name: "family_name"
    attribute-name-format: *attribute-name-format 
  - saml-name: "email"
    attribute-name-format: *attribute-name-format
---