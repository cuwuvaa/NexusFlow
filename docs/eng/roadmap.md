# Roadmap

## Roadmap Goal

The roadmap exists not as a “wishlist”, but as a way to develop NexusFlow in a **phased, controlled, and engineering-oriented manner**.

Core principle:

> First the foundation, then the core workflows, then AI, then product hardening.

---

## Milestone 1 — Foundation

### Goal
Prepare the engineering foundation of the project.

### What should be completed

#### Product / Project Setup
- finalize MVP scope
- prepare docs/
- define domain model
- choose naming conventions
- create an initial backlog

#### Repository / Engineering Setup
- initialize backend repository
- set up project structure
- configure environments
- Docker / Docker Compose
- pre-commit hooks
- linters / formatters
- basic CI

#### Backend Core
- FastAPI bootstrap
- config management
- logging
- database connection
- Alembic migrations
- base models / shared abstractions
- error handling strategy

### Milestone outcome
By the end of this phase, there should be a **clean backend skeleton ready for development**.

---

## Milestone 2 — Auth / Users / Teams

### Goal
Build the identity and organizational foundation of the product.

### What should be completed

#### Auth
- registration
- login
- JWT access / refresh
- logout
- password hashing
- auth dependencies

#### Users
- user profile
- profile update
- self account endpoint

#### Teams
- create team
- team detail
- invite members
- join flow
- member list

#### Roles
- predefined team roles
- role assignment
- role display in team context

### Milestone outcome
By the end of this phase, a user should be able to:

- sign up,
- log in,
- create a team,
- invite people,
- organize the team by roles.

---

## Milestone 3 — Tasks / Chat

### Goal
Build the main operational workflow of the product.

### What should be completed

#### Tasks
- create task
- edit task
- assign task
- task status lifecycle
- task listing
- basic filtering

#### Chat
- team channels
- send message
- read message history
- basic WebSocket support
- real-time delivery

#### Team Workflow Integration
- integration of team → members → tasks → chat
- unified access model

### Milestone outcome
By the end of this phase, a team should already be able to **use the product for real coordination work**.

---

## Milestone 4 — AI Layer

### Goal
Add the first genuinely useful AI workflow embedded into the product.

### What should be completed

#### AI Infrastructure
- AI module scaffold
- provider abstraction
- prompt management
- async job pipeline

#### AI Features
- summarize chat messages
- extract key discussion points
- generate discussion digest
- basic summary persistence

#### Reliability / Cost Control
- retries
- request logging
- token / usage tracking
- fallback handling

### Milestone outcome
By the end of this phase, the product should include a **real AI feature that improves the core workflow**.

---

## Milestone 5 — Hardening

### Goal
Make the system more stable, cleaner, and more ready for demo / growth.

### What should be completed

#### Backend Hardening
- permission cleanup
- validation hardening
- error contract cleanup
- API consistency pass
- code refactoring

#### Performance / Infra
- Redis usage refinement
- background jobs stabilization
- DB query optimization
- observability basics

#### Testing
- unit tests for services
- integration tests for critical flows
- auth / team / task / chat smoke coverage

#### Documentation
- API docs refinement
- architecture updates
- deployment notes
- onboarding notes

### Milestone outcome
By the end of this phase, the project should feel like a **coherent, engineering-grade MVP system**, not just a collection of features.

---

## Post-MVP Direction

After MVP completion and hardening, the following directions become realistic.

### Candidate Post-MVP Features
- voice / video calls
- board / collaborative canvas
- architecture graph editor
- GitHub integration
- advanced notifications
- analytics / activity insights
- mobile-first clients

---

## Delivery Philosophy

Development should follow this rule:

> Every milestone must end in a **working, logically complete state of the system**.

That matters more than “building as many features as possible”.

---

## Summary

Recommended development order for NexusFlow:

1. **Foundation**
2. **Auth / Users / Teams**
3. **Tasks / Chat**
4. **AI**
5. **Hardening**

This provides a realistic path to a strong MVP without architectural collapse or uncontrolled scope expansion.