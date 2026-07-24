# System Architecture

## Purpose

This document describes the overall architecture of Atlas. It explains how different components of the system interact, the technologies used, and the design principles followed to ensure scalability, maintainability, and future AI integration.

---

# High-Level Architecture

Atlas follows a modern client-server architecture.

```
+-----------------------+
|      Web Browser      |
+----------+------------+
           |
           |
           ▼
+-----------------------+
|   Next.js Frontend    |
+----------+------------+
           |
     REST API (HTTPS)
           |
           ▼
+-----------------------+
|    FastAPI Backend    |
+-----+---------+-------+
      |         |
      |         |
      ▼         ▼
 PostgreSQL   File Storage
(Database)   (Contracts, PDFs)

           |
           ▼
      AI Services (Future)
```

---

# Technology Stack

| Layer | Technology |
|--------|------------|
| Frontend | Next.js (React + TypeScript) |
| Styling | Tailwind CSS |
| Backend | FastAPI |
| Database | PostgreSQL |
| ORM | SQLAlchemy |
| Authentication | JWT |
| File Storage | Local (Development) |
| Version Control | Git + GitHub |
| AI | OpenAI Compatible APIs (Future) |

---

# Architecture Principles

Atlas follows these design principles:

- Modular architecture
- RESTful APIs
- Separation of concerns
- Scalable database design
- Independent feature modules
- Future-ready AI integration

---

# Core Modules

## Authentication

- User registration
- Login
- JWT authentication

---

## Creator Profile

Stores creator information such as:

- Name
- Social links
- Niche
- Contact information

---

## Brand Management

Stores:

- Brand information
- Contacts
- Collaboration history

---

## Campaign Management

Tracks:

- Deliverables
- Deadlines
- Status
- Campaign details

---

## Payment Management

Tracks:

- Amount
- Payment status
- Invoice status
- Payment date

---

## File Management

Stores:

- Contracts
- Invoices
- Campaign assets

---

## Dashboard

Provides:

- Active campaigns
- Pending payments
- Upcoming deadlines
- Recent activity

---

# API Structure

/api/v1/auth

/api/v1/users

/api/v1/brands

/api/v1/campaigns

/api/v1/payments

/api/v1/files

---

# Security

Atlas will implement:

- Password hashing
- JWT authentication
- Role-based authorization (future)
- Input validation
- Secure API communication

---

# Future Integrations

Future versions may integrate:

- Gmail
- Google Calendar
- Google Drive
- Instagram
- YouTube
- Stripe
- Notion

---

# Conclusion

The architecture is designed to support the MVP while remaining flexible enough to accommodate AI-powered features, automation, and third-party integrations as Atlas evolves.