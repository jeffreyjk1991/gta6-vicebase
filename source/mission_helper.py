"""Spoiler-controlled gameplay help, generated as crawlable HTML.

General checklists are GTASIX guidance. Specific early-mission hints are
attributed to VGC's published walkthroughs and are not independent playtests.
"""
import json
from html import escape as h

PATH = "/gta-6-mission-help/"
TITLE = "Stuck in GTA 6? Mission Help & Next Steps | GTASIX"
DESCRIPTION = "Stuck in a GTA 6 mission or missing your next objective? Get spoiler-controlled hints, driving help and a saved next-step checklist for PS5 and Xbox."
REVIEWED = "2026-11-20"
SETTINGS_SOURCE = "https://support.rockstargames.com/articles/4jUHNdP22SmaKSF8DWqhXC/how-to-change-grand-theft-auto-vi-settings"
WALKTHROUGH_SOURCE = "https://www.videogameschronicle.com/guide/grand-theft-auto-6-complete-walkthrough-hub/"

ISSUES = {
    "objective": {
        "label": "I can't find the next objective",
        "title": "Find the next thing the game is asking for",
        "intro": "Start with the current instruction. A missing marker and an unfinished objective need different checks.",
        "steps": [
            "Pause and read the current objective exactly as it appears. Note whether it asks you to travel, meet someone, use an item or make contact.",
            "Check the map legend and your active destination. If directions or prompts seem absent, review Pause > Settings > UI > Navigation and Prompts.",
            "Return to the last instruction you completed. Look for an on-screen interaction or contact request before leaving the area.",
            "If a mission name is visible, choose it above for a targeted hint or use the linked walkthrough directory. Do not assume every available mission must be played in one fixed order.",
        ],
        "hints": [
            "Use the wording of the objective as your clue: 'reach', 'collect' and 'call' each require a different action.",
            "If the same instruction never changes after you complete it, switch to 'A mission won't progress' and check whether you missed an interaction.",
        ],
        "links": [["Browse mission walkthroughs", WALKTHROUGH_SOURCE], ["Explore the map", "/map/"]],
    },
    "mission": {
        "label": "A mission won't progress",
        "title": "Work out which objective is still incomplete",
        "intro": "Try these checks before replaying a whole mission. The exact on-screen instruction is more useful than guessing what should happen next.",
        "steps": [
            "Read the current objective and compare it with what you actually did. Reaching a place may still require talking, collecting or using a marked entrance.",
            "Look around the objective area for an interaction prompt. Try the marked approach rather than forcing an unmarked shortcut.",
            "Check whether a companion or required vehicle has reached the objective with you. Wait for any active dialogue or animation to finish.",
            "Use a mission-specific hint below if your mission is covered. Otherwise open the walkthrough directory and match the exact mission title.",
            "If the game appears frozen or an interaction repeatedly fails, record the objective and game version, then use the technical Help Center. Avoid deleting saved progress.",
        ],
        "hints": [
            "Separate 'I do not know the solution' from 'the expected interaction is not happening'. A walkthrough helps with the first; technical checks help with the second.",
            "If the game offers a checkpoint retry, read its warning before using it. Expect unsaved actions after that checkpoint to be lost.",
        ],
        "links": [["Mission walkthrough directory", WALKTHROUGH_SOURCE], ["Crashes, freezes and loading help", "/gta-6-help/"]],
    },
    "route": {
        "label": "I can't reach a destination",
        "title": "Find a workable approach to the destination",
        "intro": "Treat the in-game objective and navigation as the authority. Our community map is a discovery aid, not a verified mission route.",
        "steps": [
            "Recheck the destination and route in your game. Zoom in before the last turn so you can see nearby roads, entrances or a change in elevation.",
            "If the direct approach is blocked, look for a marked entrance or a road around the site. Do not assume a visible door can be opened.",
            "Check whether the objective requires a particular vehicle, passenger or approach. Follow the current instruction before choosing a shortcut.",
            "If guidance is difficult to read, inspect Pause > Settings > UI > Navigation and Prompts. Change one setting, return to play and compare.",
        ],
        "hints": [
            "When you appear to be at the marker, check whether the destination is above, below or behind your current position.",
            "Slow down for the final approach. It is easier to identify the correct entrance without overshooting the objective.",
        ],
        "links": [["Open the community map", "/map/"], ["Find comfortable camera settings", "/guides/gta-6-best-settings/"]],
    },
    "driving": {
        "label": "Driving or a chase is too difficult",
        "title": "Make the next driving attempt easier",
        "intro": "Use a controlled retry to identify whether the problem is the route, visibility or steering. These are practice suggestions, not measured vehicle rankings.",
        "steps": [
            "Read the fail message or objective first. Work out whether you need to follow, escape, reach a destination or keep something intact.",
            "Review vehicle controls under Pause > Settings > Control Scheme > Land/Water Vehicles. Use the button labels shown for your selected console and control scheme.",
            "Inspect Pause > Settings > Camera > Land & Water Vehicles if the camera makes turns difficult to judge. Try one change at a time.",
            "On your next attempt, brake before a sharp turn, steer smoothly and build speed after the exit. Focus on completing the route before trying shortcuts.",
            "For a boat objective, check whether you need to slow down or approach a marker from another side. If you are in Gone Fishing, select that mission for a specific hint.",
        ],
        "hints": [
            "Choose one difficult corner or instruction to improve on the next attempt, rather than changing every setting at once.",
            "If motion makes the road hard to read, use the settings finder to review camera and motion-comfort options.",
        ],
        "links": [["Open the settings finder", "/guides/gta-6-best-settings/?style=driving"], ["Driving and route guides", "/categories/gameplay/"]],
    },
    "combat": {
        "label": "Combat or escaping keeps failing",
        "title": "Check the objective before taking another fight",
        "intro": "Some objectives are about reaching safety or interacting with a target. Check the instruction before assuming every opponent must be defeated.",
        "steps": [
            "Read the objective and last fail message. Identify whether the game asks you to fight, protect, escape or reach a marked location.",
            "Before the next attempt, check your available equipment and the controls for aiming, movement and taking cover in the current control scheme.",
            "Use the environment to reduce exposure and move with a clear destination in mind. If the objective is to escape, prioritize a safe route.",
            "Review Pause > Settings > Gameplay for Combat, Movement and Accessibility options. Choose available assistance that makes the game comfortable for you.",
        ],
        "hints": [
            "If the fight repeatedly ends in the same place, change your position or approach before changing multiple settings.",
            "A mission-specific hint can tell you when reaching the next objective matters more than finishing a fight.",
        ],
        "links": [["Aim, camera and accessibility settings", "/guides/gta-6-best-settings/"], ["Find your mission walkthrough", WALKTHROUGH_SOURCE]],
    },
    "character": {
        "label": "I can't switch characters",
        "title": "Check the current story and mission context",
        "intro": "A control that works in free roam may be restricted by the current story sequence. Follow the active prompt before forcing a different action.",
        "steps": [
            "Check whether you are in a mission, cutscene or required interaction. Finish the current instruction before trying to switch again.",
            "Read the character-switching guide and compare its conditions with your current progress. Do not assume the feature is available at every point.",
            "Check your selected control scheme in the game instead of copying a button combination for another console.",
            "If an expected prompt is absent, inspect UI > Prompts in Settings. If a control does not respond anywhere, use the controller troubleshooting guide.",
        ],
        "hints": [
            "An unavailable action during a scripted sequence does not by itself mean your save is broken.",
            "Record the objective shown on-screen if the guide's expected conditions and your game do not match.",
        ],
        "links": [["Character-switching guide", "/guides/gta-6-how-to-switch-characters/"], ["Controller troubleshooting", "/guides/gta-6-audio-controller-problems/"]],
    },
    "save": {
        "label": "I can't save or find my progress",
        "title": "Protect your progress while checking the save",
        "intro": "Keep your current save intact while you establish what is missing. Saving a checklist here does not save your game.",
        "steps": [
            "Check which in-game save or autosave you loaded and compare its timestamp with your last session.",
            "If saving is unavailable during an active sequence, finish the current objective and read the save guide before exiting.",
            "Do not overwrite or delete another slot while investigating missing progress. Keep any existing local and cloud versions until you understand their timestamps.",
            "Use the Help Center for missing saves or cloud-sync problems. Follow the instructions for your console before making changes to stored data.",
        ],
        "hints": [
            "A completed objective in this web checklist is just your note; it is not connected to your game or console.",
            "If you need support, record the console, last known save time and what happened immediately before the progress disappeared.",
        ],
        "links": [["How saving works", "/guides/gta-6-how-to-save/"], ["Missing-save troubleshooting", "/gta-6-help/?issue=save"]],
    },
    "technical": {
        "label": "The game is frozen, crashing or loading",
        "title": "Use the technical troubleshooting path",
        "intro": "A frozen screen or crash needs a different checklist from a mission puzzle. Start with the console-specific Help Center.",
        "steps": [
            "Note your console, the exact error text and whether the failure occurs at the same objective each time.",
            "Open the Help Center below and choose crashing, loading or the matching symptom.",
            "Check game and console updates. Preserve save data while following the suggested first checks.",
            "If the issue repeats, keep the mission name and game version ready for Rockstar Support.",
        ],
        "hints": [
            "A working menu with an unclear objective is different from a game that no longer responds. Choose the symptom that matches what you can still do.",
        ],
        "links": [["Open GTA 6 Help Center", "/gta-6-help/"], ["Rockstar Support", "https://support.rockstargames.com/VI"]],
    },
}

