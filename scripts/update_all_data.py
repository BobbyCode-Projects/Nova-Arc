#!/usr/bin/env python3
"""
Expands all capabilities across NovaArc website data files to exactly 10 points each,
and updates challenges to the high-quality 4-point Problem & Resolution structure
matching the user's specific guidance and 8th visual reference layout.
"""

import os
import sys
import pprint

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

import data_services as ds1
import data_services_domain2 as ds2
import data_services_domain3 as ds3
import data_services_domain4 as ds4
import data_tech_ind_connect as dtic

# ==============================================================================
# Domain 1 Additional Points (6 per capability to make 10 total)
# ==============================================================================
DS1_EXTRA_POINTS = {
    # services/digital-commerce-platforms.html
    ("services/digital-commerce-platforms.html", "Enterprise B2B Portals"): [
        "Multi-tier procurement approval chains and custom budget limits",
        "Contracted price-list matrix with customer-specific volume discounts",
        "Split-shipment multi-destination order routing",
        "Purchase order (PO) upload and OCR ingestion",
        "ERP ledger synchronization for automated invoicing and credit terms",
        "Role-based buyer permissions and departmental spend tracking"
    ],
    ("services/digital-commerce-platforms.html", "Omnichannel B2C Storefronts"): [
        "Headless Progressive Web App (PWA) with sub-second page rendering",
        "Localized currency conversion with automated tax calculation",
        "Unified digital wallet support (Apple Pay, Google Pay, UPI)",
        "Automated cart recovery and push notification sequences",
        "Real-time store pickup and local fulfillment availability",
        "Integrated customer review moderation and UGC widgets"
    ],
    ("services/digital-commerce-platforms.html", "Dynamic Catalog Management"): [
        "Multi-channel product syndication across marketplaces",
        "Automated asset tagging and image optimization pipelines",
        "Configurable SKU bundling and dynamic kitting logic",
        "Custom taxonomy hierarchies with faceted attribute filters",
        "Scheduled promotional pricing and campaign scheduling",
        "Cross-channel inventory synchronization with safety stock buffers"
    ],
    ("services/digital-commerce-platforms.html", "Payment & Tax Gateway Integration"): [
        "Automated fraud scoring and risk evaluation rules",
        "Multi-gateway routing with automatic failover fallback",
        "Chargeback and dispute management automation",
        "Automated sales tax nexus calculation across international jurisdictions",
        "Direct debit, ACH, and corporate credit line checkout",
        "Audit-compliant transaction ledger reconciliation"
    ],

    # services/foodtech.html
    ("services/foodtech.html", "Digital Food Ordering & Distribution"): [
        "Kitchen Display System (KDS) integration with preparation timers",
        "Dynamic menu scheduling based on real-time ingredient stock",
        "Multi-outlet delivery radius mapping and surge pricing controls",
        "Contactless QR-code ordering and table bill splitting",
        "Automated delivery aggregator dispatch and driver tracking",
        "Customer loyalty and repeat order subscription models"
    ],
    ("services/foodtech.html", "Batch & Expiry Date Management"): [
        "Automated First-Expired, First-Out (FEFO) warehouse pick routing",
        "Lot traceability from farm gate to consumer packaging",
        "Automated quarantine flags for temperature-compromised batches",
        "Digital health inspection and food safety audit logs",
        "Barcode and RFID scanning for batch movement verification",
        "Supplier shelf-life compliance scoring and penalty tracking"
    ],
    ("services/foodtech.html", "Food Procurement & Supplier Coordination"): [
        "Automated supplier purchase orders based on recipe consumption forecasts",
        "Contract compliance monitoring for perishables and staples",
        "Supplier quality grading and rejection workflow logging",
        "Central commissary requisition consolidation across restaurant units",
        "Real-time wholesale market price feed integrations",
        "Vendor delivery window appointment scheduling"
    ],
    ("services/foodtech.html", "Cold Chain & Temperature Telemetry"): [
        "Sub-zero and ambient wireless sensor network telemetry",
        "Real-time excursion alerts across refrigerated freight trucks",
        "Automated HACCP temperature compliance digital log generation",
        "Compressor power consumption and predictive maintenance alerts",
        "Door-open duration tracking on commercial walk-in freezers",
        "Audit-ready thermal historical reports for regulatory authorities"
    ],

    # services/supply-chain-management.html
    ("services/supply-chain-management.html", "Multi-Node Inventory Tracking"): [
        "Distributed inventory visibility across warehouses, 3PLs, and stores",
        "Cycle count scheduling and automated variance reconciliation",
        "Serialization and RFID asset tracking across transit nodes",
        "Safety stock calculations adjusted for seasonal variability",
        "Cross-docking coordination and dock door scheduling",
        "Phantom inventory detection via sales-to-stock delta analytics"
    ],
    ("services/supply-chain-management.html", "Order Lifecycle Orchestration"): [
        "Distributed Order Management (DOM) with least-cost routing",
        "Automated order split rules based on geographic proximity",
        "Backorder queue prioritization and automated release upon restock",
        "Returns authorization (RMA) triage and restock inspection workflows",
        "SLA monitoring with proactive delay escalations to customer support",
        "Carrier label generation and customs manifest auto-creation"
    ],
    ("services/supply-chain-management.html", "Demand Forecasting & Planning"): [
        "Predictive machine learning models trained on historical sales patterns",
        "Promotional lift and price elasticity modeling",
        "Supplier lead-time volatility buffer calculations",
        "Collaborative planning, forecasting, and replenishment (CPFR)",
        "Bill of materials (BOM) explosion for manufacturing component demand",
        "Scenario-based simulation for supply chain disruption resilience"
    ],
    ("services/supply-chain-management.html", "Replenishment Automation"): [
        "Dynamic reorder point recalculation based on demand velocity",
        "Automated purchase requisition generation upon threshold breach",
        "Container load optimization and pallet configuration calculations",
        "Inter-facility inventory balancing and transfer order dispatch",
        "Vendor minimum order quantity (MOQ) optimization engines",
        "Emergency stock replenishment protocols for critical high-velocity SKUs"
    ],

    # services/procurement.html
    ("services/procurement.html", "Digital Purchase Requisitions"): [
        "Pre-approved catalog ordering with standardized item descriptions",
        "Automated general ledger (GL) coding and department cost center assignment",
        "Budget validation against live enterprise accounting systems",
        "Mobile requisition approvals for department supervisors",
        "Blanket purchase order draw-down and remaining balance tracking",
        "Emergency off-catalog requisition forms with escalated sign-off"
    ],
    ("services/procurement.html", "Configurable Approval Hierarchies"): [
        "Multi-tiered financial threshold approval matrices",
        "Delegation of authority rules during manager out-of-office periods",
        "Parallel approvals across finance, legal, and operational leadership",
        "Automated escalation triggers for overdue pending authorizations",
        "Complete immutable audit logging of every approval decision",
        "Custom workflow branching based on vendor risk profile and item category"
    ],
    ("services/procurement.html", "Vendor Portals & Onboarding"): [
        "Self-service supplier profile, banking, and tax ID registration",
        "Automated insurance certificate and license expiration tracking",
        "Supplier performance scorecards evaluating on-time delivery and quality",
        "Digital request for quote (RFQ) distribution and bid comparison matrices",
        "Secure document repository for signed master service agreements (MSAs)",
        "Direct supplier messaging and purchase order acknowledgment tracking"
    ],
    ("services/procurement.html", "Automated 3-Way Invoice Matching"): [
        "OCR extraction of line-item details from electronic invoices",
        "Automated matching against purchase orders and warehouse receipts",
        "Configurable price and quantity tolerance thresholds",
        "Exception routing to buyers for mismatched line-item resolution",
        "Early payment discount optimization and payment scheduling",
        "Automated posting to accounts payable ledger in enterprise ERP"
    ],

    # services/logistics.html
    ("services/logistics.html", "Transportation Management (TMS)"): [
        "Multi-modal freight rate calculation and contract tariff comparison",
        "Automated freight bill auditing against agreed carrier contracts",
        "Consolidated shipment planning for full truckload (FTL) and LTL",
        "Hazardous material compliance validation and documentation",
        "Carrier allocation enforcement based on contracted volume commitments",
        "Carbon footprint calculation and green route reporting"
    ],
    ("services/logistics.html", "Real-Time Shipment Visibility"): [
        "Telematics and GPS integration across fleet tracking devices",
        "Dynamic predictive ETA calculation considering traffic and weather",
        "Geofence entry and exit timestamp logging at distribution hubs",
        "Automated exception notifications for transit delays and detours",
        "Customer-facing branded tracking portals with milestone progress",
        "Sensor telemetry for shock, tilt, and temperature sensitive freight"
    ],
    ("services/logistics.html", "Dispatch & Route Optimization"): [
        "Multi-stop vehicle routing algorithms minimizing mileage and drive time",
        "Driver hours-of-service (HOS) and rest-break compliance routing",
        "Vehicle weight and volumetric capacity optimization",
        "Dynamic re-routing around traffic incidents and road closures",
        "Mobile driver application for manifest viewing and turn-by-turn navigation",
        "Automated dispatch assignment based on driver proximity and availability"
    ],
    ("services/logistics.html", "Digital Proof of Delivery (ePOD)"): [
        "Contactless signature capture on mobile driver devices",
        "High-resolution photographic capture of delivered freight and condition",
        "Geotagged and timestamped delivery location confirmation",
        "Immediate customer delivery receipt transmission via SMS and email",
        "Driver exception logging for partial deliveries, refusals, or damages",
        "Instant delivery status sync to ERP to trigger billing and revenue recognition"
    ],
}

