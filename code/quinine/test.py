import nmrespy as ne
import matplotlib.pyplot as plt

e = ne.Estimator2DJ.new_bruker("../../data/quinine/1")
e.phase_data(p0=1.803, p1=-6.239)
e.baseline_correction()
fid = ne.sig.zf(ne.sig.zf(e._data[0]))
fid = ne.sig.ft(fid).real
plt.plot(fid)
plt.show()
