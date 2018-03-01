---
# -------------------------- #
#        Page Controls       #
# -------------------------- #
title: Amazon S3 Destination
permalink: /destinations/amazon-s3/
layout: destination-overview
tags: [bigquery_destination]
keywords: amazon-s3, amazon-s3, amazon-s3 data warehouse, amazon-s3 etl, etl to amazon-s3
summary: &summary "{{ destination.display_name }} is an extremely simple, reliable, and cost-effective object store that provides nearly endless capacity to safely store data in the cloud. Its flexibility allows users the ability to not only persist data ranging from bytes to petabytes, but also consume it via a myriad of tools like Amazon Athena and Qubole."
toc: true
destination: true

# -------------------------- #
#    Destination Details     #
# -------------------------- #
display_name: "Amazon S3"
type: "amazon-s3"
db-type: "s3"
pricing_tier: "standard"
status: "Closed Beta"
description: *summary
pricing_model: "Storage"
free_option: "Yes (plan & trial)"
fully-managed: false
pricing_notes: "{{ destination.display_name }} pricing is based on two factors: the amount of data stored in and location (region) of your {{ destination.display_name }} bucket."
icon: /images/destinations/icons/amazon-s3.svg


# -------------------------- #
#           Support          #
# -------------------------- #
replication-methods: "All"
connection-methods: "n/a"
supported-versions: "n/a"

nested-structures: true ## if true, natively supports nested structures
case: "Case Insensitive"
table-name-limit: "" ## max # of characters
column-name-limit: "" ## max # of characters
column-limit: "" ## max # of columns allowed in tables
timestamp-range: ""
timezones:
  supported: false
  storage: ""
varchar-limit: "" ## max width for varchars
decimal-limit: ""
decimal-range: ""
reserved-words: ""


# -------------------------- #
#    Object Key Elements     #
# -------------------------- #
key-elements:
  - name: "integration_name"
    required: true
  - name: "table_name"
    required: true
  - name: "table_version"
    required: true
  - name: "timestamp_loaded"
    required: true
    description: " - <strong>Note</strong>: This is a Unix timestamp."
  - name: "year_loaded"
    required: false
  - name: "day_loaded"
    required: false
  - name: "month_loaded"
    required: false
  - name: "hour_loaded"
    required: false
  - name: "Arbitrary text"
    required: false

default-key: "[integration_name]/[table_name]/[table_version]_[timestamp_loaded].[csv|jsonl]"
example-key-1: "salesforce-prod/account/1_1519235654474.[csv|jsonl]"
example-key-2: "salesforce-prod/opportunity/1_1519327555000.[csv|jsonl]"

# -------------------------- #
#    Required Permissions    #
# -------------------------- #
permissions:
  - name: "s3:PutObject"
    operations:
      - name: "PUT Object"
        link: "https://docs.aws.amazon.com/AmazonS3/latest/API/RESTObjectPUT.html"
        description: "Allows the addition of objects to a bucket."

      - name: "POST Object"
        link: "http://docs.aws.amazon.com/AmazonS3/latest/API/RESTObjectPOST.html"
        description: "An alternate form of `PUT Ojbect`, this allows the addition of objects to a bucket using HTML forms."

      - name: "Initiate Multipart Upload"
        link: "https://docs.aws.amazon.com/AmazonS3/latest/API/mpUploadInitiate.html"
        description: "Allows a multipart upload and return of an upload ID."

      - name: "Upload Part"
        link: "http://docs.aws.amazon.com/AmazonS3/latest/API/mpUploadUploadPart.html"
        description: "Allows for the upload of a part in a multipart upload."

      - name: "Complete Multipart Upload"
        link: "https://docs.aws.amazon.com/AmazonS3/latest/API/mpUploadComplete.html"
        description: "Allows for the completion of a multipart upload by assembling previously uploaded parts."

      - name: "PUT Object - Copy"
        link: "https://docs.aws.amazon.com/AmazonS3/latest/API/mpUploadUploadPartCopy.html"
        description: "Allows for the upload of a part by copying data from an existing object as the data source."
  - name: "s3:GetObject"
    operations:
      - name: "GET Object"
        link: "http://docs.aws.amazon.com/AmazonS3/latest/API/RESTObjectGET.html"
        description: "Allows for the retrieval of objects from {{ destination.display_name }}."

      - name: "HEAD Object"
        link: "https://docs.aws.amazon.com/AmazonS3/latest/API/RESTObjectHEAD.html"
        description: "Allows for the retrieval of metadata from an object without returning the object itself."
  - name: "s3:ListBucket"
    operations:
      - name: "GET Bucket (List Objects)"
        link: "http://docs.aws.amazon.com/AmazonS3/latest/API/v2-RESTBucketGET.html"
        description: "Allows for the return of some or all (up to 1,000) of the objects in a bucket."

      - name: "HEAD Bucket"
        link: "http://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketHEAD.html"
        description: "Used to determine if a bucket exists and access is allowed."


# -------------------------- #
#    Incompatible Sources    #
# -------------------------- #
incompatible-with: 0



# -------------------------- #
#            Links           #
# -------------------------- #
status-url: https://status.aws.amazon.com/
sign-up: https://aws.amazon.com/s3/
documentation: https://aws.amazon.com/documentation/s3/
pricing: https://aws.amazon.com/s3/pricing/
price-calculator: http://aws.amazon.com/calculator/


# -------------------------- #
#      Overview Content      #
# -------------------------- #

introduction: "{{ destination.description | flatify }}"

