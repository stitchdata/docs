---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

product-type: "connect"
content-type: "api-form"
form-type: "destination"
key: "destination-form-properties-azure-sql-data-warehouse-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Microsoft Azure SQL Data Warehouse Destination Form Property"
api-type: "azuresql_dw"
display-name: "Azure SQL Data Warehouse"

docs-name: "microsoft-azure"
db-type: "mssql"

description: ""


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-common-fields: true
## See these fields in _data/connect/common/destination-forms.yml > all-destinations

object-attributes:
  - name: "azure_storage_account_token"
    type: "string"
    required: true
    description: |
      An Azure Storage Access Key. This is used to access Azure Blob Storage, which Stitch uses to stage data for Polybase before loading it into an {{ form-property.display-name }} destination.

      For more info and instructions for generating this credential, refer to our [{{ form-property.display-name }} setup documentation]({{ link.destinations.setup.azure | prepend: site.baseurl | append: "#retrieve-storage-access-key" }}).
    value: |
      "<AZURE_STORAGE_ACCESS_KEY>"


  - name: "azure_storage_sas_url"
    type: "string"
    required: true
    description: |
      An Azure Blob service Shared Access Signature (SAS) URL, which is used to grant Stitch restricted access to Azure Storage resources. These resources are used to load data into an {{ form-property.display-name }} destination.

      For more info and instructions for generating this credential, refer to our [{{ form-property.display-name }} setup documentation]({{ link.destinations.setup.azure | prepend: site.baseurl | append: "#generate-shared-access-signature-url" }}).
    value: |
      "<AZURE_STORAGE_SAS_URL>"
---