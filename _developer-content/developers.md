---
title: Stitch Developers
permalink: /developers

sidebar: overview
layout: general

product-type: "all-developer"
content-type: "overview"

dev-categories:
  - title: "Import API"
    description: |
      Push data from an arbitrary data source to Stitch.
    plan: "all-plans"
    links:
      - name: "Quick start"
        url: "{{ link.import-api.guides.quick-start | prepend: site.baseurl }}"

      - name: "Authentication"
        url: "{{ link.import-api.api | prepend: site.baseurl }}#authentication"

      - name: "API reference"
        url: "{{ link.import-api.api | prepend: site.baseurl }}"

      - name: "Libraries and resources"
        url: "{{ link.import-api.overview | prepend: site.baseurl }}#libraries-and-resources"

      - name: "All Import API guides"
        url: "{{ link.import-api.guides.category | prepend: site.baseurl }}"

  - title: "Post-load webhooks"
    description: |
      Stay informed with post-load webhooks, which fire each time data is loaded into your destination.
    plan: "enterprise"
    links:
      - name: "Post-load webhooks guide"
        url: "{{ link.account.post-load-notifications | prepend: site.baseurl }}"

      - name: "Setting up post-load webhooks"
        url: "{{ link.account.post-load-notifications | prepend: site.baseurl }}#manage-post-load-hooks"

      - name: "Webhook triggers"
        url: "{{ link.webhooks.post-load | prepend: site.baseurl }}#webhook-triggers"

      - name: "Data model reference"
        url: "{{ link.webhooks.post-load | prepend: site.baseurl }}#webhook-payload"

  - title: "Connect API"
    description: "Programmatically manage your Stitch account or integrate Stitch with other applications with our REST API."
    plan: "enterprise"
    links:
      # - name: "Quick start"
      #   url: "{{ link.connect.api | prepend: site.baseurl }} TODO"

      - name: "Authentication"
        url: "{{ link.connect.api | prepend: site.baseurl}}#authentication"

      - name: "API reference"
        url: "{{ link.connect.api | prepend: site.baseurl }}"

      - name: "All Connect guides"
        url: "{{ link.connect.guides.category | prepend: site.baseurl }}"

  - title: "Connect.js"
    description: "In conjunction with the Connect API, send users to Stitch to complete data source configuration workflows with this JavaScript library."
    plan: "enterprise"
    links:
      - name: "Installation"
        url: "{{ link.connect.js | prepend: site.baseurl }}#installation"

      - name: "JavaScript reference"
        url: "{{ link.connect.js | prepend: site.baseurl }}"

sections:
  - content: |
      Welcome to the Stitch Developer Portal! TODO: Ask Sales if they have any go-to copy for selling Connect.

      {% include misc/data-files.html %}
      <ul class="tiles two-columns">
      {% for category in page.dev-categories %}
        <li class="developer-tile">
          <div class="div-flag {{ category.plan }}">
              {{ category.plan | replace:"-"," " | upcase }}
            </div>
          <span class="h3" style="margin-top: 30px;">{{ category.title }}</span>
          
          {% case category.plan %}
          {% when 'enterprise' %}
          {{ category.description | flatify | append:" **This is a Stitch Enterprise feature.**" | markdownify }} 

          {% else %}
          {{ category.description | flatify | markdownify }} 
          {% endcase %}

          <ul>
          {% for section-link in category.links %}
          <li>
            <a href="{{ section-link.url | flatify }}">{{ section-link.name | flatify }}</a>
          </li>
          {% endfor %}
          </ul>

        </li>
      {% endfor %} 
      </ul>
---