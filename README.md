# IQA-measures


Implementation of two evaluation metrics to access the similarity between two images. The two metrics are as follows:

 * <i><a href="https://en.wikipedia.org/wiki/Peak_signal-to-noise_ratio">Peak signal-to-noise ratio (PSNR)</a></i>,
 * <i><a href="https://en.wikipedia.org/wiki/Root-mean-square_deviation">Root mean square error (RMSE)</a></i>, and


## Instructions

The following step-by-step instructions will guide you through installing this package and run evaluation using the command line tool.


### Install package

```bash
pip install IQA
```

For faster evaluation of the metric, the `pyfftw` package is required.
You can install it separately, or via the `speedups` extra:

```bash
pip install IQA[speedups]
```

You may also install the `rasterio` package to allow the CLI tool to use it for reading TIFF
images instead of OpenCV. It, too, is available as an extra:


```bash
pip install IQA[rasterio]
```


#### Installing the required libraries

First create a new virtual environment called `IQA-measures`, for example by using
[virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/):

```bash
mkvirtualenv --python=$(which python3.7) IQA-measures
```

Activate the new environment:

```bash
workon IQA-measures
```

Install the necessary Python libraries via:

```bash
bash setup.sh
```


### Usage

#### Parameters
```
  --org_img_path FILE   Path to original input image
  --pred_img_path FILE  Path to predicted image
  --metric METRIC       select an evaluation metric (fpsnr, rmse,
                        PCLOGSIM, all) (can be repeated)
```

#### Evaluation

For doing the evaluation, you can easily run the following command:

```bash
IQA --org_img_path=a.tif --pred_img_path=b.tif
```
The results are printed in machine-readable JSON, so you can redirect the output of the command into a file.


#### Usage in python

```bash
import IQA
from IQA.quality_metrics import rmse, psnr, PCLOGSIM
```

### Install package from source


#### Clone the repository

```bash
git clone https://github.com/gonarahmaniani/IQA.git
cd IQA
```

Then navigate to the folder via `cd IQA`.