# ==============================================================================
# Domain 2 Additional Points (6 per capability to make 10 total)
# ==============================================================================
DS2_EXTRA_POINTS = {
    # services/crm.html
    ("services/crm.html", "Lead Management & Scoring"): [
        "Predictive lead scoring algorithms based on historical win profiles",
        "Automated deduplication and contact data enrichment",
        "Territory-based lead routing and sales rep assignment rules",
        "Behavioral website interaction tracking and intent signals",
        "Inbound lead capture forms with instant CRM sync and notification",
        "Lead aging reports and automated recycling of stale prospects"
    ],
    ("services/crm.html", "Sales Pipeline & Deal Tracking"): [
        "Custom stage gating requiring mandatory deal qualification milestones",
        "Weighted revenue forecasting across monthly and quarterly targets",
        "Automated contract generation and CPQ (configure, price, quote) integration",
        "Deal stagnation alerts when opportunities exceed expected stage duration",
        "Competitor battlecard integration directly within opportunity views",
        "Win/loss post-mortem tracking and conversion velocity analytics"
    ],
    ("services/crm.html", "Customer Onboarding Workflows"): [
        "Structured post-sale handoff checklists between sales and client success",
        "Automated customer kickoff email sequences and calendar scheduling",
        "Implementation milestone tracking with progress percentage bars",
        "Customer portal for document submission and onboarding sign-offs",
        "Health score calculation based on product adoption and milestone completion",
        "Escalation workflows when onboarding projects fall behind scheduled SLAs"
    ],
    ("services/crm.html", "Support Desk & Ticketing"): [
        "Multi-channel ticket aggregation from email, chat, web, and phone",
        "SLA priority matrix with automated escalation timers",
        "Internal knowledge base search for rapid support agent resolution",
        "Customer satisfaction (CSAT) survey distribution upon ticket closure",
        "Canned responses and macro shortcuts for common technical inquiries",
        "Product defect escalation pipeline directly to engineering Jira boards"
    ],

    # services/hrms.html
    ("services/hrms.html", "Recruitment & Digital Onboarding"): [
        "Applicant Tracking System (ATS) with pipeline stage management",
        "Automated interview scheduling and calendar invitation sync",
        "Standardized candidate evaluation scorecards for hiring panels",
        "Electronic offer letter generation with e-signature tracking",
        "Background check and document verification workflow integration",
        "Automated IT asset and software license provisioning requests"
    ],
    ("services/hrms.html", "Employee Self-Service (ESS) Portal"): [
        "Personal profile updates and emergency contact management",
        "Digital pay slip and annual tax document retrieval",
        "Company policy handbook repository with acknowledgment sign-offs",
        "Internal job board and employee referral submission forms",
        "Reimbursement claim filing with digital receipt attachment",
        "Team directory and organizational chart visualization"
    ],
    ("services/hrms.html", "Attendance & Leave Management"): [
        "Biometric and mobile geofenced clock-in/out integration",
        "Automated shift scheduling and overtime calculation rules",
        "Configurable leave balance accrual policies and holiday calendars",
        "Manager approval dashboard for time-off and shift swaps",
        "Absence trend analysis identifying chronic absenteeism patterns",
        "Automated payroll deduction sync based on unpaid time off"
    ],
    ("services/hrms.html", "Performance Reviews & Analytics"): [
        "360-degree feedback cycles involving managers, peers, and reports",
        "Goal setting and OKR alignment tracking with milestone weights",
        "Continuous feedback logging between formal appraisal cycles",
        "Nine-box talent grid plotting performance versus leadership potential",
        "Compensation review modeling linked to appraisal outcomes",
        "Skill matrix gap analysis and recommended training pathways"
    ],

    # services/business-process-automation.html
    ("services/business-process-automation.html", "Dynamic Approval Orchestration"): [
        "Multi-condition workflow branching based on monetary value and department",
        "Parallel and sequential approval paths with fallback signatories",
        "Mobile approval buttons embedded directly in email notifications",
        "Time-based auto-escalation when approvals remain pending past SLA",
        "Delegation rules during employee leaves and business travel",
        "Comprehensive historical audit log documenting every approval decision"
    ],
    ("services/business-process-automation.html", "Automated Task Routing & Assignment"): [
        "Skills-based task assignment matching tickets to qualified operators",
        "Workload balancing distributing tasks across available team members",
        "Automated task reassignment upon shift conclusion or team absences",
        "Priority scoring determining task queue position in real time",
        "Automated deadline calculation and reminder push notifications",
        "Consolidated team task boards with Kanban and list views"
    ],
    ("services/business-process-automation.html", "Exception & Escalation Management"): [
        "Automated rule engines flagging anomalous data entries or transaction values",
        "Tiered escalation ladders triggering SMS, email, and Slack alerts",
        "Root cause categorization and incident recurrence reporting",
        "Temporary process bypass protocols with required management sign-off",
        "Automated containment workflows isolating disputed records",
        "Post-incident review task generation for operational process improvement"
    ],
    ("services/business-process-automation.html", "Cross-System Event Triggers"): [
        "Webhook listeners reacting to ERP, CRM, and database status changes",
        "Bidirectional data propagation between legacy systems and modern apps",
        "Automated file processing upon drop into cloud storage buckets",
        "Scheduled cron jobs executing batch data synchronization cycles",
        "Message queue buffering preventing system overloads during traffic spikes",
        "Dead-letter queue handling with automated retry logic on transient errors"
    ],

    # services/enterprise-applications.html
    ("services/enterprise-applications.html", "Custom Business Portals"): [
        "Role-based permission schemas enforcing strict data access boundaries",
        "Responsive interfaces optimized for desktop workstations and mobile tablets",
        "Single Sign-On (SSO) integration supporting SAML 2.0 and OAuth / OIDC",
        "Custom report generators with PDF, CSV, and Excel export options",
        "Granular activity audit logging capturing all user view and edit actions",
        "Multi-language user interface support for global enterprise divisions"
    ],
    ("services/enterprise-applications.html", "Operational Dashboards & BI"): [
        "Real-time visual KPI widgets updating via WebSocket data feeds",
        "Drill-down capability from executive metrics to individual transaction logs",
        "Scheduled executive summary emails with embedded dashboard snapshots",
        "Cross-departmental metric aggregation combining sales, finance, and ops",
        "Custom filtering by time range, geographic division, and business unit",
        "Interactive trend charts with forecast projection overlays"
    ],
    ("services/enterprise-applications.html", "Legacy System Modernization"): [
        "Monolith-to-microservices gradual migration using the Strangler pattern",
        "Legacy SQL database schema normalization and performance tuning",
        "Modern RESTful API wrapping around legacy mainframe/ERP systems",
        "Cloud-native rehosting with containerization via Docker and Kubernetes",
        "Automated data migration pipelines with zero business downtime",
        "Legacy UI redesign into modern high-speed web application interfaces"
    ],
    ("services/enterprise-applications.html", "Scalable Cloud Architecture"): [
        "Automated horizontal auto-scaling accommodating unexpected traffic surges",
        "Multi-region high availability with automated disaster recovery failover",
        "Infrastructure as Code (IaC) deployment via Terraform and GitHub Actions",
        "End-to-end data encryption in transit (TLS 1.3) and at rest (AES-256)",
        "Zero-trust network architecture with microsegmentation and VPC peering",
        "Cost optimization governance minimizing idle cloud resource spend"
    ],

    # services/enterprise-integration.html
    ("services/enterprise-integration.html", "Robust API Connectors (REST & GraphQL)"): [
        "Rate limiting and traffic throttling protecting internal backend services",
        "Standardized OpenAPI/Swagger schema definitions and developer docs",
        "API versioning support maintaining backward compatibility for legacy clients",
        "Automated token validation and OAuth 2.0 authentication handshakes",
        "Caching layer utilizing Redis to reduce redundant database queries",
        "Comprehensive API telemetry tracking error rates, latency, and throughput"
    ],
    ("services/enterprise-integration.html", "Bidirectional ERP/CRM Synchronization"): [
        "Event-driven webhook connectors syncing customer data upon change",
        "Conflict resolution rules determining system of record per field",
        "Transaction rollback mechanisms preventing partial or corrupted syncs",
        "Batch reconciliation routines resolving off-hours network drops",
        "Field mapping transformation engine handling disparate data schemas",
        "Real-time sync status monitoring dashboard with manual re-try controls"
    ],
    ("services/enterprise-integration.html", "Centralized Business Intelligence & ETL"): [
        "Automated ETL/ELT pipelines extracting data from disparate siloed databases",
        "Data warehouse modeling across Snowflake, BigQuery, and Redshift",
        "Data quality validation rules flagging malformed or missing records",
        "Change Data Capture (CDC) streaming real-time operational updates",
        "Historical data archiving pipelines optimizing operational DB speed",
        "Business glossary and data dictionary governance tools"
    ],
    ("services/enterprise-integration.html", "Role-Based Access & Governance"): [
        "Granular attribute-based access control (ABAC) and RBAC policies",
        "Centralized directory synchronization via Active Directory / Azure AD",
        "Automated user deprovisioning upon employee departure",
        "Compliance monitoring verifying adherence to SOC 2, HIPAA, and GDPR",
        "Privileged access management (PAM) for administrative accounts",
        "Periodic access certification workflows for departmental managers"
    ],
}

