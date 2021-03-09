--- 
title: Liquid Tutorial Week 5
permalink: /liquid-tutorial/week-5 
layout: page
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