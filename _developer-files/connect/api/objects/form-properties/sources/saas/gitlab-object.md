---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

product-type: "connect"
content-type: "api-form"
form-type: "source"
key: "source-form-properties-gitlab-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "GitLab Source Form Property"
api-type: "platform.gitlab"
display-name: "GitLab"

source-type: "saas"
docs-name: "gitlab"

description: ""


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-start-date: true

object-attributes:
  - name: "api_url"
    type: "string"
    required: true
    description: |
      The URL for the {{ form-property.display-name }} API. This value must be `https://gitlab.com/api/v3`.
      
    value: "https://gitlab.com/api/v3"

  - name: "private_token"
    type: "string"
    required: true
    description: |
      A {{ form-property.display-name }} Personal Access token. Refer to the [{{ form-property.display-name }} documentation]({{ doc-link }}) for instructions on generating this credential.
    value: "<PRIVATE_TOKEN>"

  - name: "groups"
    type: "string"
    required: false
    description: |
      **Note**: While providing this property is optional, either `projects` or `groups` must be provided. You may also provide both properties.

      {% capture attribute-behavior %}
      A space separated list of groups you want to track. How data is replicated using this property depends on the value of the `{{ attribute.name }}` property:

      - If `groups` is provided but `projects` is not, all group projects will be replicated.
      - If `groups` and `projects` are provided, the selected projects of the provided groups will be replicated.
      - If `projects` is provided but `groups` is not, all selected projects will be replicated.
      {% endcapture %}

      {{ attribute-behavior | flatify }}
    value: "your-org/group-a"

  - name: "projects"
    type: "string"
    required: false
    description: |
      **Note**: While providing this property is optional, either `projects` or `groups` must be provided. You may also provide both properties.

      A space-separated list of projects you want to track.

      For example: In an organization named `stitch`, there are two projects to track: `stitch-data` and `stitch-docs`. To track them, this value would be: `stitch/stitch-data stitch/stitch-docs`

      {{ attribute-behavior | flatify }}
    value: "your-org/project-a your-org/project-b"
---