MISSIONS = {
    "prologue": {
        "title": "Prologue",
        "description": "Hints for interactions and the opening chase, based on VGC's walkthrough.",
        "source": "https://www.videogameschronicle.com/guide/gta-6-prologue-mission-walkthrough/",
        "hints": [
            "For the opening interaction, speak to your cellmate, then follow the guard to the office.",
            "If the later chase keeps ending the same way, wait to see whether another sequence begins before restarting.",
        ],
        "solution": "VGC's walkthrough says being caught during that opening chase can advance the story. Follow the resulting sequence rather than restarting immediately.",
    },
    "gone-fishing": {
        "title": "Gone Fishing",
        "description": "Help with the boat collection, camp entrance and escape objective.",
        "source": "https://www.videogameschronicle.com/guide/gta-6-gone-fishing-mission-walkthrough/",
        "hints": [
            "Slow the boat near floating packages so Cal can collect them.",
            "At the camp, approach the marked building through its front door.",
        ],
        "solution": "For the escape, prioritize reaching the dock. VGC's walkthrough does not require clearing every enemy first.",
    },
    "gear-up": {
        "title": "Gear Up",
        "description": "Find the next interaction when the shopping objective seems finished.",
        "source": "https://www.videogameschronicle.com/guide/gta-6-gear-up-mission-walkthrough/",
        "hints": [
            "Check the mailbox outside Jason's house for the cash you need.",
            "At Ammu-Nation, choose one of the offered longarms; the walkthrough does not require a single specific choice.",
        ],
        "solution": "After the encounter outside, call Donnie to continue. Check the current objective before driving away.",
    },
    "lab-fees": {
        "title": "Lab Fees",
        "description": "Find the correct shop and reveal door codes only if you want the solution.",
        "source": "https://www.videogameschronicle.com/guide/gta-6-lab-fees-mission-walkthrough/",
        "hints": [
            "Look behind the surf shop for the shop you need.",
            "After collecting what the objective requires, call Brian for the drop location.",
        ],
        "solution": "VGC lists 0420 for the backroom and 7700 for the drop-off lockup. Use each code at its matching objective.",
    },
}

