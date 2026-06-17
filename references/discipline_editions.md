# Discipline Editions - Domain-Specific Models
When analyzing papers from specific disciplines, apply these specialized criteria.
---

## Remote Sensing Edition
### Key Evaluation Dimensions
- Spatial resolution improvement vs. existing methods
- Temporal frequency analysis capability
- Spectral band utilization and fusion methods
- Cloud/shadow handling techniques
- Ground truth data quality and quantity
- Study area representativeness (single site vs. multi-region)
- Code/data availability for reproducibility
- Transferability to other regions/sensors

### Preferred Methods (2024-2025)
- Self-supervised learning for label-efficient mapping
- Foundation models (SpectralGPT, SatMAE, DOFA)
- Change detection with contrastive learning
- Multi-modal fusion (SAR + Optical, HS + MS)
- Pan-sharpening with deep learning
- OBIA with Graph Neural Networks
- Spatio-temporal fusion and prediction
- Physics-guided neural networks

### Preferred Data Sources
- Sentinel-2 (10m MSI) - most common for land cover
- Sentinel-1 (C-band SAR) - cloud-penetrating
- Landsat 8/9 (30m OLI) - long time series
- MODIS (250-1000m) - global scale, daily
- GaoFen series (GF-1/2/6) - Chinese high-res
- PlanetScope/Dove (3m) - daily global coverage
- UAV/drone imagery - sub-meter, flexible
- ICESat-2 / GEDI - LiDAR for 3D structure

### Journal Fit Guidelines
- High-res urban/forest mapping => RSE, ISPRS JPRS, TGRS
- SAR method development => TGRS, GRSL, IEEE JSTARS
- Deep learning method => TGRS, RSE, Pattern Recognition
- Regional application (single area) => Remote Sensing (MDPI)
- Global mapping => Scientific Data, Nature Sci Reports
- Ecology + RS => Landscape Ecology, Ecological Indicators

---
## Ecology & Environmental Science Edition
### Key Evaluation Dimensions
- Experimental design rigor (replicates, controls, randomization)
- Study duration (single season vs. multi-year)
- Spatial scale (plot, landscape, regional, global)
- Sample size adequacy and statistical power
- Taxonomic resolution and identification accuracy
- Mechanistic understanding vs. correlational patterns
- Climate/human impact quantification
- Biodiversity metrics and functional diversity

### Preferred Methods
- Structural equation modeling (SEM)
- Species distribution modeling (MaxEnt, BRT, RF)
- Meta-analysis and systematic review
- Bayesian hierarchical models
- Remote sensing + field data integration
- Isotope analysis (stable C, N, O)
- eDNA metabarcoding for biodiversity
- Time series analysis (Mann-Kendall, Breakpoints)
- Network analysis (food webs, species interactions)

### Journal Fit Guidelines
- Mechanistic experiments => Ecology Letters, J Ecology
- Large-scale patterns + big data => Global Change Biology
- Conservation application => Biological Conservation
- Indicator methods => Ecological Indicators
- Environmental monitoring => STOTEN, Environ Pollution
- Modeling focus => Ecological Modelling

---
## Medical & Biomedical Edition
### Key Evaluation Dimensions
- Clinical trial phase and registration
- Sample size and statistical power calculation
- Ethics approval and patient consent documentation
- Effect size and clinical significance
- Mechanism of action elucidation
- Reproducibility and validation in independent cohorts
- Translational potential (bench to bedside)
- Safety assessment and adverse event reporting

### Study Type by Journal Tier
- Nature/Science/Cell: Groundbreaking mechanisms, therapies
- NEJM/Lancet/JAMA: Phase 3 RCTs, large meta-analyses
- Nature Medicine: Translational studies, biomarker discovery
- Nature Comms: Well-done mechanistic + cohort studies
- PLoS Medicine: Public health, epidemiological studies
- BMC Medicine: Methodologically sound clinical research
- Frontiers series: Preliminary findings, pilot studies
- Medicine (Baltimore): Case reports, small case series

---
## Computer Science & AI Edition
### Key Evaluation Dimensions
- Theoretical contribution and formal guarantees
- Benchmark performance and standardized evaluation
- Reproducibility (code release, environments, seeds)
- Ablation studies and component analysis
- Computational efficiency (FLOPs, params, inference speed)
- Generalization to unseen domains/data
- Real-world applicability considerations
- Novelty vs. incremental improvement assessment

### Publication Venue Tiers (CCF)
- CCF-A: NeurIPS, ICML, CVPR, ICCV, AAAI, IJCAI, ACL, ICLR
- CCF-A Journals: TPAMI, IJCV, AIJ, JMLR, TIP, TIFS
- CCF-B: ECCV, EMNLP, ECAI, ICRA, IROS, AAMAS
- CCF-B Journals: TNNLS, TKDE, TMM, TC, TFS, PR
- CCF-C: ICIP, ICPR, ACCV, COLING, ICME
- CCF-C Journals: Neurocomputing, KBS, EAAI, NEUCOM, CAEE

### Current Hot Topics (2024-2025)
- Large Language Models (LLMs) and foundation models
- Multimodal learning (vision + language + audio)
- Diffusion models and generative AI
- AI for Science (AI4Science, AlphaFold, weather pred)
- Efficient deep learning (pruning, quantization, distill)
- Federated learning and privacy-preserving ML
- Causal inference and representation learning
- Embodied AI and robotics
- AI alignment and safety

### Submission Strategy by Paper Type
- Novel architecture + SOTA => NeurIPS/CVPR/ICML/ICLR
- Solid benchmark improvement => AAAI/IJCAI/ECCV
- Application with limited novelty => Neurocomputing/KBS/PR
- Survey/review => ACM Computing Surveys (IF 23.8)
- Interdisciplinary AI => Nature MI, Patterns, iScience