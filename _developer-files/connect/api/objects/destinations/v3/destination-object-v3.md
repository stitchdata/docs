---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

product-type: "connect"
content-type: "api-version-object"
endpoint: "destinations"

# -------------------------- #
#        VERSION INFO        #
# -------------------------- #

version: "3"

# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

object-attributes:
  - name: "connection"
    type: "object"
    sub-type: "destination form properties"
    url: "{{ api.form-properties.destination-forms.section }}"
    description: |
      Parameters for connecting to the destination, excluding any sensitive credentials.

      The parameters must adhere to the type of destination.

      **Note**: This has been renamed to `properties` in v4 of the Destinations endpoint.

  - name: "last_check"
    type: "timestamp"
    # sub-type: "connection check"
    # url: "{{ api.data-structures.connection-checks.section }}"
    description: |
      The time the last connection check to the destination completed.

      **Note**: This field has been deprecated in v4 of the Destinations endpoint.
---