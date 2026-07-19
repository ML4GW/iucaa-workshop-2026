---
layout: page
title: Agenda
permalink: /agenda/
---

# Agenda for Sept 25, 2026

<ul class="agenda-list">
  {% assign sessions = site.pages | where: "session", true | sort: "order" %}
  {% for session in sessions %}
    <li>
      <a href="{{ session.url | prepend: site.baseurl }}">{{ session.title }}</a>
    </li>
  {% endfor %}
</ul>

<p style="margin-top:1em;"><strong>Lunch break:</strong> 12:45 &ndash; 14:15</p>

---

[← to Home]({{ "/" | prepend: site.baseurl }})

