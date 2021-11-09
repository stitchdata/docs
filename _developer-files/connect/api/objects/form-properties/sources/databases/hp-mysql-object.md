---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/connect-templates/database-source-form-property/
## FOR INSTRUCTIONS & REFERENCE INFO


# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

product-type: "connect"
content-type: "api-form"
form-type: "source"
key: "source-form-properties-hp-mysql-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "MySQL (HP) Source Form Property"
api-type: "platform.hp-mysql"
display-name: "MySQL (HP)"

source-type: "database"
docs-name: "mysql"
db-type: "mysql"

property-description: |
  MySQL databases

description: |
  **Note**: This version of the MySQL source differs from the version used by the `platform.mysql` form property. Refer to the [{{ form-property.display-name }} integration feature summary]({{ doc-link | append: "#feature-summary" }}) for more info.


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-common-fields: true
uses-feature-fields: true
uses-start-date: true

object-attributes:
  - name: "ssl_ca"
    type: "string"
    required: false
    description: |
      **Optional**: The certificate (typically a CA or server certificate) Stitch should verify the SSL connection against. The connection will succeed only if the server's certifcate verifies against the certificate provided.

      **Note**: Providing a certifcate via this property isn't required to use SSL. This is only if Stitch should verify the connection against a specific certificate.
    value: "<SSL_CERTIFICATE>"
  
  - name: "ssl_cert"
    type: "string"
    required: false
    description: |
      **Optional**: If `ssl_client_auth_enabled: true`, the SSL client authentication cerficiate stitch should use. The `ssl_key` property must also be provided to ensure the connection is successful.
    value: "<CA_CERTIFICATE>"

  - name: "ssl_key"
    type: "string"
    required: false
    description: |
      **Optional**: If `ssl_client_auth_enabled: true`, the SSL client authentication key stitch should use. The `ssl_ca` property must also be provided to ensure the connection is successful.
    value: "<CA_KEY>"
    
  - name: "verify_mode"
    type: "string"
    required: false
    description: |
      **Optional**: SSL certificate verification is enabled when a Certificate Authority (CA) is provided. If `true`, Stitch will enforce it in lieu of a custom CA. Accepted values are:

      - `true`
      - `false'

      **Note**: If you don't want to use a custom CA, this property and the `check_hostname` property should both be enabled (`true`).
    value: "true"        
---