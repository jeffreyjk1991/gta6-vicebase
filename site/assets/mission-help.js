/* Browser-local mission checklists. No network requests or game-save access. */
(() => {
  'use strict';

  const form = document.getElementById('mission-form');
  const dataElement = document.getElementById('mission-help-data');
  if (!form || !dataElement) return;

  let data;
  try {
    data = JSON.parse(dataElement.textContent);
  } catch (_) {
    return; // The crawlable quick-help sections remain usable.
  }

  const own = (object, key) => typeof key === 'string' && Object.prototype.hasOwnProperty.call(object, key);
  const validIssue = value => own(data.issues, value);
  const validMission = value => value === 'none' || own(data.missions, value);
  const validPlatform = value => value === 'ps5' || value === 'xbox';
  const byId = id => document.getElementById(id);
  const platform = byId('mission-platform');
  const issue = byId('mission-issue');
  const mission = byId('mission-choice');
  const note = byId('mission-note');
  const results = byId('mission-results');
  const resultTitle = byId('mission-result-title');
  const stepList = byId('mission-steps');
  const status = byId('mission-status');
  const resumePanel = byId('mission-resume');
  const STORAGE_KEY = 'gtasix-mission-plan-v1';
  let plan = null;
  let savedPlan = null;
  let generalHintCount = 0;
  let missionHintCount = 0;
  let revision = 0;

  function platformLabel(value) {
    return value === 'xbox' ? 'Xbox Series X|S' : 'PS5 / PS5 Pro';
  }

  function validatePlan(value) {
    if (!value || typeof value !== 'object' || value.version !== 1 ||
        !validPlatform(value.platform) || !validIssue(value.issue) || !validMission(value.mission)) return null;
    const length = data.issues[value.issue].steps.length;
    const completed = Array.isArray(value.completed)
      ? [...new Set(value.completed.filter(index => Number.isInteger(index) && index >= 0 && index < length))]
      : [];
    return {version: 1, platform: value.platform, issue: value.issue, mission: value.mission, completed};
  }

  function readSavedPlan() {
    try {
      const text = localStorage.getItem(STORAGE_KEY);
      return text ? validatePlan(JSON.parse(text)) : null;
    } catch (_) {
      return null;
    }
  }

  function updateResumePanel() {
    resumePanel.hidden = !savedPlan;
    byId('mission-clear').hidden = !savedPlan;
  }

  function say(message) {
    status.textContent = message;
  }

  function safeUrl() {
    const url = new URL(window.location.pathname, window.location.origin);
    if (plan) {
      url.searchParams.set('platform', plan.platform);
      url.searchParams.set('issue', plan.issue);
      if (plan.mission !== 'none') url.searchParams.set('mission', plan.mission);
    }
    return url.href;
  }

  function updateUrl() {
    try {
      window.history.replaceState(null, '', safeUrl());
    } catch (_) {
      // Embedded previews may deny history changes; the checklist still works.
    }
  }

  function suggestIssue(text) {
    const patterns = [
      ['technical', /crash|freez|frozen|black screen|loading screen|won.?t (launch|start)|error code/i],
      ['save', /save|autosave|lost progress|missing progress|cloud sync/i],
      ['character', /switch|swap|character|partner menu/i],
      ['driving', /driv|chase|steer|boat|handling|corner|vehicle|car\b/i],
      ['combat', /combat|shoot|aim|fight|enemy|enemies|escape|cover/i],
      ['route', /route|destination|entrance|reach|waypoint|road|lost|map/i],
      ['objective', /next mission|no mission|marker|objective|what (do|to)|where (do|to)/i],
      ['mission', /mission|stuck|progress|interact|collect|door|code|call/i],
    ];
    const match = patterns.find(([, pattern]) => pattern.test(text));
    return match ? match[0] : 'objective';
  }

  function suggestMission(text) {
    const normalized = text.toLowerCase().replace(/[^a-z0-9]+/g, ' ').trim();
    return Object.keys(data.missions).find(key => {
      const title = data.missions[key].title.toLowerCase();
      return (` ${normalized} `).includes(` ${title} `);
    }) || 'none';
  }

  function updateProgress() {
    if (!plan) return;
    byId('mission-progress').textContent = `${plan.completed.length} of ${data.issues[plan.issue].steps.length} checks completed`;
  }

  function makeLink(label, href) {
    const anchor = document.createElement('a');
    anchor.textContent = label;
    const url = new URL(href, window.location.origin);
    if (url.protocol !== 'https:' && url.origin !== window.location.origin) return anchor;
    anchor.href = url.href;
    if (url.origin !== window.location.origin) {
      anchor.target = '_blank';
      anchor.rel = 'noopener noreferrer';
    }
    return anchor;
  }

  function appendHint(container, text, number) {
    const item = document.createElement('div');
    item.className = 'mission-hint';
    const label = document.createElement('strong');
    label.textContent = `Hint ${number}`;
    const paragraph = document.createElement('p');
    paragraph.textContent = text;
    item.append(label, paragraph);
    container.append(item);
  }

  function renderPlan(nextPlan, reason, moveFocus) {
    plan = validatePlan(nextPlan);
    if (!plan) return;
    revision += 1;
    const currentIssue = data.issues[plan.issue];
    platform.value = plan.platform;
    issue.value = plan.issue;
    mission.value = plan.mission;
    generalHintCount = 0;
    missionHintCount = 0;
    byId('mission-start').hidden = true;
    results.hidden = false;
    resultTitle.textContent = currentIssue.title;
    byId('mission-match').textContent = `${platformLabel(plan.platform)} · ${reason}`;
    byId('mission-result-intro').textContent = currentIssue.intro;
    stepList.replaceChildren();
    currentIssue.steps.forEach((text, index) => {
      const item = document.createElement('li');
      const label = document.createElement('label');
      const input = document.createElement('input');
      input.type = 'checkbox';
      input.checked = plan.completed.includes(index);
      input.setAttribute('aria-label', `Complete check ${index + 1}: ${text}`);
      const span = document.createElement('span');
      span.textContent = text;
      item.classList.toggle('is-complete', input.checked);
      input.addEventListener('change', () => {
        plan.completed = input.checked
          ? [...new Set([...plan.completed, index])]
          : plan.completed.filter(value => value !== index);
        item.classList.toggle('is-complete', input.checked);
        revision += 1;
        updateProgress();
        say('Checklist updated. Select Save plan to keep these changes for your next visit.');
      });
      label.append(input, span);
      item.append(label);
      stepList.append(item);
    });
    updateProgress();
    byId('mission-general-hints').replaceChildren();
    byId('mission-next-hint').disabled = false;
    byId('mission-next-hint').textContent = 'Show a hint';
    byId('mission-gentle').hidden = !currentIssue.hints.length;
    byId('mission-specific').hidden = plan.mission === 'none';
    byId('mission-specific-hints').replaceChildren();
    byId('mission-solution').open = false;
    byId('mission-solution-text').textContent = '';
    if (plan.mission !== 'none') {
      const currentMission = data.missions[plan.mission];
      byId('mission-specific-title').textContent = currentMission.title;
      byId('mission-specific-next').disabled = false;
      byId('mission-specific-next').textContent = 'Reveal a mission hint';
      byId('mission-solution-text').textContent = currentMission.solution;
      byId('mission-source').href = currentMission.source;
    }
    const links = byId('mission-result-links');
    links.replaceChildren(...currentIssue.links.map(([label, href]) => makeLink(label, href)));
    byId('mission-copy-fallback').hidden = true;
    byId('mission-copy-text').value = '';
    say('Check off the steps as you try them. Save plan keeps choices and completed steps in this browser.');
    updateUrl();
    updateResumePanel();
    if (moveFocus) resultTitle.focus({preventScroll: true});
    if (moveFocus && window.matchMedia('(max-width: 960px)').matches) {
      results.scrollIntoView({block: 'start', behavior: 'auto'});
    }
  }

  form.addEventListener('submit', event => {
    event.preventDefault();
    const description = note.value.trim().slice(0, 300);
    const wasSuggested = !validIssue(issue.value);
    const chosenIssue = wasSuggested ? suggestIssue(description) : issue.value;
    const chosenMission = mission.value === 'none' ? suggestMission(description) : mission.value;
    const reason = wasSuggested && description
      ? `Suggested match: ${data.issues[chosenIssue].label}. Change the problem above if needed.`
      : `Selected: ${data.issues[chosenIssue].label}`;
    renderPlan({version: 1, platform: validPlatform(platform.value) ? platform.value : 'ps5',
      issue: chosenIssue, mission: validMission(chosenMission) ? chosenMission : 'none', completed: []}, reason, true);
  });

  byId('mission-next-hint').addEventListener('click', () => {
    if (!plan) return;
    const hints = data.issues[plan.issue].hints;
    if (generalHintCount >= hints.length) return;
    appendHint(byId('mission-general-hints'), hints[generalHintCount], generalHintCount + 1);
    generalHintCount += 1;
    const button = byId('mission-next-hint');
    button.disabled = generalHintCount >= hints.length;
    button.textContent = button.disabled ? 'All hints shown' : 'Show another hint';
  });

  byId('mission-specific-next').addEventListener('click', () => {
    if (!plan || plan.mission === 'none') return;
    const hints = data.missions[plan.mission].hints;
    if (missionHintCount >= hints.length) return;
    appendHint(byId('mission-specific-hints'), hints[missionHintCount], missionHintCount + 1);
    missionHintCount += 1;
    const button = byId('mission-specific-next');
    button.disabled = missionHintCount >= hints.length;
    button.textContent = button.disabled ? 'All mission hints shown' : 'Reveal the next mission hint';
  });

  byId('mission-save').addEventListener('click', () => {
    if (!plan) return;
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(plan));
      savedPlan = validatePlan(plan);
      updateResumePanel();
      say('Plan saved in this browser. Your objective note and revealed spoilers were not saved.');
    } catch (_) {
      say('This browser could not save the plan. Use Copy checklist to keep a copy instead.');
    }
  });

  function clearSavedPlan() {
    try {
      localStorage.removeItem(STORAGE_KEY);
      savedPlan = null;
      updateResumePanel();
      if (plan) say('Saved plan cleared. Your current on-screen checklist is still available.');
    } catch (_) {
      if (plan) say('This browser did not allow clearing stored data. Check its site-data settings.');
      else resumePanel.querySelector('p').textContent = 'This browser did not allow clearing stored data. Check its site-data settings.';
    }
  }

  byId('mission-clear').addEventListener('click', clearSavedPlan);
  byId('mission-clear-start').addEventListener('click', clearSavedPlan);
  byId('mission-resume-button').addEventListener('click', () => {
    if (!savedPlan) return;
    note.value = '';
    renderPlan(savedPlan, 'Resumed your saved checklist. Spoiler hints are hidden again.', true);
    say('Saved checklist resumed. Select Save plan after making changes to keep the latest version.');
  });

  function checklistText() {
    const currentIssue = data.issues[plan.issue];
    const lines = ['GTASIX — ' + currentIssue.title, platformLabel(plan.platform)];
    if (plan.mission !== 'none') lines.push('Mission: ' + data.missions[plan.mission].title);
    lines.push('', ...currentIssue.steps.map((text, index) => `${plan.completed.includes(index) ? '[x]' : '[ ]'} ${text}`));
    lines.push('', safeUrl(), 'Mission solutions and your private note are not included.');
    return lines.join('\n');
  }

  async function copyText(text, successMessage) {
    const currentRevision = revision;
    try {
      if (!navigator.clipboard || typeof navigator.clipboard.writeText !== 'function') throw new Error('clipboard unavailable');
      await navigator.clipboard.writeText(text);
      if (currentRevision !== revision) return;
      byId('mission-copy-fallback').hidden = true;
      say(successMessage);
    } catch (_) {
      if (currentRevision !== revision) return;
      byId('mission-copy-fallback').hidden = false;
      const field = byId('mission-copy-text');
      field.value = text;
      field.focus();
      field.select();
      say('Automatic copying is unavailable. Select and copy the text shown below.');
    }
  }

  byId('mission-copy').addEventListener('click', () => {
    if (plan) copyText(checklistText(), 'Checklist copied. Your private note and mission solutions were left out.');
  });
  byId('mission-share').addEventListener('click', () => {
    if (plan) copyText(safeUrl(), 'Help link copied. It contains your console, problem and selected mission, but no note or completed steps.');
  });

  savedPlan = readSavedPlan();
  updateResumePanel();
  const params = new URLSearchParams(window.location.search);
  const queryPlatform = params.get('platform');
  const queryIssue = params.get('issue');
  const queryMission = params.get('mission');
  if (validPlatform(queryPlatform)) platform.value = queryPlatform;
  if (validIssue(queryIssue)) issue.value = queryIssue;
  if (validMission(queryMission)) mission.value = queryMission;
  if (validIssue(queryIssue) || (validMission(queryMission) && queryMission !== 'none')) {
    renderPlan({version: 1, platform: platform.value, issue: validIssue(queryIssue) ? queryIssue : 'mission',
      mission: validMission(queryMission) ? queryMission : 'none', completed: []}, 'Opened from a help link. Hints and solutions start hidden.', false);
  }
})();
