# Architecture

## Цель архитектуры

Архитектура NexusFlow должна обеспечить:

- модульность,
- расширяемость,
- понятную domain-структуру,
- готовность к real-time сценариям,
- удобную интеграцию AI-компонентов,
- хорошую основу для дальнейшего масштабирования.

На этапе MVP архитектура должна быть **достаточно сильной**, но не переусложнённой.

Ключевой принцип:

> Сначала — **modular monolith with clean boundaries**, затем при необходимости — выделение отдельных сервисов.

Это даст лучший баланс между инженерной дисциплиной и скоростью разработки.

---

## High-Level Architecture

NexusFlow на старте рекомендуется строить как:

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
- LLM integration via dedicated AI service/module
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

### Для первой версии: монолит, в последствие разбиение на микросервисы



Путь:

- единый backend application,
- чёткое разделение по доменным модулям,
- отдельные boundaries,
- отдельные repositories / services / schemas / routers.

Это позволит:

- быстрее разрабатывать,
- не утонуть в DevOps complexity слишком рано,
- сохранить чистую архитектуру,
- позже без боли выделять отдельные сервисы.

---

## Core Modules

Система может быть организована в следующие backend-модули:

### 1. Auth Module
Отвечает за:

- регистрацию,
- login,
- token lifecycle,
- identity validation,
- security basics.

---

### 2. Users Module
Отвечает за:

- профили пользователей,
- базовые account данные,
- отображение участника в системе.

---

### 3. Teams Module
Отвечает за:

- команды,
- membership,
- приглашения,
- team settings,
- принадлежность пользователя к командам.

---

### 4. Roles Module
Отвечает за:

- роли участников,
- team-level role assignment,
- базовую модель полномочий.

---

### 5. Tasks Module
Отвечает за:

- задачи,
- статусы,
- назначение исполнителей,
- task ownership,
- task lifecycle.

---

### 6. Chat Module
Отвечает за:

- каналы / чаты,
- сообщения,
- историю сообщений,
- real-time коммуникацию.

---

### 7. AI Module
Отвечает за:

- summarization,
- extraction of key points,
- AI job orchestration,
- работу с LLM providers.

---

## Базовые сущности

Ниже — базовые сущности системы.

---

### User
Представляет пользователя платформы.

Примерные поля:

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
Представляет команду.

Примерные поля:

- id
- name
- slug
- description
- owner_id
- created_at
- updated_at

---

### TeamMember
Связь между пользователем и командой.

Примерные поля:

- id
- team_id
- user_id
- role_id
- joined_at
- status

---

### Role
Роль участника внутри команды.

Примерные поля:

- id
- name
- code
- description

Примеры:

- owner
- manager
- backend
- frontend
- devops
- tester
- ai

---

### Task
Представляет задачу.

Примерные поля:

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
Канал общения внутри команды.

Примерные поля:

- id
- team_id
- name
- type
- created_at

---

### Message
Сообщение внутри чата.

Примерные поля:

- id
- channel_id
- author_id
- content
- created_at
- edited_at

---

### AISummary
Результат AI-обработки переписки.

Примерные поля:

- id
- channel_id
- source_range
- summary_text
- created_by_system
- created_at

---

## Entity Relationships

Основные связи между сущностями:

- Один **User** может состоять во многих **Teams**
- Одна **Team** содержит много **TeamMembers**
- Один **TeamMember** связан с одной **Role**
- Одна **Team** содержит много **Tasks**
- Одна **Task** может быть назначена одному **User**
- Одна **Team** содержит много **ChatChannels**
- Один **ChatChannel** содержит много **Messages**
- Один **ChatChannel** может иметь много **AISummaries**

---

## Suggested Project Structure

Пример backend-структуры:

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