# ==============================================================================
# Domain 3 Additional Points (6 per capability to make 10 total)
# ==============================================================================
DS3_EXTRA_POINTS = {
    # services/real-time-monitoring.html
    ("services/real-time-monitoring.html", "Sub-Second Telemetry Visualization"): [
        "High-frequency time-series charting with smooth live visual updates",
        "Configurable dashboard layouts tailored to specific engineering roles",
        "Multi-screen command center display support with auto-refreshing tiles",
        "Visual color-coded alert thresholds highlighting critical operating bands",
        "Latency profiling down to the individual microservice invocation",
        "Historical comparison overlays comparing live telemetry against past baselines"
    ],
    ("services/real-time-monitoring.html", "Equipment Status & Health Mapping"): [
        "Interactive floorplan diagrams displaying real-time machine operating states",
        "Component-level health scoring predicting impending hardware failures",
        "Thermal and vibration trend tracking on high-wear mechanical assets",
        "Operating hour accumulation tracking for scheduled maintenance dispatch",
        "Power draw and electrical load monitoring across industrial circuits",
        "Automated equipment lockout upon safety threshold breach"
    ],
    ("services/real-time-monitoring.html", "Configurable Alerting Rules"): [
        "Composite alerting conditions combining multiple telemetry signals",
        "Flapping detection preventing alert storms during borderline conditions",
        "On-call schedule integration routing alerts via PagerDuty and OpsGenie",
        "Severity-based notification channels (SMS, voice call, push, webhook)",
        "Quiet hour filters suppressing non-critical notifications outside shifts",
        "One-click alert acknowledgment directly from mobile notifications"
    ],
    ("services/real-time-monitoring.html", "Historical Replay & Shift Reporting"): [
        "Time-scrubber visual replay of plant floor events leading to an outage",
        "Automated end-of-shift operational summary generation and email dispatch",
        "Downtime categorization reports tracking mechanical, electrical, and human factors",
        "Mean Time Between Failures (MTBF) and Mean Time to Repair (MTTR) tracking",
        "Shift-to-shift handover notes repository documenting ongoing issues",
        "Exportable compliance records for regulatory equipment safety audits"
    ],

    # services/iot-integration.html
    ("services/iot-integration.html", "Industrial Sensor Connectivity"): [
        "Protocol normalization for Modbus RTU/TCP, OPC-UA, and BACnet devices",
        "Wireless sensor mesh networking across BLE, Zigbee, and LoRaWAN",
        "Analog and digital signal conditioning for legacy industrial machinery",
        "High-density sensor deployments supporting thousands of concurrent nodes",
        "Battery life telemetry and power optimization for remote wireless sensors",
        "Environmental sensor integration tracking humidity, air quality, and dust"
    ],
    ("services/iot-integration.html", "Edge Gateway & Protocol Translation"): [
        "Edge computing runtime executing local business logic and filtering",
        "Local data caching during broadband internet or cellular network dropouts",
        "Over-The-Air (OTA) firmware update orchestration across edge fleets",
        "Hardware watchdog timers ensuring automatic gateway reboot on freeze",
        "JSON payload serialization for low-bandwidth cellular transmission",
        "Edge-level sensor calibration offset adjustment and zero-point calibration"
    ],
    ("services/iot-integration.html", "Environmental Condition Monitoring"): [
        "Server room and data center temperature and humidity threshold logging",
        "Cleanroom positive pressure differential and particulate monitoring",
        "Water leak and moisture detection sensors in critical facility spaces",
        "Cold storage refrigeration logging satisfying food safety standards",
        "Hazardous gas and air toxicity detection with emergency siren triggers",
        "Long-term ambient climate trend analysis for facility HVAC optimization"
    ],
    ("services/iot-integration.html", "Secure Edge-to-Cloud Ingestion"): [
        "Mutual TLS (mTLS) authentication with unique per-device X.509 certificates",
        "Hardware security module (HSM) and TPM integration for private key storage",
        "Encrypted MQTT communication over TLS port 8883",
        "Device quarantine protocols for sensors exhibiting anomalous telemetry",
        "Scalable cloud ingestion queues handling millions of telemetry points/second",
        "Data retention tiering moving historical sensor records to low-cost cold storage"
    ],

    # services/operational-analytics.html
    ("services/operational-analytics.html", "Operational KPI Dashboards"): [
        "Overall Equipment Effectiveness (OEE) metrics broken down by shift",
        "Work-in-progress (WIP) tracking across complex multi-step manufacturing",
        "Throughput and cycle time metrics compared against target run rates",
        "Executive scorecards consolidating operational performance across facilities",
        "Visual scrap and rework rate indicators with defect category breakdown",
        "Customizable widget library allowing rapid report creation without coding"
    ],
    ("services/operational-analytics.html", "Statistical Anomaly Detection"): [
        "Machine learning models identifying subtle drift in operational metrics",
        "Dynamic thresholding adjusting acceptable bounds for seasonal changes",
        "Multi-variable correlation analysis highlighting compounding friction points",
        "False positive suppression algorithms filtering out normal operating spikes",
        "Root cause discovery algorithms ranking likely contributing factors",
        "Automated incident ticket creation upon confirmed anomaly detection"
    ],
    ("services/operational-analytics.html", "Predictive Maintenance Modeling"): [
        "Remaining Useful Life (RUL) calculations on critical bearing and motor assets",
        "Predictive maintenance scheduling aligned with planned plant changeovers",
        "Spare parts inventory replenishment triggers based on failure probabilities",
        "Degradation modeling trained on thousands of historical component lifecycles",
        "Cost-benefit analysis comparing run-to-failure versus planned servicing",
        "Maintenance work order integration with attached diagnostic data packets"
    ],
    ("services/operational-analytics.html", "Historical Trend & Bottleneck Analysis"): [
        "Long-term operational capacity utilization trends across quarters",
        "Process flow bottleneck mapping identifying systemic queuing delays",
        "Energy efficiency analysis identifying peak tariff consumption periods",
        "Supplier raw material quality correlation against production downtime",
        "Year-over-year operational efficiency and yield improvement tracking",
        "Standardized reporting packages for board of directors and stakeholders"
    ],

    # services/workflow-automation.html
    ("services/workflow-automation.html", "Event-Triggered Automated Actions"): [
        "Real-time event streaming triggering instantaneous cross-system actions",
        "Complex event processing (CEP) evaluating multi-event conditions",
        "Automated equipment shutdown upon critical safety sensor trip",
        "Instant inventory reservation upon high-priority work order approval",
        "Customer alert dispatch upon shipment arrival at local delivery hub",
        "Automated backup snapshot initiation following major database batch runs"
    ],
    ("services/workflow-automation.html", "Automated Work Order Generation"): [
        "Work order drafting prepopulated with sensor telemetry and asset IDs",
        "Automated bill-of-materials assignment for required replacement parts",
        "Skill-based technician dispatch matching certifications to repair complexity",
        "Estimated labor hour calculations and scheduling into maintenance calendars",
        "Digital checklists requiring step-by-step sign-off on mobile devices",
        "Closing sign-off and equipment recommissioning notification to ops managers"
    ],
    ("services/workflow-automation.html", "Multi-Tier Incident Escalation"): [
        "Tiered escalation trees notifying front-line, engineering, and VP levels",
        "Escalation timers advancing unresolved tickets to the next tier",
        "War room bridge initiation (Zoom/Teams) for critical Severity-1 outages",
        "Stakeholder broadcast messages updating executive leadership on resolution",
        "Customer-facing status banner updates on public corporate service portals",
        "Incident post-mortem scheduling and documentation template creation"
    ],
    ("services/workflow-automation.html", "Human-in-the-Loop Approvals"): [
        "Interactive approval cards in Slack, Microsoft Teams, and mobile apps",
        "One-click decision buttons (Approve, Reject, Request More Info)",
        "Audit-logged reviewer comments explaining justification for decisions",
        "Timeout fallback actions executing safe defaults if approval lapses",
        "Multi-signer consensus requirements for high-financial-impact operations",
        "Mobile biometrics (Face ID / Touch ID) verification for sensitive sign-offs"
    ],

    # services/infrastructure-monitoring.html
    ("services/infrastructure-monitoring.html", "Synthetic API & Endpoint Monitoring"): [
        "Global multi-region synthetic probes pinging public and private endpoints",
        "Multi-step user journey synthetic transactions (login, cart, checkout)",
        "TLS/SSL certificate expiration countdown tracking and automated alerting",
        "DNS lookup time, TCP handshake, and TTFB latency breakdown",
        "HTTP response code and expected payload regex validation",
        "Automated traceroute capture upon detected packet loss or endpoint failure"
    ],
    ("services/infrastructure-monitoring.html", "Centralized Log Aggregation"): [
        "High-throughput log ingestion across application, server, and network tiers",
        "Real-time log parsing, tokenization, and structured field extraction",
        "Fast full-text search across terabytes of indexed operational logs",
        "Saved search queries and shareable investigation views for DevOps teams",
        "Log-based metric generation transforming recurring error strings into KPIs",
        "Compliance-driven log retention policies with automated cold storage archiving"
    ],
    ("services/infrastructure-monitoring.html", "Application Performance Tracing (APM)"): [
        "Distributed request tracing across complex microservice architectures",
        "Slow database query identification with execution time and explain plans",
        "Thread pool, CPU utilization, and JVM garbage collection pause metrics",
        "Third-party API dependency latency tracking and error budgets",
        "Service dependency map visualization with real-time error rate color coding",
        "Code-level bottleneck profiling pinpointing specific slow methods"
    ],
    ("services/infrastructure-monitoring.html", "Incident Reporting & Status Portals"): [
        "Public and private status pages displaying real-time system component health",
        "Subscriber email, SMS, and webhook notification broadcasts during downtime",
        "Scheduled maintenance window announcements with countdown timers",
        "Uptime SLA calculation and historical availability percentage widgets",
        "Post-incident root cause analysis (RCA) publishing and archive",
        "Internal service desk integration syncing status changes with incident tickets"
    ],
}

