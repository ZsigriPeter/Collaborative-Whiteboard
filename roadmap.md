PHASE 1 — Project Setup (1–2 days)

Goal: Get the basic microservice structure running.

Tasks

Create repo with 3 backend services:

auth-service (Django REST Framework)

board-service (Django REST Framework)

realtime-service (Django Channels + Redis)

Dockerize each service

Docker Compose for:

PostgreSQL

Redis

All backend containers

React dev server

Deliverables

✔ multi-container project bootstrapped
✔ local dev environment fully running

Difficulty: ⭐⭐☆☆☆ (Easy–Medium)

PHASE 2 — Backend Fundamentals (3–5 days)

Goal: CRUD + microservice communication ready.

auth-service

User model + tokens (Simple JWT or Django tokens)

Endpoints: register, login, me

board-service

Models:

Workspace

Board

Column

Card

Endpoints:

Create/update boards

CRUD cards

Reorder columns/cards (via PATCH)

Internal Service Communication

board-service checks auth by calling auth-service (or reading JWT)

Deliverables

✔ fully working REST backend for Kanban board
✔ microservices can talk to each other
✔ stable DB schema

Difficulty: ⭐⭐⭐☆☆ (Medium)

PHASE 3 — Frontend Base (3–4 days)

Goal: Visual board with React + TS.

Tasks

Vite + React + TypeScript setup

Use dnd-kit or react-beautiful-dnd for drag & drop

Layout:

Sidebar

Board view

Columns + cards

Integrate backend:

Login

Load workspace

Display boards

Deliverables

✔ visually appealing UI
✔ basic drag & drop working
✔ fetch boards/cards from backend

Difficulty: ⭐⭐⭐☆☆ (Medium)

PHASE 4 — Real-Time Communication (4–7 days)

Goal: WebSockets + live updates

realtime-service

Implement Django Channels

Create channels:

board_{id} group for all users on the same board

Events:

card moved

card created/deleted

column added/moved

user joined/left (presence)

Frontend

Create WebSocket client

Subscribe to board channel

When event received → update UI state

Features

When user A moves a card → user B sees instantly

When user A edits card title → live update

User online indicators (avatars in corner)

“X is editing this board” status

Deliverables

✔ Real-time syncing
✔ Presence system
✔ Live card updates

Difficulty: ⭐⭐⭐⭐☆ (Hard)

PHASE 5 — Collaboration Features (3–5 days)

Goal: Make the app feel collaborative and alive.

Add:

Activity log (board timeline)

Highlight card borders when another user is editing

Locking mechanism → temporarily lock card editing to avoid conflicts

Show cursor/selection of other users (optional but impressive)

Keyboard shortcuts (create card, edit, move)

Deliverables

✔ real-time collaboration polish
✔ impressive visual effects
✔ UI clearly supports multi-user editing

Difficulty: ⭐⭐⭐⭐☆ (Hard but fun)

PHASE 6 — Polished UI + UX (4–7 days)

Goal: Make it demo-ready.

Tasks

Add color themes

Animations for drag/drop

Smooth transitions on updates

Responsive design

Small toast notifications (“Card moved by Alex”)

Add light/dark mode

Deliverables

✔ visually appealing board UI
✔ smooth UX
✔ professional-quality interface

Difficulty: ⭐⭐☆☆☆ (Easy)

PHASE 7 — QA, Tests, and Deployment (3–7 days)

Goal: Make it production-like.

Testing

Unit tests for both Django services

Integration tests:

move card

real-time events

permissions

Deployment

Docker images

Deploy to:

Railway

Fly.io

or DigitalOcean

Monitoring

Logging service

Basic metrics (Redis connections, active sessions)

Deliverables

✔ deployed app
✔ tested backend
✔ clean logs and error handling

Difficulty: ⭐⭐☆☆☆ (Medium)