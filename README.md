# Quadcopter Dynamics Simulator

This project implements a quadcopter simulation from first principles using Python.
The goal is to understand the underlying dynamics, numerical simulation, and feedback
control involved in autonomous aerial vehicles, without relying on existing autopilot
or robotics frameworks.

---

## Phase 0: Baseline Dynamics (Completed)

**Objective:**  
Establish a physically correct simulation foundation.

**Implemented:**
- 1D vertical (altitude) dynamics
- State-space formulation
- Open-loop numerical simulation
- Validation via expected parabolic motion under constant thrust

---

## Phase 1: Closed-Loop Control (Completed)

**Objective:**  
Stabilize the quadcopter altitude using feedback control.

**Implemented:**
- PID controller for altitude control
- Hover thrust compensation
- Closed-loop simulation
- Verification via stable convergence to a desired height

---

## Phase 2: Sensor Modeling (Completed)

**Objective:**  
Introduce realism by separating true state from measured state.

**Implemented:**
- Noisy altitude (altimeter) sensor model
- Controller operating on noisy measurements
- Observation of steady-state jitter due to sensor noise
- Validation of closed-loop robustness under realistic sensing

---

## Phase 3: State Estimation (Completed)

**Objective:**  
Estimate the quadcopter’s true altitude and vertical velocity from noisy sensor
measurements using a model-based state estimator.

**Implemented:**
- Linear Kalman Filter for 1D vertical motion
- State vector: altitude and vertical velocity
- Prediction step using the system’s physical model
- Measurement update using a noisy altimeter
- Proper separation of control and estimation loops

**Results:**
- Estimated altitude closely tracks the true simulated state
- Measurement noise is significantly reduced compared to raw sensor data
- Stable estimation without divergence or excessive lag
- Demonstrates correct fusion of model dynamics and sensor measurements


## Motivation

This project is intended to build intuition for what real autopilot stacks
(e.g., PX4) abstract away by implementing the core components from scratch.
The simulator is developed incrementally, with each phase adding one layer
of realism.
