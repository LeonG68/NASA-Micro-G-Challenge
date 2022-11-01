
class KerberosSDR:

    def __init__(self, frequency=None):
        #want to write the value to desktop
        self.doa_fname = '/home/pi/Desktop/doa.txt'

    def get_DOA(self):
        doa_file = open(self.doa_fname, 'r')
        value = doa_file.read()
        if value == "None":
            return None
        else:
            return int(value)
