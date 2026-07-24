# Database Design

## Purpose

The database is designed to organize creator business information efficiently while supporting future AI-powered features.

---

# Core Entities

## User

Represents a creator using Atlas.

Fields:

- id
- full_name
- email
- password_hash
- niche
- bio
- created_at

---

## Brand

Represents companies a creator works with.

Fields:

- id
- name
- industry
- contact_person
- email
- phone
- website

---

## Campaign

Represents a collaboration.

Fields:

- id
- brand_id
- title
- description
- start_date
- deadline
- status

---

## Deliverable

Represents work within a campaign.

Fields:

- id
- campaign_id
- type
- due_date
- status

---

## Payment

Tracks payments.

Fields:

- id
- campaign_id
- amount
- currency
- payment_status
- invoice_number
- payment_date

---

## File

Stores uploaded documents.

Fields:

- id
- campaign_id
- file_name
- file_path
- uploaded_at

---

# Relationships

User

↓

Campaign

↓

Brand

↓

Deliverables

↓

Payments

↓

Files

---

# Design Goals

- Avoid duplicate information
- Support fast searching
- Maintain referential integrity
- Allow future AI indexing

---

# Future Tables

- Meeting Notes
- Creator Analytics
- AI Memories
- Notifications
- Activity Logs