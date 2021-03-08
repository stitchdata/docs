--- 

title: "Liquid Tutorial Week 4" 

permalink: /liquid-tutorial/week-4 

layout: general  

  

# -------------------------- # 

#         Tap Details        # 

# -------------------------- # 

  

name: "facebook-ads" 

display_name: "Facebook Ads"  

this-version: "1" 

  

# -------------------------- # 

#       Stitch Details       # 

# -------------------------- # 

  

certified: true 

  

historical: "1 year" 

frequency: "30 minutes" 

tier: "Standard"  

 

api-type: "platform.facebook"  

anchor-scheduling: true 

cron-scheduling: false 

  

table-selection: true 

column-selection: true 

table-level-reset: true 

  

extraction-logs: true 

loading-reports: true  

 

feature-list: 

  - name: "anchor-scheduling" 

    supported: true 

  - name: "cron-scheduling" 

    supported: false 

  - name: "table-selection" 

    supported: true 

  - name: "column-selection" 

    supported: true 

  - name: "table-level-reset" 

    supported: true 

  - name: "extraction-logs" 

    supported: true 

  - name: "loading-reports" 

    supported: true 

--- 


EXAMPLE 1

{% if page.certified == true %}

This is a certified integration.

{% endif %}




EXAMPLE 2
{% unless page.table-selection == false %}

This integration has table selection.

{% endunless %}



EXAMPLE 3
{% if page.certified == true %}

This is a certified integration.

{% elsif page.certified == false %}

This is a community integration.

{% endif %}



EXAMPLE 4
{% if page.table-selection == true and page.column-selection == true %}

This integration has object selection.

{% endif %}



EXAMPLE 5
{% if page.api-type %}

This integration is available in the API.

{% endif %}


EXAMPLE 6
{% for feature in page.feature-list %}
  {{ feature.name }}

{% case feature.supported %}

{% when true %}

This feature is supported.

{% when false %}

This feature is not supported.

{% endcase %}
{% endfor %}