# py-waitgroup

This is WaitGroup like Go sync.WaitGroup.

## How to install

```sh
pip install git+https://github.com/juv-shun/py-waitgroup
```

## Synopsis
Usage:

```python
import multiprocessing
import time
from waitgroup import WaitGroupProcess

wg = WaitGroupProcess()

def do_sample():
    time.sleep(1) # do something
    wg.done()

for i in range(3):
    wg.add()
    multiprocessing.Process(target=do_sample).start()

wg.wait()
print('all finished')
```
