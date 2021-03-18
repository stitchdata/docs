--- 

title: Liquid Tutorial Week 1 

permalink: /liquid-tutorial/week-3 

layout: page

a-string: a string of text
null-value:
an-integer: 26
pie: true
cake: false
date: Febrary 5, 2020

paragraph: |
  This is line one of a paragraph.

  This is line two of the paragraph.

tools: connection-check

name: A liquid hash
id: liquid-hash
title: "A liquid hash"

strings-list:
  - example: "string number 1"
  - item: "string number 2"
  - example: "string number 3"

object-list:
  - name: a-liquid-hash
    id: liquid-hash
    title: "A liquid hash"

  - name: a-liquid-hash
    id: liquid-hash
    title: "A liquid hash"
    
  - name: a-liquid-hash
    id: liquid-hash
    title: "A liquid hash"    
--- 

Example 1

Here is an example of me accessing data in a nested hash: {{ page.name }}


Example 2

I need to provide an example of an object using a string, so here's {{ page.a-string }}.


Example 3

{% assign tools = site.data.tooltips[page.tools] %}

A connection check is {{ tools }}

{{ site.data.tooltips.connection-check }}


WEEK 3 HW

Example 1

{% for string in page.strings-list %}
  {{ string.example }}
  {{ strings-list.item }}
{% endfor %}


Example 2

{% for id in page.object-list %}
  {{ id.id }}
{% endfor %}

Example 3

{% for attribute in site.saas-integrations %}
  {{ attribute.display_name }}
{% endfor %}