FAQS = [
    ("What should I do if I am stuck in a GTA 6 mission?", "Read the current objective, identify the missing interaction, and choose a problem in the helper. For a covered early mission, reveal a hint first and open the solution only if you need it. A frozen game belongs in the technical Help Center."),
    ("How do I find my next GTA 6 mission?", "Check your active objective, map legend and any contact instruction. Review the in-game UI navigation and prompt settings if markers are difficult to see. Match your mission name with a walkthrough instead of assuming there is one fixed mission order."),
    ("Does this cover every GTA 6 mission?", "No. Detailed hints currently cover Prologue, Gone Fishing, Gear Up and Lab Fees, attributed to VGC's published walkthroughs. General checklists help with objectives, routes, driving, combat, character switching and saves. The linked walkthrough directory offers broader coverage."),
    ("Will the mission helper reveal story spoilers?", "The initial checklist avoids story outcomes. Mission hints appear one at a time when you ask. Exact solutions and codes require a separate reveal action. Linked external walkthroughs may contain spoilers."),
    ("Can I save my checklist and return later?", "Yes. Select Save plan to keep the console, problem, mission choice and completed checklist steps in this browser. Your objective note is not saved. Use Resume saved plan on your next visit, or Clear saved plan to remove it. This does not connect to your game save."),
    ("What happens to the objective text I enter?", "It is used only on this page to suggest a matching problem or covered mission. It is not sent to GTASIX, saved by this helper, copied into the checklist or included in shared links."),
]


