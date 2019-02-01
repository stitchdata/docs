---
title: Stitch Connect
permalink: /stitch-connect/
sidebar: overview
layout: developer

type: "connect"
content-type: "connect-overview"

toolkit:
  - title: "{{ api.name }}"
    icon: "{{ api.icon }}"
    url: "{{ api.section | flatify }}"
    description: "{{ api.description | flatify }}"

  - title: "{{ js.name }}"
    icon: "{{ js.icon }}"
    url: "{{ js.section | flatify }}"
    description: "{{ js.description | flatify }}"
---