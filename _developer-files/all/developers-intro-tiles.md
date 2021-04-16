---
title: "Welcome!"
product-type: "all-developer"
content-type: "overview"
order: 1

sections:
  - content: |
      Welcome to the Stitch Developer Portal! Whether you're building on top of Stitch for your own use or integrating Stitch features into your service, you can find everything you need to get started right here.

      Need some help? Check out the [Stitch Community]({{ site.community }}){:target="new"} for guidance and to see what others are working on.

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