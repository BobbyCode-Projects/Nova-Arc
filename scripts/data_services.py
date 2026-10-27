# Services Domain Landings & Subpages Data
SERVICES_PAGES = [
    # -------------------------------------------------------------
    # DOMAIN 1: Digital Commerce & Supply Chain
    # -------------------------------------------------------------
    {
        "rel_path": "services/digital-commerce.html",
        "category_badge": "SERVICE DOMAIN 01",
        "page_title": "Digital Commerce & Supply Chain",
        "page_subtitle": "Connect commerce, procurement, inventory, distribution, and logistics through integrated digital platforms that improve operational visibility and streamline complex supply chain workflows.",
        "seo_desc": "Nova Arc Digital Commerce & Supply Chain: Connect digital commerce, FoodTech solutions, inventory, procurement, and logistics distribution.",
        "breadcrumbs": [("Home", "index.html"), ("Services", "services.html"), ("Digital Commerce & Supply Chain", None)],
        "overview_paragraphs": [
            "Modern commerce requires deep synchronization between customer-facing storefronts, supplier purchasing, warehouse operations, and freight logistics. Fragmented systems create inventory inaccuracies, checkout delays, and fulfillment errors that erode customer trust and enterprise profitability.",
            "Nova Arc's Digital Commerce & Supply Chain service domain provides end-to-end software engineering and system integration. We build robust B2B and B2C commerce portals, specialized FoodTech supply chain platforms, automated procurement systems, and real-time logistics tracking networks.",
            "Our solutions connect buyers, vendors, inventory managers, and carriers into a cohesive operational ecosystem. By unifying transactional data and automating cross-system handoffs, we help organizations accelerate order fulfillment, optimize working capital, and scale commercial operations."
        ],
        "capabilities": [
            {"title": "Digital Commerce Platforms", "desc": "B2B/B2C storefronts, digital ordering portals, customer account management, and pricing workflows.", "points": ["Multi-storefront architecture", "Dynamic pricing matrices", "Self-service buyer portals", "ERP checkout integration"]},
            {"title": "FoodTech Solutions", "desc": "Specialized digital food ordering, supplier coordination, batch/expiry tracking, and food supply traceability.", "points": ["Cold chain traceability", "Batch & expiry management", "Commissary inventory sync", "Restaurant supplier portals"]},
            {"title": "Supply Chain Management", "desc": "Warehouse inventory optimization, multi-node tracking, demand forecasting workflows, and replenishment.", "points": ["Live multi-node stock views", "Automated replenishment rules", "Safety stock calculations", "Dead-stock identification"]},
            {"title": "Procurement & Vendor Management", "desc": "Digital purchase requisitions, approval hierarchies, vendor onboarding portals, and invoice workflows.", "points": ["3-way invoice matching", "Vendor scorecard tracking", "Contract compliance rules", "PO requisition pipelines"]},
            {"title": "Logistics & Distribution", "desc": "Dispatch coordination, shipment tracking, carrier route optimization, and logistics performance analytics.", "points": ["Carrier API integrations", "Real-time freight milestones", "Dynamic route planning", "Proof of delivery capture"]}
        ],
        "challenges": [
            {"challenge": "Disconnected Order & Inventory Data", "impact": "Orders taken online fail to reflect actual warehouse availability, leading to backorders and customer dissatisfaction.", "solution": "We engineer real-time bidirectional connectors that tie digital shopping carts directly to warehouse management inventory ledgers."},
            {"challenge": "Manual Procurement Requisitions", "impact": "Departmental purchasing via email and paper causes rogue spending, budget overruns, and delayed approvals.", "solution": "Our digital procurement portals enforce organizational approval matrices, budget caps, and contracted vendor catalog routing."},
            {"challenge": "Supply Chain Blind Spots", "impact": "Inability to track in-transit freight and vendor shipment statuses results in manufacturing bottlenecks and dock congestion.", "solution": "We deploy centralized logistics visibility consoles that aggregate carrier telemetry and generate proactive delay notifications."}
        ],
        "workflow_steps": [
            {"step": "01", "title": "Supply Chain Audit", "desc": "Assessing current order workflows, inventory nodes, procurement bottlenecks, and carrier integrations."},
            {"step": "02", "title": "Architecture & Data Modeling", "desc": "Designing unified product catalogs, vendor schemas, inventory allocation logic, and API endpoints."},
            {"step": "03", "title": "Platform Engineering", "desc": "Developing the commerce interfaces, procurement portals, WMS data synchronization, and logistics tracking."},
            {"step": "04", "title": "Deployment & Optimization", "desc": "Executing end-to-end UAT, vendor onboarding, carrier API certification, and continuous performance tuning."}
        ],
        "outcomes": [
            {"title": "Accelerated Order Turnaround", "desc": "Reduce order-to-dispatch cycles through automated validation and instant ERP transmission."},
            {"title": "Lower Carrying Costs", "desc": "Optimize warehouse inventory levels and reduce excess buffer stock through data-informed replenishment."},
            {"title": "Complete Spend Visibility", "desc": "Gain real-time corporate oversight into vendor commitments, purchase orders, and contracted price compliance."},
            {"title": "Enhanced Delivery Reliability", "desc": "Improve on-time delivery rates with proactive carrier milestone tracking and exception management."}
        ],
        "related_links": [
            {"title": "Digital Commerce Platforms", "link": "services/digital-commerce-platforms.html", "tag": "Sub-Capability", "desc": "Explore custom B2B/B2C digital ordering and catalog management architecture."},
            {"title": "FoodTech Solutions", "link": "services/foodtech.html", "tag": "Sub-Capability", "desc": "Specialized food ordering, expiry tracking, and supply chain traceability."},
            {"title": "Supply Chain Management", "link": "services/supply-chain-management.html", "tag": "Sub-Capability", "desc": "Multi-warehouse inventory optimization and automated replenishment."}
        ]
    },
    {
        "rel_path": "services/digital-commerce-platforms.html",
        "category_badge": "DIGITAL COMMERCE & SUPPLY CHAIN",
        "page_title": "Digital Commerce Platforms",
        "page_subtitle": "B2B and B2C commerce platforms, digital ordering, customer portals, product catalog management, pricing workflows, order processing, and fulfillment integration.",
        "seo_desc": "Nova Arc Digital Commerce Platforms: Custom B2B and B2C digital ordering storefronts, product catalog management, and payment fulfillment integrations.",
        "breadcrumbs": [("Home", "index.html"), ("Services", "services.html"), ("Digital Commerce", "services/digital-commerce.html"), ("Digital Commerce Platforms", None)],
        "overview_paragraphs": [
            "Modern commercial transactions require agile, high-performance digital platforms that cater to both consumer expectations for speed and enterprise requirements for complex ordering workflows.",
            "Nova Arc develops bespoke digital commerce platforms engineered for scalability, high concurrency, and seamless enterprise system integration. Our platforms support multi-currency transactions, dynamic contract pricing, custom product configurators, and complex organizational purchasing hierarchies.",
            "From high-volume consumer storefronts to specialized B2B customer self-service portals, we build technology that empowers buyers, simplifies order management, and drives digital revenue growth."
        ],
        "capabilities": [
            {"title": "Enterprise B2B Portals", "desc": "Custom buyer account structures, credit terms, multi-user purchasing permissions, and quick-order spreadsheet uploads.", "points": ["Corporate account hierarchies", "Credit limit validation", "Quick re-ordering templates", "PunchOut catalog support"]},
            {"title": "Omnichannel B2C Storefronts", "desc": "Blazing-fast mobile-first shopping experiences with sub-second page loads, intelligent search, and frictionless checkout.", "points": ["Faceted product search", "One-click mobile checkout", "Personalized recommendations", "Unified cart across devices"]},
            {"title": "Dynamic Catalog Management", "desc": "Robust product information management (PIM) handling millions of SKUs, custom attribute matrices, and digital assets.", "points": ["Rich attribute modeling", "Batch CSV/API imports", "Localized product descriptions", "Automated stock availability"]},
            {"title": "Payment & Tax Gateway Integration", "desc": "Secure integration with global payment processors, digital wallets, automated sales tax calculation, and fraud prevention.", "points": ["PCI-DSS compliant gateways", "Automated regional tax calculation", "Tokenized recurring billing", "Instant refund processing"]}
        ],
        "challenges": [
            {"challenge": "Checkout Latency & Cart Abandonment", "impact": "Slow, bloated checkout pages cause buyers to abandon carts, directly reducing top-line commercial revenue.", "solution": "We engineer lean, microservices-driven checkout funnels with instant address validation and tokenized payment processing."},
            {"challenge": "Complex Corporate Pricing Rules", "impact": "Managing customer-specific discount schedules across thousands of accounts causes invoicing errors and pricing disputes.", "solution": "Our platforms incorporate dynamic rule-based pricing engines that evaluate customer tier, volume, and contract agreements in real time."},
            {"challenge": "ERP Synchronization Delays", "impact": "Orders placed online take hours to appear in back-office ERP systems, delaying warehouse picking and fulfillment.", "solution": "We deploy real-time event-driven webhook connectors that instantly transmit completed orders directly to your enterprise ERP ledger."}
        ],
        "workflow_steps": [
            {"step": "01", "title": "Catalog & Workflow Analysis", "desc": "Mapping product hierarchies, customer segments, pricing structures, and back-office integration requirements."},
            {"step": "02", "title": "UX & Architecture Design", "desc": "Crafting intuitive buyer purchasing journeys, mobile-responsive layouts, and scalable database schemas."},
            {"step": "03", "title": "Platform Engineering", "desc": "Developing front-end storefronts, secure customer portals, catalog search clusters, and payment pipelines."},
            {"step": "04", "title": "Testing & Launch", "desc": "Conducting payment gateway certification, high-concurrency load testing, security audits, and cutover."}
        ],
        "outcomes": [
            {"title": "Increased Conversion Rates", "desc": "Sub-second catalog search and streamlined checkout funnels convert more visitors into completed purchases."},
            {"title": "Self-Service Operational Savings", "desc": "Enable B2B buyers to manage orders, download invoices, and reorder independently without sales rep intervention."},
            {"title": "100% Pricing Accuracy", "desc": "Eliminate manual pricing errors and billing discrepancies through automated contract rule enforcement."},
            {"title": "Seamless Fulfillment Handoff", "desc": "Automated order routing ensures immediate transmission to warehouse packing stations upon checkout completion."}
        ],
        "related_links": [
            {"title": "Supply Chain Management", "link": "services/supply-chain-management.html", "tag": "Related Service", "desc": "Synchronize storefront orders with multi-warehouse inventory and replenishment."},
            {"title": "Procurement & Vendor Management", "link": "services/procurement.html", "tag": "Related Service", "desc": "Automate upstream supplier purchasing to fulfill downstream commerce demand."},
            {"title": "Retail & Digital Commerce Industry", "link": "industries/retail-ecommerce.html", "tag": "Industry Focus", "desc": "Tailored commerce architectures for modern consumer and wholesale brands."}
        ]
    },
    {
        "rel_path": "services/foodtech.html",
        "category_badge": "DIGITAL COMMERCE & SUPPLY CHAIN",
        "page_title": "FoodTech Solutions",
        "page_subtitle": "Digital food ordering and distribution, food procurement, supplier coordination, batch and expiry tracking, inventory visibility, and food supply chain traceability.",
        "seo_desc": "Nova Arc FoodTech Solutions: Digital food ordering, supplier coordination, batch and expiry tracking, and farm-to-fork supply chain traceability.",
        "breadcrumbs": [("Home", "index.html"), ("Services", "services.html"), ("Digital Commerce", "services/digital-commerce.html"), ("FoodTech Solutions", None)],
        "overview_paragraphs": [
            "The food and beverage industry operates under stringent regulatory compliance, perishable shelf-life constraints, variable commodity pricing, and high customer expectations for freshness and traceability.",
            "Nova Arc builds specialized FoodTech Solutions that modernize food procurement, digital ordering, multi-kitchen inventory coordination, and distribution logistics. We engineer platforms that connect agricultural producers, food distributors, commercial kitchens, and end customers.",
            "Our systems incorporate automated First-Expired, First-Out (FEFO) inventory algorithms, real-time temperature telemetry monitoring, batch recall tracking, and digital supplier portals, ensuring food quality, minimizing spoilage, and maximizing operational margins."
        ],
        "capabilities": [
            {"title": "Digital Food Ordering & Distribution", "desc": "B2B wholesale food ordering and B2C delivery management platforms with real-time menu and stock availability.", "points": ["Live menu & catalog availability", "Automated order cutoff schedules", "Multi-location dispatch routing", "Split delivery order handling"]},
            {"title": "Batch & Expiry Date Management", "desc": "Strict automated FEFO inventory management tracking lot numbers, production dates, and shelf-life expiration.", "points": ["Automated FEFO picking rules", "Perishable shelf-life alerts", "Batch recall search tools", "Spoilage reduction analytics"]},
            {"title": "Food Procurement & Supplier Coordination", "desc": "Connected supplier ordering portals linking central production commissaries with raw agricultural ingredient suppliers.", "points": ["Daily commissary demand sync", "Yield & recipe costing models", "Supplier quality scorecards", "Automated purchase orders"]},
            {"title": "Cold Chain & Temperature Telemetry", "desc": "IoT sensor connectivity tracking environmental conditions and storage temperatures across warehouse walk-ins and delivery vans.", "points": ["Continuous thermal logging", "Temperature threshold alerts", "Automated HACCP compliance logs", "Carrier compliance tracking"]}
        ],
        "challenges": [
            {"challenge": "Perishable Inventory Spoilage", "impact": "Poor rotation and delayed visibility into expiry dates lead to high food waste and severe margin erosion.", "solution": "We deploy automated FEFO inventory logic that directs warehouse pickers to oldest compliant batches first, sending automated alerts on expiring lots."},
            {"challenge": "Food Safety & Recall Compliance", "impact": "Locating affected products during food safety recalls using paper records takes days, increasing consumer health risks and liability.", "solution": "Our digital batch tracking provides instantaneous farm-to-fork trace reports, identifying every recipient of a specific lot within seconds."},
            {"challenge": "Fragmented Multi-Kitchen Requisitions", "impact": "Individual restaurant units ordering independently lead to inefficient spot purchasing and missed volume discounts.", "solution": "We centralize commissary and restaurant requisitions into consolidated bulk purchase orders that maximize purchasing power."}
        ],
        "workflow_steps": [
            {"step": "01", "title": "Kitchen & Chain Audit", "desc": "Analyzing ingredient turnover, supplier delivery cadence, regulatory requirements (HACCP), and kitchen workflows."},
            {"step": "02", "title": "System Architecture", "desc": "Configuring recipe yield databases, FEFO inventory allocation logic, and digital ordering interfaces."},
            {"step": "03", "title": "Integration & IoT Setup", "desc": "Deploying cold chain temperature sensors, POS integrations, and automated supplier PO pipelines."},
            {"step": "04", "title": "Operational Training", "desc": "Training kitchen managers and warehouse staff on mobile barcode scanning, batch logging, and automated reordering."}
        ],
        "outcomes": [
            {"title": "30%+ Reduction in Spoilage", "desc": "Automated FEFO rotation and expiry alert triggers dramatically decrease perishable food waste."},
            {"title": "Instant Recall Traceability", "desc": "Identify and isolate affected lot numbers across the entire supply network in seconds."},
            {"title": "Automated HACCP Compliance", "desc": "Replace manual temperature clipboards with tamper-proof automated IoT thermal audit logs."},
            {"title": "Optimized Food Margins", "desc": "Accurate recipe yield tracking and centralized procurement prevent unauthorized food cost variances."}
        ],
        "related_links": [
            {"title": "FoodTech & Distribution Industry", "link": "industries/foodtech.html", "tag": "Industry Focus", "desc": "Explore complete industry solutions for food distributors, commissaries, and restaurant chains."},
            {"title": "Supply Chain Management", "link": "services/supply-chain-management.html", "tag": "Related Service", "desc": "Warehouse inventory management, demand forecasting, and replenishment."},
            {"title": "Intelligent Monitoring & IoT", "link": "services/intelligent-monitoring.html", "tag": "Related Domain", "desc": "Real-time telemetry and sensor monitoring for refrigerated facilities."}
        ]
    },
    {
        "rel_path": "services/supply-chain-management.html",
        "category_badge": "DIGITAL COMMERCE & SUPPLY CHAIN",
        "page_title": "Supply Chain Management",
        "page_subtitle": "Inventory and warehouse management, order lifecycle tracking, demand forecasting workflows, replenishment, supplier collaboration, and operational reporting.",
        "seo_desc": "Nova Arc Supply Chain Management: Multi-warehouse inventory optimization, demand forecasting workflows, automated replenishment, and operational reporting.",
        "breadcrumbs": [("Home", "index.html"), ("Services", "services.html"), ("Digital Commerce", "services/digital-commerce.html"), ("Supply Chain Management", None)],
        "overview_paragraphs": [
            "In modern enterprise operations, maintaining the balance between customer order availability and lean working capital requires real-time visibility across every warehouse, fulfillment node, and transit channel.",
            "Nova Arc provides comprehensive Supply Chain Management (SCM) software engineering that unifies inventory management, multi-warehouse coordination, order lifecycle tracking, and automated stock replenishment.",
            "Our platforms transform static spreadsheet inventories into dynamic, event-driven supply networks. By connecting sales demand directly with upstream procurement and warehouse picking stations, we help businesses eliminate stockouts, prevent overstocking, and lower fulfillment costs."
        ],
        "capabilities": [
            {"title": "Multi-Node Inventory Tracking", "desc": "Centralized inventory visibility tracking on-hand, allocated, and in-transit stock across regional warehouses and retail nodes.", "points": ["Live cross-warehouse balances", "Virtual stock pooling", "Cycle count automation", "Barcode & RFID scan integration"]},
            {"title": "Order Lifecycle Orchestration", "desc": "End-to-end order routing that evaluates delivery destination, warehouse stock levels, and carrier costs to determine optimal fulfillment.", "points": ["Intelligent order splitting", "Nearest-node routing", "Backorder management", "Drop-ship automation"]},
            {"title": "Demand Forecasting & Planning", "desc": "Data-informed planning models that analyze historical sales velocities, seasonality, and promotional surges to project stock needs.", "points": ["Historical velocity modeling", "Lead time variance buffers", "Seasonal trend adjustment", "Safety stock calculations"]},
            {"title": "Replenishment Automation", "desc": "Rule-based purchase triggers that automatically generate supplier purchase orders when inventory reaches calculated reorder thresholds.", "points": ["Dynamic reorder thresholds", "Economic order quantity (EOQ)", "Supplier minimum order rules", "Automated PO generation"]}
        ],
        "challenges": [
            {"challenge": "Inaccurate Stock Records & Phantom Inventory", "impact": "Discrepancies between computer records and physical warehouse shelves lead to failed pick operations and cancelled orders.", "solution": "We implement mobile barcode scanning workflows and automated cycle count schedules that maintain 99%+ inventory record accuracy."},
            {"challenge": "Disconnected Fulfillment Hubs", "impact": "Warehouses operate as isolated islands, causing redundant inventory holding in one region while another experiences stockouts.", "solution": "Our platforms pool inventory virtually across all nodes and automate cross-docking and inter-facility stock transfers."},
            {"challenge": "Stockout Panics & Expensive Air Freight", "impact": "Late discovery of impending stock depletion forces companies to pay premium expedited freight fees to replenish inventory.", "solution": "We deploy predictive lead-time tracking that flags potential stock depletions weeks in advance, allowing standard ground reordering."}
        ],
        "workflow_steps": [
            {"step": "01", "title": "Network Assessment", "desc": "Mapping distribution centers, fulfillment partners, inventory turnover rates, and existing ERP interfaces."},
            {"step": "02", "title": "Data Architecture", "desc": "Standardizing SKU attribute models, warehouse location naming schemas, and replenishment algorithms."},
            {"step": "03", "title": "Software Engineering", "desc": "Building warehouse inventory consoles, mobile scanner interfaces, and bidirectional ERP data pipelines."},
            {"step": "04", "title": "Pilot & Rollout", "desc": "Running parallel inventory tracking in pilot facilities, training warehouse personnel, and deploying network-wide."}
        ],
        "outcomes": [
            {"title": "99%+ Inventory Accuracy", "desc": "Eliminate lost inventory and phantom stock through real-time scan verification at every touchpoint."},
            {"title": "25% Reduction in Safety Stock", "desc": "Maintain customer service levels with lower working capital by relying on accurate real-time inventory visibility."},
            {"title": "Minimized Backorders", "desc": "Automated replenishment triggers ensure timely reordering before stock levels reach critical depletion points."},
            {"title": "Lower Fulfillment Freight Costs", "desc": "Intelligent order routing selects the closest warehouse with complete stock, reducing shipping distances and transit times."}
        ],
        "related_links": [
            {"title": "Procurement & Vendor Management", "link": "services/procurement.html", "tag": "Upstream Service", "desc": "Automate supplier purchase orders generated by inventory replenishment triggers."},
            {"title": "Logistics & Distribution", "link": "services/logistics.html", "tag": "Downstream Service", "desc": "Coordinate carrier dispatch and freight tracking for completed warehouse orders."},
            {"title": "Logistics & Supply Chain Industry", "link": "industries/logistics.html", "tag": "Industry Focus", "desc": "Enterprise solutions for third-party logistics and global distribution operations."}
        ]
    },
    {
        "rel_path": "services/procurement.html",
        "category_badge": "DIGITAL COMMERCE & SUPPLY CHAIN",
        "page_title": "Procurement & Vendor Management",
        "page_subtitle": "Digital purchase requisitions, approval workflows, supplier onboarding, vendor portals, purchase order management, invoice workflows, and spend visibility.",
        "seo_desc": "Nova Arc Procurement & Vendor Management: Digital purchase requisitions, automated approval workflows, vendor portals, and 3-way invoice matching.",
        "breadcrumbs": [("Home", "index.html"), ("Services", "services.html"), ("Digital Commerce", "services/digital-commerce.html"), ("Procurement & Vendor Management", None)],
        "overview_paragraphs": [
            "Corporate procurement processes are frequently hindered by decentralized purchasing, cumbersome manual approvals, missing contract terms, and time-consuming invoice reconciliations that tie up accounts payable teams.",
            "Nova Arc develops centralized Procurement & Vendor Management platforms that enforce spending policies, streamline purchase requisition approvals, and provide secure self-service portals for external suppliers.",
            "Our platforms automate the entire procure-to-pay (P2P) cycle. By digitizing supplier onboarding, tracking vendor compliance, and automating three-way matching, we help organizations eliminate maverick spend, capture early payment discounts, and gain complete control over corporate expenditures."
        ],
        "capabilities": [
            {"title": "Digital Purchase Requisitions", "desc": "Intuitive employee purchase request portals with automatic budget checks, department tagging, and category routing.", "points": ["Catalog-based requisitioning", "Budget pre-check validation", "Multi-department expense splitting", "Mobile requisition submission"]},
            {"title": "Configurable Approval Hierarchies", "desc": "Dynamic approval routing that evaluates spending thresholds, department budgets, and expense types to assign approvers.", "points": ["Threshold-based approval matrices", "Out-of-office delegation rules", "Automated email/app approvals", "SLA escalation timers"]},
            {"title": "Vendor Portals & Onboarding", "desc": "Self-service supplier registration, tax document collection (W-9/GST), banking detail verification, and compliance tracking.", "points": ["Digital supplier self-onboarding", "Secure banking detail capture", "Contract & insurance tracking", "Vendor performance scorecards"]},
            {"title": "Automated 3-Way Invoice Matching", "desc": "Intelligent matching comparing purchase orders, warehouse receiving slips, and supplier invoices to approve payments.", "points": ["Line-item variance tolerance checks", "Automated exception routing", "Early payment discount capture", "Direct ERP ledger posting"]}
        ],
        "challenges": [
            {"challenge": "Uncontrolled Maverick Spending", "impact": "Employees buy supplies outside contracted vendor catalogs, losing volume discounts and blowing project budgets.", "solution": "We enforce strict requisition controls where non-catalog purchases require explicit executive justification and approval."},
            {"challenge": "Slow Purchase Order Approvals", "impact": "Critical purchasing requests get buried in manager inboxes, delaying project timelines and operational procurement.", "solution": "Our mobile-enabled approval workflows allow managers to approve requests in one click, auto-escalating overdue approvals."},
            {"challenge": "Accounts Payable Reconciliation Burden", "impact": "AP accountants spend hundreds of hours manually comparing paper invoices against POs to identify billing overcharges.", "solution": "We automate three-way matching, auto-clearing 80%+ of invoices within pre-set price and quantity tolerance thresholds."}
        ],
        "workflow_steps": [
            {"step": "01", "title": "Procurement Audit", "desc": "Reviewing existing approval chains, purchasing policies, vendor contracts, and ERP accounting interfaces."},
            {"step": "02", "title": "Workflow Architecture", "desc": "Configuring approval matrices, spending limits, vendor onboarding forms, and invoice matching tolerances."},
            {"step": "03", "title": "Portal & ERP Integration", "desc": "Building employee requisition interfaces, secure supplier portals, and bidirectional ERP data sync."},
            {"step": "04", "title": "Rollout & Vendor Adoption", "desc": "Onboarding suppliers to the digital portal, conducting employee training, and activating automated invoice matching."}
        ],
        "outcomes": [
            {"title": "100% Spend Compliance", "desc": "Ensure every corporate expenditure is pre-approved and routed through contracted supplier agreements."},
            {"title": "75% Faster Approval Cycles", "desc": "Reduce purchase requisition turnaround from weeks to hours with automated notifications and mobile approvals."},
            {"title": "Eliminated Invoice Discrepancies", "desc": "Automated 3-way matching catches pricing overcharges and duplicate billing before funds are disbursed."},
            {"title": "Enhanced Supplier Collaboration", "desc": "Suppliers gain transparent self-service visibility into POs, delivery receipts, and expected payment dates."}
        ],
        "related_links": [
            {"title": "Supply Chain Management", "link": "services/supply-chain-management.html", "tag": "Downstream Service", "desc": "Tie procurement purchase orders directly to warehouse replenishment requirements."},
            {"title": "Enterprise Business Solutions", "link": "services/enterprise-business.html", "tag": "Core Domain", "desc": "Integrate procurement workflows with enterprise financial systems and ERP ledgers."},
            {"title": "Enterprise & Professional Services", "link": "industries/enterprise.html", "tag": "Industry Focus", "desc": "Tailored procurement and spend governance for corporate and professional firms."}
        ]
    },
    {
        "rel_path": "services/logistics.html",
        "category_badge": "DIGITAL COMMERCE & SUPPLY CHAIN",
        "page_title": "Logistics & Distribution",
        "page_subtitle": "Transportation management, shipment tracking, dispatch coordination, route planning, delivery visibility, and logistics performance analytics.",
        "seo_desc": "Nova Arc Logistics & Distribution: Transportation management, shipment tracking, dispatch coordination, and route planning analytics.",
        "breadcrumbs": [("Home", "index.html"), ("Services", "services.html"), ("Digital Commerce", "services/digital-commerce.html"), ("Logistics & Distribution", None)],
        "overview_paragraphs": [
            "Efficient logistics and freight distribution require coordinated communication between shippers, dispatchers, commercial drivers, and receiving docks across complex multi-modal transit networks.",
            "Nova Arc engineers Transportation Management Systems (TMS) and logistics distribution platforms that optimize carrier selection, plan dynamic delivery routes, coordinate warehouse dock loading, and provide real-time shipment visibility.",
            "By aggregating GPS carrier telemetry, automating dispatch assignments, and tracking delivery milestones digitally, our solutions lower fleet fuel expenditures, reduce driver dwell times, and provide customers with accurate, reliable delivery updates."
        ],
        "capabilities": [
            {"title": "Transportation Management (TMS)", "desc": "Centralized freight management managing carrier rate cards, tender assignments, load consolidation, and billing reconciliation.", "points": ["Automated load tendering", "Carrier rate comparison", "Multi-stop load consolidation", "Freight bill audit & payment"]},
            {"title": "Real-Time Shipment Visibility", "desc": "Live freight tracking integrating with commercial telematics, ELD devices, and carrier APIs to report accurate transit milestones.", "points": ["GPS tracking integration", "Geofence arrival/departure alerts", "Dynamic ETA calculations", "Proactive delay notifications"]},
            {"title": "Dispatch & Route Optimization", "desc": "Algorithmic routing engines that evaluate vehicle capacity, delivery time windows, traffic, and driver hours of service (HOS).", "points": ["Multi-drop route planning", "Vehicle weight & cube optimization", "Driver dispatch mobile app", "Turn-by-turn route compliance"]},
            {"title": "Digital Proof of Delivery (ePOD)", "desc": "Mobile driver capture for electronic customer signatures, delivery photos, barcode package scans, and exception notes.", "points": ["Digital signature capture", "Timestamped photo verification", "Shortage & damage exception logging", "Instant billing trigger"]}
        ],
        "challenges": [
            {"challenge": "Unreliable Delivery ETAs", "impact": "Customers call customer service repeatedly asking for delivery statuses because carrier milestones are outdated or missing.", "solution": "We deploy real-time telemetry pipelines that recalculate ETAs dynamically based on traffic and route progress, sending automated alerts."},
            {"challenge": "High Dwell Times & Detention Fees", "impact": "Trucks sit idle at congested warehouse docks for hours, resulting in substantial carrier detention fees and driver frustration.", "solution": "Our dock appointment scheduling module coordinates arrival slots with warehouse labor availability to minimize dock dwell times."},
            {"challenge": "Lost Paperwork & Delayed Billing", "impact": "Paper delivery receipts get lost or damaged, delaying customer invoicing and creating accounts receivable delays.", "solution": "We implement mobile electronic proof of delivery (ePOD) that instantly uploads signatures and photos to trigger immediate customer invoicing."}
        ],
        "workflow_steps": [
            {"step": "01", "title": "Logistics Audit", "desc": "Evaluating shipping volumes, freight corridors, carrier agreements, dock capacities, and existing TMS/WMS tools."},
            {"step": "02", "title": "System Architecture", "desc": "Configuring route optimization algorithms, carrier rate matrices, geofencing parameters, and mobile interfaces."},
            {"step": "03", "title": "Carrier & Telematics Integration", "desc": "Connecting carrier EDI/API networks, commercial ELD feeds, and ERP sales order databases."},
            {"step": "04", "title": "Rollout & Fleet Training", "desc": "Deploying the mobile driver application, training dispatchers, and activating live customer tracking portals."}
        ],
        "outcomes": [
            {"title": "15-20% Lower Fleet Fuel Costs", "desc": "Optimized delivery routing reduces total fleet mileage and eliminates redundant transit loops."},
            {"title": "Eliminated Detention Penalties", "desc": "Scheduled dock appointments ensure trucks are unloaded promptly upon arrival, avoiding carrier detention fees."},
            {"title": "Instant Invoicing Upon Delivery", "desc": "Electronic proof of delivery (ePOD) uploads instantly to trigger billing within minutes of customer handoff."},
            {"title": "95%+ On-Time Delivery Rates", "desc": "Proactive route optimization and traffic adaptation help fleets consistently meet strict customer delivery windows."}
        ],
        "related_links": [
            {"title": "Logistics & Supply Chain Industry", "link": "industries/logistics.html", "tag": "Industry Focus", "desc": "Explore complete industry solutions for third-party logistics providers and freight carriers."},
            {"title": "Supply Chain Management", "link": "services/supply-chain-management.html", "tag": "Upstream Service", "desc": "Coordinate warehouse inventory and order pick/pack with transportation dispatch."},
            {"title": "Intelligent Monitoring & IoT", "link": "services/intelligent-monitoring.html", "tag": "Related Domain", "desc": "Vehicle fleet telematics, fuel monitoring, and environmental tracking."}
        ]
    }
]
print(f"Loaded {len(SERVICES_PAGES)} services pages (Domain 1 + subpages).")
