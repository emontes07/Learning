---
title: Online Hosted Instructions
permalink: index.html
layout: home
---

Hyperlinks to each of the demos are listed below.

## Demos

{% assign demos = site.pages | where_exp:"page", "page.url contains '/Instructions/Demos'" %}
| Demo |
| --- |
{% for activity in demos  %}| [{{ activity.demo.title }}]({{ site.github.url }}{{ activity.url }}) |
{% endfor %}

## Sample Prompts for immersion experience

#### [Executives](https://learn.microsoft.com/en-us/training/modules/envision-new-ideas-with-microsoft-365-copilot/) (Redirects to Microsoft Learn)

#### [Communications](https://emontes07.github.io/Learning/Instructions/Prompts/Communications-Prompts.html)

#### [HR](https://emontes07.github.io/Learning/Instructions/Prompts/HR-Prompts.html)

#### [Sales](https://emontes07.github.io/Learning/Instructions/Prompts/Sales-Prompts.html)

#### [IT](https://emontes07.github.io/Learning/Instructions/Prompts/IT-Prompts.html)

#### [Executive Assistant](https://emontes07.github.io/Learning/Instructions/Prompts/EA-Prompts.html)

#### [Business Manager](https://emontes07.github.io/Learning/Instructions/Prompts/Business-Manager-Prompts.html)

#### [Marketing](https://emontes07.github.io/Learning/Instructions/Prompts/Marketing-Prompts.html)

#### [Operations](https://emontes07.github.io/Learning/Instructions/Prompts/Operations-Prompts.html)

#### [Legal](https://emontes07.github.io/Learning/Instructions/Prompts/Legal-Prompts.html)

#### [Finance](https://emontes07.github.io/Learning/Instructions/Prompts/Finance-Prompts.html)

#### [Agents - Business Users](https://emontes07.github.io/Learning/Instructions/Prompts/EU-Agents.html)

#### [Agents - Executives](https://emontes07.github.io/Learning/Instructions/Prompts/Exec-Agents.html)

#### [Copilot Chat](https://emontes07.github.io/Learning/Instructions/Prompts/CopilotChat.html)

### [Developers & IT](https://github.com/emontes07/Learning/blob/main/Instructions/Prompts/DigiKeyDev.md)

#### [Arcos Dorados - Agente Research](https://emontes07.github.io/Learning/Instructions/Prompts/ArcosDorados-ResearcherAgent.html)

#### [Arcos Dorados - Agente Analyst](https://emontes07.github.io/Learning/Instructions/Prompts/ArcosDoradosAnalyst.html)

#### [Arcos Dorados - Copilot](https://emontes07.github.io/Learning/Instructions/Prompts/ArcosDorados-Inmersion.html)

#### [Arcos Dorados - Copilot](https://emontes07.github.io/Learning/Instructions/Prompts/ArcosDoradosITv02.html)

#### [Arcos Dorados - Executives](https://emontes07.github.io/Learning/Instructions/Prompts/ArcosEX.html)

#### [Caseys - Prompt-a-Thon](https://emontes07.github.io/Learning/Instructions/Prompts/CaseysPromptathon.html)





