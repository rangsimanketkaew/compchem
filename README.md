# Guide for Theoretical/Computational Chemists <!-- omit in toc -->

## What is computational chemistry? <!-- omit in toc -->
tl;dr 
> Computational chemistry describes the use of computer modelling and simulation - 
> including ab initio approaches based on quantum chemistry, and empirical approaches - 
> to study the structures and properties of molecules and materials. 
> Computational chemistry is also used to describe the computational techniques 
> aimed at understanding the structure and properties of molecules and materials. 

## Research topics <!-- omit in toc -->

- Chemical reactions
- Photochemistry
- Catalyst design
- Potential energy surface
- Vibrational and electronic spectroscopy
- Solid-state chemistry
- Drug discovery, biomolecular docking
- Cheminformatics
- Machine learning

## Community <!-- omit in toc -->

- Conference: [WATOC](https://www.watoc.net/), [ICQC](https://en.wikipedia.org/wiki/International_Congress_of_Quantum_Chemistry), [APATCC](https://www.apatcc.org/)
- Journals: [A list of well-known journals that regularly publish computational chemistry articles](https://www.chemtheorist.com/comp-chem-journals.html)
- Forum: [StackExchange](https://chemistry.stackexchange.com/questions/tagged/computational-chemistry), [Matter Modeling](https://mattermodeling.stackexchange.com/)
- Mailing list: [CCL](http://www.ccl.net/)

## Skills needed to be a theoretical/computational chemist <!-- omit in toc -->

- [Core skills](#core-skills)
- [General technical skills](#general-technical-skills)
- [Essential skills for method development](#essential-skills-for-method-development)
- [Essential skills for software development](#essential-skills-for-software-development)
- [Essential skills for HPC](#essential-skills-for-hpc)
- [Essential skills for coding GPU](#essential-skills-for-coding-gpu)
- [Essential skills for machine learning (bonus)](#essential-skills-for-machine-learning-bonus)
- [Essential skills for machine learning chemistry (bonus)](#essential-skills-for-machine-learning-chemistry-bonus)

## Core skills

- Understanding of theoretical principles, including kinetics, thermodynamics, and quantum chemistry
- Various levels of programming, code development, and software architecture skills
- Problem-solving skills and an interest in solving basic and applied research problems
- Skills in adapting and integrating computer software to solve new categories of problems
- Critical thinking for analyzing and interpreting computational results and statistical data
- Googling and stackoverflowing :upside_down_face:

## General technical skills

- For Windows:
  - Install programs and modify system variables such as `PATH`
  - Install Nvidia CUDA toolkit and driver
  - Setup VPN and local network
  - Setup dual boost for Linux, or install WSL for Ubuntu
- For Linux and macOS:
  - Basic/intermediate commands: `ls`, `cd`, `cp`, `rm`, `ssh`, `scp`, and many more
  - Know some important files/folders: `.bashrc`, `.ssh`
  - Understand some environmen variables: `$PATH`, `$LD_LIBRARY_PATH`
- Scripting programming language
  - Bash, awk, perl, Python + Jupyter notebook
- Cluster / HPC
  - Understand terminology: master node, compute node, scheduler, CPU cores, processes, memory
  - Scheduler: Slurm, PBS, SGE
  - Software manager: module (`avail`, `load`, `unload`, `switch`)
- Software
  - Commercial: Gaussian, Q-Chem, ADF, MOLPRO, MOLCAS, TURBOMOLE and many more
  - Non-commercial: PySCF, Psi4, OpenMOLCAS, GAMESS, ORCA, NWChem, DIRAC, DALTON, CP2K, LAMMPS, VASP, QE and many more
  - Full list is [here](https://en.wikipedia.org/wiki/List_of_quantum_chemistry_and_solid-state_physics_software)
- Graphic visualization
  - JMol, Molden, Gaussview, Avogadro, UCSF Chimera, VMD, Ovito, PyMol
  - 2D and 3D plots
- Other useful tools
  - ASE, MDTraj, Pymatgen, RDKit, OpenBabel
- Writing
  - Microsoft Word
  - LaTeX
    - Compiler: pdflatex, xelatex, lualatex
    - Distribution: TeX Live, MikTeX
    - Editor: OverLeaf, TeXstudio, Texmaker
- Presentation
  - Powerpoint
  - LaTeX Beamer

## Essential skills for method development

- Linear algebra
  - Vectors and matrices
    - Geenral properties: Complex conjugate, transpose and conjugate transpose
    - Diagonalization
    - Matrix multiplication (Dense and sparse)
  - Operators & commutators
  - Eigen-problem
    - Jacobi iteration
    - Eigenvalue & eigenvector
    - Singular value decomposition
- Calculus
  - Numerical method
  - Differential equation & ODE
  - Vector calculus
- Data fitting
  - Taylor expansion
  - Polynomial interpolation
  - Least squeare approximation
- Finding roots
  - Bilinear interpolation
  - Newton-Raphson method
  - PDE
- Quantum chemistry
  - Understand electronic structures
    - Wavefunction and its properties, Hilbert space, linearity, Bra-Ket notation, Basis sets
  - Excited state, transition state, atomic/molecular bond
  - *Ab initio* (wavefunction-based) method
    - HF, MPn, CI, CC, MRCI, MSSCF, CASSCF, CASPT2
    - DMRG (matrix product states), FCIQMC
  - Density functional theory method
    - KS equation, exchange and correlation functionals
    - (Real-time) TDDFT
    - Tight-binding (DFTB)
    - Gaussian and plane wave method
  - Semi-empirical
  - Dynamic
    - Adiabatic and non-adiabatic methods
  - Other methods
    - QM/MM
- Molecular dynamics
  - Classical mechanics
  - Force field
  - Statistical mechanics
  - Enhanced sampling: Free energy, unbrella sampling, etc.
  - Monte Carlo method
- Material simulation
  - Multiscale modeling
  - Coarse grained
  - Condense matter simulation
- Programming (for mathematical proof)
  - Scripting language: Bash, Python
  - Intensive subroutine with OOP: C++, Fortran
  - Symbolic programming (Mathematica, SymPy)

## Essential skills for software development

- Tex editor
  - Vi/Vim, Nano
  - VS Code, Atom, Eclipse, Sublime
- File format
  - XML, JSON
- General programming skills
  - Type of variables
  - Loops and conditional statement
  - Input/output
- High-level programming
  - Python
    - Pip and conda: Python helper
    - NumPy: Array (vector, matrix) computation
    - Numba: JIT compiler for NumPy
    - Jax: autograd of NumPy array
    - SciPy: a collection of math functions/routines
    - Scikit-learn: statistics routines, optimization, curve fitting
      - Intel Scikit-learn is 10x faster than the standard one
    - Matplotlib / Plotly for plotting graph
    - Theano: numerical computation
    - SCOOP: distributed modules for parallel programming
    - NetworkX: Graph library
- Low-level programming
  - C
    - Function, pointer, storage class
    - Enum, struct, union
    - Preprocessor
    - Operator, memory management, array
    - File handling
  - C++
    - C++ 11 or newer
    - Type of variable: signed, unsigned, long, double, etc.
    - Loops, conditional statement
    - Standard libraries: vector, rand
    - Understanding header (`.hpp`) and source file (`.cpp` or `.cc`)
    - Preprocessor (`#if`, `#ifdef`, `#ifndef`, `#define`, etc.)
    - Function, class, struct, template
    - Declaration
      - namespace, const, attribute, pointer, pass by reference, static_assert
    - Initialization
    - Misc: casting, lambda expression, encapsulation, file handling, exception handling
  - Fortran
    - Learn either F77 or F90 or modern fortran (2003, 2008, 2018)
    - Module, subroutine, function
    - Array (allocatable and multidimentional) and string
    - Operator overloading
    - Flow control
    - Derived type
    - Callback
    - Interfacing to other language e.g. Python or C++
  - GNU library
    - GSL
    - Many more libraries [here](https://en.wikipedia.org/wiki/List_of_GNU_packages)
- Memory allocation
  - Stack, heap, global memory
- Math libraries
  - BLAS (OpenBLAS)
  - LAPACK for linear algebra
  - ScaLAPACK - a higher level LAPACK
  - Intel MKL (Intel oneAPI)
  - FFTW: for computing the discrete Fourier transform in one or more dimensions, real and complex data
  - Eigen: linear algebra library
  - Boost: a collection of C++ functions e.g. `regex`, `serialization`
- QM libraries
  - libxc: XC function library
  - libint: For computing Gaussian integral
  - libcint: general GTO integrals
- Code optimization
  - Benchaming/scaling
  - Complexity (Big O)
- GNU
  - Static and dynamic libraries
  - Archive
  - Compiling (g++, gcc) and linking (ld)
  - Useful flags for compiler and linker e.g. `-O2`, `-O3`, `-fPIC`
- Compilng tools
  - autoconf
  - configure
  - Make, cmake, automake
- Debugging
  - gdb for general debugging
  - Valgrind for memory leak analysis
- Git (source code control)
  - Basic/intermediate commands
  - GitHub & GitLab
- Documentation
  - Sphinx (for markdown and reStructuredText)
  - Doxygen

## Essential skills for HPC

- Architecture
  - Memory management
  - Threading, multithreading
  - Block
- Parallel computing (SPMD)
  - Shared memory: OpenMP
  - Distributed memory: MPI
    - Implementations: OpenMPI, Intel MPI, MVAPICH
- Intel ecosystem
  - OpenMP compiler: icc, ifort
  - MPI compiler: mpicc, mpiicc (for Intel C compiler), mpicxx (for C++), mpiifort (for Fortran)
- Cloud computing (bonus)
- Server and database
- Networking

## Essential skills for coding GPU

- Intermediate/advanced C or C++ skills
- Programming model: Kernels, thread hierarchy, memory hierarchy, heterogeneous hierarchy, asynchronous SIMT
- CUDA
  - Understand CUDA operation:
    1. Declare and allocate host and device memory.
    2. Initialize host data.
    3. Transfer data from the host to the device.
    4. Execute one or more kernels.
    5. Transfer results from the device to the host.
  - CUDA C and CUDA C++ API
  - Compiler: nvcc

## Essential skills for machine learning (bonus)

- Basic math: linear algebra and calculus
- Programming
  - Python, R, Julia, Matlab
  - TensorFlow, PyTorch, Scikit-learn
- Python lib
  - NumPy
  - Pandas
- Terminology: regression, classification, descriptor, feature, kernel, activation function
- Data analysis/engineering: EDA, ETL
- Graphical representation
  - Histogram, bar plot, heatmaps
- ML algorithms
  - Decision tree
  - Random forest
  - Support vector machine
  - Principal component analysis
  - Kernel-ridge method
  - Neural network
    - Feedforward NN
      - Autoencoder
    - CNN
    - RNN (LSTM)
    - GNN
    - Adversarial NN
      - GAN
- Model training and optimization
  - Hyperparameter optimization
- Techniques to prevent overfittingTechniques
  - Data augmentation, early stopping, regularization, dropout, batch normalization
- Deploying model

## Essential skills for machine learning chemistry (bonus)

- Atomic and molecular representation
  - Structural-based: one-hot, fingerprint
  - Electronic-based: Coulomb matrix, BoB, Symmetry and Gaussian functions, Gaussian function and many more
- Configurational and chemical space
- Target prediction
  - Energy and force
  - Molecular properties: dipole moment, polarizability
- Database
  - PubChem
  - GDB
  - DrugBank
  - QM: QM7, QM8, QM9