# ==============================================================================
# Domain 4 Additional Points (6 per capability to make 10 total)
# ==============================================================================
DS4_EXTRA_POINTS = {
    # services/agentic-ai.html
    ("services/agentic-ai.html", "Multi-Step Task Orchestration"): [
        "Dynamic task planning decomposing complex objectives into subtasks",
        "Execution graph tracking with fallback branches on subtask failure",
        "Context window optimization retaining pertinent long-term memory",
        "Multi-agent coordination dividing tasks between specialized worker agents",
        "Self-reflection loops evaluating output quality against defined benchmarks",
        "Graceful task suspension and state checkpointing during system updates"
    ],
    ("services/agentic-ai.html", "API-Connected Tool Calling"): [
        "Strictly validated JSON Schema definitions for internal API endpoints",
        "Authentication credential vaulting isolating API keys from prompt context",
        "Rate limit management and exponential backoff retry algorithms",
        "Read-only versus mutating tool classification with safety restrictions",
        "Input parameter sanitization preventing SQL injection and prompt hacking",
        "Comprehensive tool execution telemetry capturing latency and payload sizes"
    ],
    ("services/agentic-ai.html", "Human-in-the-Loop Approval Gates"): [
        "Configurable confidence score thresholds triggering required human review",
        "Interactive approval diff views highlighting proposed database modifications",
        "Mobile push notifications for rapid on-the-go supervisor sign-offs",
        "Audit trail recording user identity, timestamp, and modification comments",
        "Supervisory intervention controls allowing agents to be paused or redirected",
        "Post-review feedback loops updating agent fine-tuning and prompt guidelines"
    ],
    ("services/agentic-ai.html", "Continuous Agent Monitoring & Auditing"): [
        "Cost and token expenditure tracking broken down by department and agent",
        "Hallucination and drift detection against established truth datasets",
        "Latency percentile tracking (p50, p95, p99) per agent execution chain",
        "Compliance auditing verifying alignment with enterprise safety policies",
        "Prompt injection vulnerability scanning and red-teaming test suites",
        "Detailed session replay capturing full reasoning chains and tool logs"
    ],

    # services/generative-ai.html
    ("services/generative-ai.html", "Enterprise Knowledge Assistants (RAG)"): [
        "Semantic vector search over internal technical wikis, SOPs, and manuals",
        "Document chunking algorithms optimized for complex tables and lists",
        "Hybrid search combining dense vector embeddings with sparse keyword BM25",
        "Citation attribution linking every generated answer to verified source docs",
        "Access control filtering ensuring users see only documents they have rights to",
        "Multi-lingual translation and summarization of international enterprise docs"
    ],
    ("services/generative-ai.html", "Semantic Document Search"): [
        "Natural language query understanding handling synonyms and acronyms",
        "Faceted search filters by department, document creation date, and file type",
        "Instant document preview with highlighted text passages answering queries",
        "Automated metadata tagging extracting author, department, and keywords",
        "Zero-result query analytics identifying gaps in enterprise knowledge bases",
        "Real-time index updates upon new file upload to cloud repositories"
    ],
    ("services/generative-ai.html", "Automated Summarization & Reporting"): [
        "Executive briefing generation condensing multi-page technical reports",
        "Meeting transcript summarization extracting action items and decisions",
        "Customer feedback sentiment clustering and recurring pain point digests",
        "Financial earnings and balance sheet narrative generation",
        "Regulatory compliance delta reporting comparing draft policies to standards",
        "Exportable formatted reports in PDF, Markdown, and Word formats"
    ],
    ("services/generative-ai.html", "Privacy & Security Guardrails"): [
        "Automated Personally Identifiable Information (PII) masking and redaction",
        "Enterprise zero-data-retention agreements with frontier model providers",
        "Prompt injection and jailbreak prevention filter layers",
        "Toxicity and corporate tone enforcement guardrails",
        "Air-gapped on-premise model hosting for highly regulated defense/banking data",
        "Comprehensive model input/output audit logging for security compliance"
    ],

    # services/document-processing.html
    ("services/document-processing.html", "Automated Document Classification"): [
        "Multi-modal deep learning models categorizing scanned PDFs and images",
        "Document separation identifying individual forms within multi-page scans",
        "Language detection and routing to specialized OCR translation engines",
        "Confidence score assignment determining straight-through processing eligibility",
        "Automated routing to corresponding line-of-business department queues",
        "Re-classification feedback loops training categorization classifiers"
    ],
    ("services/document-processing.html", "Complex Table & Entity Extraction"): [
        "Multi-page financial table boundary detection and column alignment",
        "Handwritten signature, date, and checkbox detection algorithms",
        "Key-value pair extraction matching non-standard form layouts",
        "Entity normalization converting dates, currencies, and addresses to standards",
        "Barcode and QR code decoding embedded within scanned documentation",
        "High-accuracy extraction on skewed, low-resolution, and degraded scans"
    ],
    ("services/document-processing.html", "Cross-System Validation Rules"): [
        "Cross-referencing extracted invoice totals against purchase order databases",
        "Vendor tax ID validation against government registry APIs",
        "Mathematical line-item checksum verification (quantities times unit price)",
        "Patient insurance policy ID verification against clearinghouse databases",
        "Duplicate document submission detection preventing double payments",
        "Automated exception flagging when extracted fields contradict business rules"
    ],
    ("services/document-processing.html", "Human-in-the-Loop Review Queues"): [
        "Side-by-side verification interface displaying scan alongside extracted fields",
        "Single-click field correction with automatic coordinate bounding box zoom",
        "Keyboard shortcut navigation enabling rapid data entry operator review",
        "Quality assurance sampling auditing 5% of automated straight-through documents",
        "Operator productivity metrics tracking keystrokes and documents per hour",
        "Immediate downstream API dispatch upon human approval"
    ],

    # services/ai-workflow-automation.html
    ("services/ai-workflow-automation.html", "Inbound Email & Communication Triage"): [
        "Intent recognition classifying incoming support and sales inquiries",
        "Sentiment analysis prioritizing frustrated enterprise clients",
        "Automated extraction of order numbers, account IDs, and core requests",
        "Pre-drafted context-aware email responses ready for agent review",
        "Automated routing to specialized departmental queues and account reps",
        "Spam and phishing heuristic filtering protecting communication channels"
    ],
    ("services/ai-workflow-automation.html", "Cross-System Administrative Sync"): [
        "Automated client contact updates across CRM, billing, and support tools",
        "Calendar synchronization and automated follow-up meeting booking",
        "Document attachment archiving into cloud storage repositories",
        "Cross-platform status synchronization keeping legacy databases updated",
        "Bi-directional transaction synchronization between sales and accounting",
        "Automated daily reconciliation reports logging all cross-system updates"
    ],
    ("services/ai-workflow-automation.html", "Policy & Contract Compliance Validation"): [
        "Natural language scanning verifying contracts match standard terms",
        "Deviation identification highlighting non-standard indemnity or warranty clauses",
        "Master Service Agreement (MSA) term tracking and expiration alerts",
        "Regulatory clause verification satisfying regional compliance mandates",
        "Standardized risk score assignment for proposed third-party contract drafts",
        "Legal review escalation queues for high-risk contractual modifications"
    ],
    ("services/ai-workflow-automation.html", "Audit-Ready Transaction Tracking"): [
        "Immutable append-only transaction ledgers documenting workflow steps",
        "Timestamped recording of automated agent actions and user interventions",
        "Cryptographic hash chaining verifying log integrity for external auditors",
        "Exportable audit trail packages satisfying SOC 2 and ISO 27001 criteria",
        "Role-based audit viewer permissions restricting log visibility",
        "Automated retention schedules archiving aged logs to immutable storage"
    ],

    # services/healthcare-automation.html
    ("services/healthcare-automation.html", "Digital Patient Pre-Registration"): [
        "Mobile-first patient intake forms accessible via SMS link prior to visit",
        "Digital health insurance card photo capture with instant OCR extraction",
        "Electronic signature capture for HIPAA disclosure and consent forms",
        "Automated demographic matching preventing duplicate electronic medical records",
        "Co-pay calculation and secure digital payment processing prior to arrival",
        "Self-check-in kiosk integration with QR code verification upon arrival"
    ],
    ("services/healthcare-automation.html", "Appointment Coordination & Scheduling"): [
        "Multi-provider calendar optimization reducing schedule white space",
        "Automated multi-channel appointment reminders via SMS, email, and phone",
        "Two-way SMS conversational rescheduling updating clinic schedules in real time",
        "Waitlist automation offering cancelled slots to available patients",
        "Provider appointment duration modeling based on procedure complexity",
        "Post-visit follow-up scheduling aligned with clinical care plans"
    ],
    ("services/healthcare-automation.html", "Referral Document Classification"): [
        "Inbound fax and PDF referral triage categorizing clinical urgency",
        "Specialist matching based on referring provider orders and clinical notes",
        "Insurance prior-authorization requirement checking for referred procedures",
        "Automated intake notification to referring physician upon appointment booking",
        "Attachment of diagnostic lab and imaging records directly to patient chart",
        "Referral leakage analytics tracking completed versus dropped referral appointments"
    ],
    ("services/healthcare-automation.html", "Administrative Billing Data Assistance"): [
        "Encounter note pre-scrubbing identifying missing clinical documentation",
        "Charge capture validation ensuring all rendered procedures are billed",
        "Fee schedule validation against contracted commercial and CMS payer rates",
        "Automated claim scrubbing correcting formatting errors prior to clearinghouse submission",
        "Patient statement generation with clear breakdown of balance responsibility",
        "Payment plan setup and recurring automated card-on-file charging"
    ],

    # services/healthcare-data-analytics.html
    ("services/healthcare-data-analytics.html", "Operational Clinic Dashboards"): [
        "Real-time patient rooming and exam room turnaround velocity tracking",
        "Provider schedule utilization and patient no-show rate monitoring",
        "Average patient wait time metrics broken down by intake and exam phases",
        "Clinic staffing level recommendations based on predicted appointment volume",
        "Multi-facility comparative scorecards for healthcare system executives",
        "Mobile dashboard views for clinic practice managers"
    ],
    ("services/healthcare-data-analytics.html", "EHR & Practice Management Integration"): [
        "Bi-directional HL7 v2 and FHIR API connectors to Epic, Cerner, and Athena",
        "Real-time ADT (admission, discharge, transfer) feed consumption",
        "Clinical observation result synchronization (ORU) from lab systems",
        "Secure health information exchange (HIE) integration across community health",
        "Master Patient Index (MPI) deduplication and demographic normalization",
        "Audit logging compliant with HIPAA security rules for all data transactions"
    ],
    ("services/healthcare-data-analytics.html", "Patient Access & Intake Quality Analytics"): [
        "Call center abandonment rate and average speed of answer (ASA) metrics",
        "Registration error rate tracking identifying training needs for intake staff",
        "Patient conversion rate from initial appointment inquiry to completed visit",
        "Digital intake adoption metrics tracking online vs in-clinic registration",
        "Patient satisfaction (CAHPS) correlation against wait time metrics",
        "Demographic access disparity analysis supporting community health initiatives"
    ],
    ("services/healthcare-data-analytics.html", "Administrative Denial & Billing Analytics"): [
        "Denial rate categorization tracking medical necessity, eligibility, and coding",
        "First-pass clean claim rate tracking by commercial and government payer",
        "Accounts Receivable (A/R) aging bucket visualization (30, 60, 90, 120+ days)",
        "Underpayment identification flagging payer remittances below contracted rates",
        "Root cause denial analysis recommending front-end operational fixes",
        "Revenue cycle team productivity metrics tracking resolved claims per day"
    ],
}