def mission_index():
    return [{
        "slug": PATH.strip("/"), "href": PATH,
        "title": "Stuck in GTA 6? Mission help and next steps",
        "summary": DESCRIPTION, "category": "Gameplay & tips", "status": "INTERACTIVE HELP",
        "aliases": ["gta 6 mission help", "gta vi stuck", "what to do next", "next mission not showing",
                    "gta 6 walkthrough", "prologue", "gone fishing", "gear up", "lab fees",
                    "driving chase help", "mission not progressing", "spoiler free hints"],
    }]


def _link(label, url, class_name=""):
    external = url.startswith("https://")
    return ('<a href="' + h(url, quote=True) + '"' + (' class="' + class_name + '"' if class_name else '') +
            (' target="_blank" rel="noopener noreferrer"' if external else '') + '>' + h(label) + '</a>')


def mission_views(site_url):
    issue_options = '<option value="auto">Suggest from my description</option>' + ''.join(
        '<option value="' + key + '">' + h(issue["label"]) + '</option>' for key, issue in ISSUES.items()
    )
    mission_options = '<option value="none">Not listed / not sure</option>' + ''.join(
        '<option value="' + key + '">' + h(mission["title"]) + '</option>' for key, mission in MISSIONS.items()
    )
    quick_help = ''.join(
        '<details class="mission-quick"><summary>' + h(issue["label"]) + '</summary><p>' + h(issue["intro"]) +
        '</p><ol>' + ''.join('<li>' + h(step) + '</li>' for step in issue["steps"] if not any(word in step for word in ('Settings', 'UI >', 'Control Scheme'))) + '</ol><div class="mission-links">' +
        ''.join(_link(label, url) for label, url in issue["links"]) + '</div></details>'
        for issue in ISSUES.values()
    )
    mission_cards = ''.join(
        '<article class="mission-source-card"><h3>' + h(mission["title"]) + '</h3><p>' + h(mission["description"]) +
        '</p>' + _link("Read VGC's walkthrough", mission["source"]) + '</article>' for mission in MISSIONS.values()
    )
    faq_html = ''.join('<details class="mission-quick"><summary>' + h(q) + '</summary><p>' + h(a) + '</p></details>' for q, a in FAQS)
    data = json.dumps({"issues": ISSUES, "missions": MISSIONS}, ensure_ascii=False, separators=(",", ":")).replace("<", "\\u003c")
    body = f'''<main class="wrap mission-main">
<section class="mission-hero" aria-labelledby="mission-heading">
  <nav class="mission-crumb" aria-label="Breadcrumb"><a href="/">Home</a><span>/</span><a href="/guides/">Guides</a><span>/</span><span>Mission help</span></nav>
  <p class="mission-kicker">YOUR NEXT MOVE</p>
  <h1 id="mission-heading">Stuck in GTA 6?<br><span>Find your next step.</span></h1>
  <p class="mission-lead">An unclear objective. A tricky chase. A mission that just won't move on. Choose what's holding you up and get a practical plan, with hints you reveal at your own pace.</p>
  <div class="mission-badges"><span>PS5 &amp; Xbox</span><span>Spoilers on your terms</span><span>Free, no account</span></div>
</section>

<section class="mission-workspace" aria-labelledby="mission-form-title">
  <div class="mission-form-panel">
    <p class="mission-kicker">START HERE</p><h2 id="mission-form-title">What's holding you up?</h2>
    <p>Describe the objective or pick a problem. You can change the suggested match before trying the steps.</p>
    <div id="mission-resume" class="mission-resume" hidden><p>A saved plan is available in this browser.</p><div class="mission-actions"><button type="button" id="mission-resume-button" class="mission-button secondary">Resume saved plan</button><button type="button" id="mission-clear-start" class="mission-button text">Clear saved plan</button></div></div>
    <form id="mission-form" action="#quick-help">
      <div class="mission-fields">
        <label for="mission-platform">Your console<select id="mission-platform"><option value="ps5">PS5 / PS5 Pro</option><option value="xbox">Xbox Series X|S</option></select></label>
        <label for="mission-issue">What is happening?<select id="mission-issue">{issue_options}</select></label>
      </div>
      <label for="mission-note">Current objective or problem <span class="mission-optional">(optional)</span></label>
      <textarea id="mission-note" rows="3" maxlength="300" placeholder="For example: Gone Fishing — the packages aren't being collected" aria-describedby="mission-note-help"></textarea>
      <p id="mission-note-help" class="mission-small">Your note stays on this page. It isn't saved, copied or included in shared links.</p>
      <label for="mission-choice">Early mission <span class="mission-optional">(optional)</span><select id="mission-choice">{mission_options}</select></label>
      <p class="mission-small">Detailed hints cover these four early missions. Other problems still get a practical checklist and a walkthrough link.</p>
      <button type="submit" class="mission-button primary">Find next steps</button>
    </form>
    <noscript><p class="mission-notice">The interactive checklist needs JavaScript. You can still use the quick-help sections and mission walkthrough links below.</p></noscript>
    <p class="mission-tech-link">Game crashing or stuck loading? <a href="/gta-6-help/">Open technical Help</a></p>
  </div>

  <div id="mission-start" class="mission-start">
    <span class="mission-compass" aria-hidden="true">✦</span><h2>One useful next step.<br>Then the next.</h2>
    <p>Get a checklist you can tick off, reveal a small hint when you need it, and save the plan to pick up later.</p>
    <ul><li>Start with the current objective</li><li>Keep story solutions hidden</li><li>Use a named source for specific missions</li></ul>
    <a href="#quick-help">Browse quick answers</a>
  </div>

  <section id="mission-results" class="mission-results" aria-labelledby="mission-result-title" hidden>
    <p class="mission-kicker">YOUR NEXT STEPS</p><h2 id="mission-result-title" tabindex="-1"></h2>
    <p id="mission-match" class="mission-match"></p><p id="mission-result-intro"></p>
    <p id="mission-progress" class="mission-progress" aria-live="polite"></p><ol id="mission-steps" class="mission-checklist"></ol>
    <div id="mission-gentle" class="mission-hint-panel"><h3>Need another nudge?</h3><div id="mission-general-hints" aria-live="polite"></div><button type="button" id="mission-next-hint" class="mission-button secondary">Show a hint</button></div>
    <div id="mission-specific" class="mission-hint-panel mission-specific" hidden>
      <p class="mission-kicker">MISSION-SPECIFIC HELP</p><h3 id="mission-specific-title"></h3><p class="mission-small">Based on VGC's published walkthrough. GTASIX has not independently playtested these steps.</p>
      <div id="mission-specific-hints" aria-live="polite"></div><button type="button" id="mission-specific-next" class="mission-button secondary">Reveal a mission hint</button>
      <details id="mission-solution" class="mission-solution"><summary>Reveal the mission solution / codes</summary><p id="mission-solution-text"></p></details>
      <a id="mission-source" target="_blank" rel="noopener noreferrer">Read the source walkthrough (may contain spoilers)</a>
    </div>
    <div id="mission-result-links" class="mission-links"></div>
    <div class="mission-actions"><button type="button" id="mission-save" class="mission-button primary">Save plan</button><button type="button" id="mission-copy" class="mission-button secondary">Copy checklist</button><button type="button" id="mission-share" class="mission-button secondary">Copy help link</button><button type="button" id="mission-clear" class="mission-button text">Clear saved plan</button></div>
    <p id="mission-status" class="mission-small" role="status" aria-live="polite">Saving keeps choices and checked steps in this browser. It does not save your game.</p>
    <div id="mission-copy-fallback" hidden><label for="mission-copy-text">Copy this text manually</label><textarea id="mission-copy-text" readonly rows="6"></textarea></div>
  </section>
</section>

<section id="quick-help" class="mission-section" aria-labelledby="quick-help-title"><div class="mission-section-heading"><p class="mission-kicker">QUICK ANSWERS</p><h2 id="quick-help-title">Common places players get stuck</h2><p>Use these first checks even if your mission isn't in the helper yet. Advice is conditional on the objective and options visible in your game.</p></div><div class="mission-quick-grid">{quick_help}</div><p class="mission-small">Settings menu references: {_link("Rockstar's GTA VI settings guide", SETTINGS_SOURCE)}. The practice checklists are GTASIX guidance, not guaranteed fixes for game bugs.</p></section>

<section class="mission-section" aria-labelledby="early-missions-title"><div class="mission-section-heading"><p class="mission-kicker">EARLY MISSION COVERAGE</p><h2 id="early-missions-title">A hint when you need it</h2><p>Select one of these missions in the helper to reveal hints individually. These are four covered missions, not a required play order. External guides contain spoilers.</p></div><div class="mission-source-grid">{mission_cards}</div><p class="mission-small">Need a different mission? {_link("Open VGC's complete walkthrough hub", WALKTHROUGH_SOURCE)}.</p></section>

<section class="mission-section" aria-labelledby="mission-faq-title"><h2 id="mission-faq-title">Mission help: common questions</h2><div class="mission-faqs">{faq_html}</div></section>
<section class="mission-source-note"><h2>How this help is checked</h2><p>Reviewed November 20, 2026. Rockstar's documentation supports the settings paths. Mission details are attributed to VGC's published walkthroughs; general checklists are editorial suggestions. Game updates and your current objective can change the right next step.</p><a href="/editorial-policy/">Read our editorial standards</a></section>
<script type="application/json" id="mission-help-data">{data}</script>
</main>'''
    ld = [
        {"@context": "https://schema.org", "@type": "Article", "headline": "Stuck in GTA 6? Mission help and next steps", "description": DESCRIPTION,
         "datePublished": REVIEWED, "dateModified": REVIEWED, "author": {"@type": "Organization", "name": "GTASIX Editorial"},
         "citation": [SETTINGS_SOURCE, WALKTHROUGH_SOURCE] + [mission["source"] for mission in MISSIONS.values()]},
        {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQS]},
        {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": site_url + "/"},
            {"@type": "ListItem", "position": 2, "name": "Guides", "item": site_url + "/guides/"},
            {"@type": "ListItem", "position": 3, "name": "Mission help", "item": site_url + PATH},
        ]},
    ]
    extra = '<link rel="stylesheet" href="/assets/mission-help.css"><script defer src="/assets/mission-help.js"></script>'
    yield PATH, TITLE, DESCRIPTION, body, ld, extra
