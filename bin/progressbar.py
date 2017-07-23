# -*- coding: utf-8 -*-
import time

class progressbarClass: 
    def __init__(self, finalcount, progresschar=None):
        import sys
        
        self.finalcount=finalcount
        self.blockcount=0
        #
        # See if caller passed me a character to use on the
        # progress bar (like "*").  If not use the block
        # character that makes it look like a real progress
        # bar.
        #
        if not progresschar: self.block='='
        else:                self.block=progresschar
        #
        # Get pointer to sys.stdout so I can use the write/flush
        # methods to display the progress bar.
        #
        self.f=sys.stdout
        #
        # If the final count is zero, don't start the progress gauge
        #
        if not self.finalcount : return
        self.f.write('\n------------------- % Progress -------------------\n')
        self.f.flush()
        self.time = time.time()
        self.findn = 0 # how many cannot be calculated when evaluate the remaining time
        self.textleft = False
        return
 
    def progress(self, count, find=False):
        #
        # Make sure I don't try to go off the end (e.g. >100%)
        #
        count=min(count, self.finalcount)
        #
        # If finalcount is zero, I'm done
        #
        if self.finalcount:
            percentcomplete=round(100*count/self.finalcount,2)
        else:
            percentcomplete=100
            
        #print "percentcomplete=",percentcomplete
        blockcount=int(percentcomplete/2)
        #print "blockcount=",blockcount
#        if blockcount > self.blockcount:
#            for i in range(self.blockcount,blockcount):
#                self.f.write(self.block)
#                self.f.flush()
        self.findn += find
  
        txt = str(percentcomplete)+'%('
        if (count-self.findn)==0:
            txt += '-'
        else:
            left_s = (time.time()-self.time)/(count-self.findn)*(self.finalcount-count)
            if left_s>3600:
                txt += str(round(left_s/3600,2))+'h'
            elif left_s>60:
                txt += str(round(left_s/60,2))+'m'
            else:
                txt += str(round(left_s,2))+'s'
        txt+=' left)'
        if self.textleft:
            txt += self.block*(blockcount-len(txt))
        elif blockcount+len(txt)>50:
            txt += self.block*(blockcount-len(txt))
            self.textleft=True
        else:
            txt = self.block*blockcount + txt
        if len(txt)<50:
            txt+=' '*(50-len(txt))
        txt += '\r'
        self.f.write(txt)
        self.f.flush()
        self.blockcount=blockcount
        return
    def done(self):
        self.f.write("\n")
        self.f.flush()
if __name__ == "__main__":
    from time import sleep
    pb=progressbarClass(51,"=")
    count=0
    for count in range(52):
        pb.progress(count)
        sleep(0.2)
    pb.done()