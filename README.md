# python-progress-bar
Simple progress bar for python.

```python
import time
import progressBar
startTime = time.time()
for i in range(10):
    time.sleep(1)
    progressBar.printProgress(step=i+1, totalSteps=10, seconds=time.time()-startTime, barWidth=20)
```
