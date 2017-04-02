# CBRF receiver

Module for obtaining data of value currency from CBRF site.

## Install
```bash
git clone https://github.com/shirolapov/cbrf-receiver.git
cd cbrf-receiver
python setup.py install
```

## Use
Module takes char code of currency and python datetime object. If successful,
the module returns "X".

X = Currency / RUB

### Use to get the value of the currency by its char code for today.
 
```python
import cbrf_receiver
cbrf_receiver.get_value("USD")
>>> 55.9606
```

### Use to get the value of the currency by its char code for certain date.
 
 ```python
import  cbrf_receiver
from datetime import datetime
dt = datetime(year=2006, month=5, day=17)
cbrf_receiver.get_value("USD", dt)
>>> 27.0209
```
