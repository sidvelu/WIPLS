#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Gnu V3
# Generated: Fri Jan 23 17:02:08 2015
##################################################

from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import baz

class GNU_v3(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Gnu V3")

        ##################################################
        # Variables
        ##################################################
        self.sr = sr = 512
        self.samp_rate = samp_rate = 32000

        ##################################################
        # Blocks
        ##################################################
        self.rtl2832_source_0 = baz.rtl_source_c(defer_creation=True, output_size=gr.sizeof_gr_complex)
        self.rtl2832_source_0.set_verbose(True)
        self.rtl2832_source_0.set_vid(0x0)
        self.rtl2832_source_0.set_pid(0x0)
        self.rtl2832_source_0.set_tuner_name("")
        self.rtl2832_source_0.set_default_timeout(0)
        self.rtl2832_source_0.set_use_buffer(True)
        self.rtl2832_source_0.set_fir_coefficients(([]))
        
        self.rtl2832_source_0.set_read_length(0)
        
        
        
        
        if self.rtl2832_source_0.create() == False: raise Exception("Failed to create RTL2832 Source: rtl2832_source_0")
        
        self.rtl2832_source_0.set_bandwidth(1.4e6)
        
        self.rtl2832_source_0.set_sample_rate(1.4e6)
        
        self.rtl2832_source_0.set_frequency(436000000)
        
        
        
        self.rtl2832_source_0.set_auto_gain_mode(False)
        self.rtl2832_source_0.set_relative_gain(True)
        self.rtl2832_source_0.set_gain(20)
          
        self.blocks_head_0 = blocks.head(gr.sizeof_gr_complex*1, 15000)
        self.blocks_file_sink_1 = blocks.file_sink(gr.sizeof_gr_complex*1, "passband_sig.bin", False)
        self.blocks_file_sink_1.set_unbuffered(False)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.rtl2832_source_0, 0), (self.blocks_head_0, 0))
        self.connect((self.blocks_head_0, 0), (self.blocks_file_sink_1, 0))



    def get_sr(self):
        return self.sr

    def set_sr(self, sr):
        self.sr = sr

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    tb = GNU_v3()
    tb.start()
    tb.wait()
