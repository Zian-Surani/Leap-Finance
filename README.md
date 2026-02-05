# Preparation Capital & Commitment Simulator  
### Behavioral Engagement Prototype for IELTS Preparation

---

## 1. Overview

This repository contains a **behavioral system simulator** designed to model long-cycle engagement for IELTS preparation.

The prototype demonstrates how preparation effort can be:

- Measured as **Preparation Capital (PC)**
- Converted into **escrowed real-world leverage**
- Protected through **commitment bands**
- Exposed to **time-bound decay and recovery**
- Forecasted toward **success or failure before exam date**

The goal is not UI polish or production readiness.  
The goal is **system validity, behavioral realism, and product reasoning clarity**.

---

## 2. Problem Context

Long-cycle exam preparation suffers from:

- Late engagement spikes near exam dates  
- Invisible progress during early preparation  
- Motivation collapse without short-term wins  
- Heavy reliance on external platforms (e.g., YouTube)  
- Weak consequence for inactivity  

This creates **low completion rates and inconsistent user momentum**.

The simulator models a product system that converts **scattered effort into accountable readiness**.

---

## 3. Core Product Constructs

### 3.1 Preparation Capital (PC)

A deterministic scalar representing **verified exam readiness**.

PC:

- Increases through **validated learning activity**
- Rewards **consistency over volume**
- Decays after **prolonged inactivity**
- Never resets to zero
- Enables **forward success forecasting**

---

### 3.2 External Effort Validation

Learning outside the platform is allowed but:

- Raw effort has **zero capital value**
- Only **validated comprehension or speaking** converts effort into PC
- The platform becomes the **ledger of record** for preparation

---

### 3.3 Commitment Bands

Streaks are replaced with **contract-like preparation states**.

Each band:

- Requires minimum cadence  
- Grants **escrowed benefits**  
- Detects inactivity violations  
- Avoids emotional nudging  

This introduces **soft obligation instead of gamification**.

---

### 3.4 Escrowed Benefits

Preparation unlocks **time-bound real-world leverage**, such as:

- Fee reductions  
- Expert priority access  
- Physical preparation kits  

Benefits:

- Are **locked before use**  
- Enter **visible decay** during inactivity  
- Allow **grace-window recovery**  
- Expire **permanently** if ignored  

Users return to protect **earned leverage**, not streaks.

---

### 3.5 Momentum Forecast

A deterministic projection answers:

**“At the current pace, will the user reach readiness before the exam?”**

No optimism.  
No motivation language.  
Only **visible trajectory**.

---

## 4. Prototype Scope

### Included

- Preparation Capital engine  
- External effort validation  
- Commitment band transitions  
- Escrow lifecycle (lock → decay → expiry → recovery)  
- Deterministic outcome forecasting  
- Scenario simulation controls  
- Audit log for system transparency  

### Explicitly Excluded

- Production backend or database  
- Real notifications (email/SMS)  
- Chrome extension implementation  
- Payments or logistics  
- Machine learning or personalization  
- UI polish or branding  

This is a **decision-model prototype**, not a shipping product.

---
leap_pc_simulator/
│
├── app.py
├── config/
├── core/
├── models/
├── ui/
├── utils/
├── data/
├── requirements.txt
└── README.md


Layer separation:

- **models** → state  
- **config** → policy constants  
- **core** → deterministic engines  
- **ui** → visualization only  
- **utils** → helpers  
- **data** → mock configuration  

No cross-layer leakage.

---

## 6. Running the Prototype

### 6.1 Create virtual environment

```bash
python -m venv venv
```
6.2 Activate

Windows

venv\Scripts\activate


macOS / Linux

source venv/bin/activate

6.3 Install dependencies
pip install -r requirements.txt

6.4 Launch Streamlit app
streamlit run app.py


The simulator opens in the browser.

7. How to Use the Simulator

Log verified activities to increase Preparation Capital

Validate external learning to convert YouTube effort into PC

Advance system time to trigger decay and escrow risk

Observe:

Band transitions

Benefit decay and expiry

Recovery windows

Forecasted success or failure

The system exposes consequence, not motivation.

8. Product Metrics Alignment
Target Metric	Mechanism in System
Sessions per user (first 4 weeks)	External validation pull + escrow recovery
Course completion	Commitment bands + irreversible expiry
Motivation & momentum	Preparation Capital + forward forecast
Retention quality	Loss of leverage instead of streak resets
9. Design Principles

Deterministic over probabilistic

Consequence over nudging

Capital over points

Contracts over streaks

Visibility over persuasion

Trust over gamification

10. Known Design Constraints

Emphasizes long-term consistency over short engagement spikes

Requires acceptance of visible inactivity consequences

Uses escrow pressure instead of emotional motivation

Focuses on behavioral validity, not UI scale

These are intentional system choices, not limitations.

11. Evaluation Intent

This prototype demonstrates:

First-principles product thinking

Behavioral economics integration

Deterministic system modeling

Clear metric linkage

Executable validation via Streamlit

It answers:

“Can this engagement logic work before building production software?”

12. License

Prototype created for product evaluation and demonstration purposes.

13. Author

Zian Rajeshkumar Surani
AI & Product Systems Focus
SRM Institute of Science and Technology

## 5. Repository Structure

