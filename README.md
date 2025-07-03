# Library Management System Documentation (Odoo 17)

## Overview
This Odoo 17 module provides a comprehensive library management system with features for book tracking, loan management, and member administration. The system allows librarians to manage book inventory, track loans, and monitor overdue items.

## Module Structure
```
library_management_system/
├── data/
│   ├── ir_cron.xml          # Scheduled actions
│   ├── ir_report.xml        # Report definitions
│   ├── security/
│   │   ├── groups.xml       # User groups
│   │   └── ir.model.access.csv # Access rights
├── models/
│   ├── __init__.py          # Python imports
│   ├── library_book.py      # Book model
│   ├── library_loan.py      # Loan model
│   └── res_partner.py       # Partner extensions
├── reports/
│   ├── loan_report.xml      # Report template
├── security/
│   └── ir.model.access.csv  # Model access rights
├── views/
│   ├── book_views.xml       # Book UI
│   ├── loan_views.xml       # Loan UI
│   ├── menu_views.xml       # Menu structure
│   └── partner_views.xml    # Partner extensions
├── __init__.py
└── __manifest__.py
```

## Main Features

### 1. Book Management
- Track book titles, authors, ISBNs, and publication years
- Book status (Available/Borrowed)
- ISBN validation (must be 13 digits)

### 2. Loan Management
- Track book loans to partners
- Loan statuses (Draft, Borrowed, Returned, Overdue)
- Automatic overdue detection (14 days past return date)
- Manual borrow/return actions

### 3. Partner Extensions
- Library member flag
- Loan history tracking
- Loan count computation

### 4. Automated Processes
- Scheduled daily check for overdue loans
- Automatic status updates for books when loans change

### 5. Reporting
- PDF report for loans showing book and borrower information

## Technical Implementation

### Models
1. **Library Book (`library.book`)**
   - Core book information and status tracking
   - ISBN validation constraint

2. **Library Loan (`library.loan`)**
   - Loan lifecycle management
   - Automated overdue detection
   - Business methods for borrow/return actions

3. **Res Partner Extension**
   - Adds library-specific fields to partners
   - Computes active loan count

### Scheduled Actions
- Daily check for loans that are 14+ days overdue
- Automatically updates status to "overdue"

### Security
- Custom groups: Library Manager and Library Employee
- Model-level access controls for books and loans

### User Interface
- Tree and form views for books and loans
- Custom buttons for borrow/return actions
- Menu structure under Library root
- Partner form extension for library features

## Usage Instructions

1. **Book Management**:
   - Add books through the Books menu
   - Set title, author, ISBN, and publication year
   - Status automatically updates based on loans

2. **Loan Management**:
   - Create loans through the Loans menu
   - Select book and partner
   - Use Borrow button to confirm loan
   - Use Return button when book is returned

3. **Member Management**:
   - Mark partners as library members
   - View loan history on partner form

4. **Reports**:
   - Generate loan reports showing book and borrower information

## Future Enhancements
1. Add barcode scanning for books and members
2. Implement reservation system for books
3. Add fine calculation for overdue loans
4. Enhance reports with more detailed information
5. Add dashboard for library statistics

