#!/usr/bin/env python3
"""
Nova Arc - Page Data Enhancer
Ensures that all 47 subpages have:
1. 5 or 6 authentic, detailed capability cards
2. 4-6 tailored industries served with icons
3. Proper introductory and supporting paragraph lengths
"""

# Map of curated industries for each domain/page
DEFAULT_INDUSTRIES = [
    {"name": "Retail & E-Commerce", "icon": "shopping-bag"},
    {"name": "FoodTech & QSR", "icon": "coffee"},
    {"name": "Supply Chain & Logistics", "icon": "truck"},
    {"name": "Industrial Manufacturing", "icon": "cpu"},
    {"name": "Healthcare & Life Sciences", "icon": "activity"},
    {"name": "Enterprise Business", "icon": "briefcase"}
]

INDUSTRY_ICON_MAP = {
    "shopping-bag": '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#0284C7" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 2L3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"></path><line x1="3" y1="6" x2="21" y2="6"></line><path d="M16 10a4 4 0 0 1-8 0"></path></svg>',
    "truck": '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#0284C7" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect x="1" y="3" width="15" height="13"></rect><polygon points="16 8 20 8 23 11 23 16 16 16 16 8"></polygon><circle cx="5.5" cy="18.5" r="2.5"></circle><circle cx="18.5" cy="18.5" r="2.5"></circle></svg>',
    "coffee": '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#0284C7" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 8h1a4 4 0 0 1 0 8h-1"></path><path d="M2 8h16v9a4 4 0 0 1-4 4H6a4 4 0 0 1-4-4V8z"></path><line x1="6" y1="1" x2="6" y2="4"></line><line x1="10" y1="1" x2="10" y2="4"></line><line x1="14" y1="1" x2="14" y2="4"></line></svg>',
    "cpu": '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#0284C7" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="4" width="16" height="16" rx="2" ry="2"></rect><rect x="9" y="9" width="6" height="6"></rect><line x1="9" y1="1" x2="9" y2="4"></line><line x1="15" y1="1" x2="15" y2="4"></line><line x1="9" y1="20" x2="9" y2="23"></line><line x1="15" y1="20" x2="15" y2="23"></line><line x1="20" y1="9" x2="23" y2="9"></line><line x1="20" y1="14" x2="23" y2="14"></line><line x1="1" y1="9" x2="4" y2="9"></line><line x1="1" y1="14" x2="4" y2="14"></line></svg>',
    "activity": '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#0284C7" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline></svg>',
    "briefcase": '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#0284C7" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path></svg>',
    "layers": '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#0284C7" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 2 7 12 12 22 7 12 2"></polygon><polyline points="2 17 12 22 22 17"></polyline><polyline points="2 12 12 17 22 12"></polyline></svg>'
}

def get_industries_for_page(rel_path):
    """Returns 5 targeted industry objects for any page."""
    if "foodtech" in rel_path:
        return [
            {"name": "FoodTech & Cloud Kitchens", "icon": "coffee"},
            {"name": "Quick-Service Restaurant Chains", "icon": "coffee"},
            {"name": "Central Commissary Networks", "icon": "truck"},
            {"name": "Food Processing & Packaging", "icon": "cpu"},
            {"name": "Perishable Cold-Chain Logistics", "icon": "truck"}
        ]
    elif "commerce" in rel_path or "retail" in rel_path:
        return [
            {"name": "B2B & B2C E-Commerce", "icon": "shopping-bag"},
            {"name": "Omnichannel Retail Brands", "icon": "shopping-bag"},
            {"name": "Wholesale & Distribution", "icon": "truck"},
            {"name": "Consumer Packaged Goods (CPG)", "icon": "briefcase"},
            {"name": "Specialty Merchant Networks", "icon": "layers"}
        ]
    elif "supply-chain" in rel_path or "procurement" in rel_path or "logistics" in rel_path:
        return [
            {"name": "Third-Party Logistics (3PL)", "icon": "truck"},
            {"name": "Industrial Manufacturing", "icon": "cpu"},
            {"name": "Multi-Echelon Distribution Hubs", "icon": "layers"},
            {"name": "Automotive & Heavy Equipment", "icon": "truck"},
            {"name": "Wholesale Supply Networks", "icon": "shopping-bag"}
        ]
    elif "healthcare" in rel_path:
        return [
            {"name": "Hospital Networks & Health Systems", "icon": "activity"},
            {"name": "Ambulatory & Specialty Clinics", "icon": "activity"},
            {"name": "Diagnostic Imaging & Labs", "icon": "cpu"},
            {"name": "Digital Health & Telemedicine", "icon": "layers"},
            {"name": "Healthcare Payers & TPA Services", "icon": "briefcase"}
        ]
    elif "crm" in rel_path or "hrms" in rel_path or "enterprise" in rel_path or "business-process" in rel_path:
        return [
            {"name": "Enterprise SaaS & Technology", "icon": "layers"},
            {"name": "Financial Services & FinTech", "icon": "briefcase"},
            {"name": "Global Professional Services", "icon": "briefcase"},
            {"name": "Healthcare Provider Systems", "icon": "activity"},
            {"name": "Retail & Commercial Services", "icon": "shopping-bag"}
        ]
    elif "monitoring" in rel_path or "iot" in rel_path or "operational-analytics" in rel_path:
        return [
            {"name": "Smart Factory & Industrial IoT", "icon": "cpu"},
            {"name": "Cold-Chain & Asset Telematics", "icon": "truck"},
            {"name": "Automated Warehousing Facilities", "icon": "layers"},
            {"name": "Mission-Critical Cloud Infrastructure", "icon": "activity"},
            {"name": "Renewable Energy & Utilities", "icon": "briefcase"}
        ]
    elif "ai-" in rel_path or "agentic" in rel_path or "generative" in rel_path or "document" in rel_path:
        return [
            {"name": "Enterprise Software & Cloud Platforms", "icon": "layers"},
            {"name": "Financial Services & Underwriting", "icon": "briefcase"},
            {"name": "Healthcare Documentation & Clinical", "icon": "activity"},
            {"name": "Supply Chain & Order Operations", "icon": "truck"},
            {"name": "Customer Support & High-Volume Ops", "icon": "briefcase"}
        ]
    return DEFAULT_INDUSTRIES

def get_supplemental_capabilities(rel_path, current_caps):
    """
    Ensures that every page has at least 5 or 6 detailed capabilities.
    Returns 1 or 2 high-quality additional capabilities if current count is < 5.
    """
    if len(current_caps) >= 5:
        return current_caps

    needed = 5 - len(current_caps)
    supplements = []

    if "digital-commerce-platforms" in rel_path:
        supplements.append({
            "title": "Headless Microservices & API Orchestration",
            "desc": "Decoupled frontend storefronts connecting seamlessly with backend inventory, pricing, and fulfillment via GraphQL and REST gateways.",
            "points": [
                "Sub-50ms catalog retrieval and personalized facet indexing",
                "Decoupled edge caching with automated cache invalidation hooks",
                "Standardized OpenAPI contracts for third-party marketplace integration",
                "High-resilience circuit breakers preventing cart checkout drop-offs"
            ]
        })
    elif "foodtech" in rel_path:
        supplements.append({
            "title": "Commissary Production & Shift Depletion",
            "desc": "Automated batch planning for central kitchens, coordinating raw ingredient demand across multiple restaurant branches.",
            "points": [
                "Yield calculation based on standard operating recipes and variance logs",
                "Automated inter-branch transfer orders with real-time dispatch manifests",
                "Expiration date alerting with first-in, first-out (FIFO) stock rotation",
                "Waste tracking dashboards identifying recipe preparation discrepancies"
            ]
        })
    elif "supply-chain-management" in rel_path:
        supplements.append({
            "title": "Multi-Echelon Safety Stock Optimization",
            "desc": "Dynamic reorder algorithms that balance working capital with stockout risks across central hubs and regional distribution centers.",
            "points": [
                "Automated safety stock recalculation based on supplier lead-time variance",
                "Lead-time deviation alerting identifying chronic supplier bottlenecks",
                "Cross-docking candidate identification for high-velocity SKUs",
                "Inter-depot rebalancing transfer automation reducing duplicate purchasing"
            ]
        })
    elif "procurement" in rel_path:
        supplements.append({
            "title": "Automated Spend Analytics & Contract Auditing",
            "desc": "Real-time visibility into off-contract spend, vendor price compliance, and corporate purchasing budget consumption.",
            "points": [
                "Off-contract rogue spend detection and automated exception alerts",
                "Contract pricing audit engine preventing billing overcharges",
                "Vendor category spend concentration and alternative sourcing models",
                "Early-payment discount optimization with cash-flow schedule planning"
            ]
        })
    elif "logistics" in rel_path:
        supplements.append({
            "title": "Automated Freight Audit & Carrier Bill Reconciliation",
            "desc": "Digital auditing of carrier freight invoices against contract tariffs, dimensional weights, and milestone delivery proofs.",
            "points": [
                "Automated accessorial charge verification and rate dispute handling",
                "Dimensional weight discrepancies and billable freight validation",
                "Carrier scorecarding measuring SLA compliance and damage claims",
                "Consolidated invoice processing cutting accounts payable cycle times"
            ]
        })
    elif "crm" in rel_path:
        supplements.append({
            "title": "Account Health Scoring & Proactive Renewal Tracking",
            "desc": "Algorithmic monitoring of customer product engagement, support ticket frequency, and contract expiration milestones.",
            "points": [
                "Automated renewal pipeline creation 90 days prior to contract end",
                "Customer satisfaction sentiment scoring derived from support interactions",
                "Key stakeholder departure detection and re-engagement playbooks",
                "Expansion opportunity alerts triggered by license tier utilization"
            ]
        })
    elif "hrms" in rel_path:
        supplements.append({
            "title": "Employee Performance & Skill Competency Matrix",
            "desc": "Continuous feedback cycles, goal tracking, and corporate skill inventory mapping for workforce development.",
            "points": [
                "Quarterly review automation with 360-degree peer feedback aggregation",
                "Internal skill taxonomy and candidate matching for open project roles",
                "Individual development plan (IDP) milestone tracking and check-ins",
                "Executive succession planning dashboards identifying organizational talent gaps"
            ]
        })
    elif "business-process-automation" in rel_path:
        supplements.append({
            "title": "Exception Escalation & SLA Breach Prevention",
            "desc": "Intelligent monitors that detect workflow bottlenecks and automatically reroute stalled tasks to secondary approvers.",
            "points": [
                "Dynamic countdown timers on high-priority operational approval steps",
                "Automatic delegation rules for out-of-office approvers with audit logs",
                "Executive escalation dashboards highlighting chronic organizational hold-ups",
                "Historical process latency analytics enabling ongoing workflow optimization"
            ]
        })
    elif "enterprise-applications" in rel_path:
        supplements.append({
            "title": "Modular Domain Architecture & Cloud Modernization",
            "desc": "Transforming brittle monolithic software into scalable, containerized microservices built on secure modern frameworks.",
            "points": [
                "Domain-driven design isolating business logic from infrastructure concerns",
                "Containerized deployment pipelines on Kubernetes with zero-downtime rollouts",
                "Comprehensive unit and integration test automation ensuring code reliability",
                "Granular role-based authorization (RBAC) backed by corporate Single Sign-On"
            ]
        })
    elif "enterprise-integration" in rel_path:
        supplements.append({
            "title": "Resilient Queue Buffering & Dead-Letter Recovery",
            "desc": "Asynchronous messaging backbones that prevent data loss during third-party endpoint downtime or network outages.",
            "points": [
                "Guaranteed at-least-once message delivery via Kafka or RabbitMQ backbones",
                "Automatic retry policies with exponential backoff on transient network faults",
                "Dead-letter queue inspection consoles allowing safe message replay after repairs",
                "Real-time integration health metrics alerting engineers to API latency spikes"
            ]
        })
    elif "real-time-monitoring" in rel_path:
        supplements.append({
            "title": "Dynamic Threshold Tuning & False-Positive Suppression",
            "desc": "Adaptive alert baselines that account for normal business cycle spikes, eliminating notification fatigue for operations teams.",
            "points": [
                "Seasonal baseline modeling adjusting thresholds during peak transaction windows",
                "Correlated alert grouping consolidating secondary alarms into single incidents",
                "Automated mute windows during scheduled maintenance and software updates",
                "Direct incident dispatch to on-call engineers via Slack and PagerDuty"
            ]
        })
    elif "iot-integration" in rel_path:
        supplements.append({
            "title": "Edge Gateway Computing & Local Failover Caching",
            "desc": "On-premise edge runtimes that process telemetry locally and buffer data securely during intermittent cloud disconnections.",
            "points": [
                "Local sensor anomaly evaluation executing emergency stops without cloud latency",
                "Encrypted offline telemetry buffering with automated burst sync on reconnection",
                "Over-the-air (OTA) secure firmware deployment across distributed gateway fleets",
                "Device authentication via mutual TLS (mTLS) and hardware security modules"
            ]
        })
    elif "operational-analytics" in rel_path:
        supplements.append({
            "title": "Automated Cohort Benchmarking & Metric Discrepancy Alerts",
            "desc": "Continuous comparison of performance indicators across operating units, facilities, or regional depots.",
            "points": [
                "Statistical outlier detection flagging locations with anomalous costs or cycle times",
                "Automated scheduled executive briefings delivered via email and secure mobile links",
                "Interactive drill-down from enterprise rollups to individual transaction records",
                "Exportable governance-grade audit reports compliant with corporate regulatory needs"
            ]
        })
    elif "workflow-automation" in rel_path:
        supplements.append({
            "title": "Cross-System Event Synchronization & Rollback Guards",
            "desc": "Transactional integrity across multi-step workflows spanning disparate software applications and cloud vendors.",
            "points": [
                "Compensating transaction triggers automatically reverting changes if a step fails",
                "Distributed idempotency tokens preventing accidental duplicate actions",
                "Real-time visual execution graphs detailing current step progress for operators",
                "Granular execution logs documenting payload timestamps and response codes"
            ]
        })
    elif "infrastructure-monitoring" in rel_path:
        supplements.append({
            "title": "Synthetic Transaction Probing & User Journey Monitoring",
            "desc": "Automated headless browser scripts that continuously test critical business flows from multiple global points of presence.",
            "points": [
                "Continuous emulation of login, search, checkout, and invoice generation flows",
                "Page load waterfall breakdown identifying slow third-party scripts and assets",
                "Global latency benchmarking alerting on regional internet routing degradations",
                "Automated screen capture on synthetic failure aiding immediate triage"
            ]
        })
    elif "agentic-ai" in rel_path:
        supplements.append({
            "title": "Dynamic Tool-Calling & Safe Execution Sandboxing",
            "desc": "Secure sandboxed environments enabling autonomous AI agents to execute code, query databases, and invoke enterprise APIs.",
            "points": [
                "Deterministic parameter validation preventing out-of-bounds API mutations",
                "Ephemeral sandbox runtimes isolating computational tasks from production cores",
                "Multi-agent debate protocols evaluating plan feasibility before execution",
                "Granular audit trails recording every prompt, tool parameter, and system response"
            ]
        })
    elif "generative-ai" in rel_path:
        supplements.append({
            "title": "Private Hybrid Semantic Retrieval & Vector Indexing",
            "desc": "Combines dense vector embeddings with sparse keyword search to deliver pinpoint accuracy across complex enterprise documentation.",
            "points": [
                "Reciprocal Rank Fusion (RRF) unifying vector search with traditional keyword lookups",
                "Chunking strategies optimized for complex tables, technical diagrams, and legal clauses",
                "Document-level permission filtering guaranteeing users only retrieve authorized info",
                "Automated vector re-indexing triggered by document repository updates"
            ]
        })
    elif "document-processing" in rel_path:
        supplements.append({
            "title": "Confidence Score Routing & Active Learning Feedback",
            "desc": "Automated routing of borderline extractions to specialist reviewers, using verified corrections to continuously improve parsing models.",
            "points": [
                "Field-level confidence scoring flagging uncertain dates, totals, or tax amounts",
                "Intuitive side-by-side human validation interface with document bounding boxes",
                "Continuous retraining pipelines updating extraction models based on human corrections",
                "Strict privacy masking for Personally Identifiable Information (PII) before storage"
            ]
        })
    elif "ai-workflow-automation" in rel_path:
        supplements.append({
            "title": "Unstructured Request Triage & Automated Routing",
            "desc": "Natural language classification of incoming emails, tickets, and customer attachments, instantly routing items to the right department.",
            "points": [
                "Intent classification identifying urgent complaints, billing disputes, or RFPs",
                "Automated entity extraction parsing policy numbers, invoice IDs, and customer codes",
                "Priority scoring accelerating high-value accounts into expedited queues",
                "Draft response generation preparing contextual reply templates for human agents"
            ]
        })
    elif "healthcare-automation" in rel_path:
        supplements.append({
            "title": "Clinical Pre-Service Clearance & Denial Prevention",
            "desc": "Automated verification of clinical necessity and insurance pre-authorization rules prior to scheduled patient procedures.",
            "points": [
                "Automated check against payer-specific clinical coverage guidelines",
                "Missing clinical documentation alerts prompting physicians before submission",
                "Real-time prior authorization status tracking reducing patient rescheduling",
                "Denial root-cause categorization identifying preventable administrative errors"
            ]
        })
    elif "healthcare-data-analytics" in rel_path:
        supplements.append({
            "title": "FHIR Interoperability & Patient Data De-Identification",
            "desc": "Standardized health data translation enabling cross-institutional research and clinical benchmarking while safeguarding patient privacy.",
            "points": [
                "Automated translation between legacy HL7 v2 messages and modern FHIR R4 resources",
                "HIPAA Safe Harbor and Expert Determination de-identification algorithms",
                "Longitudinal patient journey timeline unifying pharmacy, clinic, and lab records",
                "Role-based clinical views tailored for physicians, care managers, and analysts"
            ]
        })
    else:
        # General supplemental capability
        supplements.append({
            "title": "Enterprise Security Governance & Continuous Compliance",
            "desc": "End-to-end encryption, granular role-based access control, and comprehensive audit logging aligned with corporate compliance standards.",
            "points": [
                "TLS 1.3 in-transit and AES-256 at-rest encryption across all storage tiers",
                "Role-based access control (RBAC) integrated with corporate identity providers",
                "Immutable event auditing capturing user, system, and automated actions",
                "Continuous security posture assessments and automated vulnerability checks"
            ]
        })

    # Add supplemental capabilities
    extended = list(current_caps) + supplements[:needed]
    return extended

