# Architecture

## Architecture Goal

The architecture of NexusFlow should provide:

- modularity,
- extensibility,
- a clear domain structure,
- readiness for real-time workflows,
- convenient AI integration,
- a strong foundation for future scaling.

At the MVP stage, the architecture should be **strong enough**, but not overengineered.

Core principle:

> Start with a **modular monolith with clean boundaries**, then extract services only when justified.

This provides the best balance between engineering discipline and development speed.

---

## High-Level Architecture

At the start, NexusFlow should be built as:

- **Backend API**
- **Real-time communication layer**
- **AI processing layer**
- **Database + cache + async jobs**
- **Web / client frontend**

---

## Recommended Tech Stack

### Backend
- **Python**
- **FastAPI**
- **SQLAlchemy 2.x**
- **Alembic**
- **Pydantic v2**

### Database
- **PostgreSQL**

### Cache / fast state / pub-sub
- **Redis**

### Async background jobs
- **Celery** or **Dramatiq**
- Redis / RabbitMQ as broker

### Real-time
- **WebSockets** via FastAPI
- Redis pub/sub for scaling chat events

### AI Layer
- LLM integration via a dedicated AI service/module
- Prompt orchestration layer
- Async summarization jobs

### Infra / DevOps
- **Docker**
- **Docker Compose**
- Later:
  - **Nginx**
  - **Prometheus**
  - **Grafana**
  - **CI/CD pipeline**

---

## Architectural Style

### Recommended approach: Modular Monolith

At MVP and early stages, **microservices are unnecessary**.

The right path is:

- a single backend application,
- strict separation by domain modules,
- clean boundaries,
- separate repositories / services / schemas / routers.

This allows you to:

- build faster,
- avoid premature DevOps complexity,
- preserve clean architecture,
- extract services later without pain.

---

## Core Modules

The system can be organized into the following backend modules:

### 1. Auth Module
Responsible for:

- registration,
- login,
- token lifecycle,
- identity validation,
- security basics.

---

### 2. Users Module
Responsible for:

- user profiles,
- basic account data,
- representing a user in the system.

---

### 3. Teams Module
Responsible for:

- teams,
- membership,
- invitations,
- team settings,
- user-team associations.

---

### 4. Roles Module
Responsible for:

- member roles,
- team-level role assignment,
- the basic authorization model.

---

### 5. Tasks Module
Responsible for:

- tasks,
- statuses,
- assignee assignment,
- task ownership,
- task lifecycle.

---

### 6. Chat Module
Responsible for:

- channels / chats,
- messages,
- message history,
- real-time communication.

---

### 7. AI Module
Responsible for:

- summarization,
- key point extraction,
- AI job orchestration,
- interaction with LLM providers.

---

## Core Domain Entities

Below are the baseline domain entities of the system.

---

### User
Represents a platform user.

Example fields:

- id
- email
- username
- full_name
- password_hash
- avatar_url
- is_active
- created_at
- updated_at

---

### Team
Represents a team.

Example fields:

- id
- name
- slug
- description
- owner_id
- created_at
- updated_at

---

### TeamMember
Association between a user and a team.

Example fields:

- id
- team_id
- user_id
- role_id
- joined_at
- status

---

### Role
Represents a member role inside a team.

Example fields:

- id
- name
- code
- description

Examples:

- owner
- manager
- backend
- frontend
- devops
- tester
- ai

---

### Task
Represents a task.

Example fields:

- id
- team_id
- title
- description
- status
- priority
- assignee_id
- creator_id
- due_date
- created_at
- updated_at

---

### ChatChannel
A communication channel inside a team.

Example fields:

- id
- team_id
- name
- type
- created_at

---

### Message
A chat message.

Example fields:

- id
- channel_id
- author_id
- content
- created_at
- edited_at

---

### AISummary
The result of AI processing over conversation data.

Example fields:

- id
- channel_id
- source_range
- summary_text
- created_by_system
- created_at

---

## Entity Relationships

Key relationships between entities:

- One **User** can belong to many **Teams**
- One **Team** contains many **TeamMembers**
- One **TeamMember** is associated with one **Role**
- One **Team** contains many **Tasks**
- One **Task** can be assigned to one **User**
- One **Team** contains many **ChatChannels**
- One **ChatChannel** contains many **Messages**
- One **ChatChannel** can have many **AISummaries**

---

## Suggested Project Structure

Example backend structure:

```txt
app/
  api/
    v1/
      routers/
  core/
    config.py
    security.py
    database.py
    logging.py
  modules/
    auth/
      router.py
      service.py
      repository.py
      schemas.py
      models.py
      dependencies.py
    users/
    teams/
    roles/
    tasks/
    chat/
    ai/
  shared/
    exceptions/
    utils/
    enums/
    mixins/
  workers/
    tasks.py
  main.py
```