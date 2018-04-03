---
title: Import API
permalink: /integrations/import-api/
redirect_from: 
  - /integrations/import-api/faq
  - /integrations/import-api/revoking-an-api-access-token
layout: page
tags: [import_api]
keywords: import api, iapi, import, csv, api, api authentication, auth, upsert, validate, status, endpoint, method, methods, access token, api token, return codes, return code, response code, push, pushing data
summary: "The Stitch Import API - or IAPI for short - is a REST API that allows you to push arbitrary data into your data warehouse. With the IAPI you can replicate data from Google Sheets, CSVs, and a variety of other sources."

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "import-api"
display_name: "Import API"
author: "Stitch"
author-url: "https://www.stitchdata.com"
status-url: "http://status.stitchdata.com/"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: true

historical: "None"
frequency: "Continuous" 
tier: "Free"
icon:  /images/integrations/icons/import-api.svg
whitelist:
  tables: false
  columns: false

request-body-example: |
  [
   {
    "client_id": 4231,
    "table_name": "users",
      "sequence": 100,
    "action": "upsert",
    "key_names": [
     "id"
    ],
    "data": {
     "id": 10,
     "status": "pending"
    }
  ]


# -------------------------- #
#        Return Codes        #
# -------------------------- #

# See _data/taps/import-api/return-codes.yml


# -------------------------- #
#   Required Request Fields  #
# -------------------------- #

# See _data/taps/import-api/required-reqiest-body-fields.yml

---
{% assign integration = page %}
{% assign import-api = site.data.taps.import-api %}

{% include misc/data-files.html %}

The Stitch {{ integration.display_name }} is a REST API that allows you to push arbitrary data into your data warehouse. Once the data enters the {{ integration.display_name }}, it’ll be processed and sent through Stitch like data from any other integration.

The {{ integration.display_name }} accepts JSON or [Transit][transit] and returns JSON for all of its [methods](#methods). Each method uses a standard HTTP verb (`GET/POST`) and standard HTTP response codes for [returning statuses](#return-codes).

Before you get started, you may want to consider how you will prepare the data to send to the Import API. The [Singer](https://www.singer.io/) specification is a better way to write and collaborate on scripts that move data from databases, web APIs, files, and just about any data source to Stitch. If you develop a [Singer Tap](https://github.com/singer-io/getting-started#developing-a-tap) to pull data, you can then send it to the [Stitch Target](https://github.com/singer-io/target-stitch). 

If you decide to go this route, you do not need to worry about specific requests to the Import API as described in this doc. Rather, you can simply pass your [Stitch Import API token](https://www.stitchdata.com/docs/integrations/import-api#add-stitch-data-source) to the Stitch Target to get your data into an Import API connection.

That being said, if neither the Stitch integrations nor Singer scripts are for you, this document goes into detail on the functionality of our Import API.

---

## Security

Data submitted to the {{ integration.display_name }} is handled according to [Stitch's security standards]({{ link.account.security-faq | prepend: site.baseurl }}).

---

## Prerequisites

To use the {{ integration.display_name }}:

1. **You must have a Stitch account**. The {{ integration.display_name }} integration is available to all Stitch users, whether you’re on a Free or Paid tier.
2. **You'll need a bit of technical know-how**. Anyone comfortable writing and maintaining a small Ruby or PHP script should be more than qualified.

### Request Requirements

Requests sent to the Import API:

1. Must be valid JSON or Transit and specified in the request header. See the [Upsert](#upsert-method) section for more info.

   For more info on working with Transit, check out the [Transit GitHub repo][transit].
2. Must contain all of the required request body fields. See the [Upsert](#upsert-method) section for more info.
3. Must be less than 4MB
4. Must not contain arrays of data with more than 10,000 individual data points

More info about request requirements can be found in the [Upsert](#upsert-method) section.

---

## Authentication {#auth}

Authentication with the {{ integration.display_name }} is done with a single API access token placed in the `Authorization` header of your request and [your client ID](#client-id), which will be used in the request body.

### Step 1: Generate an API Access Token {#generate-api-token}

You can generate an API access token by logging into your Stitch account and adding an {{ integration.display_name }} integration:

{% include integrations/shared-setup/connection-setup.html %}

4. Click the {{ app.buttons.create-api-token }} button.

Your API access token has write access to your Stitch account, so **keep it secret, keep it safe.** 

Note that if someone does get ahold of your key, they won't be able to **access** your data - they'll only be able to send it. If at any time your API access token is lost or compromised, you can [revoke it and generate a new one](#revoke-access-token).

#### Example Request Header {#request-header-auth-example}

The API access token is used to authenticate to the {{ integration.display_name }} via bearer auth, as demonstrated in the example below:

{% highlight json %}
curl -X POST {{ import-api.endpoints.urls.upsert }} \
	-H 'Content-Type: application/json' \
	-H 'Authorization: Bearer < [access_token] >' \
	-d @filename
{% endhighlight %}

### Step 2: Locate Your Client ID {#client-id}

Your client ID is used in the request body in the `client_id` field to perform the second authentication step for the {{ integration.display_name }}.

Log into your Stitch account and look at the URL while you're on the {{ app.page-names.dashboard }} page to find your client ID. It's the number between `client` and `pipeline`:

{% highlight json %}
https://app.stitchdata.com/v2/client/XXXX/pipeline/connections    

    // XXXX is where your client ID will be
{% endhighlight %}

Note that your client ID can be between four and six digits.

### Example Request Body {#client-id-example}

```json
{{ integration.request-body-example }}
```

---

## Return Codes {#return-codes}

The {{ integration.display_name }} uses standard HTTP return codes to indicate the status of a request. Generally speaking, codes in: 

- the `2xx` range indicate success
- the `4xx` range indicate a bad request - for example: invalid or omitted credentials, a required field is missing, etc.
- the `5xx` range indicate an error on our end. We recommend checking our [status page]({{ site.status }}) for reported outages if you receive a code in this range. If nothing has been reported and these errors persist, please reach out to our support team.

Your app should handle each of the following return statuses gracefully:

{% assign return-codes = import-api.return-codes.codes %}

<table>
<tbody>
{% for code in return-codes %}
<tr>
<td width="27%; fixed" align="right" markdown="span">**{{ code.name }}**</td>
<td markdown="span">{{ code.description }}</td>
</tr>
{% endfor %}
</tbody>
</table>

---

## Methods {#methods}

The {{ integration.display_name }} supports three methods:

{% capture status %}The `status` endpoint can be used to determine if the Import API is operating correctly. This endpoint doesn't require any authentication.{% endcapture%}
{% capture validate %}The `validate` endpoint can be used to validate requests but will **not** persist them to Stitch.{% endcapture%}
{% capture upsert %}The `upsert` endpoint is used to push data into your data warehouse.{% endcapture%}

- [Status](#status-method) - {{ status }}
- [Validate](#validate-method) - {{ validate }} We recommend using this endpoint for development and testing.
- [Upsert](#upsert-method) - {{ upsert }}

### Status {#status-method}
{{ status }}

#### Example Request {#example-status-request}
{% highlight json %}
curl -i {{ import-api.endpoints.urls.status }}

200 OK - The Import API is operating correctly.
503 Service Unavailable - The Import API is experiencing problems. Do not attempt to post any data.
{% endhighlight %}

#### Example Response {#example-status-response}
{% highlight json %}
HTTP/1.1 200 OK
Content-Type: application/json;charset=UTF-8
Date: Thu, 07 Jan 2016 13:13:37 GMT
Server: http-kit
Vary: Accept
Content-Length: 53
Connection: keep-alive

{"name":"pipeline.gate","status":"OK"}
{% endhighlight %}

### Validate {#validate-method}

{{ validate }} This endpoint will validate your credentials, meaning you can check your token or `client-id` while developing and testing. If either credentials are invalid, a `403 Not Authenticated` message will be returned.

The behavior of this endpoint mirrors that of the `upsert` endpoint, with two exceptions:

- If the request is valid, a `200 OK` response will be returned.
- Regardless of whether Stitch is functional, a `503 Service Unavailable` response will never be returned.

#### Example Request {#example-validate-request}

{% highlight json %}
curl -X POST {{ import-api.endpoints.urls.validate }} \
	-H 'Content-Type: application/json' \
	-H 'Authorization: Bearer < access-token >' \
	-\d @filename

[
   {
      "client_id": 4231,
      "table_name": "users",
      "sequence": 100,
      "action": "upsert"
   }
]
{% endhighlight %}

### Upsert {#upsert-method}

{{ upsert }} In addition to the [required request body fields](#required-request-body-fields) this endpoint **will only accept requests that contain the following properties**:

- The data being sent must be valid JSON or [Transit][transit] AND specified in the request header: `Content-Type: application/json`
- If a Primary Key is a `string`, it must be 256 characters or less.
- An array of data cannot contain more than 10,000 individual data points.
- The request body cannot be larger than 4MB.

#### Example Request Header {#example-upsert-request-header}

{% highlight json %}
curl -X POST {{ import-api.endpoints.urls.upsert }} \
	-H 'Content-Type: application/json' \
	-H 'Authorization: Bearer < access-token >' \
	-\d @filename
{% endhighlight %}

#### Required Request Body Fields {#required-request-body-fields}

For the {{ integration.display_name }} to successfully accept and process your data, your request body must contain all of the request body fields listed below:

<table>
<tbody>
{% for field in import-api.request-body.fields %}
<tr>
<td width="18%; fixed" align="right" markdown="span">**{{ field.name }}**</td>
<td markdown="span">{{ field.description | flatify }}</td>
</tr>
{% endfor %}
</tbody>
</table>

If the request was successful, the response will have an HTTP status code of `201 Created` and an empty body.

#### Define Tables {#defining-tables}

When you push data to an arbitrary table name using the {{ integration.display_name }}, the table will be generated dynamically in your data warehouse. When creating requests, keep the following in mind:

1. **The {{ integration.display_name }} doesn't enforce any limitation on the hierarchy of your tables.**
2. **There aren't any commands to create or destroy a table in the {{ integration.display_name }}.**
3. **You should create one table for each type of data point that you'll push.** For example: if you have customer and product data, you should create `customer` and `product` tables.
4. **Each data point pushed to a single table should have the same data structure.** For example: if a `customers` table contains `customer_id`, `name`, and `email` columns, every customer record pushed into this table should contain those columns.
5. **You can push more than one table using the same API access token.** Think of it this way: one schema for each API access token. All tables pushed using the same API access token will be housed in the same schema in your data warehouse.

#### Define the Sequence {#defining-the-sequence}

Sequence properties communicate the order in which data points should be considered – newer data points can replace older ones, but not vice versa. 

Every data point pushed to the Import API must have a `sequence` property.

A simple solution is just to use the current timestamp, but before doing so, consider the following:

1. **Are the rows being considered frequently updated?**
   Rows that are updated every few milliseconds can result in failure if records with identical key values are pushed simultaneously. This means that records with the same key values cannot be sent during the same clock resolution.

   For example: if the resolution is measured in milliseconds, records with identical key values cannot be sent during the same millisecond.
2. **Are the records coming from multiple sources?**
   If records from multiple sources will be sent to the Import API, the time clocks of these sources must be synchronized. This is especially important if different sources are pushing rows to the same table.

##### Sequence Example

Take a look at the following example. The first three requests are all for one record (`id 10`), while the fourth is for a different record (`id 22`).

If the requests were received in this order:

- Requests 1 and 2 would continue to Stitch, but not Request 3. This is because Request 3 has a **lower** sequence value than Request 2.
- Request 4 would continue to Stitch.

{% highlight json %}
[
 {
  "client_id": 4231,              // Request 1
  "table_name": "users",
  "sequence": 100,
  "action": "upsert",
  "key_names": [
   "id"
  ],
  "data": {
   "id": 10,
   "status": "pending"
  }
 }
]
[
 {
  "client_id": 4231,              // Request 2
  "table_name": "users",
  "sequence": 101,
  "action": "upsert",
  "key_names": [
   "id"
  ],
  "data": {
   "id": 10,
   "status": "canceled"
  }
 }
]
[
 {
  "client_id": 4231,              // Request 3
   "table_name": "users",
   "sequence": 99,
   "action": "upsert",
   "key_names": [
    "id"
   ],
   "data": {
    "id": 10,
    "status": "new"
   }
  }
 ]
[
 {
  "client_id": 4231,              // Request 4
  "table_name": "users",
  "sequence": 90,
  "action": "upsert",
  "key_names": [
   "id"
  ],
  "data": {
   "id": 22,
   "status": "new"
  }
 }
]
{% endhighlight %}

---

## Revoke {{ integration.display_name }} Access Tokens {#revoke-access-token}

{% include important.html content="We recommend that you generate a new token before revoking the old one. If you revoke access first, the connection to your data will be interrupted." %}

1. On the {{ app.page-names.dashboard }} page, click the **{{ integration.display_name }}** integration that needs a new token.
2. When the {{ app.page-names.int-details }} page displays, click {{ app.buttons.update-int-settings }}.
3. In the **API Access Tokens** section, you'll see a list of tokens currently in use:
   ![Revoking an {{ integration.display_name }} token.]({{site.baseurl}}/images/integrations/import-api-revoke-token.png)
4. If you haven't already generated a new token, click **Generate** to do so now.
5. Once the new token has been generated, click the **Revoke** button next to the token you need to revoke. 

   Note that the tokens are listed by creation date - if you generated a new token, you'll want to revoke the oldest token.
<br><br>


[transit]: https://github.com/cognitect/transit-format
