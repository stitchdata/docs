--- 

title: Liquid Tutorial Week 1 

permalink: /liquid-tutorial/week-1 

layout: page

--- 


#Example 1

{% assign liquid-lesson = page %}

This is the first demonstration of using an object for the `{{ liquid-lesson.title }}` assignment.


#Example 2

{% if liquid-lesson.title == 'Liquid Tutorial Week 1' %}

You will be a Liquid Master in no time!

{% endif %}


#Example 3

{{ 'liquid-tutorial' | append: '.yaml'}}

