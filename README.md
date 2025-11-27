**Disciplina:** Rețele Neuronale  
**Instituție:** POLITEHNICA București – FIIR  
**Student:** [Caraiman Petrisor Stefan]  
**Data:** [20.11.2025]  

## Introducere

## 1.Structura Repository-ului Github

```
project-name/
├── README.md
├── docs/
│   └── datasets/          # descriere seturi de date, surse, diagrame
├── data/
│   ├── raw/               # date brute
│   ├── processed/         # date curățate și transformate
│   ├── train/             # set de instruire
│   ├── validation/        # set de validare
│   └── test/              # set de testare
├── src/
│   ├── preprocessing/     # funcții pentru preprocesare
│   ├── data_acquisition/  # generare / achiziție date (dacă există)
│   └── neural_network/    # implementarea RN (în etapa următoare)
├── config/                # fișiere de configurare
└── requirements.txt       # dependențe Python (dacă aplica bil)
```

## 2. Descriere Setului de date

### 2.1 Sursa datelor

* **Origine:** [(Constantin Stancescu si alti;Album de proiectare 3D cu AutoCAD,Editura Fast,2004),[Universitatea Tehnică "Gheorghe Asachi"-Interfața utilizator. Descrierea funcțiilor elementelor ferestrei de lucru](https://sim.tuiasi.ro/wp-content/uploads/2020/04/Grafica-industriala-in-ingineria-materialelor-complet.pdf) , [Universitatea Tehnică din Cluj-Napoca-8.1 Reprezentarea arborilor și axelor](https://gdgi.utcluj.ro/scurtu%20doc/scurtu/Laboratoare%20DTI_IM_MTR/C10.pdf)]
* **Modul de achiziție:** ☐ Senzori reali / ☐ Simulare / ☐ Fișier extern / ☐ Generare programatică
* **Perioada / condițiile colectării:** []

### 2.2 Caracteristicile dataset-ului

* **Număr total de observații:** [Ex: 15,000]
* **Număr de caracteristici (features):** [Ex: 12]
* **Tipuri de date:** ☐ Imagini
* **Format fișiere:** ☐ JPEG / ☐ PNG / ☐ Altele: [...]

### 2.3 Descrierea fiecărei caracteristici

| **Caracteristică** | **Tip** | **Unitate** | **Descriere** | **Domeniu valori** |
|-------------------|---------|-------------|---------------|--------------------|

## 3, Analiza Exploratorie a Datelor (EDA) - Sintetic

### 3.1 Statistici descriptive aplicate

*
*
*
*

### 3.2 Analiza calităților datelor

*
*
*

### 3.3 Probleme identificate

*
*
*

## 4. Preprocesare Datelor

### 4.1 Curățarea datelor

*
*



### 4.2 Transformarea caracteristicilor

*
*
*

### 4.3 Structurarea seturilor de date

**

### 4.4 Salvarea rezultatelor preprocesării

##  5. Fișiere Generate în Această Etapă

##  6. Stare Etapă

- [x] Structură repository configurată
- [ ] Dataset analizat (EDA realizată)
- [ ] Date preprocesate
- [ ] Seturi train/val/test generate
- [ ] Documentație actualizată în README + `data/README.md`

<!-- todo: Căutare poze brute si pentru test ,Resize(120x120) si scoaterea outline cu labview -->
<!-- [Image borders](https://www.ni.com/docs/en-US/bundle/ni-vision/page/image-borders.html?srsltid=AfmBOoqNhvKpEyzseq3GRL_0QCm7rd6JyF8OyngowavB21bIEYFMH5zL) -->
<!-- [Extracting Drop Outline](https://forums.ni.com/t5/LabVIEW/Extracting-Drop-Outline/td-p/749026) -->