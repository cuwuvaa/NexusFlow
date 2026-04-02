# MVP Scope

## Document Purpose

This document defines the **MVP boundaries** for NexusFlow.

Its purpose is to protect the project from **feature creep** and preserve focus on the first usable release.  

---

## MVP Goal

The NexusFlow MVP should prove that the product can solve the core problem:

> **provide a technical team with a unified space for communication, role distribution, task execution, and AI-assisted context support.**

In practical terms, the first version should allow a team to:

- sign up,
- create a team,
- assign roles,
- communicate,
- create and track tasks,
- use AI to summarize communication.

If this works in a stable and coherent way, the MVP is successful.

---

## IN Scope

### 1. Authentication
Basic authentication and access management.

Includes:

- user registration,
- login,
- refresh/access tokens,
- logout,
- password change,
- basic route protection.

---

### 2. Users
Basic user management.

Includes:

- user profile,
- name / username / email,
- avatar URL (optional),
- self-profile view,
- updating basic profile information,
- team member list.

---

### 3. Teams
Team management as the primary organizational unit of the product.

Includes:

- team creation,
- team view,
- inviting members,
- member joining,
- member list,
- basic team settings.

---

### 4. Roles
A role model inside the team.

Includes:

- system roles (e.g. owner, manager, backend, frontend, devops, tester, ai),
- assigning a role to a member,
- displaying role information inside the team,
- using roles for basic organizational structure.

> In the MVP, roles are primarily for team organization, not for a highly complex permission system.

---

### 5. Tasks
Basic task management.

Includes:

- task creation,
- task editing,
- assignee assignment,
- task statuses,
- priority,
- deadline (optional),
- task list view,
- tasks by member / by team view.

This is one of the core blocks of the MVP.

---

### 6. Chat
Real-time team communication.

Includes:

- team chats,
- message sending,
- message history,
- basic real-time delivery,
- linking messages to a team / channel.

> For MVP, a text-first chat is sufficient without advanced media scenarios.

---

### 7. AI Summaries
The first AI module embedded directly into the main workflow.

Includes:

- chat summarization,
- key decision extraction,
- discussion highlights,
- digest generation for a conversation / channel.

This should be **useful AI**, not decorative AI.

---

## OUT of Scope

The following features are **intentionally excluded** from the first version.

They may be implemented later, but they must not block MVP delivery.

---

### 1. Calls / Voice / Video
Not part of MVP:

- voice calls,
- video calls,
- group calls,
- live meeting rooms.

Reason: high real-time media complexity and low criticality for the first release.

---

### 2. Board / Shared Canvas
Not part of MVP:

- visual boards,
- whiteboard,
- collaborative canvas,
- Miro-like collaboration.

Reason: this is a large standalone product block that significantly expands scope.

---

### 3. Architecture Graph Editor
Not part of MVP:

- visual architecture editor,
- drag-and-drop service diagrams,
- dependency graph,
- interactive architecture map.

Reason: a strong long-term feature, but too large for MVP and better built after validating the product’s core value.

---

### 4. GitHub Integrations
Not part of MVP:

- repository sync,
- pull requests,
- issues,
- GitHub webhooks,
- commit activity.

Reason: integrations sharply increase complexity and should come only after the core platform is stable.

---

### 5. Advanced Notifications
Not part of MVP:

- advanced notification rules,
- email notifications,
- push notifications,
- smart reminder pipelines,
- notification preferences matrix.

In MVP, only **simple in-app notifications** are acceptable if needed for baseline UX.

---

## Non-Goals of MVP

The MVP does **not** aim to:

- replace every tool a team uses,
- become a full Slack + Jira + Miro + GitHub equivalent in one release,
- cover every possible engineering workflow,
- solve all collaboration problems at once.

The MVP only needs to prove one thing:

> **a team can work comfortably in NexusFlow as a unified operational environment.**

---

## MVP Success Criteria

The MVP can be considered successful if a team can complete the following flow:

1. A user signs up
2. Creates a team
3. Invites members
4. Assigns roles
5. Creates tasks
6. Discusses work in chat
7. Uses AI to get concise summaries of discussions

If this flow works:

- reliably,
- coherently,
- without architectural chaos,
- on top of a strong backend foundation,

then the MVP has achieved its goal.

---

## Scope Control Rule

Any new feature idea that appears during development must pass this rule:

> If the MVP still solves the core problem without it, then it is not required for MVP.

This rule should be enforced strictly.