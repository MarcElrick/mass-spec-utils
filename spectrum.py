# spectrum.py
# classes / methods for handling spectra

import math

class SpectralRecord(object):
    def __init__(self,precursor_mz,peaks,metadata,original_file,spectrum_id):
        self.peaks = peaks
        self.peaks.sort(key = lambda x: x[0]) # similarity scores assume sorting by m/z
        self.spectrum_id = spectrum_id
        self.metadata = metadata
        self.original_file = original_file
        self.precursor_mz = precursor_mz
        self._sqrt_normalise()
        self.n_peaks = len(self.peaks)
        

    def __str__(self):
        if 'names' in self.metadata:
            names = self.metadata['names'][0]
        else:
            names = ""
        return ", ".join([self.spectrum_id,names,str(self.precursor_mz),self.original_file])

    def __repr__(self):
        return self.__str__()

    def __lt__(self,other):
        return(self.precursor_mz < other.precursor_mz)

    def _sqrt_normalise(self):
        temp = []
        total = 0.0
        for mz,intensity in self.peaks:
            temp.append((mz,math.sqrt(intensity)))
            total += intensity
        norm_facc = math.sqrt(total)
        self.normalised_peaks = []
        for mz,intensity in temp:
            self.normalised_peaks.append((mz,intensity/norm_facc))
