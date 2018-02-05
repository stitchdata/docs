---
content-type: "embed-structure"
key: "properties-object"

title: "Properties"
description: "A properties object contains the properties necessary to complete a connection step. Returned within a source or destination object, these properties provide information about the configuration status of the connection."

object-attributes:
  - name: "name"
    type: "string"
    description: "The name of the property."

  - name: "required_to_be_fully_configured"
    type: "boolean"
    description: "If `true`, the property is required for complete configuration."

  - name: "provided"
    type: "boolean"
    description: "If `true`, the property has been provided."

  - name: "is_credential"
    type: "boolean"
    description: "If `true`, the property is a credential or otherwise sensitive data."

  - name: "system_provided"
    type: "boolean"
    description: "If `true`, the system provides this property."
---