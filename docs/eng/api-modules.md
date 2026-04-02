# API Modules

## Document Purpose

This document describes the **core API modules of NexusFlow** at the backend design level.

It is not intended to be the final OpenAPI specification.  
Its purpose is to define:

- module boundaries,
- domain responsibilities,
- approximate API structure.

---

# 1. Auth Module

## Purpose
The authentication module is responsible for user identity and access lifecycle management.

## Responsibilities
- registration
- login
- refresh tokens
- logout
- password change
- access validation

## Example endpoints

### `POST /auth/register`
Create a new account.

### `POST /auth/login`
Authenticate a user.

### `POST /auth/refresh`
Refresh access token.

### `POST /auth/logout`
Terminate a session.

### `POST /auth/change-password`
Change password.

## Core entities
- User
- RefreshToken / Session (if used)

---

# 2. Users Module

## Purpose
The users module is responsible for profile and basic user account data.

## Responsibilities
- retrieving profile data
- updating profile data
- viewing member information

## Example endpoints

### `GET /users/me`
Get the current user profile.

### `PATCH /users/me`
Update the current user profile.

### `GET /users/{user_id}`
View a publicly available user profile.

## Core entities
- User

---

# 3. Teams Module

## Purpose
The teams module is responsible for the organizational structure of the product.

## Responsibilities
- team creation
- team retrieval
- member management
- invitations
- basic team settings

## Example endpoints

### `POST /teams`
Create a team.

### `GET /teams`
Get the current user’s teams.

### `GET /teams/{team_id}`
Get team details.

### `PATCH /teams/{team_id}`
Update team settings.

### `POST /teams/{team_id}/invite`
Invite a member.

### `GET /teams/{team_id}/members`
Get team members.

## Core entities
- Team
- TeamMember
- Invitation (optionally as a separate entity)

---

# 4. Tasks Module

## Purpose
The tasks module is responsible for operational execution inside a team.

## Responsibilities
- task creation
- task updates
- assignee assignment
- status changes
- task list retrieval

## Example endpoints

### `POST /teams/{team_id}/tasks`
Create a task.

### `GET /teams/{team_id}/tasks`
Get team tasks.

### `GET /tasks/{task_id}`
Get task details.

### `PATCH /tasks/{task_id}`
Update a task.

### `PATCH /tasks/{task_id}/status`
Change task status.

### `PATCH /tasks/{task_id}/assign`
Assign a task to a user.

## Core entities
- Task

---

# 5. Chat Module

## Purpose
The chat module is responsible for communication inside a team.

## Responsibilities
- channel creation / retrieval
- sending messages
- message history
- real-time interaction

## Example endpoints

### `GET /teams/{team_id}/channels`
Get team channels.

### `POST /teams/{team_id}/channels`
Create a channel.

### `GET /channels/{channel_id}/messages`
Get message history.

### `POST /channels/{channel_id}/messages`
Send a message.

## WebSocket endpoints

### `WS /ws/channels/{channel_id}`
Real-time message channel.

## Core entities
- ChatChannel
- Message

---

# 6. AI Module

## Purpose
The AI module is responsible for AI capabilities embedded into the team workflow.

## Responsibilities
- summarization
- key point extraction
- AI jobs
- persistence of AI-generated outputs

## Example endpoints

### `POST /ai/channels/{channel_id}/summaries`
Trigger summarization for a chat / channel.

### `GET /ai/channels/{channel_id}/summaries`
Get AI summaries for a channel.

### `GET /ai/summaries/{summary_id}`
Get a specific AI summary.

## Core entities
- AISummary
- AIJob (optionally as a separate entity)

---

# Access Model

## Team-Scoped Access
Most major NexusFlow modules should operate under a **team-scoped access model**.

This means:

- a user only sees teams they belong to,
- a user only sees tasks, chats, and summaries associated with their team,
- access must be validated through membership.

This is one of the core architectural principles of the product.

---

# API Design Principles

## 1. Resource-oriented API
The API should be built around domain resources, not arbitrary actions.

## 2. Clear ownership
Each resource should have a clear ownership scope:

- user-scoped
- team-scoped
- channel-scoped
- task-scoped

## 3. Predictable naming
Endpoint names should be predictable and consistent.

## 4. Thin routers, strong service layer
Business logic should not live in route handlers.  
The service layer should own the core logic.

## 5. Async-friendly architecture
AI and real-time workflows should be designed with asynchronous execution in mind.

---

# Future Expansion

In the future, the API can be extended with additional modules such as:

- notifications
- calls
- boards
- architecture editor
- github integration
- analytics

However, these modules must not compromise the cleanliness of the MVP core API.

---

# Summary

The baseline API modules of NexusFlow are:

- **auth**
- **users**
- **teams**
- **tasks**
- **chat**
- **ai**

These modules form the minimum but already strong backend foundation of the product.