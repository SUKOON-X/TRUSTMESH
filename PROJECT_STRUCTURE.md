# Project Architecture

                           🏪 MARKETPLACE
                                 │
                          Orders / Sellers
                          Products / Returns
                          Payments / Shipping
                          Delivery / Inventory
                             Complaints
                                 │
                                 ↓
                          📡 EVENTS / APIs
                                 │
                                 ↓
                              KAFKA
                                 │
                                 ↓
                         EVENT WORKER
                                 │
                    ┌────────────┴────────────┐
                    ↓                         ↓
               Validate                  Deduplicate
                    └────────────┬────────────┘
                                 ↓
                         DETECTION ENGINE
                                 │
                    Rules / SQL / Anomaly
                                 ↓
                     🚨 COMPLIANCE SIGNAL
                                 │
                                 ↓
                         👨‍💼 SUPERVISOR
                                 │
                        
                                 |
                                 ↓                  
                        Specialist Agents            
                                 |
                                 ↓
                              Evidence
                                 ↓
                         👨‍💼 SUPERVISOR
                                 │
                         Finding + Recommendation
                                 ↓
                        📝 Approval Request
                                 ↓
                           PostgreSQL
                                 │
                       WebSocket / SSE
                                 ↓
                         ⚛️ REACT UI
                                 ↓
                            👤 HUMAN
                         ┌───────┴───────┐
                         ↓               ↓
                      APPROVE          REJECT
                         ↓               ↓
                   FastAPI            FastAPI
                         ↓
                  Authorization
                         ↓
                  Action Guard
                         ↓
                   Kill Switch
                         ↓
                 Execute Action
                         ↓
              ┌──────────┼───────────┐
              ↓          ↓           ↓
          Marketplace   Jira      Audit Log
                         │
                         ↓
                    MCP Server



## MARKETPLACE 
- Collect data from marketplace

### DATA 
- Seller Data
- Order Data
- Product Data
- Inventory Data
- Payment Data
- Complaint Data
- Return Data
- Delivery Data


## EVENTS 
- Where the data comes from 

### eg.
 "event_type": "ORDER_CANCELLED",
  "order_id": "ORD124",
  "seller_id": "SELLER456",
  "actor": "CUSTOMER",
  "reason": "CUSTOMER_CHANGED_MIND"


## EVENT BROKER
- It works like a breaker

### eg.
Now imagin 10,000 events arriving every second. You don't want to directly send all of them into our AI system. we put a waiting/transport system in between. That's the Event Broker.


## TRURSTMESH  (E-COMMERCE)
<!-- - System start from here  -->
- Control-tower platform for seller compliance across five business units: supervisor-led parallel specialist agents, custom MCP Jira server, Streamlit approvals, per-unit token budgets, kill switch; delivered discovery-to-training


## INGESTION
- This is first step where TRUSTMESH recieve incomming marketplace events from EVENT BROKER



## VALIDATATION
- Chech event validation for example suppose someone sends
"event_type": "ORDER_CANCELLED"
but there is not seller_id then system might say "invalid event"

### VALID EVENT MIGHT BE:
 "event_type": "ORDER_CANCELLED",
  "seller_id": "ABC",
  "order_id": "123",
  "timestamp": "..."


## DEDUPLICATION
- Make sure the same event isn't processed multiple times
like:
ORDER_CANCELLED
ORDER_CANCELLED
ORDER_CANCELLED

But in reality the order was cancelled only once. You don't want your system to think:
"Seller cancelled 3 orders."

It should recognize
"These are duplicate copies of the same event"

## DETECTION
- Does this data indicate a problem
One cancellation is probably normal:
1 cancellation → ✅ Normal

### But suppose we see:

Seller ABC
1,000 orders
350 cancellations

The system calculates: 350 / 1000 = 35%
Your marketplace rule might say: Cancellation rate must be < 10%

Therefore: 35% > 10%

"🚨 Potential compliance violation"

This is Detection

## INVESTINGATING SIGNAL
- Now the system has enough information to say:
"This deserves investigation"

So it creates an investigation signal.
Like:
{
  "signal_type": "HIGH_SELLER_CANCELLATION_RATE",
  "seller_id": "ABC",
  "severity": "HIGH",
  "cancellation_rate": 0.35
}


## CREATE JIRA ISSUES
- TRUSTMESH create jira issues through MCP (Model Context Protocol)

## SUPERVISOR AGENT
- Take decisions and according to the event decide which specialist agent to call or should I need more than two specialist agents and categorize the agents.

## SPECIALIST AGENTS
- Each specialist agents are master at their work
Like:
### SELLER AGENT

### ORDER AGENT

### PAYMENT AGENT

### INVENTORY AGENT

### COMPLAINT AGENT

### RETURN AGENT

### PRODUCT AGENT

### DELIVERY AGENT


## SUPERVISOR RECIEVES
- Supervisor agent recieve execution plan from SPECIALIST AGENTS 

## HUMAN
- HUMAN TAKE DECISION TO APPROVE OR REJECT THE ACTION 

## REJECT
- HUMAN CHOICE

## EXIT
- Shut down the current action and than exit

## APPROVE
- Human choice

## EXECUTE ACTION
- After approved, take decision to execute action

## UPDATE JIRA
- And after executed the action, update Jira through JIRA MCP. 


