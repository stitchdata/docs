---
content-type: "api-form"
form-type: "source"
key: "source-form-properties-facebook-ads-object"

title: "Facebook Ads Source Form Property"
description: "{{ api.form-properties.source-forms.facebook-ads.description }}"

object-attributes:
  # - name: "aggregate_level"
  #   type: "PLACEHOLDER"
  #   description: "[PLACEHOLDER]"

  - name: "attribution_window"
    type: "string"
    required: false
    description: |
      Defines the number, in days, [Stitch should use as an attribution window]({{ site.baseurl }}/integrations/saas/facebook-ads#attribution-windows-data-extraction). An attribution window is the period of time for attributing results to ads and the lookback period after those actions occur during which ad results are counted.

      Accepted values, in days:

      - `1`
      - `7`
      - `28`

      To ensure your Facebook Ads and Stitch settings align, we recommend using the same attribution window in Stitch that you use in Facebook Ads. For example: If the attribution window is 28 days in Facebook, this value should be `28`.

  - name: "frequency_in_minutes"
    type: "string"
    required: true
    description: |
      {{ connect.common.attributes.frequency | replace: "[INTEGRATION]","Facebook Ads" }}

  - name: "include_deleted"
    type: "string"
    required: false
    description: "If `true`, Stitch will replicate data for deleted campaigns, ads, and adsets. **Note**: This data will not be included alongside insights data."

  # - name: "insights_buffer_days"
  #   type: "string"
  #   description: "[PLACEHOLDER]"

  - name: "start_date"
    type: "string"
    required: true
    description: |
      {{ connect.common.attributes.start-date | replace: "[INTEGRATION]","Facebook Ads" }}

examples: 
  - code: |
      {  
       "type":"platform.facebook",
       "properties":{  
          "frequency_in_minutes":"30",
          "include_deleted":"true",
          "start_date":"2018-01-10T00:00:00Z"
        }
      }
---