---
content-type: "api-form"
form-type: "source"
key: "source-form-properties-facebook-ads-object"

title: "Facebook Ads Source Form Property"
api-type: "facebook"
display-name: "Facebook Ads"

description: "{{ api.form-properties.source-forms.facebook-ads.description }}"

object-attributes:
  # - name: "aggregate_level"
  #   type: "PLACEHOLDER"
  #   description: "[PLACEHOLDER]"

  - name: "anchor_time"
    type: "string"
    required: false
    description: |
      {{ connect.common.attributes.anchor-time | replace: "[INTEGRATION]",form-property.display-name }}
    value: "{{ sample-property-data.anchor-time }}"

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

      If your click and view windows differ, you should select the **greater** of the two. For example: If clicks have a window of `7` days and views have a window of `1` day, you should enter `7` for this setting.
    value: "7"

  - name: "frequency_in_minutes"
    type: "string"
    required: true
    description: |
      {{ connect.common.attributes.frequency | replace: "[INTEGRATION]",form-property.display-name }}
    value: "{{ sample-property-data.frequency }}"

  - name: "include_deleted"
    type: "string"
    required: false
    description: "If `true`, Stitch will replicate data for deleted campaigns, ads, and adsets. **Note**: This data will not be included alongside insights data."
    value: "true"

  # - name: "insights_buffer_days"
  #   type: "string"
  #   description: "[PLACEHOLDER]"

  - name: "start_date"
    type: "string"
    required: true
    description: |
      {{ connect.common.attributes.start-date | replace: "[INTEGRATION]","Facebook Ads" }}
    value: "{{ sample-property-data.start-date }}"
---