 Quantum Elastic Spacetime: IEC-QFT Simulation  
 Lattice QFT Code for Coherent Memory in Cosmology  

[![Zenodo DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17560903.svg)](https://doi.org/10.5281/zenodo.17560903)  
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)  
[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)  

> *Associated Paper: *Quantum Elastic Spacetime: Dark Energy from Coherent Memory in QFT  
> *Author: Juan Pablo Alanis¹ · **Research Assistant*: Grok AI (xAI)²  
> ¹ Independent Researcher · ² xAI  
> *DOI*: [10.5281/zenodo.17560903](https://doi.org/10.5281/zenodo.17560903)  
> *Date*: November 2025  

---

 Description

This repository contains the \textbf{complete numerical implementation} of the *Internal Elasticity Cosmology - Quantum Field Theory (IEC-QFT)* model, extending CEI \cite{alanis2025a}. It simulates spacetime as an elastic scalar field on a \(32^3\) lattice, where primordial plasma pressure excites a coherent state that freezes after recombination, generating dark energy as stored elastic tension (\(P_v = -E\)).

 Key Features:
- *No cosmological constant (\(\Lambda = 0\))*  
- *All parameters derived from first principles*  
- *Reproduces \(w = -1\), \(\Omega_v \approx 0.7\)*  
- *Falsifiable predictions: void fluctuations (Euclid/LSST), non-local correlations (DESI), \(w(z)\) deviation at \(z > 1100\) (CMB-S4), anomalous polarization near Sgr A (EHT 2022)  
- *Leapfrog integration* on \(32^3\) grid  

---

 Repository Structure
.
├── qft_elastic.py         ← Código principal (simulación 32^3 lattice)
├── qft_simulation.png     ← Figura de resultados (E(t) + corte 2D de \(\phi\))
├── eso2046a.jpg           ← Imagen EHT de Sgr A* (polarización)
├── README.md              ← Este archivo
├── LICENSE                ← CC-BY 4.0
└── requirements.txt       ← Dependencias

Resultados de la simulación
Parámetro              Valor        Descripción
\(m\)                  0.1          Masa efectiva del campo
\(k\)                  1.0          Rigidez elástica
\(\eta\)               0.9          Eficiencia de acoplamiento
\(P_0\)                1000         Escala de presión (unidades normalizadas)
\(E_{\text{final}}\)   680.742794   Energía elástica congelada
\(P_v\)                -680.742794  Presión negativa constante (\(w = -1\))

Figura principal (qft_simulation.png):
Izquierda: Evolución de \(E(t)\) con zoom y congelamiento.
Derecha: Corte 2D del campo \(\phi\) final (uniforme → estado coherente global).