# ==============================================================================
# Tech, Industries & Connect Additional Points (6 per capability to make 10 total)
# ==============================================================================
DTIC_EXTRA_POINTS = {
    # technology/agentic-ai.html
    ("technology/agentic-ai.html", "Goal Decomposition & Task Planning"): [
        "Multi-branch planning trees evaluating optimal subtask sequencing",
        "Contextual memory retaining past planning successes and edge cases",
        "Resource constraint evaluation before executing computationally heavy tasks",
        "Autonomous goal reformulation when initial strategies meet obstacles",
        "Dynamic priority re-weighting based on changing enterprise business goals",
        "Structured task serialization for reproducible audit inspections"
    ],
    ("technology/agentic-ai.html", "Safe API Tool Calling"): [
        "Strict JSON schema validation for all incoming and outgoing tool parameters",
        "Encrypted credential management ensuring agents never access raw API keys",
        "Idempotency token enforcement preventing duplicate operations on retry",
        "Rate limiting and concurrency controls protecting upstream microservices",
        "Read-only execution modes for sensitive financial and operational tools",
        "Detailed execution logging recording parameters, status, and response latency"
    ],
    ("technology/agentic-ai.html", "Retrieval-Augmented Memory (RAG)"): [
        "Hybrid search merging dense vector embeddings with BM25 keyword indexes",
        "Document chunking algorithms retaining hierarchical headings and tables",
        "Semantic caching reducing repetitive LLM lookups for common queries",
        "Document freshness scoring prioritizing recently updated enterprise policies",
        "Strict access-control filtering preserving enterprise permission boundaries",
        "Automated citation linking validating answers against internal documentation"
    ],
    ("technology/agentic-ai.html", "Human-in-the-Loop Approval Gates"): [
        "Confidence threshold rules requiring supervisor approval on low-confidence plans",
        "Visual execution diff preview displaying proposed system modifications",
        "Slack, Teams, and email interactive approval action cards",
        "Emergency kill-switch stopping active autonomous agent workflows immediately",
        "Time-bounded approval expirations defaulting to safe containment behaviors",
        "Continuous feedback logging updating agent fine-tuning and system prompts"
    ],

    # technology/generative-ai.html
    ("technology/generative-ai.html", "Retrieval-Augmented Generation (RAG)"): [
        "Multi-vector representations capturing code, text, and tabular data",
        "Cross-encoder reranking algorithms elevating the most relevant chunks",
        "Dynamic query expansion converting colloquial phrases to technical terms",
        "Source document lineage tracking showing exact page and section references",
        "Enterprise access control synchronization reflecting Active Directory rights",
        "Incremental re-indexing keeping vector databases synchronized with updates"
    ],
    ("technology/generative-ai.html", "Private Enterprise Knowledge Search"): [
        "Natural language search across Confluence, Google Drive, and SharePoint",
        "Semantic deduplication consolidating repeated procedural documentation",
        "Instant snippet extraction providing immediate concise answers",
        "Department-level search scoping isolating confidential HR/Finance records",
        "Multi-lingual search capabilities enabling global team collaboration",
        "Search analytics identifying internal documentation blind spots"
    ],
    ("technology/generative-ai.html", "Automated Document Summarization"): [
        "Multi-page technical specification synthesis into executive briefings",
        "Meeting transcript summarization highlighting decisions and action items",
        "Customer feedback digest grouping recurring complaints into themes",
        "Contract difference analysis comparing supplier proposals against standard MSAs",
        "Regulatory update summaries highlighting required operational adjustments",
        "Exportable summary formats in Markdown, PDF, and HTML"
    ],
    ("technology/generative-ai.html", "Zero-Retention Security Architecture"): [
        "Air-gapped on-premise model hosting for sensitive healthcare and financial data",
        "Zero-retention enterprise SLAs with cloud model providers",
        "Real-time PII and sensitive data masking prior to model inference",
        "Prompt injection and jailbreak detection guardrail layers",
        "Strict outbound content filtering ensuring brand and regulatory compliance",
        "Complete cryptographic audit logging of all system prompts and responses"
    ],

    # technology/intelligent-automation.html
    ("technology/intelligent-automation.html", "Deterministic Business Rule Engines"): [
        "Visual business rule authoring enabling ops managers to update logic without code",
        "High-performance rule execution evaluating thousands of conditions per second",
        "Version-controlled rule sets with instant rollback capabilities",
        "Unit testing frameworks simulating rule behavior across historical datasets",
        "Multi-variable decision tables handling complex financial and operational matrices",
        "Audit-logged execution traces showing which specific rules fired per transaction"
    ],
    ("technology/intelligent-automation.html", "Event-Driven Webhook Orchestration"): [
        "High-throughput message buffering preventing downstream server overloads",
        "Exponential backoff retry algorithms with dead-letter queue isolation",
        "Payload signature verification ensuring incoming webhooks are authentic",
        "Dynamic header injection and payload transformation between disparate APIs",
        "Real-time delivery status monitoring with manual re-trigger capabilities",
        "Cross-region event distribution ensuring 99.99% uptime availability"
    ],
    ("technology/intelligent-automation.html", "Document & Data Transformation"): [
        "Schema mapping transforming XML, CSV, EDI, and JSON formats seamlessly",
        "Data validation rules asserting correct types, ranges, and mandatory fields",
        "Automated character encoding normalization resolving malformed text",
        "Lookup table integration enriching transaction records with master data",
        "High-speed streaming parsers processing multi-gigabyte data files",
        "Transformation error logging isolating problematic rows without failing batches"
    ],
    ("technology/intelligent-automation.html", "Exception Routing & Human Review"): [
        "Configurable exception severity levels determining escalation speed",
        "Operator triage queues with side-by-side data comparison views",
        "Single-click bulk exception resolution for known recurring systemic issues",
        "Root cause tagging feeding weekly continuous improvement reviews",
        "Automated customer notification when exceptions impact order delivery",
        "Comprehensive operator audit tracking recording all manual edits"
    ],

    # technology/iot.html
    ("technology/iot.html", "Lightweight Edge Protocols"): [
        "MQTT over TLS for battery-efficient low-bandwidth telemetry transmission",
        "CoAP (Constrained Application Protocol) integration for resource-limited nodes",
        "Binary payload serialization using Protocol Buffers to minimize cellular data",
        "Configurable telemetry transmission frequencies based on equipment state",
        "Keep-alive heartbeat monitoring detecting silent sensor connectivity drops",
        "Quality of Service (QoS 0, 1, 2) message delivery guarantees"
    ],
    ("technology/iot.html", "Edge Gateway Computing"): [
        "Local containerized microservices executing data filtering at the machine edge",
        "Offline telemetry buffering preventing data loss during network blackouts",
        "Edge-based statistical anomaly detection flagging spikes before cloud transmission",
        "Over-The-Air (OTA) remote firmware deployment with rollback protection",
        "Hardware watchdog monitoring ensuring automatic gateway self-healing",
        "Dual-SIM cellular failover guaranteeing continuous remote connectivity"
    ],
    ("technology/iot.html", "Time-Series Data Ingestion"): [
        "Scalable time-series storage optimized for millions of writes per second",
        "Automated downsampling and rollup policies preserving long-term trends",
        "Sub-second query performance across months of continuous sensor logs",
        "Data tiering policies moving aged readings to ultra-low-cost cold storage",
        "Time-series anomaly detection algorithms identifying sensor drift",
        "High-speed export pipelines for external machine learning model training"
    ],
    ("technology/iot.html", "Device Security & Management"): [
        "Unique per-device X.509 cryptographic certificates and mutual TLS (mTLS)",
        "Hardware root of trust (TPM 2.0) securing private encryption keys",
        "Automated device quarantine isolating compromised or misbehaving hardware",
        "Remote device reboot, configuration updates, and diagnostic commands",
        "Vulnerability scanning verifying edge gateway Linux kernel patch levels",
        "Centralized device inventory dashboard tracking location, firmware, and health"
    ],

    # technology/enterprise-integration.html
    ("technology/enterprise-integration.html", "API Gateways (REST & GraphQL)"): [
        "Centralized authentication and authorization using OAuth 2.0 and JWT",
        "Granular rate limiting and traffic shaping per API client tier",
        "Automated API documentation generation conforming to OpenAPI 3.0",
        "Edge caching reducing database load for high-frequency read requests",
        "Request and response schema validation preventing malformed payloads",
        "Real-time distributed tracing tracking API calls across microservice meshes"
    ],
    ("technology/enterprise-integration.html", "Bidirectional Data Buses"): [
        "Apache Kafka and RabbitMQ distributed pub/sub event backbones",
        "Event replay capabilities allowing new services to reconstruct historical state",
        "Guaranteed at-least-once and exactly-once message processing semantics",
        "Schema Registry integration enforcing data contract compatibility",
        "High-throughput message compression optimizing network bandwidth",
        "Dead-letter queues capturing failed messages for diagnostic inspection"
    ],
    ("technology/enterprise-integration.html", "Third-Party SaaS Connectors"): [
        "Pre-built certified connectors to Salesforce, SAP, NetSuite, and Workday",
        "Automated token refresh and credential rotation for cloud SaaS APIs",
        "Pagination and bulk data extraction handling millions of cloud records",
        "Field mapping transformation engine reconciling custom SaaS attributes",
        "Webhook ingestion listeners capturing real-time SaaS record updates",
        "SaaS API deprecation monitoring alerting teams to required endpoint updates"
    ],
    ("technology/enterprise-integration.html", "Enterprise Security & Governance"): [
        "Zero-trust network segmentation and private VPC peering connectivity",
        "Data masking and tokenization for sensitive financial and PII fields",
        "Role-based and attribute-based access controls (RBAC & ABAC)",
        "Automated compliance reporting verifying SOC 2 and ISO 27001 controls",
        "Comprehensive immutable audit logging tracking all integration transactions",
        "Regular automated penetration testing of integration gateway surfaces"
    ],

    # technology/data-analytics.html
    ("technology/data-analytics.html", "Interactive Operational Dashboards"): [
        "Sub-second visualization rendering over massive multi-million row datasets",
        "Role-tailored dashboard presets for executives, managers, and operators",
        "Mobile-responsive layout optimized for on-the-go tablet review",
        "Visual drill-down paths linking high-level KPIs to underlying transactions",
        "Automated dashboard distribution via scheduled PDF and email reports",
        "Custom formula builder enabling rapid calculation of composite metrics"
    ],
    ("technology/data-analytics.html", "Automated ETL & Data Warehousing"): [
        "Automated change data capture (CDC) streaming live database updates",
        "Data warehouse modeling across Snowflake, Google BigQuery, and Databricks",
        "Automated schema evolution handling new database columns dynamically",
        "Data quality testing frameworks verifying completeness and uniqueness",
        "Historical data archiving reducing operational database storage footprints",
        "Data lineage mapping tracing every dashboard metric back to source tables"
    ],
    ("technology/data-analytics.html", "Statistical Trend Modeling"): [
        "Time-series forecasting models projecting quarterly revenue and demand",
        "Seasonality decomposition separating recurring cycles from secular trends",
        "Cohort analysis tracking customer retention and lifetime value (LTV)",
        "Correlation matrices identifying hidden operational relationships",
        "Monte Carlo risk simulations modeling supply chain disruption probabilities",
        "Automated anomaly alerts notifying leadership of statistically unusual shifts"
    ],
    ("technology/data-analytics.html", "Data Governance & Role-Based Access"): [
        "Column-level and row-level security masking sensitive data by user role",
        "Data catalog and searchable business glossary standardizing definitions",
        "Data access request workflows with manager sign-off and expiration dates",
        "Compliance auditing verifying adherence to GDPR, CCPA, and HIPAA",
        "Data retention policy enforcement automating cold storage and purging",
        "Data stewardship tracking assigning departmental owners to datasets"
    ],

    # industries/foodtech.html
    ("industries/foodtech.html", "Digital Food Ordering & B2B Portals"): [
        "Multi-vendor restaurant wholesale ordering portals with volume pricing",
        "Mobile-first digital menus with allergen disclosures and calorie counts",
        "Unified order aggregation across third-party delivery apps (UberEats, DoorDash)",
        "Contactless QR-code ordering and split-bill payment processing",
        "Automated kitchen routing directing orders to corresponding prep stations",
        "Repeat order subscription management for recurring commercial food deliveries"
    ],
    ("industries/foodtech.html", "FEFO Inventory & Batch Traceability"): [
        "Automated First-Expired, First-Out warehouse picker dispatch logic",
        "Farm-to-fork chain-of-custody tracking satisfying regulatory food safety laws",
        "Automated shelf-life expiration countdowns with markdown triggers",
        "Batch recall isolation tools identifying affected customers within seconds",
        "Barcode and RFID scanning logging batch movements at every transit step",
        "Supplier quality grading and return workflows for sub-standard shipments"
    ],
    ("industries/foodtech.html", "Cold Chain IoT Telemetry Monitoring"): [
        "Wireless temperature and humidity sensors in refrigerated trucks and freezers",
        "Instant SMS alerts notifying fleet managers of thermal threshold breaches",
        "Automated HACCP digital compliance log generation eliminating paper charts",
        "Compressor health monitoring predicting refrigeration unit breakdowns",
        "Geofenced arrival logging at cold storage distribution hubs",
        "Historical temperature certificate generation attached to delivery invoices"
    ],
    ("industries/foodtech.html", "Commissary & Recipe Yield Management"): [
        "Central production planning consolidating restaurant unit requisitions",
        "Standardized recipe costing with dynamic raw material price updates",
        "Ingredient batch scaling calculations for industrial-scale batch cooking",
        "Scrap and waste tracking identifying kitchen preparation inefficiencies",
        "Inter-branch transfer dispatch with digital transit manifests",
        "Nutritional calculation engines generating compliant packaging labels"
    ],

    # industries/retail-ecommerce.html
    ("industries/retail-ecommerce.html", "Unified Omnichannel Storefronts"): [
        "Headless commerce architecture delivering sub-second page rendering",
        "Unified shopping cart synchronizing across mobile, web, and tablet",
        "End-to-end support for Buy Online, Pick Up In Store (BOPIS / Curbside)",
        "Personalized product recommendation carousels based on browsing history",
        "Localized currency, tax, and multi-language internationalization",
        "Frictionless checkout supporting Apple Pay, Google Pay, and digital wallets"
    ],
    ("industries/retail-ecommerce.html", "Dynamic Product Information (PIM)"): [
        "Multi-channel product syndication across marketplaces (Amazon, eBay, etc.)",
        "Rich attribute modeling managing complex size, color, and fit matrices",
        "Digital asset management (DAM) with automated high-res image optimization",
        "Batch catalog import and export via CSV, XML, and automated APIs",
        "Scheduled promotional pricing and campaign launch countdowns",
        "SEO-optimized structured data markup generating rich search results"
    ],
    ("industries/retail-ecommerce.html", "Real-Time Multi-Node Inventory Sync"): [
        "Distributed inventory ledger synchronizing stock across stores and 3PLs",
        "Real-time stock reservation preventing overselling during flash promotions",
        "Safety stock buffer rules adjusting dynamically for seasonal demand",
        "Cycle count auditing with mobile barcode scanning reconciliation",
        "Phantom inventory detection via point-of-sale versus ledger variance alerts",
        "Inter-store inventory transfer requests for out-of-stock customer orders"
    ],
    ("industries/retail-ecommerce.html", "Fulfillment & Carrier Integration"): [
        "Distributed Order Management (DOM) routing orders to nearest fulfillment node",
        "Carrier rate shopping selecting optimal balance of speed and freight cost",
        "Automated shipping label and commercial customs manifest generation",
        "Real-time tracking portals with branded milestone updates for consumers",
        "Automated returns authorization (RMA) with prepaid return label printing",
        "Reverse logistics triage sorting returned items for restock or liquidation"
    ],

    # industries/manufacturing.html
    ("industries/manufacturing.html", "Industrial IoT Telemetry Ingestion"): [
        "High-frequency sensor connectivity normalizing Modbus, OPC-UA, and BACnet",
        "Vibration, heat, and power consumption monitoring on core production lines",
        "Edge gateway buffering preventing telemetry loss during network dropouts",
        "Standardized time-series storage handling thousands of readings per second",
        "Sensor health diagnostics detecting calibration drift or physical damage",
        "Mutual TLS encryption securing all plant-floor-to-cloud data pathways"
    ],
    ("industries/manufacturing.html", "Real-Time OEE & Plant Dashboards"): [
        "Overall Equipment Effectiveness (OEE) metrics updated per production shift",
        "Availability, performance, and quality KPI breakdowns on plant displays",
        "Work-in-progress (WIP) tracking across multi-stage assembly lines",
        "Downtime categorization logging mechanical, electrical, and tooling faults",
        "Shift handover digital logs documenting machine anomalies and run rates",
        "Mobile dashboard views enabling plant managers to monitor operations remotely"
    ],
    ("industries/manufacturing.html", "Condition-Based Predictive Maintenance"): [
        "Remaining Useful Life (RUL) calculations on high-wear rotating machinery",
        "Predictive vibration frequency analysis identifying bearing wear weeks early",
        "Automated spare part inventory reservation upon failure probability threshold",
        "Maintenance work order scheduling coordinated with planned changeovers",
        "Failure mode and effects analysis (FMEA) library tracking component history",
        "Reduction of catastrophic machine failure and unplanned plant shutdowns"
    ],
    ("industries/manufacturing.html", "Automated Maintenance Dispatch"): [
        "Automated work order creation populated with real-time sensor diagnostics",
        "Technician skill matching ensuring certified personnel handle complex repairs",
        "Mobile maintenance app providing digital schematics and step-by-step repair SOPs",
        "Spare part barcode scanning logging component consumption in ERP ledgers",
        "Sign-off workflows verifying calibration before machine recommissioning",
        "Mean Time to Repair (MTTR) metrics tracking maintenance team efficiency"
    ],

    # industries/logistics.html
    ("industries/logistics.html", "Real-Time Freight & Fleet Tracking"): [
        "Telematics and GPS tracking across linehaul tractors and delivery vans",
        "Predictive ETA calculations factoring live traffic congestion and weather",
        "Geofence entry and exit alerts at distribution hubs and client docks",
        "Driver hours-of-service (HOS) and electronic logging device (ELD) integration",
        "Speeding, harsh braking, and fuel consumption telematics for safety scoring",
        "Public tracking links with milestone updates for freight shippers"
    ],
    ("industries/logistics.html", "Dynamic Route Planning & Optimization"): [
        "Multi-stop route algorithms minimizing total mileage, tolls, and drive time",
        "Vehicle weight, bridge height, and hazmat routing constraints",
        "Dynamic re-routing around road closures and sudden weather emergencies",
        "Consolidated dispatch combining LTL shipments into full truckloads",
        "Turn-by-turn mobile commercial navigation tailored for heavy freight trucks",
        "Carbon footprint calculation and green route selection reporting"
    ],
    ("industries/logistics.html", "Warehouse Dock Appointment Scheduling"): [
        "Carrier self-service portal for booking inbound and outbound dock doors",
        "Automated dock door allocation based on trailer size and freight handling type",
        "Dwell time tracking alerting dock supervisors to detention fee thresholds",
        "Cross-docking coordination synchronizing inbound freight directly to outbound trailers",
        "Gate check-in kiosk integration with barcode and license plate recognition",
        "Dock productivity metrics tracking pallet unloading speed per team"
    ],
    ("industries/logistics.html", "Electronic Proof of Delivery (ePOD)"): [
        "Mobile glass signature capture confirming recipient name and title",
        "High-resolution photographic capture of delivered freight and condition",
        "Geotagged coordinate stamping verifying physical delivery location",
        "Exception logging for damaged packaging, refusals, or piece count shortages",
        "Immediate delivery receipt generation transmitted via automated email",
        "Instant status synchronization to ERP systems triggering freight billing"
    ],

    # industries/enterprise.html
    ("industries/enterprise.html", "Client Relationship Management (CRM)"): [
        "Centralized 360-degree client account profiles with complete interaction history",
        "Sales pipeline tracking with weighted revenue forecasting and stage gates",
        "Automated lead routing assigning prospects to qualified regional executives",
        "Omnichannel communication logging integrating email, phone, and video notes",
        "Contract lifecycle management tracking renewals, amendments, and MSAs",
        "Client health scoring identifying expansion opportunities and churn risks"
    ],
    ("industries/enterprise.html", "Workforce & HRMS Platforms"): [
        "Centralized employee directory and organizational chart visualization",
        "Digital onboarding workflows with automated equipment and software provisioning",
        "Biometric and mobile time-and-attendance tracking with overtime calculation",
        "Self-service portal for leave requests, benefit enrollments, and pay slips",
        "360-degree performance evaluation cycles linked to goal and OKR tracking",
        "Compliance monitoring verifying mandatory corporate training completions"
    ],
    ("industries/enterprise.html", "Automated Approval Hierarchies"): [
        "Multi-tiered financial delegation matrices based on spend threshold and department",
        "Parallel approval routing across legal, finance, and procurement leadership",
        "Interactive approval buttons directly inside email, Slack, and Microsoft Teams",
        "Time-based escalation timers re-routing pending approvals to secondary signers",
        "Immutable audit trails logging user identity, timestamp, and reviewer rationale",
        "Mobile biometrics (Face ID / Touch ID) authorization for sensitive transactions"
    ],
    ("industries/enterprise.html", "Executive Business Intelligence"): [
        "Real-time visual KPI dashboards consolidating metrics across subsidiaries",
        "Cross-departmental financial and operational metric aggregation",
        "Interactive drill-down paths from high-level summaries to transactional logs",
        "Predictive trend modeling projecting quarterly cash flow and capacity",
        "Scheduled executive summary digests delivered via automated PDF reports",
        "Role-based dashboard security ensuring executives see relevant division data"
    ],

    # industries/healthcare.html
    ("industries/healthcare.html", "Digital Patient Pre-Registration"): [
        "Mobile-first patient intake forms completed securely prior to appointments",
        "Insurance card photo capture with instant OCR extraction and verification",
        "Digital signature capture for HIPAA compliance, consent, and financial policies",
        "Automated demographic matching preventing duplicate electronic medical records",
        "Estimated patient co-pay calculation and digital payment collection",
        "Self-service check-in kiosk integration with contactless QR verification"
    ],
    ("industries/healthcare.html", "Appointment Coordination & Scheduling"): [
        "Provider calendar optimization reducing schedule fragmentation and wait times",
        "Automated appointment reminder sequences sent via SMS, email, and voice",
        "Two-way SMS conversational scheduling updating clinical calendars in real time",
        "Automated waitlist notifications offering cancelled appointment slots",
        "Procedure duration modeling adjusting slot lengths for clinical complexity",
        "Post-procedure follow-up appointment booking aligned with care protocols"
    ],
    ("industries/healthcare.html", "Referral Document Classification"): [
        "Automated triage of inbound clinical referral faxes, PDFs, and letters",
        "Clinical specialist matching based on physician orders and insurance networks",
        "Insurance prior-authorization requirement checking for referred procedures",
        "Automated notification to referring physicians upon completed patient visit",
        "Diagnostic report and imaging attachment directly to patient medical charts",
        "Referral leakage analytics tracking completed versus dropped specialty appointments"
    ],
    ("industries/healthcare.html", "Administrative Billing Data Assistance"): [
        "Clinical documentation pre-scrubbing identifying missing clinical details",
        "Automated charge capture verification ensuring all procedures are coded",
        "Fee schedule validation ensuring accurate billing against commercial payer contracts",
        "Claim scrubbing rules reducing initial clearinghouse rejection rates",
        "Patient billing statement generation with clear balance breakdowns",
        "Payment plan setup and recurring automated card-on-file charging"
    ],

    # connect/general-enquiries.html
    ("connect/general-enquiries.html", "Corporate Communications"): [
        "Official executive statement and press release distribution channels",
        "Media inquiry handling with designated corporate communications officers",
        "Brand asset and corporate logo guideline repository access",
        "Executive interview and conference speaking engagement coordination",
        "Corporate social responsibility and sustainability initiative inquiries",
        "Investor relations contact routing and quarterly report distribution"
    ],
    ("connect/general-enquiries.html", "Strategic Partnerships"): [
        "Technology alliance exploration for software vendors and cloud providers",
        "System integrator and consultant referral program agreements",
        "Joint go-to-market solution development and co-marketing initiatives",
        "Reseller and channel partner program evaluation and onboarding",
        "Academic and research institution collaboration agreements",
        "Partner portal access with shared technical documentation and roadmaps"
    ],
    ("connect/general-enquiries.html", "Corporate Administration"): [
        "Headquarters and regional branch office physical address information",
        "Official corporate legal entity documentation and vendor registration",
        "Accounts payable and vendor invoice submission routing",
        "Compliance, privacy, and data protection officer (DPO) communications",
        "Human resources employment verification and corporate inquiries",
        "General feedback and executive office correspondence management"
    ],
    ("connect/general-enquiries.html", "Direct Contact Channels"): [
        "Dedicated corporate telephone switchboard (040-46146093)",
        "Centralized general inquiry email monitoring (info@novaarc.net)",
        "Interactive web inquiry form with automated acknowledgment receipts",
        "Business hour operational schedules for regional support offices",
        "Physical office visit appointment scheduling and security badge clearance",
        "Emergency corporate security and facility incident reporting"
    ],

    # connect/project-enquiry.html
    ("connect/project-enquiry.html", "Architecture Discovery Sessions"): [
        "Comprehensive technical discovery evaluating existing legacy tech stacks",
        "Enterprise system integration point mapping and data flow modeling",
        "Cloud infrastructure capacity and scalability assessment",
        "Security, compliance, and governance requirement workshops",
        "Identification of operational bottlenecks and high-ROI automation targets",
        "Executive stakeholder interviews aligning technical roadmap with business goals"
    ],
    ("connect/project-enquiry.html", "Tailored Solution Roadmaps"): [
        "Phased implementation timeline with clearly defined deliverables",
        "Risk mitigation strategies addressing legacy system dependencies",
        "Technology stack recommendations tailored to internal team capabilities",
        "Resource allocation models outlining required engineering capacity",
        "Key performance indicator (KPI) definitions measuring project success",
        "Milestone gating ensuring architecture review sign-offs before production rollout"
    ],
    ("connect/project-enquiry.html", "Transparent Commercial Models"): [
        "Fixed-scope milestone contracts for clearly defined transformation projects",
        "Dedicated engineering squad engagements for agile continuous development",
        "Transparent blended hourly and monthly rate structures",
        "Detailed cost estimation broken down by architectural component",
        "Clear change order protocols preventing budget overruns or scope creep",
        "Flexible payment terms tied to verified milestone deliverable acceptances"
    ],
    ("connect/project-enquiry.html", "Dedicated Sales Contacts"): [
        "Direct pairing with senior enterprise technology solutions directors",
        "Single point of contact managing communication across technical discovery",
        "Rapid non-disclosure agreement (NDA) execution protecting proprietary data",
        "Collaborative shared workspace setup for project documentation",
        "Access to senior architects and engineering leads during proposal review",
        "Structured RFP and RFI response management with detailed technical submissions"
    ],

    # connect/service-enquiry.html
    ("connect/service-enquiry.html", "Digital Commerce & SCM Advisory"): [
        "Evaluation of omnichannel commerce platforms and headless architectures",
        "Warehouse management and distributed order orchestration advisory",
        "Supply chain visibility audits identifying carrier and inventory blind spots",
        "B2B buyer portal architecture design with corporate credit terms",
        "Logistics TMS and route optimization ROI assessments",
        "Cold chain telemetry and food safety batch traceability guidance"
    ],
    ("connect/service-enquiry.html", "Enterprise Business Advisory"): [
        "CRM sales pipeline velocity and customer data fragmentation assessments",
        "HRMS workforce management and digital onboarding optimization",
        "Business process automation roadmaps targeting high-volume manual tasks",
        "Enterprise legacy system modernization and cloud migration strategies",
        "Middleware and API gateway architecture reviews (REST, GraphQL, Kafka)",
        "Operational BI dashboard and centralized data warehousing audits"
    ],
    ("connect/service-enquiry.html", "Monitoring & Automation Advisory"): [
        "Industrial IoT sensor connectivity and edge gateway feasibility reviews",
        "Real-time operational telemetry dashboard architecture planning",
        "Condition-based predictive maintenance modeling recommendations",
        "Incident response escalation workflows and automated work order design",
        "Cloud infrastructure and application APM monitoring audits",
        "Overall Equipment Effectiveness (OEE) metrics calculation and benchmarking"
    ],
    ("connect/service-enquiry.html", "AI & Healthcare Tech Advisory"): [
        "Agentic AI workflow feasibility assessments and tool-calling governance",
        "Private enterprise knowledge retrieval (RAG) architecture planning",
        "Intelligent document processing (IDP) and automated OCR evaluation",
        "Healthcare administrative automation and digital patient intake design",
        "FHIR and HL7 v2 interoperability roadmaps for clinical systems",
        "HIPAA compliance, PII redaction, and model security guardrail reviews"
    ],

    # connect/technical-support.html
    ("connect/technical-support.html", "Ticket Submission & Tracking"): [
        "24/7 self-service online customer support portal access",
        "Granular issue severity categorization (Severity 1 critical through Severity 4 minor)",
        "Automated email ticket creation with unique tracking reference numbers",
        "Direct screenshot, log file, and diagnostic data attachment uploads",
        "Real-time ticket status updates and assigned engineer messaging",
        "Complete historical ticket repository for corporate team visibility"
    ],
    ("connect/technical-support.html", "Direct Helpdesk Channels"): [
        "Dedicated enterprise technical support phone line (040-46146093)",
        "Direct email routing to tier-2 and tier-3 engineering specialists",
        "Secure remote screen sharing and diagnostic sessions for complex issues",
        "Designated customer success manager escalation contacts",
        "Multilingual technical support engineers for global enterprise operations",
        "Emergency on-call developer paging for production-down incidents"
    ],
    ("connect/technical-support.html", "SLA-Defined Response Times"): [
        "Sub-15 minute initial response guarantees for Severity 1 production outages",
        "Clear Mean Time to Resolution (MTTR) targets defined in corporate service contracts",
        "Continuous around-the-clock engineering mobilization for critical system issues",
        "Formal root cause analysis (RCA) reporting delivered within 48 hours of resolution",
        "Financial service credit remedies for unexcused SLA downtime thresholds",
        "Quarterly SLA compliance reviews presented to client operational leadership"
    ],
    ("connect/technical-support.html", "System Patching & Maintenance"): [
        "Scheduled off-peak maintenance windows minimizing operational disruption",
        "Proactive security vulnerability patching and Linux kernel updates",
        "Database performance tuning, index optimization, and vacuuming",
        "Annual disaster recovery failover testing and backup restoration verification",
        "Third-party API dependency version deprecation updates",
        "Comprehensive pre-release testing in isolated staging environments"
    ]
}

