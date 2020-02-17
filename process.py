import queue
import threading
import numpy as np
import time
import os
"""

"""

class VideoCompressor():

    def __init__ (self, pool_size = 3, queue_size = 10):
        self.pool_size = pool_size
        self.queue_size = queue_size

    def compress(self, name):
        os.system(f'ffmpeg -i {name} -b:v 2M -b:a 192k -filter:v fps=fps=30 -s hd720 -c:v libx264 -crf 23 -c:a aac -strict -2 {name}_output.avi')

    def execute(self, name):
        name = threading.current_thread().getName()
        t = threading.Thread(target = self.compress, args = (name,) )
        t.start()


Compressor1 = VideoCompressor()
Compressor2 = VideoCompressor()
Compressor2.execute()
Compressor1.execute()
