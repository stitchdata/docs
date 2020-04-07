---
title: Authentication
product-type: "connect"
content-type: "api-doc"
order: 3

anchor: "authentication-overview"

sections:
  - content: |
      {% assign api = site.data.connect.api %}
      Authenticate your calls to the API by providing an access token in your requests. Each access token is associated with a single Stitch client account. Access tokens do not expire, but they may be revoked by the user at any time.

      Additionally, each request's permissions are limited to that Stitch client account.

      In the examples in this documentation, we use bearer auth:

      {% capture code %}curl -X GET {{ api.base-url }}{{ api.core-objects.sources.base }} \
           -H "Authorization: Bearer <ACCESS_TOKEN>"
      {% endcapture %}

      {% assign description = "GET " | append: api.core-objects.sources.base %}

      {% include layout/code-snippet.html code-description=description language="json" code=code %}

      All requests must be made over HTTPS or they will fail. API requests that don't contain authentication will also fail.

  - title: "Obtain an API access token"
    anchor: "obtain-access-token"
    content: |
      How you obtain an access token depends on the type of user you are:

      - **Individual Stitch user**: You will be using the API to programmatically control your own Stitch client account. You can create, revoke, and delete API access tokens on the [Account Settings page]({{ link.account.manage-api-keys | prepend: site.baseurl }}) of your Stitch client account.

      - **Stitch partner**: You will be performing actions in Stitch client accounts on behalf of users who authorize your API client. You'll need to [register as an API client]({{ site.data.connect.api.interest-form }}){:target="new"} and refer to the [Partner API Authentication guide]({{ link.connect.guides.partner-authentication | prepend: site.baseurl }}) for instructions.

  - title: "Credential reference"
    anchor: "credential-reference"
    credentials:
      - name: "API access token"
        prefix: "ac_"
        definition: "{{ site.data.connect.general.authentication.client-account-access-token }}"
        obtained-by: "Refer to the [Obtain an API access token section](#obtain-access-token)"
        required-for: "All API requests, except for Create an account"
        expiration: "None"

      - name: "Partner ID"
        prefix: "oc_"
        definition: "{{ site.data.connect.general.authentication.partner-id | flatify }}"
        obtained-by: &partner-obtain "Submitting an [interest form]() and being approved by Stitch as a partner"
        required-for: "Requests to the Create an account endpoint"
        expiration: "None"

      - name: "Partner secret"
        prefix: "oc_"
        definition: "{{ site.data.connect.general.authentication.partner-key | flatify }}"
        obtained-by: *partner-obtain
        required-for: "Requests to the Create an account endpoint"
        expiration: "None"

      - name: "Ephemeral token"
        prefix: "Not applicable"
        definition: |
          A token passed to the Connect JavaScript client to create a session in the Stitch web application and log a user into a Stitch client account.
        obtained-by: "A successful request to the [Create a session endpoint]({{ link.connect.api | prepend: site.baseurl | append: site.data.connect.core-objects.sessions.section }})"
        required-for: "Creating a temporary Stitch session using the Connect JavaScript client"
        expiration: "One hour after generation"

      - name: "Session token"
        prefix: "Not applicable"
        definition: |
          A token used to create a temporary Stitch session for the user for whom the exchanged ephemeral token was created.
        obtained-by: "Exchanging a valid ephemeral token in a Connect JavaScript function"
        required-for: "Creating a temporary Stitch session using the Connect JavaScript client"
        expiration: "Upon session termination or after 12 hours, whichever is first"

    content: |
      This section contains a list of the different credentials refered to throughout the Connect documentation. 

      {% assign attributes = "name|prefix|details" | split:"|" %}
      {% assign details = "definition|required-for|obtained-by|expiration" | split:"|" %}

      <table class="attribute-list">
      <tr>
      {% for attribute in attributes %}
      {% if forloop.first == true %}
      <td align="right">
      {% else %}
      <td>
      {% endif %}
      <strong>{{ attribute | replace:"-"," " | capitalize }}</strong>
      </td>
      {% endfor %}
      </tr>
      {% for credential in section.credentials %}
      <tr>

      <td align="right" width="20%; fixed">
      <strong>{{ credential.name }}</strong>
      </td>

      <td width="8%; fixed">
      {{ credential.prefix }}
      </td>

      <td>
      <ul>
      {% for detail in details %}
      <li style="margin-top: 0px;">
      {% capture copy %}
      **{{ detail | replace:"-"," " | capitalize }}:** {{ credential[detail] | flatify  }}
      {% endcapture %}

      {{ copy | flatify | markdownify }}
      </li>
      {% endfor %}
      </ul>
      </td>

      </tr>
      {% endfor %}
      </table>
---