# ==============================================================================
# Exact 4 Challenges for Digital Commerce as Specified in User Prompt
# ==============================================================================
DIGITAL_COMMERCE_CHALLENGES = [
    {
        'title': 'Inventory Discrepancies',
        'challenge': 'Disconnected inventory systems create inaccurate stock information, poor coordination, and fulfillment delays.',
        'impact': 'Stockout panics, backorders, and degraded customer trust.',
        'solution': 'Integrated inventory management, synchronized data, and real-time stock visibility.'
    },
    {
        'title': 'Limited Shipment Visibility',
        'challenge': 'Fragmented logistics information makes it difficult to monitor shipments and coordinate distribution.',
        'impact': 'Unpredictable transit times, dock congestion, and customer service escalation.',
        'solution': 'Connected shipment tracking, logistics dashboards, and automated exception notifications.'
    },
    {
        'title': 'Manual Procurement Workflows',
        'challenge': 'Manual purchasing and approval processes slow down procurement operations.',
        'impact': 'Uncontrolled maverick spending, delayed orders, and administrative overhead.',
        'solution': 'Digital requisitions, automated approval workflows, and connected supplier management.'
    },
    {
        'title': 'Disconnected Commerce Systems',
        'challenge': 'Separate storefront, payment, inventory, and fulfillment systems create operational gaps.',
        'impact': 'Data silos, delayed order processing, and fragmented customer experiences.',
        'solution': 'Integrated commerce platforms and connected order management workflows.'
    }
]

