import mne
from mne import pick_types_forward, convert_forward_solution, VolSourceEstimate, SourceEstimate
from mne.datasets import sample
import matplotlib.pyplot as plt
from mne.forward import is_fixed_orient, _subject_from_forward
from mne.io.proj import _has_eeg_average_ref_proj, make_eeg_average_ref_proj, make_projector
from pandas import np
from scipy import linalg
from plot_forward_sensitivity_maps import mag_map

data_path = sample.data_path()
fwd_fname = data_path + '/MEG/sample/sample_audvis-meg-eeg-oct-6-fwd.fif'
subjects_dir = data_path + '/subjects'
fwd = mne.read_forward_solution(fwd_fname)
projs=None
exclude=[]
ch_type='mag'
mode='free'
fwd = pick_types_forward(fwd, meg=ch_type, eeg=False, exclude=exclude)
convert_forward_solution(fwd, surf_ori=True, force_fixed=False,
                         copy=False, verbose=False)
gain = fwd['sol']['data']
n_sensors, n_dipoles = gain.shape
n_locations = n_dipoles // 3
sensitivity_map = np.empty(n_locations)
for k in range(n_locations):
    gg = gain[:, 3 * k:3 * (k + 1)]
    s = linalg.svd(gg, full_matrices=False, compute_uv=False)
    sensitivity_map[k] = s[2]

sensitivity_map /= np.max(sensitivity_map)
subject = _subject_from_forward(fwd)
vertices = [fwd['src'][0]['vertno'], fwd['src'][1]['vertno']]
SEClass = SourceEstimate
mag_map = SEClass(sensitivity_map[:, np.newaxis], vertices=vertices, tmin=0,
              tstep=1, subject=subject)
fig_1, ax = plt.subplots()
ax.hist([mag_map.data.ravel()],bins=20, label=['Magnetometers'],color=['c'])
fig_1.legend()
ax.set(title='orientation sensitivity', xlabel='sensitivity', ylabel='count')
mag_map.plot(time_label='Magnetometers sensitivity', subjects_dir=subjects_dir,clim=dict(lims=[0, 50, 100]))
plt.ioff()
plt.show()