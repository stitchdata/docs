--- 
title: Liquid Tutorial Week 5
permalink: /liquid-tutorial/week-5 
layout: page

originals:
  - id: "1"
    name: "Leslie"
    type: "lady"

  - id: "2"
    name: "Ron"
    type: "dude"

  - id: "3"
    name: "Tom"
    type: "dude"

  - id: "4"
    name: "Donna"
    type: "queen"

  - id: "5"
    name: "Jerry"
    type: "dude"

  - id: "6"
    name: "April"
    type: "vampire"

  - id: "7"
    name: "Ann"
    type: "lady"

  - id: "8"
    name: "Andy"
    type: "dude"

bffs:
  - id: "9"
    name: "Ben"
    type: "dude"

  - id: "10"
    name: "Chris"
    type: "dude"
---

1. Construct a Frontmatter array (list) named `originals` using the following data. Each object in the list should have an with `id`, `name`, and `type` attribute - the data for each attribute is comma-separated. Ex: id,name

1,Leslie,lady
2,Ron,dude
3,Tom,dude
4,Donna,queen
5,Jerry,dude
6,April,vampire
7,Ann,lady
8,Andy,dude

2. Construct a second Frontmatter array named `bffs` using the following data. It should have the same attributes (id,name,type) as `originals`.

9,Ben,dude
10,Chris,dude

3. Write a statement that returns the `name` of the first person in the `originals` list.


4. Write a statement that returns the total number of people in the `originals` list.


5. Write a statement that concats the people in the `bffs` list to the `originals` list and creates a new list named `parks-and-rec`.


6. This has two parts:
    1. Write a statement that loops through the `parks-and-rec` list and displays only people who have a `type` of `dude`.
    2. Re-write the statement to only use variable tags and array filters.

7. Write a statement that sorts the `parks-and-rec` list by `name`. Output the results (including `id`, `name`, and `type`) using a forloop.

8. Make a copy of the forloop you wrote in 7. Re-write the statement to use a forloop to loop through the `id`, `name`, and `type` attributes. (By this, I mean don't call each attribute explicitly - how can you use what you've learned this week to simplify your code?)


Example 3

{% assign first-person = page.originals | first  %}
{{ first-person }}

{{ first-person.name }}

{% for person in page.originals %}
{% if forloop.first == true %}
- {{ person.name }}
{% endif %}
{% endfor %}


Example 4

{{ page.originals | size }}



Example 5

{% assign parks-and-rec = page.originals | concat: page.bffs %}

{{ parks-and-rec }}




Example 6

{% for person in parks-and-rec %}
{% if person.type == "dude" %}
- {{ person.name }}
{% endif %}
{% endfor %}

because i created `parks-and-rec` within the body and not in the frontmatter, I didn't necessarily need to do an assign. The forloop is automatically going to look through each object within the list.

use `==` for when comparing to a value that actually exists

{% assign person = parks-and-rec | where:'type','dude' %}




Example 7

{% assign sorted-parks-and-rec = parks-and-rec | sort: "name" %}

{% for person in sorted-parks-and-rec %}
- {{ person.id }}
  {{ person.name }}
  {{ person.type }}
{% endfor %}


{% assign attributes = "id name type" | split: ' ' %}

{% for person in sorted-parks-and-rec %}
{% for attribute in attributes %}
- {{ person[attribute]}}
{% endfor %}
{% endfor %}