def update_page_capabilities_and_challenges(page, extra_points_map):
    rel_path = page['rel_path']
    caps = page.get('capabilities', [])
    updated_caps = []
    
    for cap in caps:
        title = cap['title']
        existing_points = cap.get('points', [])
        
        # Check if already 10 points
        if len(existing_points) >= 10:
            updated_caps.append(cap)
            continue
            
        # Get extra 6 points
        key = (rel_path, title)
        extras = extra_points_map.get(key)
        if not extras:
            # Fallback if key not exact
            for (p_path, c_title), pts in extra_points_map.items():
                if p_path == rel_path and (c_title in title or title in c_title):
                    extras = pts
                    break
                    
        if extras:
            new_points = existing_points[:4] + extras[:6]
            # Ensure exactly 10
            if len(new_points) < 10:
                needed = 10 - len(new_points)
                new_points.extend([f"Advanced enterprise capability integration {i+1}" for i in range(needed)])
            elif len(new_points) > 10:
                new_points = new_points[:10]
        else:
            print(f"  [WARN] Missing extra points for {rel_path} -> {title} (currently {len(existing_points)})")
            new_points = existing_points
            
        updated_cap = dict(cap)
        updated_cap['points'] = new_points
        updated_caps.append(updated_cap)
        
    page['capabilities'] = updated_caps
    
    # Handle challenges: ensure 4 challenges per page
    challenges = page.get('challenges', [])
    if rel_path == 'services/digital-commerce.html':
        page['challenges'] = DIGITAL_COMMERCE_CHALLENGES
    elif len(challenges) == 3:
        # Add 4th relevant challenge if only 3 exist
        ch4 = None
        if "foodtech" in rel_path:
            ch4 = {
                'title': 'Distribution Inefficiencies',
                'challenge': 'Unoptimized delivery routes and unmonitored cold chain freight create distribution delays.',
                'impact': 'High transport fuel costs and temperature-induced food quality degradation.',
                'solution': 'Hyperlocal multi-stop route optimization integrated with live telematics.'
            }
        elif "digital-commerce-platforms" in rel_path:
            ch4 = {
                'title': 'Fragmented Customer Accounts & Carts',
                'challenge': 'Customers cannot seamlessly transition between mobile, web, and corporate purchasing accounts.',
                'impact': 'Lost transactions, repeated customer service calls, and abandoned orders.',
                'solution': 'Unified omnichannel customer account ledgers with persistent carts.'
            }
        elif "supply-chain" in rel_path:
            ch4 = {
                'title': 'Multi-Echelon Replenishment Lag',
                'challenge': 'Slow order signal propagation across supply nodes causes severe bullwhip fluctuations.',
                'impact': 'Excess warehouse inventory carrying costs alongside regional stockouts.',
                'solution': 'Synchronized demand sensing with automated cross-facility replenishment balancing.'
            }
        elif "procurement" in rel_path:
            ch4 = {
                'title': 'Contract Non-Compliance & Pricing Leakage',
                'challenge': 'Buyers order outside negotiated corporate supplier agreements due to disconnected systems.',
                'impact': 'Loss of volume discount tiers and unbudgeted departmental expenditure.',
                'solution': 'Automated catalog punchouts enforcing contracted pricing and pre-approved terms.'
            }
        elif "logistics" in rel_path:
            ch4 = {
                'title': 'Inefficient Multi-Modal Route Dispatch',
                'challenge': 'Dispatchers manually coordinate carrier schedules across disconnected spreadsheets.',
                'impact': 'Underutilized trailer cube capacity, missed delivery windows, and excess deadhead miles.',
                'solution': 'Automated TMS load consolidation and algorithmic route optimization.'
            }
        elif "crm" in rel_path:
            ch4 = {
                'title': 'Disconnected Customer Communication',
                'challenge': 'Sales, support, and marketing engage clients through fragmented uncoordinated channels.',
                'impact': 'Conflicting customer messages, embarrassing miscommunications, and customer churn.',
                'solution': 'Centralized omnichannel interaction histories accessible across all client-facing teams.'
            }
        elif "hrms" in rel_path:
            ch4 = {
                'title': 'Complex Leave & Attendance Processes',
                'challenge': 'Confusing attendance rules and spreadsheet-based leave tracking create approval bottlenecks.',
                'impact': 'Payroll calculation disputes, delayed manager approvals, and employee frustration.',
                'solution': 'Automated policy-driven leave workflows with mobile calendar sync and digital approvals.'
            }
        elif "business-process" in rel_path:
            ch4 = {
                'title': 'Disconnected Legacy Enterprise Systems',
                'challenge': 'Data must be manually copied and re-entered between modern SaaS tools and legacy databases.',
                'impact': 'Costly transcription errors, delayed customer processing, and employee burnout.',
                'solution': 'Event-driven integration middleware synchronizing records automatically in real time.'
            }
        elif "enterprise-applications" in rel_path:
            ch4 = {
                'title': 'Poor Multi-Platform User Experiences',
                'challenge': 'Legacy enterprise applications lack mobile responsiveness and intuitive modern navigation.',
                'impact': 'High user training overhead, slow adoption, and operational input errors.',
                'solution': 'Modern high-performance web applications with responsive design for desktop and tablets.'
            }
        elif "enterprise-integration" in rel_path:
            ch4 = {
                'title': 'Lack of Centralized Message Middleware',
                'challenge': 'Point-to-point connections create an unmaintainable spiderweb of custom API scripts.',
                'impact': 'System-wide failures when a single endpoint updates or experiences network downtime.',
                'solution': 'Distributed pub/sub message brokers (Kafka/RabbitMQ) with guaranteed delivery semantics.'
            }
        elif "real-time-monitoring" in rel_path:
            ch4 = {
                'title': 'Delayed Incident Remediation Workflows',
                'challenge': 'When system alerts trigger, engineers lack runbooks and spend hours diagnosing root causes.',
                'impact': 'Prolonged mean-time-to-resolution (MTTR) and extended customer-facing downtime.',
                'solution': 'Automated diagnostic packet capture and contextual runbook linking on alert triggers.'
            }
        elif "iot-integration" in rel_path or "iot" in rel_path:
            ch4 = {
                'title': 'Manual Monitoring Processes',
                'challenge': 'Technicians must physically visit remote facilities and plant floors to log meter readings.',
                'impact': 'High labor expense, delayed awareness of equipment drift, and human recording errors.',
                'solution': 'Continuous remote edge sensor telemetry streaming into centralized cloud consoles.'
            }
        elif "operational-analytics" in rel_path or "data-analytics" in rel_path:
            ch4 = {
                'title': 'Unstandardized Departmental KPI Ledgers',
                'challenge': 'Different business divisions calculate operational metrics using conflicting definitions.',
                'impact': 'Executive confusion, disputed reporting numbers, and misaligned strategic priorities.',
                'solution': 'Centralized semantic data layers establishing single-source-of-truth enterprise metric definitions.'
            }
        elif "workflow-automation" in rel_path or "intelligent-automation" in rel_path:
            ch4 = {
                'title': 'Audit Trail & Compliance Vulnerabilities',
                'challenge': 'Manual task handoffs via chat and email leave no structured record for compliance auditing.',
                'impact': 'Failed regulatory compliance audits and inability to investigate process failures.',
                'solution': 'Immutable digital execution ledgers recording timestamp, user identity, and decision rationale.'
            }
        elif "infrastructure-monitoring" in rel_path:
            ch4 = {
                'title': 'Fragmented Hybrid Cloud Visibility',
                'challenge': 'Workloads split across on-premise hardware and cloud providers lack unified telemetry.',
                'impact': 'Blind spots during cross-environment outages and complex troubleshooting.',
                'solution': 'Single-pane-of-glass infrastructure monitoring aggregating metrics across all environments.'
            }
        elif "agentic-ai" in rel_path:
            ch4 = {
                'title': 'Lack of Controlled AI Workflow Execution',
                'challenge': 'Organizations hesitate to deploy AI due to fears of hallucinations and unreviewed actions.',
                'impact': 'Inability to capture productivity gains while competitors automate routine operations.',
                'solution': 'Human-in-the-loop approval gates, audit logging, and deterministically constrained guardrails.'
            }
        elif "generative-ai" in rel_path:
            ch4 = {
                'title': 'Uncontrolled Token Costs & Latency',
                'challenge': 'Direct reliance on public frontier LLMs without caching leads to unpredictable API bills.',
                'impact': 'Budget overruns and slow multi-second response times for end users.',
                'solution': 'Semantic response caching, model routing, and token optimization pipelines.'
            }
        elif "document-processing" in rel_path:
            ch4 = {
                'title': 'Lack of Automated Downstream Validation',
                'challenge': 'Extracted document text is ingested into databases without verifying against business rules.',
                'impact': 'Corrupted records, invalid customer tax IDs, and downstream operational friction.',
                'solution': 'Automated validation engines verifying extracted fields against core ERP/CRM ledgers.'
            }
        elif "healthcare-automation" in rel_path or "healthcare" in rel_path:
            ch4 = {
                'title': 'Limited Operational Visibility',
                'challenge': 'Clinic administrators struggle to anticipate patient flow bottlenecks and exam room turnaround.',
                'impact': 'Extended patient waiting room delays, frustrated clinical staff, and lost clinical revenue.',
                'solution': 'Real-time operational dashboards tracking clinic throughput and resource allocation.'
            }
        elif "healthcare-data-analytics" in rel_path:
            ch4 = {
                'title': 'Complex Regulatory Compliance Auditing',
                'challenge': 'Extracting clinical quality measures (MIPS, HEDIS) requires weeks of manual chart auditing.',
                'impact': 'Hefty regulatory penalties, lost payer quality incentives, and administrative burden.',
                'solution': 'Automated clinical registry reporting pipelines extracting compliant metrics from EHR data.'
            }
        elif "ai-workflow-automation" in rel_path:
            ch4 = {
                'title': 'Drift in Model Accuracy Over Time',
                'challenge': 'AI models deployed without continuous evaluation gradually degrade as business data changes.',
                'impact': 'Declining classification precision and increased human intervention over time.',
                'solution': 'Continuous evaluation pipelines monitoring accuracy and automated re-training triggers.'
            }
        else:
            ch4 = {
                'title': 'Operational Coordination Gaps',
                'challenge': 'Siloed communications and disconnected systems create coordination delays.',
                'impact': 'Slower response times, duplicate effort, and inconsistent execution.',
                'solution': 'Centralized coordination platforms aligning teams, workflows, and data.'
            }
        
        if ch4:
            challenges.append(ch4)
            page['challenges'] = challenges

    # Ensure all challenges have title, challenge/impact, and solution
    for ch in page.get('challenges', []):
        if not ch.get('title') and ch.get('challenge'):
            # Split if title embedded
            parts = ch['challenge'].split(':', 1)
            if len(parts) == 2 and len(parts[0]) < 40:
                ch['title'] = parts[0].strip()
                ch['challenge'] = parts[1].strip()
            else:
                ch['title'] = ch['challenge']

