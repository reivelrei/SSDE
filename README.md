# Secondary Structure Data Exploration
Code behind the Secondary Structure Data Exploration

## Table of Contents

* [Requirements](#requirements)
* [Usage](#usage)
* [Overview of file formats used](#Overview-of-file-formats)
* [Contact](#contact)
* [License](#license)

## Requirements

In the requirements.txt all required packages are listed.

To install your packages using requirements.txt, execute the following:
1. Open a terminal or command prompt
2. Navigate to the folder with your requirements.txt
3. ``` pip3 install -r requirements.txt```
4. You are done installing dependencies

## Usage:

```
main.sh
python3 convert.py
python3 tsne_dbscan.py
```
Keep in mind that in the current version all paths to the files in the files must be changed. 

## Overview of file formats
Only the following file formats are accepted and processed by SSDE:
```
### Genome Assembly (for example TAIR10) 
>Chr1
CCCTAAAC...
...
...
>Chr5
CCCTAAAC...
...


### .bed 6-column 
chrom start     stop    name        score   strand
Chr1  6879	6888	AT1G01020.1	13.7434	-

```

## Contact

For questions or problems, please feel free to write an email and I will get back to you as soon as possible.

[msohn@techfak.uni-bielefeld.de](mailto:msohn@techfak.uni-bielefeld.de)
.

## License

* The sklearn package is licensed under the [BSD 3 license](https://github.com/scikit-learn/scikit-learn/blob/main/COPYING).
* The numpy package is licensed under the [BSD 3 license](https://github.com/numpy/numpy/blob/main/LICENSE.txt).
* The matplotlib package is licensed under the [PSF license](https://github.com/matplotlib/matplotlib/blob/master/LICENSE/LICENSE).

