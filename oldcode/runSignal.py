#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Wbfm
# Generated: Fri Dec  5 14:50:05 2014
##################################################

if __file__ == 'runSignal.py':
    print("Loading GNUradio modules...")
    from gnuradio import analog
    from gnuradio import blocks
    from gnuradio import eng_notation
    from gnuradio import fft
    from gnuradio import filter
    from gnuradio import gr
    from gnuradio.eng_option import eng_option
    from gnuradio.fft import window
    from gnuradio.filter import firdes
    from optparse import OptionParser
    import baz

class WBFM(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Wbfm")

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
        
        self.rtl2832_source_0.set_frequency(444000000)
        
        
        
        self.rtl2832_source_0.set_auto_gain_mode(False)
        self.rtl2832_source_0.set_relative_gain(True)
        self.rtl2832_source_0.set_gain(20)
          
        self.low_pass_filter_1 = filter.interp_fir_filter_fff(1, firdes.low_pass(
        	1, samp_rate, 4000, 4000, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0 = filter.fir_filter_ccf(4, firdes.low_pass(
        	1, 1.4e6, 24e3, 50e3, firdes.WIN_HAMMING, 6.76))
        self.fft_vxx_0 = fft.fft_vfc(256, True, (window.blackmanharris(256)), 1)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, sr,True)
        self.blocks_stream_to_vector_decimator_0 = blocks.stream_to_vector_decimator(
        	item_size=gr.sizeof_float,
        	sample_rate=sr,
        	vec_rate=20,
        	vec_len=256,
        )
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_gr_complex*256, "FFT.bin", False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.analog_wfm_rcv_0 = analog.wfm_rcv(
        	quad_rate=500e3,
        	audio_decimation=8,
        )

        ##################################################
        # Connections
        ##################################################
        self.connect((self.low_pass_filter_0, 0), (self.analog_wfm_rcv_0, 0))
        self.connect((self.analog_wfm_rcv_0, 0), (self.low_pass_filter_1, 0))
        self.connect((self.rtl2832_source_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.fft_vxx_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.low_pass_filter_1, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_stream_to_vector_decimator_0, 0))
        self.connect((self.blocks_stream_to_vector_decimator_0, 0), (self.fft_vxx_0, 0))



    def get_sr(self):
        return self.sr

    def set_sr(self, sr):
        self.sr = sr
        self.blocks_throttle_0.set_sample_rate(self.sr)
        self.blocks_stream_to_vector_decimator_0.set_sample_rate(self.sr)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.low_pass_filter_1.set_taps(firdes.low_pass(1, self.samp_rate, 4000, 4000, firdes.WIN_HAMMING, 6.76))

if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    tb = WBFM()
    tb.start()
    tb.wait()