def process_file(file_path, var_name, pages, extra_points_map):
    print(f"\nProcessing {file_path} ({len(pages)} pages)...")
    for p in pages:
        update_page_capabilities_and_challenges(p, extra_points_map)
        
    formatted = pprint.pformat(pages, width=120, sort_dicts=False)
    content = f'''"""
{os.path.basename(file_path)} - NovaArc Website Data Module
"""

{var_name} = {formatted}
'''
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  [OK] Successfully updated {file_path}")

def main():
    print("==================================================================")
    print("NOVAARC - EXPANDING CAPABILITIES TO 10 POINTS & REFINING CHALLENGES")
    print("==================================================================")
    
    process_file(
        os.path.join(SCRIPT_DIR, 'data_services.py'),
        'SERVICES_PAGES',
        ds1.SERVICES_PAGES,
        DS1_EXTRA_POINTS
    )
    
    process_file(
        os.path.join(SCRIPT_DIR, 'data_services_domain2.py'),
        'SERVICES_DOMAIN_2',
        ds2.SERVICES_DOMAIN_2,
        DS2_EXTRA_POINTS
    )
    
    process_file(
        os.path.join(SCRIPT_DIR, 'data_services_domain3.py'),
        'SERVICES_DOMAIN_3',
        ds3.SERVICES_DOMAIN_3,
        DS3_EXTRA_POINTS
    )
    
    process_file(
        os.path.join(SCRIPT_DIR, 'data_services_domain4.py'),
        'SERVICES_DOMAIN_4',
        ds4.SERVICES_DOMAIN_4,
        DS4_EXTRA_POINTS
    )
    
    process_file(
        os.path.join(SCRIPT_DIR, 'data_tech_ind_connect.py'),
        'TECH_IND_CONNECT_PAGES',
        dtic.TECH_IND_CONNECT_PAGES,
        DTIC_EXTRA_POINTS
    )
    
    print("\nAll data files processed successfully!")

if __name__ == '__main__':
    main()

