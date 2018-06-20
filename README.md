# Maps Distance Matrix Generator
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com) [![HitCount](http://hits.dwyl.io/heronimus/Maps_Distance_Matrix.svg)](http://hits.dwyl.io/heronimus/Maps_Distance_Matrix)

About a month ago my friends ask me to make some script to generate some data. She want to make a scheduling job using saving matrix algorithm, but she found a problem when it comes to create a distance matrix between some places based on Google Maps distance. Instead of manually doing that, I create this **Maps Distance and Duration Matrix Generator** from provided location longitude and latitude by using Google Maps Distance Matrix API.

## Requirements
  - List of place name, longitude, and latitude provided on **coordinate.csv** file.
    (For example see : [coordinate.csv](coordinate.csv))
  - Python 3
  - Python package : simplejson (to install : ``` pip install simplejson ```)

## Usage
To generate your matrix, run this command inside this project folder.
```python
  python maps_matrix.py
```
After execute command above, you will see two generated file named ``` distance_matrix.csv ``` and ```duration_matrix.csv```.

## Important Notes
  - CSV format I use here is Microsoft Excel format, using `;` (semicolon) as separator.
  - Google Maps Distance Matrix API limits your free request up to **2500 request/day**. After reach your limit the distance/duration data inside the matrix will be write as **error**.  
  - If you have Google Maps API Key, for now you can add it manually to the code on variable `url`.

##### :) heronimus (github.com/heronimus)
