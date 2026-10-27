# Technology, Industries, and Connect Subpages Data
TECH_IND_CONNECT_PAGES = [
    # -------------------------------------------------------------
    # TECHNOLOGY SUBPAGES (6 Pages)
    # -------------------------------------------------------------
    {
        "rel_path": "technology/agentic-ai.html",
        "category_badge": "TECHNOLOGY PLATFORM ARCHITECTURE",
        "page_title": "Agentic AI",
        "page_subtitle": "AI agents for defined business tasks, multi-step task orchestration, tool and API integrations, knowledge retrieval, and human approval for sensitive actions.",
        "seo_desc": "Nova Arc Agentic AI Architecture: Autonomous multi-step orchestration, tool-calling APIs, RAG knowledge retrieval, and enterprise governance frameworks.",
        "breadcrumbs": [("Home", "index.html"), ("Technology", "technology.html"), ("Agentic AI", None)],
        "overview_paragraphs": [
            "Agentic AI represents a fundamental paradigm shift from static prompting to autonomous, goal-directed task orchestration. Instead of generating conversational replies, intelligent agents understand high-level business objectives, decompose them into structured sub-tasks, and execute actions across enterprise APIs.",
            "Nova Arc's Agentic AI architectural framework integrates deterministic execution boundaries, safe tool calling, short and long-term memory retrieval, and mandatory human-in-the-loop checkpoints.",
            "Our agents operate with complete transparency: every decision, API interaction, database read, and validation check is permanently recorded in immutable audit logs, ensuring that enterprise automation remains reliable, controllable, and secure."
        ],
        "capabilities": [
            {"title": "Goal Decomposition & Task Planning", "desc": "Reasoning engines that autonomously break complex business objectives into ordered, executable sub-tasks.", "points": ["Sequential task graphs", "Dynamic error re-planning", "State persistence across steps", "Loop detection & prevention"]},
            {"title": "Safe API Tool Calling", "desc": "Type-safe interfaces enabling agents to query enterprise databases, trigger webhooks, and execute ERP transactions.", "points": ["Granular tool permissioning", "Schema validation for inputs/outputs", "Read/write access segregation", "Isolated execution sandboxes"]},
            {"title": "Retrieval-Augmented Memory (RAG)", "desc": "Hybrid vector and graph memory stores allowing agents to recall past execution context and reference internal procedures.", "points": ["Short-term conversational buffer", "Long-term vector document store", "Exact source document citations", "Context window token optimization"]},
            {"title": "Human-in-the-Loop Approval Gates", "desc": "Configurable safety boundaries that pause agent execution and require explicit human supervisor approval for sensitive actions.", "points": ["Interactive approval interfaces", "Detailed action justification preview", "One-click supervisor sign-off", "Real-time supervisor override"]}
        ],
        "challenges": [
            {"challenge": "Unpredictable Autonomous Execution", "impact": "AI models operating without guardrails can trigger infinite execution loops or execute unexpected database modifications.", "solution": "We implement deterministic state machines that bound agent planning depth, enforce max execution steps, and constrain actions to approved tool schemas."},
            {"challenge": "Hallucinated Function Parameters", "impact": "Language models passing malformed or invalid parameters to external APIs, causing system crashes.", "solution": "Our tool calling architecture enforces strict Pydantic/JSON-schema validation on every parameter before any API call is dispatched."},
            {"challenge": "Lack of Accountability & Auditing", "impact": "Inability to explain why an autonomous agent executed a specific business action during compliance audits.", "solution": "We record complete, immutable execution traces that log the original prompt, reasoning chain, tool parameters, and response."}
        ],
        "workflow_steps": [
            {"step": "01", "title": "Boundary & Tool Definition", "desc": "Specifying allowed agent goals, API tool interfaces, database access permissions, and approval triggers."},
            {"step": "02", "title": "Agent Reasoning Engineering", "desc": "Configuring system prompt architectures, planning algorithms, state databases, and memory vector stores."},
            {"step": "03", "title": "Adversarial Testing & Guardrails", "desc": "Simulating system failures, invalid API responses, and edge cases to verify safe recovery and containment."},
            {"step": "04", "title": "Governed Production Deployment", "desc": "Deploying agents into production with real-time observability, latency monitoring, and supervisor review consoles."}
        ],
        "outcomes": [
            {"title": "Autonomous Operational Workflows", "desc": "Automate multi-step business operations that previously required hours of manual human coordination."},
            {"title": "Zero Unauthorized Actions", "desc": "Strict tool whitelisting and human approval gates guarantee complete organizational control."},
            {"title": "Resilient Execution", "desc": "Agents adapt to transient API errors and ambiguous inputs by adjusting intermediate steps automatically."},
            {"title": "Explainable AI Records", "desc": "Maintain permanent, audit-ready logs that demonstrate the exact rationale and data behind every automated action."}
        ],
        "related_links": [
            {"title": "Generative AI", "link": "technology/generative-ai.html", "tag": "Core Technology", "desc": "Explore enterprise knowledge assistants and semantic document search."},
            {"title": "Intelligent Automation", "link": "technology/intelligent-automation.html", "tag": "Core Technology", "desc": "Deterministic workflow automation and cross-system data routing."},
            {"title": "Agentic AI & Intelligent Agents Service", "link": "services/agentic-ai.html", "tag": "Service Domain", "desc": "Discover our commercial agentic AI engineering and implementation services."}
        ]
    },
    {
        "rel_path": "technology/generative-ai.html",
        "category_badge": "TECHNOLOGY PLATFORM ARCHITECTURE",
        "page_title": "Generative AI",
        "page_subtitle": "Enterprise AI assistants, conversational interfaces, document summarization, information extraction, enterprise knowledge search, and AI-assisted reporting.",
        "seo_desc": "Nova Arc Generative AI Architecture: Private enterprise RAG knowledge bases, dense vector search, semantic summarization, and zero-data-retention security.",
        "breadcrumbs": [("Home", "index.html"), ("Technology", "technology.html"), ("Generative AI", None)],
        "overview_paragraphs": [
            "Generative AI offers immense potential for knowledge synthesis, document intelligence, and employee assistance, but enterprises require strict architectures that protect corporate secrets and guarantee factual precision.",
            "Nova Arc's Generative AI technology architecture is engineered for private enterprise deployment. Utilizing advanced Retrieval-Augmented Generation (RAG) and dense vector embeddings, our systems connect language models directly to verified internal corporate data repositories.",
            "We enforce zero-retention security policies: your private documents, intellectual property, and queries are never retained for model training. Every response is grounded in retrieved source documents and accompanied by verifiable citations."
        ],
        "capabilities": [
            {"title": "Retrieval-Augmented Generation (RAG)", "desc": "Dynamic document chunking, embedding generation, and semantic retrieval that grounds AI responses strictly in corporate data.", "points": ["Hierarchical document chunking", "Dense vector embedding models", "Context-aware reranking pipelines", "Direct source document citations"]},
            {"title": "Private Enterprise Knowledge Search", "desc": "Unified semantic search interfaces querying across PDF archives, technical wikis, SharePoint libraries, and ticket histories.", "points": ["Natural language query parsing", "Hybrid keyword + semantic search", "Role-based document filtering", "Sub-second retrieval latency"]},
            {"title": "Automated Document Summarization", "desc": "Condensing hundreds of pages of legal agreements, technical specifications, and meeting transcripts into structured briefings.", "points": ["Executive briefing generation", "Action item & deadline extraction", "Comparative document analysis", "Standardized output formatting"]},
            {"title": "Zero-Retention Security Architecture", "desc": "Enterprise cloud environments configured with strict data isolation, encryption at rest and in transit, and no-training guarantees.", "points": ["Zero model training retention", "Automatic PII/PHI redaction", "Granular document ACL enforcement", "SOC 2-aligned access logging"]}
        ],
        "challenges": [
            {"challenge": "Model Hallucinations & Inaccuracies", "impact": "Public language models state fabricated facts with total confidence, creating serious business risks.", "solution": "Our RAG architecture instructs the model to synthesize answers solely from retrieved corporate passages, citing the exact document page."},
            {"challenge": "Corporate Intellectual Property Exposure", "impact": "Uploading confidential internal strategy documents to public consumer AI platforms risks proprietary data leaks.", "solution": "We deploy private, dedicated enterprise API endpoints where inputs are encrypted and contractually protected against model training."},
            {"challenge": "Unstructured Document Formats", "impact": "Multi-column tables, scanned diagrams, and complex formatting cause standard text scrapers to scramble document meaning.", "solution": "We implement advanced computer vision and layout-aware parsing that preserves document hierarchy and tabular relationships."}
        ],
        "workflow_steps": [
            {"step": "01", "title": "Data Corpus Ingestion", "desc": "Aggregating internal documents, performing OCR on scanned files, and chunking text with semantic boundary preservation."},
            {"step": "02", "title": "Embedding & Vector Indexing", "desc": "Generating high-dimensional vector embeddings and indexing content into private, secure vector databases."},
            {"step": "03", "title": "RAG Engine & Guardrail Tuning", "desc": "Configuring retrieval rerankers, citation generation pipelines, hallucination filters, and PII redaction rules."},
            {"step": "04", "title": "Enterprise Portal Rollout", "desc": "Deploying responsive conversational search interfaces, integrating single sign-on (SSO), and tracking search quality."}
        ],
        "outcomes": [
            {"title": "Instant Information Access", "desc": "Empower staff to extract vital procedures, contract clauses, and technical specs in seconds with direct citations."},
            {"title": "100% Data Confidentiality", "desc": "Ensure enterprise IP and customer communications are never exposed to public models or unauthorized employees."},
            {"title": "Verifiable Answer Accuracy", "desc": "Every generated response includes direct clickable citations pointing to the source document and page number."},
            {"title": "Automated Synthesis", "desc": "Condense multi-page technical documents and reports into executive summaries and action checklists automatically."}
        ],
        "related_links": [
            {"title": "Agentic AI", "link": "technology/agentic-ai.html", "tag": "Complementary Tech", "desc": "Combine generative knowledge assistants with API tool-calling agents."},
            {"title": "Data Analytics & Intelligence", "link": "technology/data-analytics.html", "tag": "Analytical Tech", "desc": "Query structured business databases and operational telemetry."},
            {"title": "Generative AI Applications Service", "link": "services/generative-ai.html", "tag": "Service Domain", "desc": "Discover our commercial generative AI engineering and implementation services."}
        ]
    },
    {
        "rel_path": "technology/intelligent-automation.html",
        "category_badge": "TECHNOLOGY PLATFORM ARCHITECTURE",
        "page_title": "Intelligent Automation",
        "page_subtitle": "Rule-based automation, AI-assisted workflows, document and data processing, workflow routing and approvals, exception handling, and cross-system automation.",
        "seo_desc": "Nova Arc Intelligent Automation Architecture: Deterministic rule engines, event-driven webhooks, automated document parsing, and enterprise orchestration.",
        "breadcrumbs": [("Home", "index.html"), ("Technology", "technology.html"), ("Intelligent Automation", None)],
        "overview_paragraphs": [
            "True enterprise scalability requires automating repetitive operational handoffs across ERP, CRM, banking, and inventory systems without introducing fragility or opaque decision-making.",
            "Nova Arc's Intelligent Automation technology stack combines deterministic business logic rules, asynchronous event-driven webhooks, and AI-assisted data parsing into a resilient workflow orchestration layer.",
            "Our platforms automate complex data routing, enforce multi-tier approval hierarchies, and trigger automated exception handling protocols, allowing organizations to process high-volume operational transactions with speed, accuracy, and full auditability."
        ],
        "capabilities": [
            {"title": "Deterministic Business Rule Engines", "desc": "High-throughput rule evaluation engines that execute complex conditional logic, spending thresholds, and policy checks in sub-milliseconds.", "points": ["Configurable decision tables", "Complex Boolean logic trees", "Instant policy versioning", "Zero-latency local execution"]},
            {"title": "Event-Driven Webhook Orchestration", "desc": "Asynchronous event architectures that capture database changes and API webhooks to trigger downstream operational workflows.", "points": ["Event publish-subscribe brokers", "Guaranteed at-least-once delivery", "Automatic retry & dead-letter queues", "Transactional rollback safety"]},
            {"title": "Document & Data Transformation", "desc": "Automated parsing, validation, and schema transformation translating messy inputs into clean, standardized database records.", "points": ["JSON/XML/CSV transformation", "Schema validation & sanitization", "Automated field mapping", "Data enrichment lookups"]},
            {"title": "Exception Routing & Human Review", "desc": "Intelligent routing that isolates transaction discrepancies and routes them to human specialist queues for rapid resolution.", "points": ["Automated discrepancy tagging", "Specialist review interfaces", "Audit trail annotation", "Active learning pattern updates"]}
        ],
        "challenges": [
            {"challenge": "Fragile Point-to-Point Scripts", "impact": "Custom scripts break whenever an external vendor updates a field name, halting critical operational data flows.", "solution": "Our architecture utilizes decoupled message queues and schema validation adapters that insulate workflows from unexpected changes."},
            {"challenge": "Manual Data Entry Friction", "impact": "Employees waste hours copying customer records and invoice details from emails into accounting software.", "solution": "We deploy automated transformation pipelines that validate and insert records directly into enterprise databases via secure APIs."},
            {"challenge": "Lack of Process Exception Visibility", "impact": "Failed data transfers sit in obscure server error logs without notifying operations supervisors.", "solution": "Our platforms surface all exceptions on centralized operational consoles, automatically alerting managers to uncompleted tasks."}
        ],
        "workflow_steps": [
            {"step": "01", "title": "Workflow Mapping", "desc": "Documenting existing manual data handoffs, system dependencies, error conditions, and required business rules."},
            {"step": "02", "title": "Engine & Queue Architecture", "desc": "Deploying asynchronous message queues, schema transformation pipelines, and rule evaluation engines."},
            {"step": "03", "title": "Connector Engineering", "desc": "Building secure API connectors to internal databases, cloud applications, and external partner endpoints."},
            {"step": "04", "title": "Testing & Deployment", "desc": "Simulating high transaction volumes, verifying automated rollback on errors, and deploying continuous monitoring."}
        ],
        "outcomes": [
            {"title": "80%+ Reduction in Processing Times", "desc": "Compress multi-day cross-departmental data transfers and approvals into automated sub-minute transactions."},
            {"title": "Guaranteed Transaction Delivery", "desc": "Asynchronous message queues ensure that temporary server downtime never results in lost customer or financial records."},
            {"title": "100% Policy Adherence", "desc": "Enforce strict organizational rules and approval thresholds automatically on every operational transaction."},
            {"title": "Audit-Ready Transparency", "desc": "Maintain permanent, timestamped records of every data payload, transformation step, and system execution."}
        ],
        "related_links": [
            {"title": "Enterprise Integration", "link": "technology/enterprise-integration.html", "tag": "Data Layer", "desc": "Explore our REST and GraphQL API connectors and data synchronization pipelines."},
            {"title": "Agentic AI", "link": "technology/agentic-ai.html", "tag": "Cognitive Layer", "desc": "Add autonomous multi-step reasoning to your automated business workflows."},
            {"title": "Business Process Automation Service", "link": "services/business-process-automation.html", "tag": "Service Domain", "desc": "Explore our commercial BPA implementation and workflow engineering services."}
        ]
    },
    {
        "rel_path": "technology/iot.html",
        "category_badge": "TECHNOLOGY PLATFORM ARCHITECTURE",
        "page_title": "Internet of Things (IoT)",
        "page_subtitle": "Connected devices and sensors, device and asset data, real-time telemetry, equipment monitoring, IoT data visualization, and edge and cloud integration.",
        "seo_desc": "Nova Arc IoT Technology Architecture: Industrial sensor ingestion, MQTT brokers, edge-to-cloud security, and real-time telemetry processing.",
        "breadcrumbs": [("Home", "index.html"), ("Technology", "technology.html"), ("Internet of Things (IoT)", None)],
        "overview_paragraphs": [
            "Connecting physical industrial machinery, warehouse facilities, and mobile vehicle fleets to modern cloud systems requires robust hardware integration, reliable communication protocols, and strict edge cybersecurity.",
            "Nova Arc's Internet of Things (IoT) technology architecture bridges physical operations with cloud intelligence. We build high-throughput telemetry pipelines that ingest sensor data via MQTT, CoAP, HTTP, and industrial Modbus/OPC-UA protocols.",
            "Our edge-to-cloud architecture incorporates local edge caching to protect against network outages, hardware-level encryption (mTLS) to secure data transmission, and scalable time-series databases that process millions of telemetry events per minute."
        ],
        "capabilities": [
            {"title": "Lightweight Edge Protocols", "desc": "Support for MQTT, CoAP, and WebSockets optimized for low-bandwidth cellular and satellite telemetry transmission.", "points": ["Low-overhead binary payloads", "QoS delivery guarantees", "Topic-based pub/sub hierarchy", "Low-power battery sensor support"]},
            {"title": "Edge Gateway Computing", "desc": "Industrial edge gateways executing local data filtering, protocol translation (Modbus to MQTT), and offline caching.", "points": ["Local buffer during network drops", "Edge anomaly pre-filtering", "Protocol translation engines", "Secure OTA firmware updates"]},
            {"title": "Time-Series Data Ingestion", "desc": "High-throughput cloud storage clusters optimized for querying and storing billions of sequential sensor measurements.", "points": ["High write-concurrency databases", "Automated data downsampling", "Long-term cold storage tiering", "Sub-second analytical queries"]},
            {"title": "Device Security & Management", "desc": "Zero-trust device authentication using individual cryptographic certificates, mutual TLS (mTLS), and remote provisioning.", "points": ["mTLS encrypted transmission", "Unique cryptographic device IDs", "Revocation & rotation policies", "Vulnerability patch monitoring"]}
        ],
        "challenges": [
            {"challenge": "Intermittent Network Outages", "impact": "Telemetry packets dropped during remote cellular or Wi-Fi interruptions, creating blind spots in compliance records.", "solution": "Our edge gateways maintain persistent local disk buffers, automatically back-filling historical telemetry once connection restores."},
            {"challenge": "High Telemetry Data Costs", "impact": "Transmitting raw, uncompressed high-frequency sensor readings over cellular networks creates astronomical data bills.", "solution": "We implement edge deadband filtering and Delta compression, transmitting updates only when values deviate from established baselines."},
            {"challenge": "Hardware Protocol Incompatibility", "impact": "Legacy PLCs and modern smart sensors operate on different communication standards that cannot share a bus.", "solution": "Our protocol translation layer converts analog inputs, RS-485 serial data, and modern IP telemetry into uniform JSON schemas."}
        ],
        "workflow_steps": [
            {"step": "01", "title": "Sensor & RF Topology Survey", "desc": "Auditing sensor electrical interfaces, ambient temperature ranges, battery requirements, and network coverage."},
            {"step": "02", "title": "Edge Gateway Deployment", "desc": "Installing edge gateway hardware, configuring protocol translation rules, local buffer sizes, and mTLS security."},
            {"step": "03", "title": "Cloud Broker & Ingestion Setup", "desc": "Deploying high-concurrency MQTT brokers, message routing pipelines, and time-series analytical databases."},
            {"step": "04", "title": "Calibration & Verification", "desc": "Benchmarking sensor telemetry against calibrated physical gauges, verifying failover buffers, and going live."}
        ],
        "outcomes": [
            {"title": "100% Data Completeness", "desc": "Local edge caching guarantees zero telemetry data loss during network dropouts or server maintenance."},
            {"title": "Sub-Second Incident Detection", "desc": "Stream real-time sensor measurements directly to control room dashboards with latency under 500 milliseconds."},
            {"title": "70% Lower Cellular Data Costs", "desc": "Edge compression and deadband filtering transmit only meaningful operational changes, minimizing network overhead."},
            {"title": "Enterprise Cybersecurity", "desc": "Protect operational assets with individual cryptographic device certificates and encrypted communication channels."}
        ],
        "related_links": [
            {"title": "Real-Time Monitoring & Dashboards", "link": "services/real-time-monitoring.html", "tag": "Operational Console", "desc": "Visualize incoming IoT telemetry streams on live control room displays."},
            {"title": "Data Analytics & Intelligence", "link": "technology/data-analytics.html", "tag": "Analytical Engine", "desc": "Apply predictive maintenance modeling and anomaly detection to sensor data."},
            {"title": "Manufacturing & Industrial Operations", "link": "industries/manufacturing.html", "tag": "Industry Focus", "desc": "Industrial IoT implementations for factories, production lines, and warehouses."}
        ]
    },
    {
        "rel_path": "technology/enterprise-integration.html",
        "category_badge": "TECHNOLOGY PLATFORM ARCHITECTURE",
        "page_title": "Enterprise Integration",
        "page_subtitle": "API integrations, third-party system connectivity, data synchronization, application interoperability, enterprise system modernization, and secure access and permissions.",
        "seo_desc": "Nova Arc Enterprise Integration Architecture: High-performance REST/GraphQL API gateways, event-driven data buses, and ERP/CRM interoperability.",
        "breadcrumbs": [("Home", "index.html"), ("Technology", "technology.html"), ("Enterprise Integration", None)],
        "overview_paragraphs": [
            "Modern enterprises rely on dozens of best-of-breed software tools across sales, finance, human resources, logistics, and supply chain. When these systems fail to communicate, business velocity grinds to a halt.",
            "Nova Arc's Enterprise Integration architecture establishes a resilient, unified communication layer across disparate cloud services, internal databases, and external partner APIs. We engineer secure REST and GraphQL API gateways, message-driven event buses, and bidirectional data connectors.",
            "Our integration designs enforce transactional data consistency, automated retry logic with exponential backoff, granular API access control, and comprehensive auditability—eliminating operational silos while protecting system stability."
        ],
        "capabilities": [
            {"title": "API Gateways (REST & GraphQL)", "desc": "High-throughput API management layer providing centralized authentication, rate limiting, and request transformation.", "points": ["OpenAPI / Swagger documentation", "Token-based OAuth2 security", "Rate limiting & DDoS protection", "Response caching & compression"]},
            {"title": "Bidirectional Data Buses", "desc": "Event-driven synchronization buses linking ERPs, CRMs, and custom databases to maintain real-time data consistency.", "points": ["Asynchronous message queues", "Automatic conflict resolution", "ACID transactional boundaries", "Data deduplication & normalization"]},
            {"title": "Third-Party SaaS Connectors", "desc": "Pre-built and bespoke connectors integrating enterprise platforms with payment gateways, carriers, and cloud providers.", "points": ["Carrier shipping APIs", "Banking & payment gateways", "Identity provider integration (SSO)", "Tax calculation services"]},
            {"title": "Enterprise Security & Governance", "desc": "Strict security controls enforcing least-privilege API permissions, payload encryption, and immutable audit logging.", "points": ["Field-level access permissions", "Mutual TLS (mTLS) connectivity", "Complete API request audit logs", "Automated secret rotation"]}
        ],
        "challenges": [
            {"challenge": "Fragile Point-to-Point Connections", "impact": "Direct spaghetti integrations between individual applications break whenever any single vendor updates an API endpoint.", "solution": "Our decoupled message bus middleware isolates applications from API changes and provides standardized translation adapters."},
            {"challenge": "Data Discrepancies Between Systems", "impact": "Customer addresses or financial transactions updated in CRM fail to reflect in ERP, causing shipping and billing errors.", "solution": "We implement event-driven synchronization with transactional rollback guarantees that ensure all systems reflect identical records."},
            {"challenge": "Unmonitored Third-Party Outages", "impact": "A third-party payment or shipping API outage halts internal orders, creating customer chaos.", "solution": "Our asynchronous queues buffer outgoing transactions during third-party downtime, automatically re-attempting delivery once the service recovers."}
        ],
        "workflow_steps": [
            {"step": "01", "title": "Integration Landscape Mapping", "desc": "Cataloging applications, data schemas, API protocols, transaction volumes, and latency requirements."},
            {"step": "02", "title": "Data Schema & Bus Design", "desc": "Designing canonical data models, event schemas, API gateway policies, and conflict resolution rules."},
            {"step": "03", "title": "Connector Development", "desc": "Engineering secure API endpoints, webhook listeners, asynchronous message queues, and error-handling routines."},
            {"step": "04", "title": "Load Testing & Go-Live", "desc": "Executing high-concurrency transaction tests, verifying rollback safety, and deploying 24/7 API monitoring."}
        ],
        "outcomes": [
            {"title": "Single Source of Truth", "desc": "Ensure customer, inventory, and financial records stay synchronized in real time across all software tools."},
            {"title": "Zero Lost Transactions", "desc": "Asynchronous message buffering guarantees that temporary partner API outages never result in dropped orders."},
            {"title": "Eliminated Manual Re-Keying", "desc": "Automate data transfer between sales, operations, and accounting to eliminate human transcription mistakes."},
            {"title": "Rapid System Onboarding", "desc": "Modular API gateway architecture allows new software tools to be plugged in without disrupting existing applications."}
        ],
        "related_links": [
            {"title": "Intelligent Automation", "link": "technology/intelligent-automation.html", "tag": "Workflow Layer", "desc": "Trigger automated cross-system actions across integrated enterprise APIs."},
            {"title": "Data Analytics & Intelligence", "link": "technology/data-analytics.html", "tag": "Analytical Layer", "desc": "Aggregate data from multiple APIs into unified business intelligence dashboards."},
            {"title": "Enterprise Business Solutions", "link": "services/enterprise-business.html", "tag": "Service Domain", "desc": "Commercial integration services for CRM, HRMS, and enterprise business software."}
        ]
    },
    {
        "rel_path": "technology/data-analytics.html",
        "category_badge": "TECHNOLOGY PLATFORM ARCHITECTURE",
        "page_title": "Data Analytics & Operational Intelligence",
        "page_subtitle": "Operational dashboards, KPI monitoring, trend analysis, reporting and visualization, anomaly detection where supported, and data-informed business decisions.",
        "seo_desc": "Nova Arc Data Analytics & Operational Intelligence: Real-time KPI dashboards, automated reporting pipelines, statistical trend modeling, and decision analytics.",
        "breadcrumbs": [("Home", "index.html"), ("Services", "services.html"), ("Technology", "technology.html"), ("Data Analytics", None)],
        "overview_paragraphs": [
            "Modern enterprises capture massive volumes of transactional, telemetry, and customer data, but often struggle to extract actionable insights that improve daily operations and bottom-line margins.",
            "Nova Arc's Data Analytics & Operational Intelligence technology platform transforms raw data into real-time operational clarity. We design automated data extraction, transformation, and loading (ETL) pipelines feeding centralized analytical data warehouses.",
            "Our platforms deliver interactive executive dashboards, statistical trend analysis, automated report exports, and anomaly detection where supported by data, empowering leadership to make fast, evidence-based operational decisions."
        ],
        "capabilities": [
            {"title": "Interactive Operational Dashboards", "desc": "Dynamic visual consoles displaying real-time business KPIs, department performance metrics, and operational throughput.", "points": ["Drill-down interactive charts", "Customizable executive views", "Mobile-optimized reporting", "Real-time query acceleration"]},
            {"title": "Automated ETL & Data Warehousing", "desc": "Scalable data ingestion pipelines extracting data from ERPs, CRMs, IoT brokers, and web databases into structured data warehouses.", "points": ["Automated scheduled ETL jobs", "Data deduplication & cleansing", "Normalized relational schemas", "High-concurrency analytical queries"]},
            {"title": "Statistical Trend & Variance Analysis", "desc": "Longitudinal modeling evaluating sales velocities, inventory turnover, machine degradation, and customer retention trends.", "points": ["Seasonal variance modeling", "Year-over-year comparative views", "Lead time distribution analysis", "Cohort retention tracking"]},
            {"title": "Automated Operational Reporting", "desc": "Scheduled generation and distribution of PDF and Excel briefings to department heads and executive stakeholders.", "points": ["Automated email report delivery", "Pixel-perfect PDF exports", "Role-based report filtering", "Audit compliance records"]}
        ],
        "challenges": [
            {"challenge": "Scattered & Inconsistent Reports", "impact": "Different departments generate conflicting revenue or inventory metrics using disconnected spreadsheets.", "solution": "We establish a single source of truth through unified data warehouse schemas with standardized KPI definitions across the organization."},
            {"challenge": "Slow Query Performance", "impact": "Running business intelligence reports directly on production transactional databases slows down live operations.", "solution": "Our architectures separate transactional databases from analytical data warehouses, ensuring zero impact on live customer operations."},
            {"challenge": "Lagging Rearview Analytics", "impact": "Waiting for monthly financial closes leaves leadership unaware of operational issues until weeks after they occur.", "solution": "We deploy real-time and daily automated ETL pipelines that provide leadership with current operational performance data."}
        ],
        "workflow_steps": [
            {"step": "01", "title": "KPI & Metric Definition", "desc": "Identifying core business metrics, data sources, update frequencies, and stakeholder reporting requirements."},
            {"step": "02", "title": "Data Pipeline Architecture", "desc": "Configuring automated ETL pipelines, data cleansing rules, analytical database schemas, and aggregation queries."},
            {"step": "03", "title": "Dashboard & Visualization Design", "desc": "Developing interactive visualization widgets, role-based security filters, and automated report generators."},
            {"step": "04", "title": "Validation & Deployment", "desc": "Verifying calculation precision against financial ledgers, conducting executive training, and deploying 24/7."}
        ],
        "outcomes": [
            {"title": "Evidence-Based Decisions", "desc": "Replace guesswork with verifiable historical trend data and real-time operational performance metrics."},
            {"title": "Eliminated Data Silos", "desc": "View consolidated business performance across sales, operations, inventory, and finance in a single console."},
            {"title": "Zero Production Impact", "desc": "Execute complex analytical queries on dedicated data warehouses without slowing down customer checkout or ERP systems."},
            {"title": "Automated Executive Briefings", "desc": "Receive automated daily and weekly operational performance reports directly in your inbox without manual preparation."}
        ],
        "related_links": [
            {"title": "Enterprise Integration", "link": "technology/enterprise-integration.html", "tag": "Data Layer", "desc": "Extract and synchronize data from core enterprise applications into analytical pipelines."},
            {"title": "Real-Time Monitoring", "link": "services/real-time-monitoring.html", "tag": "Live Console", "desc": "Sub-second telemetry displays for active control room operations."},
            {"title": "Operational Analytics Service", "link": "services/operational-analytics.html", "tag": "Service Domain", "desc": "Discover our commercial operational analytics and KPI consulting services."}
        ]
    },

    # -------------------------------------------------------------
    # INDUSTRIES SUBPAGES (6 Pages)
    # -------------------------------------------------------------
    {
        "rel_path": "industries/foodtech.html",
        "category_badge": "TARGET INDUSTRY FOCUS",
        "page_title": "FoodTech & Food Distribution",
        "page_subtitle": "Digital food commerce, supplier coordination, procurement, inventory management, batch and expiry traceability, and cold chain distribution workflows.",
        "seo_desc": "Nova Arc FoodTech & Food Distribution Solutions: Digital ordering, cold chain telemetry, multi-kitchen inventory coordination, and batch traceability.",
        "breadcrumbs": [("Home", "index.html"), ("Industries", "industries.html"), ("FoodTech & Food Distribution", None)],
        "overview_paragraphs": [
            "Food producers, commercial commissaries, and wholesale food distributors operate in a high-velocity environment defined by perishable shelf lives, strict temperature controls, complex recipe yields, and tight regulatory scrutiny.",
            "Nova Arc delivers tailored technology solutions for FoodTech and food distribution enterprises. We build digital ordering portals, automated First-Expired, First-Out (FEFO) inventory tracking systems, commissary demand planning tools, and real-time cold chain telemetry networks.",
            "Our platforms connect agricultural suppliers, central production kitchens, and multi-location retail distribution nodes, helping food businesses eliminate spoilage, maintain complete food safety compliance, and operate with maximum margin efficiency."
        ],
        "capabilities": [
            {"title": "Digital Food Ordering & B2B Portals", "desc": "Wholesale digital ordering portals with customer-specific pricing, standing recurring orders, and delivery cutoff management.", "points": ["Customer-tier pricing", "Standing order templates", "Delivery cutoff enforcement", "Mobile order placement"]},
            {"title": "FEFO Inventory & Batch Traceability", "desc": "Automated inventory management tracking lot numbers, harvest dates, and expiration to ensure proper stock rotation.", "points": ["Automated FEFO picking", "Perishable shelf-life alerts", "Batch recall search tools", "Spoilage reduction analytics"]},
            {"title": "Cold Chain IoT Telemetry Monitoring", "desc": "Continuous temperature and humidity tracking across walk-in freezers, holding staging, and refrigerated delivery vehicles.", "points": ["Continuous thermal logging", "Excursion threshold alerts", "Automated HACCP logs", "Wireless sensor integration"]},
            {"title": "Commissary & Recipe Yield Management", "desc": "Connecting central production kitchens with ingredient procurement, recipe scaling, and multi-unit restaurant distribution.", "points": ["Yield & batch costing", "Automated ingredient POs", "Inter-unit stock transfers", "Finished goods packing"]}
        ],
        "challenges": [
            {"challenge": "Perishable Spoilage & Margin Loss", "impact": "Manual inventory rotation results in forgotten batches expiring in warehouse corners, destroying gross margins.", "solution": "Our FEFO inventory logic directs warehouse pickers to oldest compliant lots first, sending automated alerts on expiring inventory."},
            {"challenge": "Complex Food Safety Recalls", "impact": "Locating contaminated ingredients using paper records takes days, increasing consumer liability and brand damage.", "solution": "We provide instant forward and backward traceability reports that identify every customer who received a specific lot in seconds."},
            {"challenge": "Manual Temperature Log Compliance", "impact": "Employees falsify or forget manual clipboard temperature logs, risking health inspection violations and fines.", "solution": "We deploy automated IoT temperature sensors that record tamper-proof HACCP compliance logs 24/7 without human intervention."}
        ],
        "workflow_steps": [
            {"step": "01", "title": "Supply Chain & Facility Audit", "desc": "Assessing kitchen workflows, cold storage locations, ingredient turnover velocities, and regulatory standards."},
            {"step": "02", "title": "System Architecture Design", "desc": "Configuring recipe databases, FEFO picking rules, customer portal pricing tiers, and sensor network topologies."},
            {"step": "03", "title": "Deployment & IoT Installation", "desc": "Installing cold chain sensors, deploying the digital ordering portal, and integrating with existing accounting ERPs."},
            {"step": "04", "title": "Staff Training & Go-Live", "desc": "Training kitchen supervisors and warehouse pickers on mobile barcode scanning and automated reordering."}
        ],
        "outcomes": [
            {"title": "30%+ Reduction in Spoilage", "desc": "Automated FEFO rotation and proactive expiry warnings eliminate preventable perishable food waste."},
            {"title": "Instant Recall Compliance", "desc": "Generate complete regulatory lot trace reports across suppliers and customers within seconds."},
            {"title": "Automated HACCP Record Keeping", "desc": "Maintain continuous, auditable digital temperature records that satisfy health inspectors."},
            {"title": "Accelerated Wholesale Ordering", "desc": "Enable commercial food buyers to submit orders and re-orders 24/7 through dedicated digital portals."}
        ],
        "related_links": [
            {"title": "FoodTech Solutions Service", "link": "services/foodtech.html", "tag": "Core Service", "desc": "Explore our dedicated food ordering, inventory, and traceability services."},
            {"title": "Supply Chain & Procurement", "link": "solutions/supply-chain.html", "tag": "Related Solution", "desc": "End-to-end inventory visibility and vendor procurement architectures."},
            {"title": "Intelligent Monitoring & IoT", "link": "services/intelligent-monitoring.html", "tag": "Related Domain", "desc": "Continuous environmental and temperature telemetry systems."}
        ]
    },
    {
        "rel_path": "industries/retail-ecommerce.html",
        "category_badge": "TARGET INDUSTRY FOCUS",
        "page_title": "Retail & Digital Commerce",
        "page_subtitle": "Digital storefronts, B2B/B2C commerce platforms, catalog management, customer portals, order fulfillment, and inventory integration.",
        "seo_desc": "Nova Arc Retail & Digital Commerce Solutions: Omnichannel commerce portals, catalog management, real-time inventory synchronization, and fulfillment workflows.",
        "breadcrumbs": [("Home", "index.html"), ("Industries", "industries.html"), ("Retail & Digital Commerce", None)],
        "overview_paragraphs": [
            "Modern retail and consumer brands face intense competition, shifting consumer expectations, and complex supply chain logistics across multiple physical and digital sales channels.",
            "Nova Arc engineers high-performance Retail & Digital Commerce solutions that unify online storefronts, retail point-of-sale systems, warehouse inventory, and fulfillment operations into a single synchronized digital ecosystem.",
            "We build blazing-fast mobile-responsive web storefronts, specialized B2B wholesale portals, dynamic pricing engines, and real-time inventory allocation tools that eliminate stockouts and maximize customer lifetime value."
        ],
        "capabilities": [
            {"title": "Unified Omnichannel Storefronts", "desc": "High-performance digital commerce platforms supporting both direct-to-consumer (B2C) and wholesale (B2B) purchasing.", "points": ["Sub-second page speeds", "Faceted product catalog search", "One-click mobile checkout", "Unified cart across devices"]},
            {"title": "Dynamic Product Information (PIM)", "desc": "Centralized catalog management supporting millions of SKUs, complex variants, digital assets, and localized pricing.", "points": ["Attribute variant modeling", "Automated currency & tax rules", "Batch CSV/API catalog sync", "Digital asset management"]},
            {"title": "Real-Time Multi-Node Inventory Sync", "desc": "Bidirectional synchronization tying storefront stock displays directly to physical warehouse and store inventory.", "points": ["Virtual inventory pooling", "Safety stock reservations", "Nearest-store fulfillment", "Backorder management"]},
            {"title": "Fulfillment & Carrier Integration", "desc": "Automated order routing to regional fulfillment centers, shipping carrier rate comparison, and live tracking updates.", "points": ["Split shipment routing", "Carrier label generation", "Real-time customer SMS tracking", "Returns & exchange portal"]}
        ],
        "challenges": [
            {"challenge": "Checkout Latency & High Cart Abandonment", "impact": "Bloated checkout funnels and slow load times frustrate mobile shoppers, causing lost retail revenue.", "solution": "We engineer streamlined, microservices-driven checkout experiences with tokenized payment processing and instant address lookup."},
            {"challenge": "Overselling & Out-of-Stock Cancellations", "impact": "Selling items online that are physically out of stock in warehouses leads to cancelled orders and angry customers.", "solution": "Our platforms enforce sub-second inventory reservation at checkout, ensuring items displayed as available are physically in stock."},
            {"challenge": "High Return & Exchange Costs", "impact": "Manual returns processing drains customer service bandwidth and delays restocking returned merchandise.", "solution": "We implement self-service customer returns portals that generate prepaid return labels and initiate exchanges automatically."}
        ],
        "workflow_steps": [
            {"step": "01", "title": "Commerce Architecture Audit", "desc": "Analyzing traffic patterns, SKU complexity, payment requirements, and existing ERP/WMS back-end tools."},
            {"step": "02", "title": "UX & Pipeline Engineering", "desc": "Designing high-converting mobile interfaces, fast catalog search clusters, and payment gateway integrations."},
            {"step": "03", "title": "Inventory & ERP Connectivity", "desc": "Connecting real-time stock feeds, warehouse picking queues, and shipping carrier label APIs."},
            {"step": "04", "title": "Concurrency Testing & Launch", "desc": "Conducting peak holiday traffic load testing, security audits, and executing zero-downtime cutover."}
        ],
        "outcomes": [
            {"title": "Higher Checkout Conversion", "desc": "Accelerated page load speeds and friction-free mobile checkouts directly increase completed purchases."},
            {"title": "Zero Overselling Incidents", "desc": "Real-time inventory reservation prevents customers from purchasing depleted stock."},
            {"title": "Lower Fulfillment Costs", "desc": "Intelligent order routing chooses the closest warehouse with complete stock, reducing shipping costs and transit times."},
            {"title": "Seamless Self-Service Returns", "desc": "Automate customer return label generation and inventory restocking without manual customer support intervention."}
        ],
        "related_links": [
            {"title": "Digital Commerce Platforms", "link": "services/digital-commerce-platforms.html", "tag": "Core Service", "desc": "B2B and B2C custom storefront engineering and catalog management."},
            {"title": "Digital Commerce Solutions", "link": "solutions/digital-commerce.html", "tag": "Parent Solution", "desc": "Comprehensive digital commerce and fulfillment architectures."},
            {"title": "Logistics & Distribution", "link": "services/logistics.html", "tag": "Related Service", "desc": "Carrier shipping integrations, route planning, and delivery tracking."}
        ]
    },
    {
        "rel_path": "industries/manufacturing.html",
        "category_badge": "TARGET INDUSTRY FOCUS",
        "page_title": "Manufacturing & Industrial Operations",
        "page_subtitle": "Industrial IoT monitoring, connected equipment, operational dashboards, event-driven alerts, predictive maintenance, and process automation.",
        "seo_desc": "Nova Arc Manufacturing & Industrial Operations: Industrial IoT telemetry, equipment condition monitoring, OEE dashboards, and automated maintenance workflows.",
        "breadcrumbs": [("Home", "index.html"), ("Industries", "industries.html"), ("Manufacturing & Industrial", None)],
        "overview_paragraphs": [
            "Modern manufacturing and heavy industrial plants operate under demanding production schedules where unexpected equipment downtime and quality defects can cost millions of dollars in lost throughput.",
            "Nova Arc engineers industrial-grade technology solutions for manufacturing plants and processing facilities. We deploy non-invasive IoT telemetry sensors, real-time Overall Equipment Effectiveness (OEE) dashboards, and automated incident escalation workflows.",
            "Our platforms connect factory-floor machinery, programmable logic controllers (PLCs), and maintenance management systems into a cohesive operational intelligence layer, enabling proactive maintenance and peak operational availability."
        ],
        "capabilities": [
            {"title": "Industrial IoT Telemetry Ingestion", "desc": "Connecting vibration, thermal, pressure, current, and RPM sensors across diverse manufacturing machinery.", "points": ["Modbus, OPC-UA & MQTT support", "Non-invasive sensor installation", "Edge telemetry filtering", "Encrypted transmission"]},
            {"title": "Real-Time OEE & Plant Dashboards", "desc": "Live production line monitoring tracking availability, performance efficiency, and quality yield rates in real time.", "points": ["Live OEE calculation", "Line throughput tracking", "Scrap & defect percentage metrics", "Multi-plant comparative views"]},
            {"title": "Condition-Based Predictive Maintenance", "desc": "Statistical analysis of sensor telemetry detecting mechanical wear and component degradation before breakdown occurs.", "points": ["Dynamic baseline anomaly alerts", "Vibration harmonic analysis", "Bearing & motor degradation models", "Optimal service window timing"]},
            {"title": "Automated Maintenance Dispatch", "desc": "Event-driven integration that creates CMMS work orders and dispatches technicians immediately when anomalies occur.", "points": ["Automated CMMS work orders", "Telemetry diagnostics attachment", "Technician skill-based routing", "Resolution audit logs"]}
        ],
        "challenges": [
            {"challenge": "Catastrophic Unplanned Downtime", "impact": "A critical motor or gearbox breaks down unexpectedly, halting the entire assembly line for hours.", "solution": "We deploy vibration and thermal sensors that identify anomalous bearing wear weeks in advance, allowing planned repairs during scheduled downtime."},
            {"challenge": "Inaccurate Manual Shift Logs", "impact": "Operators estimate line stoppage causes on paper at the end of shifts, leading to inaccurate operational data.", "solution": "Our IoT monitoring tracks machine start/stop times and cycle speeds automatically with second-by-second precision."},
            {"challenge": "Alarm Fatigue & Ignored Alerts", "impact": "Local machine panels sound dozens of nuisance alarms daily, causing operators to disable or ignore warnings.", "solution": "Our intelligent monitoring filters transient noise and escalates only confirmed, multi-condition threshold excursions to supervisors."}
        ],
        "workflow_steps": [
            {"step": "01", "title": "Plant & Asset Survey", "desc": "Cataloging critical production machinery, failure history, electrical interfaces, and factory network infrastructure."},
            {"step": "02", "title": "Edge Gateway Deployment", "desc": "Installing industrial edge gateways, sensor arrays, and secure local network data buses."},
            {"step": "03", "title": "OEE & Alert Configuration", "desc": "Configuring OEE calculation formulas, anomaly thresholds, and automated CMMS work order integration."},
            {"step": "04", "title": "Plant Floor Go-Live", "desc": "Deploying control room monitors, training plant supervisors, and validating automated alerting protocols."}
        ],
        "outcomes": [
            {"title": "20-30% Reduction in Downtime", "desc": "Proactive condition-based maintenance prevents unexpected machine failures and assembly line stoppages."},
            {"title": "Increased Plant OEE", "desc": "Real-time bottleneck identification allows supervisors to optimize machine cycle speeds and reduce idle time."},
            {"title": "Extended Machine Lifespans", "desc": "Operating machinery within optimal thermal and vibration parameters prevents severe mechanical damage."},
            {"title": "Complete Digital Plant Visibility", "desc": "Executive leadership gains accurate, real-time insight into production throughput across all manufacturing facilities."}
        ],
        "related_links": [
            {"title": "IoT & Device Integration", "link": "services/iot-integration.html", "tag": "Core Technology", "desc": "Industrial sensor connectivity, MQTT brokers, and edge telemetry ingestion."},
            {"title": "Real-Time Monitoring & Dashboards", "link": "services/real-time-monitoring.html", "tag": "Core Service", "desc": "Sub-second operational control centers and equipment health visualization."},
            {"title": "Intelligent Monitoring Solutions", "link": "solutions/intelligent-monitoring.html", "tag": "Parent Solution", "desc": "Explore complete operational telemetry and incident automation architectures."}
        ]
    },
    {
        "rel_path": "industries/logistics.html",
        "category_badge": "TARGET INDUSTRY FOCUS",
        "page_title": "Logistics & Supply Chain",
        "page_subtitle": "Shipment visibility, warehouse management, supplier collaboration, procurement workflows, logistics analytics, and dispatch coordination.",
        "seo_desc": "Nova Arc Logistics & Supply Chain Solutions: Fleet dispatch coordination, real-time freight tracking, dock appointment scheduling, and warehouse management.",
        "breadcrumbs": [("Home", "index.html"), ("Industries", "industries.html"), ("Logistics & Supply Chain", None)],
        "overview_paragraphs": [
            "Third-party logistics providers (3PLs), freight carriers, and distribution enterprises face escalating fuel costs, driver shortages, warehouse dock congestion, and customer demands for real-time shipment transparency.",
            "Nova Arc develops mission-critical technology solutions for logistics and supply chain operations. We build Transportation Management Systems (TMS), dynamic route optimization engines, warehouse appointment scheduling platforms, and freight visibility portals.",
            "By connecting GPS fleet telematics, warehouse picking queues, and carrier EDI networks, our platforms lower transportation overhead, reduce truck detention penalties, and ensure freight arrives safely and on schedule."
        ],
        "capabilities": [
            {"title": "Real-Time Freight & Fleet Tracking", "desc": "Centralized visibility integrating commercial ELD devices, GPS telematics, and carrier APIs to report live shipment milestones.", "points": ["Live GPS map tracking", "Geofence arrival/departure alerts", "Dynamic ETA calculation", "Customer tracking portals"]},
            {"title": "Dynamic Route Planning & Optimization", "desc": "Algorithmic routing engines that evaluate vehicle capacity, delivery time windows, traffic patterns, and driver hours of service.", "points": ["Multi-stop route sequencing", "Vehicle cube & weight optimization", "Turn-by-turn route compliance", "Mobile driver dispatch app"]},
            {"title": "Warehouse Dock Appointment Scheduling", "desc": "Digital self-service portal for carriers to schedule dock loading/unloading appointments based on warehouse labor availability.", "points": ["Online dock appointment booking", "Labor capacity leveling", "Driver check-in kiosks", "Detention fee mitigation"]},
            {"title": "Electronic Proof of Delivery (ePOD)", "desc": "Mobile driver capture for electronic signatures, cargo condition photos, barcode scans, and exception notes.", "points": ["Digital signature capture", "Timestamped photo verification", "Shortage & damage exception logging", "Instant billing triggers"]}
        ],
        "challenges": [
            {"challenge": "Costly Dock Detention Fees", "impact": "Trucks arriving unannounced create dock congestion, forcing carriers to wait hours and bill substantial detention fees.", "solution": "Our dock scheduling portal requires carriers to book appointment slots that align with warehouse labor capacity, eliminating congestion."},
            {"challenge": "Sub-Optimal Delivery Routes", "impact": "Drivers follow inefficient routes or get stuck in avoidable traffic, wasting fuel and missing delivery windows.", "solution": "Our dynamic routing algorithms optimize multi-stop delivery sequences in real time, reducing total fleet mileage by 15%+."},
            {"challenge": "Delayed Invoicing from Lost Proof of Delivery", "impact": "Paper delivery slips get misplaced by drivers, delaying invoicing by weeks and strangling cash flow.", "solution": "Our mobile driver app captures electronic signatures and delivery photos, triggering customer invoicing within minutes of delivery."}
        ],
        "workflow_steps": [
            {"step": "01", "title": "Fleet & Network Assessment", "desc": "Analyzing fleet size, freight corridors, carrier agreements, dock capacities, and existing TMS/WMS software."},
            {"step": "02", "title": "Routing & Portal Architecture", "desc": "Configuring route optimization algorithms, dock appointment calendars, and carrier rate comparison tools."},
            {"step": "03", "title": "ELD & Carrier Integration", "desc": "Connecting commercial ELD feeds, GPS telematics, carrier EDI/API networks, and ERP sales orders."},
            {"step": "04", "title": "Driver Rollout & Go-Live", "desc": "Deploying the mobile driver application, training warehouse dock staff, and launching public tracking portals."}
        ],
        "outcomes": [
            {"title": "15-20% Lower Fleet Fuel Costs", "desc": "Optimized delivery routing reduces total fleet mileage and eliminates redundant transit loops."},
            {"title": "Eliminated Detention Penalties", "desc": "Scheduled dock appointments ensure trucks are unloaded promptly upon arrival, avoiding carrier detention fees."},
            {"title": "Instant Invoicing Upon Delivery", "desc": "Electronic proof of delivery (ePOD) uploads instantly to trigger billing within minutes of customer handoff."},
            {"title": "95%+ On-Time Delivery Rates", "desc": "Proactive route optimization and traffic adaptation help fleets consistently meet strict customer delivery windows."}
        ],
        "related_links": [
            {"title": "Logistics & Distribution Service", "link": "services/logistics.html", "tag": "Core Service", "desc": "Explore our dedicated transportation management and shipment tracking services."},
            {"title": "Supply Chain Management", "link": "services/supply-chain-management.html", "tag": "Core Service", "desc": "Multi-warehouse inventory optimization and automated replenishment."},
            {"title": "Supply Chain & Procurement Solutions", "link": "solutions/supply-chain.html", "tag": "Parent Solution", "desc": "Comprehensive supply chain visibility and procurement workflows."}
        ]
    },
    {
        "rel_path": "industries/enterprise.html",
        "category_badge": "TARGET INDUSTRY FOCUS",
        "page_title": "Enterprise & Professional Services",
        "page_subtitle": "CRM, HRMS, business process automation, custom enterprise applications, and connected business systems for corporate and consulting firms.",
        "seo_desc": "Nova Arc Enterprise & Professional Services Solutions: Modern CRM, HRMS, approval workflow automation, custom enterprise applications, and data connectivity.",
        "breadcrumbs": [("Home", "index.html"), ("Industries", "industries.html"), ("Enterprise & Professional Services", None)],
        "overview_paragraphs": [
            "Corporate enterprises, consulting organizations, legal practices, and financial service firms depend on the intellect and efficiency of their professional staff to deliver high-value client outcomes.",
            "Nova Arc engineers specialized Enterprise & Professional Services technology solutions that eliminate internal administrative friction, automate client onboarding, and unify core business operations.",
            "We build tailored CRM platforms for complex client engagements, modern HRMS platforms for workforce management, policy-driven approval workflows, and centralized executive reporting dashboards that drive corporate profitability."
        ],
        "capabilities": [
            {"title": "Client Relationship Management (CRM)", "desc": "Managing multi-touch corporate client accounts, complex engagement proposals, contract milestones, and executive relationships.", "points": ["Corporate account hierarchies", "Engagement proposal tracking", "Billing milestone schedules", "Executive contact history"]},
            {"title": "Workforce & HRMS Platforms", "desc": "Digital employee onboarding, skill-based project assignment, leave tracking, and performance evaluations.", "points": ["Digital onboarding checklists", "Skill & certification tracking", "Automated leave approval logic", "Employee self-service portals"]},
            {"title": "Automated Approval Hierarchies", "desc": "Multi-tier approval workflows for contracts, client billing adjustments, expense reports, and capital expenditures.", "points": ["Threshold-based approval routing", "Mobile one-click authorization", "SLA escalation timers", "Audit-ready decision records"]},
            {"title": "Executive Business Intelligence", "desc": "Consolidated dashboards reporting billable utilization, project margin profitability, and forward-looking revenue forecasts.", "points": ["Billable utilization metrics", "Project margin analytics", "Weighted pipeline forecasting", "Multi-department P&L views"]}
        ],
        "challenges": [
            {"challenge": "Disconnected Client Engagement Data", "impact": "Consultants lack visibility into billing disputes, while billing teams are unaware of completed project deliverables.", "solution": "We connect your CRM, time-tracking, and accounting systems into a single unified client engagement portal."},
            {"challenge": "Administrative Overhead on Fee Earners", "impact": "Senior consultants and attorneys spend 20%+ of their working hours on administrative paperwork and timesheets.", "solution": "Our BPA platforms automate routine document intake, contract routing, and timesheet reminders, restoring billable capacity."},
            {"challenge": "Opaque Project Profitability", "impact": "Leadership discovers project cost overruns only after engagements are completed and invoices are disputed.", "solution": "Our operational analytics consoles track labor hours and project expenses in real time against contract milestones."}
        ],
        "workflow_steps": [
            {"step": "01", "title": "Operational Assessment", "desc": "Reviewing existing billing workflows, engagement lifecycles, software tools, and compliance requirements."},
            {"step": "02", "title": "Solution Architecture", "desc": "Designing unified client data schemas, approval hierarchies, employee portals, and executive dashboard views."},
            {"step": "03", "title": "Development & Integration", "desc": "Engineering custom CRM/HRMS modules, workflow automation triggers, and accounting system sync."},
            {"step": "04", "title": "Staff Onboarding & Rollout", "desc": "Conducting department-specific training sessions, migrating historical records, and deploying live systems."}
        ],
        "outcomes": [
            {"title": "Unified Client Transparency", "desc": "Provide delivery and billing teams with real-time insight into project milestones, contracts, and accounts receivable."},
            {"title": "15%+ Higher Billable Efficiency", "desc": "Automate routine administrative paperwork to allow senior professionals to dedicate more time to client service."},
            {"title": "100% Policy Compliance", "desc": "Enforce mandatory corporate approval thresholds on all client discounts, contracts, and expense reports."},
            {"title": "Real-Time Margin Protection", "desc": "Identify project scope creep and cost variances early to preserve professional service profit margins."}
        ],
        "related_links": [
            {"title": "Enterprise Business Solutions", "link": "services/enterprise-business.html", "tag": "Core Domain", "desc": "Explore our complete enterprise business software and workflow automation domain."},
            {"title": "Customer Relationship Management", "link": "services/crm.html", "tag": "Core Service", "desc": "Tailored CRM platforms for professional client account management."},
            {"title": "Human Resource Management Systems", "link": "services/hrms.html", "tag": "Core Service", "desc": "Workforce onboarding, leave tracking, and employee self-service portals."}
        ]
    },
    {
        "rel_path": "industries/healthcare.html",
        "category_badge": "TARGET INDUSTRY FOCUS",
        "page_title": "Healthcare & Health Technology",
        "page_subtitle": "Healthcare administrative automation, patient intake, scheduling workflows, healthcare document processing, system integration, and operational analytics.",
        "seo_desc": "Nova Arc Healthcare & Health Technology Solutions: Administrative workflow automation, digital patient intake, scheduling coordination, and secure EHR integration.",
        "breadcrumbs": [("Home", "index.html"), ("Industries", "industries.html"), ("Healthcare & Health Technology", None)],
        "overview_paragraphs": [
            "Hospitals, ambulatory clinics, and health technology companies confront intense administrative overhead, fragmented patient access workflows, and high documentation processing requirements that drain staff capacity.",
            "Nova Arc provides dedicated Healthcare & Health Technology solutions focused exclusively on administrative, operational, and non-clinical workflows. We do not provide clinical decision-making or replace licensed medical practitioners.",
            "Our platforms automate digital patient pre-registration, streamline appointment coordination, classify incoming physician referral packets, and support administrative billing data verification, reducing front-end administrative burden and improving clinic efficiency."
        ],
        "capabilities": [
            {"title": "Digital Patient Pre-Registration", "desc": "Mobile-responsive self-service intake forms capturing demographics, insurance cards, and digital consent before arrival.", "points": ["Mobile-friendly digital forms", "Insurance card photo capture", "Digital consent signature capture", "Automated EHR patient matching"]},
            {"title": "Appointment Coordination & Scheduling", "desc": "Automated scheduling workflows matching patient appointment requests with provider availability, location rules, and clinical modalities.", "points": ["Provider scheduling rules", "Automated reminder SMS/email", "Cancellation waitlist rebooking", "Front-end intake QA checks"]},
            {"title": "Referral Document Classification", "desc": "Intelligent categorization of incoming faxes and referral documents, extracting patient details and attaching them to EHR records.", "points": ["Referral order classification", "Demographic & provider extraction", "Automated indexing to EHR", "Urgent request flag tagging"]},
            {"title": "Administrative Billing Data Assistance", "desc": "Administrative tools that check claim data completeness, validate EDI file formatting, and track administrative denial workflows.", "points": ["EDI 837/835 format validation", "Missing demographic checks", "Administrative denial tracking", "Remittance posting reconciliation"]}
        ],
        "challenges": [
            {"challenge": "Front-Desk Registration Bottlenecks", "impact": "Long waiting room queues and illegible paper intake clipboards cause registration delays and data entry errors.", "solution": "Our digital self-service intake allows patients to complete paperwork on their smartphones prior to their appointment."},
            {"challenge": "Lost & Delayed Physician Referrals", "impact": "Incoming referral faxes sit unread in digital queues, delaying patient appointments and specialist care.", "solution": "We deploy automated document classifiers that identify referral orders immediately, extract key details, and alert scheduling coordinators."},
            {"challenge": "Administrative Claim Formatting Errors", "impact": "Claims rejected by clearinghouses due to missing subscriber IDs or invalid demographic field formatting.", "solution": "Our administrative validation tools verify EDI formatting and demographic completeness before files are transmitted."}
        ],
        "workflow_steps": [
            {"step": "01", "title": "Administrative Workflow Audit", "desc": "Mapping clinic front-desk procedures, intake documents, scheduling rules, and EHR integration requirements."},
            {"step": "02", "title": "Portal & Ingestion Setup", "desc": "Configuring digital patient intake forms, automated referral classification queues, and HL7/FHIR connectors."},
            {"step": "03", "title": "Security & Privacy Certification", "desc": "Validating end-to-end data encryption, access permissions, audit logging, and strict data privacy protections."},
            {"step": "04", "title": "Clinic Deployment", "desc": "Training front-desk and scheduling staff, activating digital intake queues, and monitoring registration velocity."}
        ],
        "outcomes": [
            {"title": "50% Shorter Check-In Times", "desc": "Pre-registered patients check in with a quick scan, significantly reducing waiting room congestion."},
            {"title": "Eliminated Manual Transcription", "desc": "Patient-entered demographic and insurance details flow directly into EHR records without manual re-typing."},
            {"title": "Rapid Referral Turnaround", "desc": "Physician referral documents are classified and routed to scheduling coordinators within minutes of receipt."},
            {"title": "Strict Administrative Scope", "desc": "All automated features maintain a clear boundary around administrative tasks, preserving medical decision-making for doctors."}
        ],
        "related_links": [
            {"title": "Healthcare Technology & Automation", "link": "services/healthcare-automation.html", "tag": "Core Service", "desc": "Explore our dedicated healthcare administrative intake and scheduling automation services."},
            {"title": "Healthcare Technology Solutions", "link": "solutions/healthcare-technology.html", "tag": "Parent Solution", "desc": "Comprehensive healthcare administrative workflows and EHR data connectivity."},
            {"title": "AI & Healthcare Technology", "link": "services/ai-healthcare.html", "tag": "Service Domain", "desc": "Discover our complete AI and healthcare administration technology service domain."}
        ]
    },

    # -------------------------------------------------------------
    # CONNECT WITH US SUBPAGES (4 Pages)
    # -------------------------------------------------------------
    {
        "rel_path": "connect/general-enquiries.html",
        "category_badge": "CONNECT WITH NOVA ARC",
        "page_title": "General Enquiries",
        "page_subtitle": "Get in touch with Nova Arc for general corporate communications, media inquiries, partnership discussions, or company information.",
        "seo_desc": "Contact Nova Arc for general company inquiries, corporate communications, and strategic technology partnerships.",
        "breadcrumbs": [("Home", "index.html"), ("Connect With Us", "contact.html"), ("General Enquiries", None)],
        "overview_paragraphs": [
            "Nova Arc Technologies engineers intelligent digital solutions, enterprise software platforms, and real-time operational automation for forward-thinking organizations globally.",
            "Whether you are seeking general company information, exploring strategic corporate partnerships, or submitting press inquiries, our administrative team is here to assist you.",
            "We review all general communications promptly and connect you with the appropriate departmental leadership across our four core technology service domains."
        ],
        "capabilities": [
            {"title": "Corporate Communications", "desc": "Official press inquiries, executive interviews, industry speaking requests, and corporate announcements.", "points": ["Press & media relations", "Executive speaking requests", "Corporate announcements", "Brand asset requests"]},
            {"title": "Strategic Partnerships", "desc": "Exploring technology integrations, system integrator relationships, and commercial collaboration agreements.", "points": ["Technology partner inquiries", "System integrator alliances", "Vendor collaboration", "Joint development discussions"]},
            {"title": "Corporate Administration", "desc": "Company headquarters information, Ministry of Corporate Affairs (MCA) communication, and administrative inquiries.", "points": ["Official corporate inquiries", "Legal notice routing", "Compliance documentation", "Vendor billing inquiries"]},
            {"title": "Direct Contact Channels", "desc": "Reach out directly via our verified company phone lines and departmental communication email addresses.", "points": ["Phone: 04046146093", "Email: admin@novaarctech.in", "Headquarters in Hyderabad", "Business hours: 9:00 AM - 6:00 PM IST"]}
        ],
        "challenges": [
            {"challenge": "Unclear Inquiry Routing", "impact": "General inquiries sent to generic inboxes get lost without reaching the responsible department.", "solution": "Our administrative team routes every incoming general communication directly to the appropriate executive lead."},
            {"challenge": "Delayed Corporate Responses", "impact": "Organizations waiting weeks for simple corporate or partnership clarifications.", "solution": "We maintain strict internal communication SLAs, ensuring general inquiries receive written acknowledgment promptly."}
        ],
        "workflow_steps": [
            {"step": "01", "title": "Inquiry Submission", "desc": "Submit your general inquiry through our contact form or official email channels."},
            {"step": "02", "title": "Administrative Review", "desc": "Our corporate team reviews your inquiry and identifies the relevant department."},
            {"step": "03", "title": "Executive Routing", "desc": "Your request is routed to appropriate leadership for review and response formulation."},
            {"step": "04", "title": "Follow-Up Communication", "desc": "We connect with you directly via email or telephone to discuss your inquiry."}
        ],
        "outcomes": [
            {"title": "Direct Executive Access", "desc": "Connect directly with Nova Arc leadership for partnerships and strategic collaboration."},
            {"title": "Verified Corporate Details", "desc": "Communicate directly with registered corporate headquarters and verified company representatives."},
            {"title": "Prompt Communication", "desc": "Receive structured, professional follow-up on all legitimate corporate and media inquiries."}
        ],
        "related_links": [
            {"title": "Discuss a Project", "link": "connect/project-enquiry.html", "tag": "Project Consultation", "desc": "Ready to explore a custom software or automation project with our engineering team?"},
            {"title": "Service Enquiries", "link": "connect/service-enquiry.html", "tag": "Service Specific", "desc": "Inquire about specific capabilities across our four core service domains."},
            {"title": "Contact Overview", "link": "contact.html", "tag": "Main Directory", "desc": "Access our central contact form and direct departmental contact directory."}
        ]
    },
    {
        "rel_path": "connect/project-enquiry.html",
        "category_badge": "CONNECT WITH NOVA ARC",
        "page_title": "Discuss a Project",
        "page_subtitle": "Schedule a technical consultation to explore your business requirements, software architecture, and implementation roadmap.",
        "seo_desc": "Discuss your software engineering, digital commerce, IoT monitoring, or AI automation project with Nova Arc technology architects.",
        "breadcrumbs": [("Home", "index.html"), ("Connect With Us", "contact.html"), ("Discuss a Project", None)],
        "overview_paragraphs": [
            "Every successful enterprise software deployment begins with an in-depth understanding of your current operational bottlenecks, business objectives, and existing technology landscape.",
            "Nova Arc provides dedicated technical consultations with our senior software architects. Whether modernizing legacy enterprise systems, building custom digital commerce platforms, deploying IoT monitoring, or implementing governed agentic AI, we help you evaluate technical feasibility and estimate project roadmaps.",
            "Tell us about your project requirements using our structured inquiry form below, or contact our sales team directly at sales@novaarctech.in. We review your specifications and follow up to schedule an architecture discovery session."
        ],
        "capabilities": [
            {"title": "Architecture Discovery Sessions", "desc": "Detailed technical reviews evaluating system requirements, integration endpoints, security, and scalability needs.", "points": ["Technical feasibility analysis", "System integration reviews", "Scalability & concurrency planning", "Security & data governance"]},
            {"title": "Tailored Solution Roadmaps", "desc": "Phased implementation roadmaps breaking complex development into structured, agile delivery milestones.", "points": ["Phase-by-phase delivery plans", "Clear milestone definitions", "Risk mitigation strategies", "Resource allocation planning"]},
            {"title": "Transparent Commercial Models", "desc": "Flexible engagement frameworks tailored to your project requirements, timeline, and organizational structure.", "points": ["Fixed-scope milestone contracts", "Dedicated engineering pods", "Hybrid agile delivery", "Transparent commercial proposals"]},
            {"title": "Dedicated Sales Contacts", "desc": "Direct access to our enterprise commercial team for proposals, contract reviews, and non-disclosure agreements (NDAs).", "points": ["Email: sales@novaarctech.in", "Phone: 04046146093", "Mutual NDA execution", "Fast proposal turnaround"]}
        ],
        "challenges": [
            {"challenge": "Ambiguous Project Requirements", "impact": "Projects start without clear technical specifications, leading to scope creep, delays, and budget overruns.", "solution": "Our discovery sessions establish clear, unambiguous architectural blueprints and scope boundaries before development begins."},
            {"challenge": "Uncertain Integration Feasibility", "impact": "Worry that modern software platforms will fail to connect with legacy ERPs or proprietary databases.", "solution": "Our senior architects evaluate your existing API landscape upfront to design verified, resilient integration adapters."}
        ],
        "workflow_steps": [
            {"step": "01", "title": "Project Inquiry Submission", "desc": "Submit your business challenge, desired scope, and timeline via our project discussion form."},
            {"step": "02", "title": "NDA & Initial Discovery", "desc": "We execute a mutual NDA and conduct an initial discovery call with our technical architects."},
            {"step": "03", "title": "Architecture Blueprint", "desc": "We provide a high-level solution blueprint, integration approach, and phased delivery roadmap."},
            {"step": "04", "title": "Commercial Proposal", "desc": "Our team delivers a transparent commercial proposal and kickoff plan for your project."}
        ],
        "outcomes": [
            {"title": "Architectural Certainty", "desc": "Gain complete technical clarity on how your software solution will be engineered, integrated, and scaled."},
            {"title": "Predictable Delivery Timelines", "desc": "Phased delivery milestones provide full transparency into project velocity and release dates."},
            {"title": "Protected Confidentiality", "desc": "All project discussions and proprietary business workflows are protected under strict mutual NDAs."}
        ],
        "related_links": [
            {"title": "All Solutions Overview", "link": "solutions.html", "tag": "Solutions Suite", "desc": "Explore our complete digital solutions across commerce, enterprise, IoT, and AI."},
            {"title": "Services Catalog", "link": "services.html", "tag": "Engineering Services", "desc": "Detailed breakdown of our four core technology service domains."},
            {"title": "Main Contact Portal", "link": "contact.html", "tag": "Contact Center", "desc": "Access our central contact form and departmental email directory."}
        ]
    },
    {
        "rel_path": "connect/service-enquiry.html",
        "category_badge": "CONNECT WITH NOVA ARC",
        "page_title": "Service Enquiries",
        "page_subtitle": "Inquire about specific technical capabilities across Digital Commerce, Enterprise Systems, Intelligent Monitoring, or AI & Healthcare Technology.",
        "seo_desc": "Submit a targeted service inquiry to Nova Arc for digital commerce, enterprise CRM/HRMS, IoT monitoring, or AI healthcare technology.",
        "breadcrumbs": [("Home", "index.html"), ("Connect With Us", "contact.html"), ("Service Enquiries", None)],
        "overview_paragraphs": [
            "Organizations looking to address a specific operational challenge often need targeted information regarding our service domain capabilities, technology stacks, and engagement models.",
            "Nova Arc provides dedicated service advisory across our four primary engineering domains: Digital Commerce & Supply Chain, Enterprise Business Solutions, Intelligent Monitoring & Automation, and AI & Healthcare Technology.",
            "Select the service domain relevant to your operational goals below to explore implementation specifications, request detailed capability briefs, or connect with our specialized practice leads."
        ],
        "capabilities": [
            {"title": "Digital Commerce & SCM Advisory", "desc": "Inquiries regarding B2B/B2C storefronts, FoodTech solutions, warehouse inventory, and logistics platforms.", "points": ["Commerce platform modernization", "FoodTech traceability solutions", "Procurement portal workflows", "Carrier logistics integration"]},
            {"title": "Enterprise Business Advisory", "desc": "Inquiries regarding custom CRM, HRMS platforms, business process automation (BPA), and ERP data connectivity.", "points": ["Custom CRM development", "Digital HRMS onboarding tools", "Approval hierarchy automation", "Enterprise system integration"]},
            {"title": "Monitoring & Automation Advisory", "desc": "Inquiries regarding real-time IoT sensor telemetry, operational dashboards, anomaly detection, and incident automation.", "points": ["Industrial IoT sensor networks", "Operational control room consoles", "Predictive maintenance modeling", "System health observability"]},
            {"title": "AI & Healthcare Tech Advisory", "desc": "Inquiries regarding agentic AI workflows, private generative RAG assistants, document extraction, and healthcare intake.", "points": ["Agentic AI workflow design", "Private enterprise RAG portals", "Intelligent document processing", "Healthcare administrative automation"]}
        ],
        "challenges": [
            {"challenge": "Selecting the Right Technology Approach", "impact": "Organizations struggle to decide between off-the-shelf SaaS, custom software development, or hybrid integration.", "solution": "Our service practice leads provide unbiased technical guidance on the most cost-effective architecture for your scale."}
        ],
        "workflow_steps": [
            {"step": "01", "title": "Service Selection", "desc": "Choose your specific service domain of interest and submit your inquiry details."},
            {"step": "02", "title": "Practice Lead Assignment", "desc": "Your inquiry is routed directly to the specialized engineering practice lead for that domain."},
            {"step": "03", "title": "Technical Consultation", "desc": "We schedule a focused consultation to review technical capabilities, case studies, and architecture."},
            {"step": "04", "title": "Engagement Proposal", "desc": "We formulate a tailored engagement scope matching your exact operational requirements."}
        ],
        "outcomes": [
            {"title": "Domain-Specific Expertise", "desc": "Communicate directly with engineers who specialize in your specific technology domain."},
            {"title": "Targeted Architecture Briefs", "desc": "Receive relevant technical specifications and integration blueprints for your target service."}
        ],
        "related_links": [
            {"title": "Full Services Catalog", "link": "services.html", "tag": "All Services", "desc": "Browse our four core service domains and 20 specialized capabilities."},
            {"title": "Discuss a Project", "link": "connect/project-enquiry.html", "tag": "Full Consultation", "desc": "Schedule a comprehensive architecture discovery session for your upcoming project."},
            {"title": "Contact Directory", "link": "contact.html", "tag": "Main Portal", "desc": "Access our central contact form and departmental communication channels."}
        ]
    },
    {
        "rel_path": "connect/technical-support.html",
        "category_badge": "CONNECT WITH NOVA ARC",
        "page_title": "Technical Support",
        "page_subtitle": "Submit product tickets, report operational anomalies, or access dedicated client technical helpdesk resources.",
        "seo_desc": "Nova Arc Technical Support & Helpdesk: Submit product tickets, report operational issues, and access client engineering support resources.",
        "breadcrumbs": [("Home", "index.html"), ("Connect With Us", "contact.html"), ("Technical Support", None)],
        "overview_paragraphs": [
            "Nova Arc provides dedicated technical support and operational maintenance for all deployed enterprise applications, digital commerce platforms, IoT monitoring networks, and automation workflows.",
            "Our engineering helpdesk team monitors operational integrity, investigates incident tickets, and deploys rapid software patches in accordance with established client Service Level Agreements (SLAs).",
            "If you are an active Nova Arc client experiencing a technical issue, submit a ticket using our helpdesk channel below or email our support desk directly at helpdesk@novaarctech.in."
        ],
        "capabilities": [
            {"title": "Ticket Submission & Tracking", "desc": "Submit detailed technical incident reports with error logs, screenshots, and severity classifications.", "points": ["Severity 1 to 4 classification", "Automated ticket confirmation", "Real-time status updates", "Dedicated engineer assignment"]},
            {"title": "Direct Helpdesk Channels", "desc": "Reach out directly to our operational support engineering team for urgent system assistance.", "points": ["Email: helpdesk@novaarctech.in", "General Support: support@novaarctech.in", "Phone: 04046146093", "Hours: 24/7 for Critical Severity 1"]},
            {"title": "SLA-Backed Response Times", "desc": "Guaranteed response and resolution windows aligned with your enterprise software maintenance agreement.", "points": ["Critical Severity 1: < 1 Hour", "High Severity 2: < 4 Hours", "Medium Severity 3: < 1 Business Day", "Low Severity 4: < 2 Business Days"]},
            {"title": "System Patching & Maintenance", "desc": "Scheduled security updates, dependency patches, database maintenance, and performance optimization.", "points": ["Scheduled maintenance windows", "Advance maintenance notices", "Zero-downtime rolling updates", "Post-patch verification tests"]}
        ],
        "challenges": [
            {"challenge": "Unclear Severity Prioritization", "impact": "Critical production outages getting queued behind minor visual adjustments, delaying urgent fixes.", "solution": "Our helpdesk ticketing enforces explicit severity classifications, immediately alerting on-call engineers for critical issues."}
        ],
        "workflow_steps": [
            {"step": "01", "title": "Ticket Submission", "desc": "Submit your technical ticket with reproduction steps, system URL, and error screenshots."},
            {"step": "02", "title": "Triage & SLA Assignment", "desc": "Our helpdesk triages the ticket, confirms severity level, and assigns a primary support engineer."},
            {"step": "03", "title": "Investigation & Patching", "desc": "The engineering team reproduces the issue, identifies root cause, and tests a patch in staging."},
            {"step": "04", "title": "Resolution & Verification", "desc": "The patch is deployed to production, verified with client stakeholders, and the ticket is resolved."}
        ],
        "outcomes": [
            {"title": "Rapid Outage Resolution", "desc": "SLA-backed response ensures that critical system interruptions receive immediate engineering intervention."},
            {"title": "Auditable Ticket Records", "desc": "Maintain permanent histories of all reported technical issues, resolution steps, and post-mortems."},
            {"title": "Continuous System Stability", "desc": "Ongoing maintenance and security patching ensure your enterprise software operates reliably."}
        ],
        "related_links": [
            {"title": "General Enquiries", "link": "connect/general-enquiries.html", "tag": "General Inquiries", "desc": "Corporate communications, partnerships, and non-technical company questions."},
            {"title": "System & Infrastructure Monitoring", "link": "services/infrastructure-monitoring.html", "tag": "Related Service", "desc": "Proactive 24/7 observability and automated uptime tracking."},
            {"title": "Main Contact Portal", "link": "contact.html", "tag": "Directory", "desc": "Return to our central contact directory and departmental email channels."}
        ]
    }
]
print(f"Loaded {len(TECH_IND_CONNECT_PAGES)} Tech, Industries & Connect subpages.")
