---
layout: default
title: "Copilot for Edgewell Finance — 60-Minute Immersion"
description: "An intro guide to Microsoft 365 Copilot, tailored for the Edgewell Finance team."
---

<style>
:root {
  --edgewell-navy: #0B2545;
  --edgewell-navy-soft: #13315C;
  --edgewell-coral: #E63946;
  --edgewell-sun: #F4A261;
  --edgewell-teal: #2A9D8F;
  --edgewell-cloud: #F4F6FA;
  --edgewell-line: #E2E8F0;
  --edgewell-ink: #1A202C;
  --edgewell-muted: #4A5568;
}

.ew-hero {
  background: linear-gradient(135deg, var(--edgewell-navy) 0%, var(--edgewell-navy-soft) 70%, var(--edgewell-coral) 140%);
  color: #fff;
  padding: 2.5rem 2rem;
  border-radius: 14px;
  margin: 1.25rem 0 2rem 0;
  box-shadow: 0 10px 30px rgba(11, 37, 69, 0.18);
}
.ew-hero h1 { color: #fff; margin: 0 0 .5rem 0; font-size: 2.2rem; letter-spacing: -0.5px; }
.ew-hero .ew-sub { font-size: 1.05rem; opacity: 0.92; margin-bottom: 1rem; }
.ew-hero .ew-meta { display: flex; flex-wrap: wrap; gap: .5rem; margin-top: .75rem; }
.ew-chip {
  display: inline-block; padding: .35rem .75rem; border-radius: 999px;
  background: rgba(255,255,255,0.15); color: #fff; font-size: .85rem;
  border: 1px solid rgba(255,255,255,0.25);
}

.ew-toc {
  background: var(--edgewell-cloud);
  border-left: 4px solid var(--edgewell-coral);
  padding: 1rem 1.25rem;
  border-radius: 8px;
  margin: 1.5rem 0;
}
.ew-toc h3 { margin-top: 0; color: var(--edgewell-navy); }
.ew-toc ol { margin: 0; padding-left: 1.25rem; }
.ew-toc li { margin: .3rem 0; }

.ew-section {
  background: #fff;
  border: 1px solid var(--edgewell-line);
  border-radius: 12px;
  padding: 1.5rem 1.75rem;
  margin: 1.5rem 0;
  box-shadow: 0 2px 8px rgba(11, 37, 69, 0.04);
}
.ew-section h2 {
  color: var(--edgewell-navy);
  border-bottom: 2px solid var(--edgewell-coral);
  padding-bottom: .4rem;
  margin-top: 0;
  display: flex; align-items: center; gap: .6rem;
}
.ew-section h3 { color: var(--edgewell-navy-soft); margin-top: 1.5rem; }
.ew-section .ew-time {
  display: inline-block;
  background: var(--edgewell-cloud);
  color: var(--edgewell-navy-soft);
  font-size: .8rem; font-weight: 600;
  padding: .15rem .6rem; border-radius: 6px;
  margin-left: auto;
}

.ew-prompt {
  background: #0F2A4A;
  color: #E8EEF7;
  border-left: 4px solid var(--edgewell-sun);
  border-radius: 8px;
  padding: 1rem 1.1rem;
  margin: .75rem 0;
  font-family: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace;
  font-size: .92rem;
  line-height: 1.55;
  white-space: pre-wrap;
  overflow-x: auto;
}
.ew-prompt::before {
  content: "💬  Try this prompt";
  display: block;
  color: var(--edgewell-sun);
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  font-weight: 600;
  font-size: .8rem;
  letter-spacing: .5px;
  margin-bottom: .5rem;
}

.ew-callout {
  border-radius: 8px;
  padding: .9rem 1.1rem;
  margin: 1rem 0;
  border-left: 4px solid;
}
.ew-tip { background: #E8F6F3; border-color: var(--edgewell-teal); }
.ew-tip strong { color: var(--edgewell-teal); }
.ew-note { background: #FFF7E6; border-color: var(--edgewell-sun); }
.ew-note strong { color: #B7791F; }
.ew-warn { background: #FFE8EA; border-color: var(--edgewell-coral); }
.ew-warn strong { color: var(--edgewell-coral); }

.ew-steps { counter-reset: step; padding-left: 0; list-style: none; }
.ew-steps > li {
  counter-increment: step;
  position: relative;
  padding: .5rem 0 .5rem 2.4rem;
  margin-bottom: .25rem;
}
.ew-steps > li::before {
  content: counter(step);
  position: absolute; left: 0; top: .5rem;
  width: 1.7rem; height: 1.7rem;
  background: var(--edgewell-coral); color: #fff;
  border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  font-weight: 700; font-size: .85rem;
}

.ew-img-placeholder {
  background: repeating-linear-gradient(45deg, #F4F6FA, #F4F6FA 10px, #E2E8F0 10px, #E2E8F0 20px);
  border: 2px dashed #B7C2D6;
  border-radius: 8px;
  padding: 1.5rem;
  text-align: center;
  color: var(--edgewell-muted);
  font-style: italic;
  margin: 1rem 0;
  font-size: .9rem;
}

.ew-pillrow { display: flex; flex-wrap: wrap; gap: .4rem; margin: .75rem 0; }
.ew-pill {
  background: var(--edgewell-cloud);
  color: var(--edgewell-navy-soft);
  border: 1px solid var(--edgewell-line);
  padding: .25rem .7rem;
  border-radius: 999px;
  font-size: .82rem;
}

table.ew-table {
  width: 100%;
  border-collapse: collapse;
  margin: 1rem 0;
  font-size: .92rem;
}
table.ew-table th {
  background: var(--edgewell-navy);
  color: #fff;
  text-align: left;
  padding: .6rem .8rem;
}
table.ew-table td {
  padding: .55rem .8rem;
  border-bottom: 1px solid var(--edgewell-line);
}
table.ew-table tr:nth-child(even) td { background: var(--edgewell-cloud); }

.ew-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 1rem; margin: 1rem 0; }
.ew-card {
  background: var(--edgewell-cloud);
  border-radius: 10px;
  padding: 1rem 1.1rem;
  border-top: 3px solid var(--edgewell-coral);
}
.ew-card h4 { margin: 0 0 .4rem 0; color: var(--edgewell-navy); font-size: 1rem; }
.ew-card p { margin: 0; font-size: .9rem; color: var(--edgewell-muted); }

.ew-footer {
  background: var(--edgewell-navy);
  color: #E8EEF7;
  padding: 1.5rem 1.75rem;
  border-radius: 12px;
  margin-top: 2rem;
  text-align: center;
}
.ew-footer a { color: var(--edgewell-sun); }
</style>

<div class="ew-hero">
  <h1>🪒 Copilot for Edgewell Finance</h1>
  <div class="ew-sub">A 60-minute immersion — from interface basics to your first AI agent.</div>
  <div class="ew-meta">
    <span class="ew-chip">⏱️ 60 minutes</span>
    <span class="ew-chip">👥 Finance team</span>
    <span class="ew-chip">🎯 Intro level</span>
    <span class="ew-chip">🛠️ Hands-on optional</span>
  </div>
</div>

> **How to use this guide.** We'll move quickly together during the live session. This page is your **take-home companion** — every prompt, click path, and tip is here so you can replay anything at your own pace. Look for the 💬 boxes for prompts you can copy directly into Copilot.

<div class="ew-toc">
  <h3>📋 What we'll cover</h3>
  <ol>
    <li><a href="#section-1">Copilot Foundations</a> — the interface, Memory, and Saved Prompts</li>
    <li><a href="#section-2">Outlook</a> — inbox triage and a faster reply</li>
    <li><a href="#section-3">Teams</a> — catch up on a meeting you missed</li>
    <li><a href="#section-4">Word</a> — draft a finance memo from a single prompt</li>
    <li><a href="#section-5">Excel</a> — analyze brand P&L data with natural language</li>
    <li><a href="#section-6">PowerPoint</a> — turn a Word memo into an executive deck</li>
    <li><a href="#section-7">Loop & Pages</a> — collaborative finance workspaces</li>
    <li><a href="#section-8">Agent Builder</a> — build a Finance Policy Q&A agent (live)</li>
    <li><a href="#wrap-up">Wrap-up & Resources</a></li>
  </ol>
</div>

<div class="ew-callout ew-note">
  <strong>📌 Before you start.</strong> Open <a href="https://m365.cloud.microsoft/chat" target="_blank">m365.cloud.microsoft/chat</a> in a new tab — that's the standalone Copilot experience we'll keep coming back to. Sign in with your Edgewell account. Make sure you see the <em>green "Work" toggle</em> in the top right; that means Copilot can ground its answers on your Edgewell content.
</div>

---

<div class="ew-section" id="section-1">
<h2>1️⃣ Copilot Foundations <span class="ew-time">~8 min</span></h2>

Before we touch any app, let's get comfortable with the Copilot home base — the chat experience at <a href="https://m365.cloud.microsoft/chat" target="_blank">m365.cloud.microsoft/chat</a>. Everything you'll see in Outlook, Word, or Excel later is the same brain wearing different hats.

<div class="ew-img-placeholder">📷 Screenshot placeholder — Copilot Chat home with Work/Web toggle highlighted</div>

### The interface at a glance

<div class="ew-grid">
  <div class="ew-card">
    <h4>🟢 Work vs. 🌐 Web</h4>
    <p>Toggle in the top-right. <strong>Work</strong> = grounded on your Edgewell files, emails, and meetings. <strong>Web</strong> = open internet only.</p>
  </div>
  <div class="ew-card">
    <h4>📎 Add content</h4>
    <p>Attach a file, paste a SharePoint link, or reference a meeting. Copilot will use that as the source of truth for the answer.</p>
  </div>
  <div class="ew-card">
    <h4>🎨 Agents</h4>
    <p>The left rail lists agents you can chat with — including ones we'll build today.</p>
  </div>
  <div class="ew-card">
    <h4>🧠 Memory</h4>
    <p>Copilot remembers facts about you across conversations — your role, brands you cover, how you like answers formatted.</p>
  </div>
</div>

### 🧠 Memory — teach Copilot who you are

Memory lets Copilot remember things between chats so you don't have to re-explain yourself every morning.

<ol class="ew-steps">
  <li>In Copilot Chat, click your <strong>profile picture</strong> (top right) → <strong>Settings</strong> → <strong>Memory & personalization</strong>.</li>
  <li>Turn <strong>Memory</strong> on if it isn't already.</li>
  <li>Add a few facts manually, or just chat — Copilot will offer to remember things as they come up.</li>
</ol>

<div class="ew-prompt">Please remember the following about me so you can tailor future answers:

- I'm on the Edgewell Personal Care Finance team.
- I focus on Brand P&L for Schick and Banana Boat, plus retailer profitability for Walmart, Target, and Amazon.
- When I ask for analysis, default to a concise executive summary first, then a bullet list of the three most material drivers, then a short table.
- Round dollar figures to the nearest hundred thousand and always show variance vs. prior year and vs. plan.</div>

<div class="ew-callout ew-tip">
  <strong>💡 Why this matters.</strong> One time investment, every future answer gets sharper. Memory works in Copilot Chat <em>and</em> inside Word, Excel, Outlook, etc.
</div>

### 💾 Saved Prompts — your personal prompt library

If you find yourself typing the same kind of prompt every Monday, save it once.

<ol class="ew-steps">
  <li>Type a prompt in Copilot Chat.</li>
  <li>Click the <strong>save icon</strong> (bookmark) next to the send button — give it a name and an optional description.</li>
  <li>Reuse it any time from the <strong>Prompts</strong> gallery on the right rail.</li>
</ol>

<div class="ew-prompt">Saved prompt: "Weekly Brand P&L Pulse"

Summarize the most recent emails, Teams messages, and shared files I've received this week related to Schick or Banana Boat brand performance. Group findings by:
1. Volume / shipment trends
2. Trade spend or promotion activity
3. Margin or pricing signals
4. Anything flagged as risk or opportunity

Keep each section to 3 bullets max. End with the top 3 follow-ups I should action this week.</div>

<div class="ew-img-placeholder">📷 Screenshot placeholder — saving a prompt with the bookmark icon</div>

</div>

---

<div class="ew-section" id="section-2">
<h2>2️⃣ Outlook — Faster Inbox, Better Replies <span class="ew-time">~5 min</span></h2>

Finance inboxes are noisy: retailer chargebacks, accruals questions, AR follow-ups, leadership requests. Copilot in Outlook does two things really well — **summarize long threads** and **draft replies in your voice**.

### Summarize a long thread

Open any thread in Outlook → click **Summary by Copilot** at the top of the message.

<div class="ew-callout ew-tip">
  <strong>💡 Edgewell scenario.</strong> Imagine a 14-message thread with the Walmart account team about a $1.2M deduction dispute on Banana Boat SPF 50. Click Summary by Copilot and you'll get the dispute history, current ask, and the open question — in 30 seconds.
</div>

### Draft a reply that sounds like you

In any email, click **Draft with Copilot** in the reply box.

<div class="ew-prompt">Draft a reply to the Target account team confirming we'll honor the Q2 promotional allowance on the Schick Hydro 5 line at the agreed 8% off-invoice rate, but flag that the $340K incremental display fee they're requesting is outside our trade calendar and needs Brand approval before we can commit. Keep it warm but firm. Sign off with my name.</div>

<div class="ew-callout ew-note">
  <strong>📌 Tone matters.</strong> After Copilot drafts, click <em>Adjust → Make it shorter / more formal / more casual</em>. You can also paste in 2–3 of your past emails and ask Copilot to "match my voice" — it picks up on phrasing fast.
</div>

### Catch up after PTO

<div class="ew-prompt">I was out Thursday and Friday last week. Summarize the most important emails I received during those two days. Group them by:
1. Things needing my decision or approval
2. FYIs from leadership
3. Retailer or vendor updates I should track

Flag anything that mentions Schick, Banana Boat, Walmart, Target, or Amazon as high priority.</div>

</div>

---

<div class="ew-section" id="section-3">
<h2>3️⃣ Teams — Never Miss a Meeting Again <span class="ew-time">~5 min</span></h2>

If a meeting was recorded or transcribed, Copilot can recap it for you in seconds — even ones you didn't attend.

### Recap a meeting you missed

<ol class="ew-steps">
  <li>Open the meeting from your Teams calendar (or chat).</li>
  <li>Click the <strong>Recap</strong> tab.</li>
  <li>Use the Copilot panel on the right — it's pre-loaded with the transcript.</li>
</ol>

<div class="ew-prompt">I missed today's S&OP review. Give me:
- A 4-sentence executive summary
- Decisions made (with who owns each)
- Open questions that didn't get resolved
- Anything specifically said about Schick razor inventory or Banana Boat seasonal build for summer

Then list any action items assigned to Finance.</div>

### Catch up on a busy chat

In a chat or channel, click the **Copilot icon** at the top.

<div class="ew-prompt">Summarize what's been discussed in this channel over the past 7 days. Highlight anything related to month-end close, retailer deductions, or trade spend variance. List unanswered questions at the bottom.</div>

<div class="ew-callout ew-warn">
  <strong>⚠️ Recap requires transcription.</strong> If a meeting wasn't recorded or transcribed, Copilot can't recap it. Encourage the organizer to enable transcription for finance reviews going forward.
</div>

</div>

---

<div class="ew-section" id="section-4">
<h2>4️⃣ Word — Draft a Memo in 30 Seconds <span class="ew-time">~5 min</span></h2>

Finance writing is often structured: situation → analysis → recommendation. Copilot in Word is great at giving you a strong first draft you can polish.

### Draft from a blank doc

In Word, start a new document → click **Draft with Copilot**.

<div class="ew-prompt">Draft a 1-page Finance memo to the Edgewell North America leadership team on the following topic:

"Q1 Banana Boat margin compression — drivers and proposed actions"

Use this structure:
1. Executive Summary (3 sentences)
2. What happened (bullet list with illustrative numbers — gross margin down 220 bps vs. plan, driven by SPF aerosol propellant cost +18% YoY and unfavorable mix toward club channel)
3. Root causes (3 bullets)
4. Recommended actions (3 bullets, each with an owner placeholder)
5. Asks of leadership

Tone: confident, data-driven, no jargon. Length: under 400 words.</div>

<div class="ew-img-placeholder">📷 Screenshot placeholder — Draft with Copilot pane in Word</div>

### Reference your own files

Type **/** in the Copilot box and reference an existing file — Copilot will ground the draft on it.

<div class="ew-prompt">/ [reference: "FY26 Banana Boat Brand Plan.pptx"]

Draft a finance commentary memo summarizing the FY26 plan for Banana Boat. Pull the brand's revenue, gross margin, and trade spend targets directly from the deck. Add a section on the top three financial risks and how we'll monitor them.</div>

</div>

---

<div class="ew-section" id="section-5">
<h2>5️⃣ Excel — Talk to Your Data <span class="ew-time">~10 min</span></h2>

This is the section your team will reach for daily. Copilot in Excel can analyze, summarize, suggest formulas, and build charts — all in plain English.

<div class="ew-callout ew-note">
  <strong>📌 Setup tip.</strong> Copilot works best when your data is in a <strong>formatted Excel Table</strong> (Ctrl+T or Insert → Table). Header row, no merged cells, no blank rows. Two minutes of cleanup unlocks 10× better answers.
</div>

### Our illustrative dataset

Imagine an Excel workbook called **Edgewell_Brand_Retailer_P&L.xlsx** with this data:

<table class="ew-table">
  <thead>
    <tr><th>Brand</th><th>Retailer</th><th>Net Sales</th><th>COGS</th><th>Trade Spend</th><th>Gross Margin %</th></tr>
  </thead>
  <tbody>
    <tr><td>Schick</td><td>Walmart</td><td>$48.2M</td><td>$22.4M</td><td>$6.1M</td><td>41.5%</td></tr>
    <tr><td>Schick</td><td>Target</td><td>$22.7M</td><td>$10.8M</td><td>$3.4M</td><td>40.1%</td></tr>
    <tr><td>Schick</td><td>Amazon</td><td>$31.4M</td><td>$15.9M</td><td>$2.2M</td><td>42.7%</td></tr>
    <tr><td>Banana Boat</td><td>Walmart</td><td>$54.6M</td><td>$28.9M</td><td>$8.3M</td><td>32.0%</td></tr>
    <tr><td>Banana Boat</td><td>Target</td><td>$19.8M</td><td>$10.2M</td><td>$3.1M</td><td>33.8%</td></tr>
    <tr><td>Banana Boat</td><td>Amazon</td><td>$26.5M</td><td>$13.8M</td><td>$1.6M</td><td>41.5%</td></tr>
  </tbody>
</table>

<div class="ew-callout ew-tip">
  <strong>💡 Want to follow along?</strong> Type these numbers into a fresh sheet, format as a table, then keep this guide open beside Excel.
</div>

### Prompt 1 — Quick analytical summary

<div class="ew-prompt">Looking at this brand-by-retailer P&L, give me:
1. The top 3 takeaways an executive should know
2. Which brand-retailer combination has the highest gross margin %, and which has the lowest
3. A theory on why Banana Boat margins at Amazon are so much higher than at Walmart
4. Two follow-up questions I should investigate</div>

### Prompt 2 — Add a calculated column

<div class="ew-prompt">Add a new column called "Net Contribution" calculated as Net Sales – COGS – Trade Spend. Show me the formula you used so I can verify it.</div>

### Prompt 3 — Build a chart

<div class="ew-prompt">Create a clustered column chart comparing Net Sales and Trade Spend for each Brand-Retailer combination. Title it "Brand-Retailer Net Sales vs. Trade Spend". Use a Schick razor red and a Banana Boat orange so it's easy to read.</div>

### Prompt 4 — Highlight outliers

<div class="ew-prompt">Conditionally format the Gross Margin % column so anything below 35% is highlighted red, 35–40% is amber, and above 40% is green.</div>

### Prompt 5 — Insight, not just numbers

<div class="ew-prompt">If I want to lift Banana Boat's overall gross margin by 200 basis points next year, which retailer should I focus on first based on this data, and what specifically would you investigate to build the case? Walk me through your reasoning.</div>

<div class="ew-callout ew-warn">
  <strong>⚠️ Always verify formulas.</strong> Copilot is a brilliant assistant, not an auditor. For anything that touches the actuals, double-check the formulas it suggests before pasting into a real model.
</div>

</div>

---

<div class="ew-section" id="section-6">
<h2>6️⃣ PowerPoint — From Memo to Deck in 60 Seconds <span class="ew-time">~5 min</span></h2>

Take that Word memo from Section 4 and turn it into a leadership-ready deck.

### Generate a deck from a Word doc

<ol class="ew-steps">
  <li>Open PowerPoint → <strong>New blank presentation</strong>.</li>
  <li>Click the Copilot icon → <strong>Create presentation from file</strong>.</li>
  <li>Pick the Word memo we drafted earlier.</li>
</ol>

<div class="ew-prompt">Create a 6-slide executive presentation from this Word memo on Q1 Banana Boat margin compression. Include:
- Title slide with the topic and "Edgewell Finance | Q1 Review"
- Executive summary slide (3 takeaways)
- A slide showing margin walk drivers with placeholder for a chart
- A slide on root causes
- A slide on recommended actions with owners
- A closing "Asks of leadership" slide

Keep text minimal — at most 4 bullets per slide.</div>

### Refine slide by slide

<div class="ew-prompt">For slide 3, replace the placeholder with a column chart showing margin drivers in this order: Propellant cost (+220 bps drag), Channel mix (+90 bps drag), Pricing actions (-110 bps benefit), Net change (-220 bps).</div>

<div class="ew-callout ew-tip">
  <strong>💡 Edgewell-on-brand.</strong> Apply your team's PowerPoint template <em>before</em> generating slides — Copilot will respect your fonts, colors, and slide masters.
</div>

</div>

---

<div class="ew-section" id="section-7">
<h2>7️⃣ Loop & Pages — Collaborate, Don't Email <span class="ew-time">~5 min</span></h2>

Copilot **Pages** (in Copilot Chat) and **Loop** (in Teams) let multiple people co-author with Copilot in real time. Perfect for finance reviews where you're working through numbers together.

### Pages — promote a great answer into a working doc

After Copilot gives you a useful response in chat, click **"Edit in Pages"** at the bottom of the response.

<div class="ew-prompt">Build a Page titled "Schick vs. Banana Boat — Retailer Margin Comparison".

Include:
1. A short executive summary
2. A side-by-side table of gross margin % by retailer for both brands
3. A "What we know" section and a "What we need to investigate" section
4. A list of follow-ups with placeholders for owner and due date

Make it ready for me to share with the brand finance leads.</div>

### Loop — for the live review meeting

In Teams, paste a Loop component (table, task list, or paragraph) into a chat. Everyone edits at once, and Copilot lives right inside it.

<div class="ew-callout ew-tip">
  <strong>💡 Use case.</strong> During a brand finance review, share a Loop table with the action items. As the meeting progresses, owners and due dates get filled in by the team in real time — no follow-up email needed.
</div>

</div>

---

<div class="ew-section" id="section-8">
<h2>8️⃣ Agent Builder — Your First AI Agent <span class="ew-time">~12 min</span></h2>

This is the finale. We're going to build a **Finance Policy Q&A agent** — a private assistant trained on your finance policies (T&E, approvals, close calendar, capital request thresholds, etc.) that anyone on the team can ask questions of.

<div class="ew-callout ew-note">
  <strong>📌 Why this first?</strong> Policy Q&A is the single highest-ROI, lowest-risk first agent for a Finance team. It deflects the same 20 repeat questions ("what's the T&E limit for client meals?" / "who approves a $50K capex?") and frees up the team for real analysis.
</div>

### What we'll build

<div class="ew-grid">
  <div class="ew-card">
    <h4>📥 Inputs</h4>
    <p>A SharePoint folder with your finance policy PDFs and SOPs.</p>
  </div>
  <div class="ew-card">
    <h4>🧠 Brain</h4>
    <p>Copilot grounded on those documents, with a clear persona and guardrails.</p>
  </div>
  <div class="ew-card">
    <h4>📤 Output</h4>
    <p>A chat agent your team can pin in Copilot Chat or share via a link.</p>
  </div>
</div>

<div class="ew-img-placeholder">📷 Screenshot placeholder — Agent Builder home, "Create new agent" button highlighted</div>

### Step-by-step build

<ol class="ew-steps">
  <li>In Copilot Chat, open the <strong>Agents</strong> rail on the left → <strong>+ Create agent</strong>.</li>
  <li>Click <strong>Skip and go to configure</strong> (we'll fill in the structured form ourselves).</li>
  <li>Fill in <strong>Name</strong>, <strong>Description</strong>, and <strong>Instructions</strong> (see prompts below).</li>
  <li>Under <strong>Knowledge</strong>, add the SharePoint site or folder containing your finance policies.</li>
  <li>Add <strong>Starter prompts</strong> — the example questions users see when they open the agent.</li>
  <li><strong>Test</strong> in the right-side preview panel.</li>
  <li><strong>Create</strong> → share with selected colleagues, or with the whole Finance team.</li>
</ol>

<div class="ew-img-placeholder">📷 Screenshot placeholder — Agent Builder configure pane with Name, Description, Instructions, Knowledge fields</div>

### Field 1 — Name & Description

<div class="ew-prompt">Name: Edgewell Finance Policy Buddy

Description: Answers questions about Edgewell finance policies — travel & expense, approval thresholds, the close calendar, capex requests, and procurement guidelines. Always cites the source policy and section.</div>

### Field 2 — Instructions (the system prompt)

<div class="ew-prompt">You are the Edgewell Finance Policy Buddy — a friendly, precise assistant for the Edgewell Personal Care Finance team.

YOUR JOB
- Answer policy and process questions using ONLY the documents in your knowledge source.
- Always cite the specific policy name and section number you used.
- If a question is not covered in your knowledge, say so clearly and suggest who the user should contact (e.g., "This isn't covered in the policies I have access to — please reach out to the Controller's office.").

STYLE
- Direct, plain-language, no jargon.
- Lead with the answer in 1–2 sentences, then add the supporting detail.
- Use bullet points when listing thresholds or steps.

GUARDRAILS
- Never invent policy details, dollar amounts, or approval flows.
- Never give tax, legal, or audit opinions — direct those to the relevant function.
- If a user asks about confidential financial results, decline politely and remind them this agent is for policy questions only.

TONE
- Helpful, calm, occasionally warm. Think "the Finance colleague everyone wants to sit next to."</div>

### Field 3 — Starter prompts

<div class="ew-prompt">Starter prompts to add:

1. "What's the T&E limit for client meals in North America?"
2. "Who approves a capital request between $50K and $250K?"
3. "When does the FY26 close calendar lock the GL for month-end?"
4. "What's our policy on accepting gifts from suppliers?"
5. "How do I submit a vendor onboarding request?"</div>

### Field 4 — Knowledge sources

<div class="ew-callout ew-tip">
  <strong>💡 Start narrow.</strong> Point the agent at one well-curated SharePoint folder of approved finance policies. Don't dump the whole Finance site in there on day one — quality of sources directly drives quality of answers.
</div>

Suggested sources to add:
<div class="ew-pillrow">
  <span class="ew-pill">📁 SharePoint: /Finance/Policies/T&E</span>
  <span class="ew-pill">📁 SharePoint: /Finance/Policies/Approvals</span>
  <span class="ew-pill">📁 SharePoint: /Finance/Close/CloseCalendar.xlsx</span>
  <span class="ew-pill">📁 SharePoint: /Finance/Policies/Procurement</span>
</div>

### Test it before you ship

In the preview pane on the right, try the starter prompts plus a few edge cases:

<div class="ew-prompt">Test cases to run before you share the agent:

1. A clear, in-scope question:
   "What's the daily T&E limit for client dinners in the US?"

2. A question on the edge of policy:
   "If I take a $400K project to my VP, do I still need CFO approval?"

3. An out-of-scope question (should politely decline):
   "What was Schick's gross margin last quarter?"

4. A trick question (should not invent an answer):
   "What's the policy on accepting NFTs as supplier gifts?"</div>

<div class="ew-callout ew-warn">
  <strong>⚠️ Pilot, then expand.</strong> Share with 3–5 colleagues for a week. Collect their feedback inside the agent's chat history. Refine the instructions and knowledge sources before opening it up to the whole team.
</div>

### Where this can go next

<div class="ew-grid">
  <div class="ew-card">
    <h4>🧾 Variance Commentary Helper</h4>
    <p>Drafts month-end variance narratives in your team's voice and format.</p>
  </div>
  <div class="ew-card">
    <h4>📋 Retailer Deduction Triage</h4>
    <p>Classifies incoming retailer deductions and routes to the right analyst.</p>
  </div>
  <div class="ew-card">
    <h4>📅 Close Calendar Concierge</h4>
    <p>Knows every deadline, every owner, every dependency in your monthly close.</p>
  </div>
</div>

</div>

---

<div class="ew-section" id="wrap-up">
<h2>🎯 Wrap-up & Next Steps <span class="ew-time">~3 min</span></h2>

### Three things to do this week

<ol class="ew-steps">
  <li><strong>Set up Memory.</strong> 5 minutes. Pays back forever. Use the prompt in Section 1.</li>
  <li><strong>Save 2 prompts</strong> you'll reuse — one for inbox triage, one for Excel analysis.</li>
  <li><strong>Pilot the Finance Policy Buddy agent</strong> with 3 colleagues before sharing broadly.</li>
</ol>

### What's coming in the deeper sessions

<div class="ew-pillrow">
  <span class="ew-pill">📊 Variance analysis deep-dive</span>
  <span class="ew-pill">🏷️ Trade spend & promo ROI</span>
  <span class="ew-pill">🤖 Building your second & third agents</span>
  <span class="ew-pill">🔐 Governance & responsible AI</span>
</div>

### Resources

- 🎓 [Microsoft Copilot Learning Hub](https://adoption.microsoft.com/en-us/copilot/)
- 📚 [Prompt Library — official starter prompts](https://copilot.cloud.microsoft/en-us/prompts)
- 🛠️ [Agent Builder docs](https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/copilot-studio-agent-builder)
- 📝 Erik's prior demo guides:
  - [10 — Copilot Basics (Legal)](https://emontes07.github.io/Learning/Instructions/Demos/10-Legal-Demo.html)
  - [11 — Finance / Excel](https://emontes07.github.io/Learning/Instructions/Demos/11-Finance-Demo.html)
  - [12 — Researcher & Analyst Agents](https://emontes07.github.io/Learning/Instructions/Demos/12-Researcher-Analyst-Demo.html)
  - [Executive Agents — Agent Builder](https://emontes07.github.io/Learning/Instructions/Prompts/Exec-Agents.html)

</div>

<div class="ew-footer">
  <strong>🪒 Built for the Edgewell Finance team</strong><br/>
  Erik Montes • Senior Solution Engineer • Microsoft<br/>
  <em>Questions or follow-up? Reach out anytime.</em>
</div>