sections:
  - title: "pricing"
    content: |
      {{ destination.pricing_notes | flatify }}

      To learn more about pricing, refer to Amazon's S3 [pricing page]({{ destination.pricing }}). **Note**: Remember to select the correct region to view accurate pricing.

  - title: "setup"
    content: |
      To use {{ destination.display_name }} as your Stitch destination, you'll need to:

      - Create an S3 bucket,
      - Allow Stitch to access the bucket,
      - Define the format data will be stored in, and
      - Define the bucket's Key, which determines how files are organized in the bucket

      **[Spin up a {{ destination.display_name }} data warehouse]({{ link.destinations.setup.amazon-s3 | prepend: site.baseurl }})**

  - title: "replication"
    include: |
      {% include destinations/overview-replication-process.html %}

  - title: "schema"
    content: |
      The file structure of your integrations' data in your {{ destination.display_name }} bucket depends on two destination setup parameters:

      1. The definition of the Object Key, and
      2. The selected data storage format (CSV or JSON)

    subsections:
      - title: "Object Keys and File Structure"
        anchor: "object-keys-file-structure"
        content: |
          {{ destination.display_name }} uses what is called an Object Key to uniquely identify objects in a bucket. During the Stitch setup process, you have the option of using our default Object Key or defining your own using a handful of Stitch-approved elements. Refer to the [{{ destination.display_name }} Setup instructions]({{ link.destinations.setup.amazon-s3 | prepend: site.baseurl | append: "#define-s3-object-key" }}) for more info on the available elements.

          The S3 Key setting determines the convention Stitch uses to create Object Keys when it writes to your bucket. It also defines the folder structure of Stitch-replicated data.

          Below is the default Key and two examples of an Object Key that an integration named `salesforce-prod` might produce:

          ```shell
          /* Default Key */
          {{ destination.default-key }}


          /* Example Object Key */
          {{ destination.example-key-1 }}
          {{ destination.example-key-2 }}
          ```

          As previously mentioned, the S3 Key also determines the folder structure of replicated data. In the AWS console, the folder structure for the `salesforce-prod` integration would look like the following:

          ```shell
          .
          └── salesforce-prod
              └── account
              |   └── 1_1519235654474.[csv|jsonl]
              └── opportunity
              |   └── 1_1519327555000.[csv|jsonl]
              └── _sdc_rejected
                  └── 1_[timestamp].jsonl
                  └── 1_[timestamp].jsonl
          ```

      - title: "Data Storage Formats"
        anchor: "data-storage-formats"
        content: |
          Stitch will store replicated data in the format you select during the initial setup of {{ destination.display_name }}. Currently Stitch supports storing data in CSV or JSON format for {{ destination.display_name }} destinations.

          The tabs below contain an example of raw source data and how it would be stored in {{ destination.display_name }} for each data storage format type. In this example, we're using data from [HubSpot workflows]({{ site.baseurl }}/integrations/saas/hubspot/#workflows).

          <ul id="profileTabs" class="nav nav-tabs">
              <li class="active">
                <a href="#original-data" data-toggle="tab">Raw Source Data</a>
              </li>
              <li>
                <a href="#csv-quoted" data-toggle="tab">CSV, Quoted</a>
              </li>
              <li>
                <a href="#csv-unquoted" data-toggle="tab">CSV, Unquoted</a>
              </li>
              <li>
                <a href="#json" data-toggle="tab">JSON</a>
              </li>
          </ul>
          <div class="tab-content">
              <div role="tabpanel" class="tab-pane active" id="original-data">
              {% highlight json %}
              {  
                 "id":2078178,
                 "updatedAt":1501802708000,
                 "name":"Onboarding",
                 "type":"DRIP_DELAY",
                 "enabled":false,
                 "inserted-at":1501802708000,
                 "personaTagIds":[  
                    {  
                       "value":"persona_1"
                    }
                 ],
                 "contactlistids":{  
                    "enrolled":5,
                    "active":0,
                    "steps":[  
                       {  
                          "value":0
                       }
                    ]
                 }
              }
              {% endhighlight %}
              </div>
              
              <div role="tabpanel" class="tab-pane" id="csv-quoted">
                <p>The resulting CSV would contain the fields shown below, along with the system fields Stitch uses.</p>

                <table width="100%">
                <tr>
                <th>
                id
                </th>
                <th>
                updatedAt
                </th>
                <th>
                name
                </th>
                <th>
                type
                </th>
                <th>
                enabled
                </th>
                <th>
                inserted-at
                </th>
                <th>
                contactListIds__enrolled
                </th>
                <th>
                contactListIds__active
                </th>
                </tr>
                <tr>
                <td>
                2078178
                </td>
                <td>
                1501802708000
                </td>
                <td>
                Onboarding
                </td>
                <td>
                DRIP_DELAY
                </td>
                <td>
                false
                </td>
                <td>
                1501802708000
                </td>
                <td>
                5
                </td>
                <td>
                0
                </td>
                </tr>
                </table>
              </div>

              <div role="tabpanel" class="tab-pane" id="csv-unquoted">
                  [PLACEHOLDER]
              </div>

              <div role="tabpanel" class="tab-pane" id="json">
              {% highlight json %}
              {  
                 "id":2078178,
                 "updatedAt":1501802708000,
                 "name":"Onboarding",
                 "type":"DRIP_DELAY",
                 "enabled":false,
                 "inserted-at":1501802708000,
                 "personaTagIds":[  
                    {  
                       "value":"persona_1"
                    }
                 ],
                 "contactlistids":{  
                    "enrolled":5,
                    "active":0,
                    "steps":[  
                       {  
                          "value":0
                       }
                    ]
                 }
              }
              {% endhighlight %}
              </div>
          </div>

---
{% assign destination = page %}
{% include misc/data-files.html %}