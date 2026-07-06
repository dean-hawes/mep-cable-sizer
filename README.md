# Automated MEP Cable Sizer & Volt-Drop Calculator

An automated, data-driven engineering tool written in Python that sizes electrical conductors based on voltage drop constraints. This utility handles both single-phase and three-phase circuits, validating system parameters against target tolerances using industry-standard engineering formulas.

## 🚀 Features
- **Dynamic Phase Toggling:** Supports both single-phase and balanced three-phase calculations.
- **Automated Conductor Selection:** Uses `pandas` to dynamically scan, sort, and filter structural cable databases, selecting the most economical wire cross-section ($mm^2$) that guarantees compliance.
- **Robust Error Handling:** Features deep input verification using localized `try-except-else` runtime protection blocks to defend against user entry exceptions and value boundary violations.
- **Persistent Iteration Loops:** Includes an application execution lifecycle loop allowing engineers to perform sequential runtime iterations without restarting the environment.

---

## 📐 Engineering Methodology

The application evaluates allowable circuit resistance parameters by rearranging fundamental AC thermal and physical voltage-drop equations.

### Single-Phase Formula
$R_{\text{wire}}$ = $V_{\text{drop}}$ / (2 * $I$ * $L$)

### Three-Phase Formula
$R_{\text{wire}}$ = $V_{\text{drop}}$ / (sqrt(3) * $I$ * $L$)

Where:
- $I$ = Design load current (Amps)
- $L$ = Length of the circuit run (Meters)
- $R_{\text{wire}}$ = Maximum allowable conductor impedance ($\Omega/m$)
- $V_{\text{drop}}$ = 3% volt drop

---

## 🛠️ Tech Stack & Requirements

- **Language:** Python 3.x
- **Libraries:** `pandas`, `math`
- **Data Source:** Structured CSV catalog containing international standard metric wire properties ($mm^2$ area vs. line resistance specifications).

---

## 💻 How to Run

1. Clone the repository to your local system:
   ```bash
   git clone [https://github.com/dean-hawes/mep-cable-sizer](https://github.com/dean-hawes/mep-cable-sizer)

2. Ensure pandas is installed:
    ```bash
    pip install pandas

3. Execute python script:
    ```bash
    python script.py

---

## ⚙️ Repository Version Control Architecture

This project is actively developed utilizing strict industry version control and code production methodologies:

- Model-Based Isolation: All feature implementation tasks are developed isolated on sandboxed `feature/` branches before integration verification.

- Clean Environment Compliance: Utilizes an active system-level `.gitignore` footprint matrix to suppress OS metadata debris (`.DS_Store`) and runtime execution footprint files (`__pycache__/`).