# Machine Learning Project (Random Forest Regression)

## Introduction
In this project, we develop a machine learning model using specific data. The goal is Gender Recognition by Voice and Speech Analysis.

## Data fields

The database contain of the following columns:

| Column Name       | Data Type    | Description                                          |
|-------------------|--------------|-----------------------------------------------------|
| `meanfreq`        | float64          | Mean frequency                                       |
| `sd`              | float64          | Standard deviation of frequency                      |
| `median`          | float64          | Median frequency                                     |
| `Q25`             | float64          | First quantile                                      |
| `Q75`             | float64          | Third quantile                                      |
| `IQR`             | float64          | Interquantile range                                 |
| `skew`            | float64            | Skewness (see note in specprop description)        |
| `kurt`            | float64        | Kurtosis (see note in specprop description)        |
| `sp.ent`          | float64          | Spectral entropy                                    |
| `sfm`             | float64          | Spectral flatness                                   |
| `mode`            | float64          | Mode frequency                                      |
| `centroid`        | float64           | Frequency centroid (see specprop)                  |
| `peakf`           | float64          | Peak frequency (frequency with highest energy)      |
| `meanfun`         | float64            | Average of fundamental frequency across acoustic signal |
| `minfun`          | float64            | Minimum fundamental frequency across acoustic signal |
| `maxfun`          | float64            | Maximum fundamental frequency across acoustic signal |
| `meandom`         | float64           | Average of dominant frequency across acoustic signal |
| `mindom`          | float64           | Minimum of dominant frequency across acoustic signal |
| `maxdom`          | float64            | Maximum of dominant frequency across acoustic signal |
| `dfrange`         | float64            | Range of dominant frequency across acoustic signal   |
| `modindx`         | float64            | Modulation index (calculated from absolute differences between adjacent fundamental frequencies divided by frequency range) |
| `label`           | string            | Male or female                                      |


## Data Source
The following data file was used in this project:

- [kaggle](https://www.kaggle.com/datasets/primaryobjects/voicegender)


## Requirements
- [Python 3.x]
- [Required libraries (seaborn, NumPy, Pandas, scikit-learn,)]

## Contributing
If you would like to contribute to the project, please follow these steps:


